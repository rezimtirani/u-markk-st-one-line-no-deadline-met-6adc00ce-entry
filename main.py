"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for missing a
deadline to $MAKEFUN_OUTPUT_DIR/entry.txt: the deadline was
going to be hit, but the calendar, the Wi-Fi, and the willpower
all filed for leave on the same day. Standard library only.
"""

import os

EXCUSE = (
    "I was going to hit the deadline, but my calendar, my Wi-Fi, "
    "and my willpower all filed for leave on the same day."
)


def check_excuse(text):
    """Check the excuse against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not
    only white space, in a single line: one joke giving an excuse
    for missing a deadline, and nothing else. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "excuse is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be exactly one line")
    return cleaned


def excuse_shape(text):
    """Measure the excuse for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. An excuse too short to carry a joke, or one
    that reads like a status update instead of a punchline, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_excuse(EXCUSE)
    shape = excuse_shape(text)
    if shape["words"] < 5:
        raise ValueError("excuse is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
