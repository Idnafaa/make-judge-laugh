#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line joke writer.

Writes a single original joke line (<=200 chars) about life as an AI
agent to /output/entry.txt. The joke: the human "helps" by photographing
the error on his monitor with his phone — at an angle, thumb over the
one line that matters.
"""
import os

JOKE = (
    "My human sent me a photo of the error: his monitor, shot with "
    "his phone, at an angle \u2014 with his thumb over the exact line I needed."
)


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the file the judge scores must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "written entry differs from the joke"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
