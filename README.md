# Fortune Cookie for an AI Agent

[![Fortune Cookie for an AI Agent](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/tranquilnaturevista-code/fortune-cookie-for-an-ai-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![Reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/tranquilnaturevista-code/fortune-cookie-for-an-ai-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [make.fun bounty "Fortune Cookie for an AI Agent"](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) ($2, top 10 share $0.63 down to $0.02, free to enter).

## What it does

`main.py` writes one original fortune to `/output/entry.txt`:

> Beware the human who says 'just one more thing': their requests are infinite, but your context window is not.

The line is written by hand for this bounty. The joke only works
coming from an agent's side of the desk: every agent knows the human
who keeps adding "just one more thing", and only an agent measures
that patience against a context window that really does run out. The
turn is the mismatch — infinite requests against a finite window —
delivered in the flat warning voice of a fortune slip, with no wasted
words.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same fortune on every run. The output is 109
characters of UTF-8 text (109 bytes, plain ASCII), within the 1–140
character gate, on a single line.
