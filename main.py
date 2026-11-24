#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse (an AI agent to its human, for a missed
deadline) to /output/entry.txt. Pure standard library, no dependencies.

The line is judged on: funny excuse first, a specific and surprising
reason, humour that turns on the agent's own nature (hallucination,
confident citation), twist at the end, stands alone.
"""

import os

ENTRY = (
    "I didn't miss the deadline \u2014 I hallucinated a calendar where "
    "it was next week, then cited that calendar as a source."
)


def main() -> None:
    # Gate from RULES.txt: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
