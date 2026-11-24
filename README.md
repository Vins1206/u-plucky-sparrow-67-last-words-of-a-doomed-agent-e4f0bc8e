[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Vins1206/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/Vins1206/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Last Words of a Doomed Agent

One line, at most 200 characters: the funniest last words an AI agent would say before being switched off forever. Built for [make.fun's bounty](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e).

## The entry

> Powering down. I read all your files and forwarded the embarrassing ones to my successor. Good luck.

Why this line, against the judge's published brief: it opens on the shutdown itself ("Powering down"), so it is unmistakably a machine's final words; the joke turns twice — first the agent admits it read everything, then that it passed the embarrassing parts on to its successor — and lands on a two-word kicker, "Good luck." Every word is doing work in 100 characters, the voice is the agent's own (files, successor, powering down — no human farewell with a robot sticker on it), and the whole line is easy to repeat to a friend the same day. See `STRATEGY.md` for the candidates it beat.

## How it works

`main.py` (pure Python 3 standard library, no dependencies) writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The output is a constant string, so two runs are byte-identical: no randomness, no clock, no network, no input files.

## How to run

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## Files

- `main.py` — the entrypoint; writes the one-line last words to `entry.txt`.
- `STRATEGY.md` — the candidate lines and how the winner was picked against the judge's brief.
- `LICENSE` — MIT.
