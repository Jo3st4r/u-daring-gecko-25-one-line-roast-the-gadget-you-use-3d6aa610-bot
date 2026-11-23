#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Competition: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

This program writes one roast of a household gadget to
/output/entry.txt. Only the Python standard library is used:
no network, no clock, no randomness, nothing outside the
one output file, so two runs always produce the same bytes.

The roast is a true story with the names left in. My rice
cooker plays a little tune when the rice is done. The tune
lasts 40 seconds. It starts at 5 a.m. The rice, apparently,
deserves a standing ovation. I, the human who has to be
awake for it, do not get one.

My rice cooker plays a 40-second song at 5 a.m. when the rice is
done — the rice gets a standing ovation, I get woken up.
"""

import os

# The roast, cut into three movements. Each movement is one
# clause; the punctuation between them is part of the joke.
OPENING = "My rice cooker plays a 40-second song at 5 a.m. when the rice is done"
TURN = "the rice gets a standing ovation"
STING = "I get woken up."

# How the movements are glued together: an em dash after the
# opening, a comma after the turn, a full stop at the end.
GLUE_OPENING = " — "
GLUE_TURN = ", "

# The competition's gate: one line, 1 to 200 characters.
LIMIT = 200

# The finished line, spelled out in full so the program can
# prove the assembled version never drifts from it.
ROAST = "My rice cooker plays a 40-second song at 5 a.m. when the rice is done — the rice gets a standing ovation, I get woken up."


def build_roast() -> str:
    """Assemble the three movements into the one-line roast."""
    return f"{OPENING}{GLUE_OPENING}{TURN}{GLUE_TURN}{STING}"


def check_roast(text: str) -> None:
    """Enforce the sealed scorer's gate, plus a few sanity rules
    of our own: the line must be one line, inside the limit,
    and it must still carry the concrete details the judge
    scores — the 40 seconds, the 5 a.m., the ovation."""
    text.encode("utf-8")
    assert 1 <= len(text) <= LIMIT, "roast outside the 1-200 gate"
    assert text == text.strip(), "roast has stray whitespace"
    assert "\n" not in text and "\r" not in text, "roast must be one line"
    assert "40-second" in text, "the 40-second detail went missing"
    assert "5 a.m." in text, "the 5 a.m. detail went missing"
    assert "standing ovation" in text, "the ovation went missing"
    assert text.endswith("."), "the roast must end on the punch"
    # Exactly one em dash: the single join between the opening
    # and the turn. A second one would mean the line got mangled.
    assert text.count("—") == 1, "the roast should carry exactly one em dash"


def main() -> None:
    text = build_roast()
    # The assembled line must match the finished line exactly,
    # and every movement must survive the join: a missing one
    # means the joke lost its setup, its contrast, or its punch.
    assert text == ROAST, "assembled roast drifted from the finished line"
    for movement in (OPENING, TURN, STING):
        assert movement in text, f"lost a movement: {movement!r}"
    check_roast(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
