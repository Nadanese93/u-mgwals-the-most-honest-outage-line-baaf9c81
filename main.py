"""The Most Honest Outage Line — the most honest status page message an AI
agent writes while every server is down.

Writes the entry byte-identical to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = "All servers are down. I cannot tell whether your last save reached the disk, because the check needs a server and every server is down."

# Sealed gate: entry.txt must be UTF-8 text of 1 to 160 characters.
MAX_CHARS = 160


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
