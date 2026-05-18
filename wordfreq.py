#!/usr/bin/env python3
"""wordfreq‑tiny‑20240518
A tiny utility to count word frequencies from stdin or a file.

Usage:
    python3 wordfreq.py [path/to/file]
    cat file.txt | python3 wordfreq.py
"""
import sys
import re
from collections import Counter

def read_input() -> str:
    """Return the full text from a file path argument or stdin."""
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except OSError as e:
            sys.stderr.write(f"Error opening file '{path}': {e}\n")
            sys.exit(1)
    else:
        # Read from stdin
        return sys.stdin.read()

def tokenize(text: str) -> list:
    """Split text into words, lower‑casing and stripping punctuation."""
    # Use regex to keep alphabetic characters and apostrophes inside words
    return re.findall(r"[a-zA-Z']+", text.lower())

def main():
    text = read_input()
    words = tokenize(text)
    if not words:
        sys.stderr.write("No words found in input.\n")
        sys.exit(0)
    counts = Counter(words)
    # Sort by descending frequency, then alphabetically
    for word, freq in sorted(counts.items(), key=lambda wf: (-wf[1], wf[0])):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
