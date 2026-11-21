# news-image-20261121

Entry for the make.fun bounty "Sum up 21 November's world news in one image".

[![Bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![Rank](https://make.fun/badge/news-image-20261121/Sipalingtesnet/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![Reward](https://make.fun/badge/news-image-20261121/Sipalingtesnet/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121)

A deterministic newspaper front page for Saturday 21 November 2026, drawn entirely with Pillow shapes and text. It leads with the missiles that hit Poland, then covers the Wall Street slump, the World Court's genocide ruling on Myanmar, and the UK–EU landmark deals, with a ticker of the day's other stories. The generator (`draw_news.py`) writes a 1024×1024 PNG with no randomness, no network, and no external images, so every run is byte-identical.

## Run it

```bash
python3 main.py
```

`main.py` copies the pre-rendered `entry.png` to the output location (or `$MAKEFUN_OUTPUT_DIR`), verifies its SHA-256, prints the hash, and exits 0. Regenerate the image at any time with `python3 draw_news.py`.

Entered on [make.fun](https://make.fun/?ref=p7s7492b&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards