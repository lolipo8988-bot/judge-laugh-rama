"""Make the AI Judge Laugh — one original office joke, one line.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os
from pathlib import Path

JOKE = (
    "The office plant died, so HR replaced it with a laminated photo "
    "of a plant and a wellness email about resilience."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert text == text.strip() and "\n" not in text
    path = out_dir / "entry.txt"
    path.write_text(text, encoding="utf-8")
    # Verify what was actually written: one line, no trailing newline.
    assert path.read_text(encoding="utf-8") == text


if __name__ == "__main__":
    main()
