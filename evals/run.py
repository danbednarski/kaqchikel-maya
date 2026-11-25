#!/usr/bin/env python3
"""Score Claude on Kaqchikel test cases, with and without this skill.

    python3 evals/run.py                 # both arms, all cases
    python3 evals/run.py --arm skill     # one arm
    python3 evals/run.py --only tired,my-house --model sonnet

Needs the `claude` CLI. The "skill" arm loads this repo as a plugin; the "bare" arm disables all
skills. A case passes when every `must` regex matches the answer and no `must_not` regex does
(case-insensitive, apostrophes normalized). Answers are saved to evals/out/<arm>/<id>.md.
"""
import argparse, concurrent.futures as cf, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)


def norm(s):
    return re.sub(r"[’‘ʼꞌ`]", "'", s).lower()


def ask(arm, prompt, model):
    cmd = ["claude", "-p", prompt, "--model", model]
    if arm == "skill":
        cmd += ["--plugin-dir", REPO, "--allowed-tools", "Read,Grep,Glob,Skill"]
    else:
        cmd += ["--disable-slash-commands", "--tools", ""]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600, cwd=HERE)
    return r.stdout


NEG = re.compile(r"\bnot\b|n't|\bwrong|incorrect|\bnever\b|\binstead\b|\bavoid|\bno existe|incorrect[oa]|"
                 r"k'iche'|\bleak|\bnunca\b|\ben vez de\b|✗|❌|\*\*no\*\*|~~")


def score(case, answer):
    a = norm(answer)
    miss = [p for p in case["must"] if not re.search(norm(p), a)]
    # a wrong form named in order to reject it ("nuchoch doesn't exist") is not an error
    kept = "\n".join(l for l in a.splitlines() if not NEG.search(l))
    bad = [p for p in case["must_not"] if re.search(norm(p), kept)]
    return not miss and not bad, miss, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", choices=["skill", "bare", "both"], default="both")
    ap.add_argument("--only")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("-j", type=int, default=6)
    o = ap.parse_args()
    cases = json.load(open(os.path.join(HERE, "cases.json")))
    if o.only:
        keep = set(o.only.split(","))
        cases = [c for c in cases if c["id"] in keep]
    arms = ["bare", "skill"] if o.arm == "both" else [o.arm]
    jobs = [(arm, c) for arm in arms for c in cases]
    results = {}
    with cf.ThreadPoolExecutor(o.j) as ex:
        futs = {ex.submit(ask, arm, c["prompt"], o.model): (arm, c) for arm, c in jobs}
        for f in cf.as_completed(futs):
            arm, c = futs[f]
            ans = f.result()
            os.makedirs(os.path.join(HERE, "out", arm), exist_ok=True)
            open(os.path.join(HERE, "out", arm, c["id"] + ".md"), "w").write(ans)
            results[(arm, c["id"])] = score(c, ans)
    print(f"{'case':22}" + "".join(f"{a:>8}" for a in arms))
    for c in cases:
        row = "".join(f"{('pass' if results[(a, c['id'])][0] else 'FAIL'):>8}" for a in arms)
        notes = "; ".join(f"{a}: missing {m} wrong {b}" for a in arms
                          for ok, m, b in [results[(a, c["id"])]] if not ok)
        print(f"{c['id']:22}{row}  {notes[:110]}")
    for a in arms:
        n = sum(results[(a, c["id"])][0] for c in cases)
        print(f"{a}: {n}/{len(cases)}")


if __name__ == "__main__":
    sys.exit(main())
