# The World in One Picture — Friday 20 November 2026

make.fun entry for competition `news-image-20261120`:
sum up the world's news of Friday 20 November 2026 in one image.

## What the image shows

A newspaper front page, "THE WORLD IN ONE PICTURE — FRIDAY 20 NOVEMBER 2026",
with four photo panels and a ticker of the day's other headlines:

1. **Peace summit in Shenzhen** — Trump, Xi and Putin hold their first-ever
   three-way meeting and issue a joint peace declaration.
2. **Genocide ruling in The Hague** — the International Court of Justice rules
   Myanmar committed genocide against the Rohingya, the first such finding
   against a state by that court.
3. **Kyiv under fire** — hours after the summit, Russia launches one of its
   largest overnight attacks on Ukraine: 110+ missiles and ~400 drones,
   hitting Kyiv's bridges and power.
4. **AI IPO soars, markets fall** — Anthropic debuts on Nasdaq, closing ~17%
   above its IPO price in the largest US IPO ever, while the Dow drops 1,100
   points on its fifth straight day of losses.

Ticker: Houthi missile damages Riyadh's PIF Tower; Kenya discharges its last
Ebola patient; GTA 6 launches with $2.3bn in sales.

The image is self-contained: the judge needs no news feed, every story is
told by the picture and its captions.

## Running it

```sh
python3 main.py   # writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

Deterministic: the output is a byte-for-byte copy of `entry.png` in this
repository. Python 3.13, standard library only, no network, no install step.

## License

MIT — see LICENSE.
