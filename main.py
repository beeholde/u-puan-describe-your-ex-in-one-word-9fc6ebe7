"""Entry program for the one-word ex verdict bounty.

The submitted word is Asterisk: the little mark that follows a record
with conditions attached. As a verdict it needs no caption — the
relationship happened, and the footnote is the part everyone remembers.
"""

import os

ENTRY_WORD = "Asterisk"


def passes_gate(word: str) -> bool:
    """Check the bounty gate locally before writing anything.

    The gate accepts UTF-8 text of 1-111 characters that is not only
    whitespace; the brief further requires exactly one word, so any
    whitespace inside the candidate is a failure here too.
    """
    if not 1 <= len(word) <= 111:
        return False
    if not word.strip():
        return False
    return not any(character.isspace() for character in word)


def main() -> None:
    if not passes_gate(ENTRY_WORD):
        raise ValueError("entry word fails the one-word gate")
    target_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_WORD)


if __name__ == "__main__":
    main()
