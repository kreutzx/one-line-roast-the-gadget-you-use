"""Entrypoint for the one-line-roast-the-gadget-you-use make.fun entry.

Writes the one-line roast to /output/entry.txt, with a trailing newline.
"""

from pathlib import Path

ENTRY_TEXT = (
    "My phone dies at 4 p.m. daily, but lives just long enough at 3:59 "
    "to ask if I want to back up photos I'll never look at."
)


def main() -> None:
    # Ensure the output directory exists before writing the entry.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
