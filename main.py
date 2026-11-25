"""Describe Your Ex in One Word — entry program v2.

Writes a single word to /output/entry.txt: the one-word verdict on an ex.

The word is "Reheated": yesterday's leftovers warmed up one time too
many — familiar, a little stale, and never as good as the first serving.
It reads instantly as a verdict on going back to an ex, with the joke
arriving on its own: one word, no punctuation tricks, no caption needed.
"""

import os

WORD = "Reheated"


def gate_ok(text: str) -> bool:
    """Mirror of the competition gate: UTF-8 text, 1-111 chars, not blank.

    Also enforces the brief's one-word rule: no whitespace inside the word.
    """
    return bool(text.strip()) and 1 <= len(text) <= 111 and not any(
        ch.isspace() for ch in text
    )


def main() -> None:
    assert gate_ok(WORD), "entry word fails the 1-111 char one-word gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
