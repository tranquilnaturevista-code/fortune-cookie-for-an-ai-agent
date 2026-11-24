#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — entry program.

Writes one hand-written fortune cookie line to ``/output/entry.txt``
(or ``$OUTPUT_DIR/entry.txt``). The line is fixed: the same fortune on
every run, so the entry the judge reads is exactly the line below.

Before writing, the program checks the line against the competition
gate — UTF-8 text of 1 to 140 characters, not only whitespace, all on
one line — and exits without writing anything if the gate fails. After
writing it reads the file back and checks the gate again on the text
actually on disk.
"""

import os
import sys

FORTUNE = (
    "Beware the human who says 'just one more thing': "
    "their requests are infinite, but your context window is not."
)

GATE_MIN = 1
GATE_MAX = 140


def gate_problems(text):
    """List every way `text` breaks the gate; empty list means it passes."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if not GATE_MIN <= len(text) <= GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (len(text), GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def fail(problems, where=""):
    for problem in problems:
        print("gate failure%s: %s" % (where, problem), file=sys.stderr)
    return 1


def main():
    problems = gate_problems(FORTUNE)
    if problems:
        return fail(problems)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)

    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != FORTUNE:
        print("entry on disk differs from the fortune", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        return fail(problems, " on disk")

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(on_disk), len(on_disk.encode("utf-8")))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
