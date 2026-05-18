# wordfreq‑tiny‑20240518

**Purpose**: Count and list word frequencies from a text source.

**Features**
- Reads from a file or `stdin`
- Case‑insensitive counting
- Outputs words sorted by frequency (high → low)
- Zero external dependencies (pure Python stdlib)

**Usage**
```bash
# From a file
python3 wordfreq.py path/to/file.txt

# From a pipe
cat document.txt | python3 wordfreq.py
```

**Example**
```bash
$ echo "Hello world hello" | python3 wordfreq.py
hello: 2
world: 1
```

**Installation**
Just clone the repo and run the script with Python 3.8+.

**License**
MIT – see the `LICENSE` file.
