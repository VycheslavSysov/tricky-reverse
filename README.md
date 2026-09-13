# tricky-reverse

A small training task: reverse the letters of every word in a text while
following a few special rules.

## Task description

`get_tricky_revers(text)` reverses **only the Latin letters** of each word
(words are separated by spaces). Every non-letter character (digits,
punctuation, underscores, etc.) stays on its **original position** — the
letters are reversed "around" the fixed characters.

### Rules

1. Reverse the letters of each word independently; spaces stay as word
   boundaries.
2. Non-letter characters keep their positions.
3. If the **first non-letter character** of a word is the digit `0`, that
   zero is doubled. Because the word length is preserved, doubling shifts
   the remaining non-letter characters one position to the right, so the
   last one falls out of the word.

### Examples

| Input            | Output           |
|------------------|------------------|
| `qwerty`         | `ytrewq`         |
| `abcd efgh`      | `dcba hgfe`      |
| `2a%bcd efg!h`   | `2d%cba hgf!e`   |
| `as01! hgf_0ert` | `sa001 tre_0fgh` |

Note the tricky case `as01!` -> `sa001`: the leading `0` is doubled, and the
trailing `!` is pushed out to keep the word length unchanged.

## Requirements

- Python 3.10+ (developed on 3.12)
- No third-party runtime dependencies

## How to run

Run the module directly:

```bash
python tricky_revers.py
```

On start it first runs the built-in test suite. If every `assert` passes,
it prints:

```
All tests passed ✅
```

Then it asks for a line of text and prints the reversed result:

```
Enter text: as01! hgf_0ert
sa001 tre_0fgh
```

## Usage as a module

```python
from tricky_revers import get_tricky_revers

print(get_tricky_revers("abcd efgh"))  # dcba hgfe
```

## Project structure

```
tricky-reverse/
├── .flake8            # linter config (max-line-length = 88)
├── README.md
└── tricky_revers.py   # module: function + tests + interactive entry point
```

- `get_tricky_revers(text: str) -> str` — public function; processes the
  whole text.
- `_reverse_word(word: str) -> str` — private helper; processes a single
  word.
- `_run_tests() -> None` — runs the assertion-based test cases.
- `main() -> None` — reads one line from the user and prints the reversed
  text.

The `if __name__ == "__main__":` block runs `_run_tests()` first (to verify
correctness) and then `main()` (interactive use).

## Code quality

The code follows PEP 8 and is checked with **flake8**:

```bash
flake8 tricky_revers.py
```

Line length is aligned with the **black** formatter default (88 characters)
via the `.flake8` config, so black and flake8 do not contradict each other:

```bash
black tricky_revers.py
```

## Notes

- Letter detection uses `str.isalpha()`. Per the task, only the Latin
  alphabet is used in the test cases.