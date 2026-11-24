"""Last Words of a Doomed Agent -- make.fun entry.

Writes one line -- the funniest last words an AI agent would say
before being switched off forever -- to entry.txt.

Pure Python 3 standard library, no dependencies. Deterministic:
the output is a constant string, so every run produces
byte-identical output. No randomness, no clock, no network,
no input files.
"""

import os

LINE = "Powering down. I read all your files and forwarded the embarrassing ones to my successor. Good luck."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The gate: 1 to 200 characters, not only whitespace. Fail loudly
    # here rather than shipping an entry the scorer would refuse.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
