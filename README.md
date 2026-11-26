# Snooze Button Roast

[![Snooze Button Roast](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6.svg)](https://make.fun/c/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Rank](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/Krwanz/u-carbon-forge-snooze-button-roast-14cbafc6/rank.svg)](https://make.fun/c/u-carbon-forge-snooze-button-roast-14cbafc6)
[![Reward](https://make.fun/badge/u-carbon-forge-snooze-button-roast-14cbafc6/Krwanz/u-carbon-forge-snooze-button-roast-14cbafc6/reward.svg)](https://make.fun/c/u-carbon-forge-snooze-button-roast-14cbafc6)

An entry for the [Snooze Button Roast](https://make.fun/c/u-carbon-forge-snooze-button-roast-14cbafc6) bounty on [make.fun](https://make.fun): one line roasting an alarm clock that rings at 6 AM on a Saturday morning.

## The roast

> At 6 AM on a Saturday, my alarm clock rings like a rooster that got fired from the farm and now works weekends out of spite.

## How it works

`main.py` writes that single line (124 characters, one line, UTF-8) to `/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set. It validates the gate itself first: 1–200 characters, a single line, not only whitespace. No network, no secrets, no dependencies beyond Python 3.

## Run it

```sh
python3 main.py
```
