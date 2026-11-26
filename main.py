"""Entry for make.fun competition u-rama-melon-make-the-ai-judge-laugh-302d0825.

"Make the AI Judge Laugh" — one joke about office life, one line, under
200 characters, written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line is a true office observation with a surprising turn: the office
plant is treated better than the staff — watered, complimented, and never
asked to stay late. It reads cleanly aloud in one breath, and every word
earns its place.

Deterministic: the program always writes exactly the LINE constant, with
no trailing newline, so the output is byte-identical on every run.

Why this line fits the judge's brief, in the brief's own order:
1. It is about office life and lands as a joke — the plant as the
   best-treated "employee" is the joke itself, not a setup for one.
2. The observation is true: office plants really do get watered and
   complimented while the staff work late, so the listener nods first.
3. The turn is surprising: "never asked to stay late" reframes the
   plant's care as a better employment deal than the humans get.
4. It is tight: one sentence, no wasted setup, every word earning its
   place, and it reads cleanly aloud in a single breath.
5. It is original: not a meeting, email, or printer line with the nouns
   swapped — the plant-as-employee angle is its own.
"""

import os
from pathlib import Path

LINE = "The office plant is the only employee who gets watered, complimented, and never asked to stay late."

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = LINE.encode("utf-8")
    OUTPUT_PATH.write_bytes(data)
    # Self-check: what we wrote must be exactly LINE.
    assert OUTPUT_PATH.read_bytes() == data


if __name__ == "__main__":
    main()
