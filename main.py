"""One Word From Grandma — entry program.

Writes the single word Grandma would text about AI to /output/entry.txt.
"""

import os

WORD = "Thingamabob"

# Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters.
MAX_CHARS = 30


def main():
    if not 1 <= len(WORD) <= MAX_CHARS:
        raise ValueError(f"word must be 1-{MAX_CHARS} chars, got {len(WORD)}")
    if WORD.split() != [WORD]:
        raise ValueError("entry must be exactly one word")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify what was written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError(f"read-back mismatch: {written!r} != {WORD!r}")


if __name__ == "__main__":
    main()
