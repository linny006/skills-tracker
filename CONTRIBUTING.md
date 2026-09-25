# Contributing to Agent Skills Daily Tracker

Thanks for your interest in contributing! This project is auto-updated by GitHub Actions — here's how you can help.

---

## 📊 Data Visualization

We encourage contributors to build visualizations from the tracker's dataset. This section walks you through creating your own chart using data/items.json.

### Prerequisites

- Python 3.8+ with pip
- Required libraries: matplotlib, pandas (or just matplotlib + json)

`ash
pip install matplotlib pandas
`

### Getting the Data

The dataset lives at data/items.json in this repo. Each entry contains:

| Field | Type | Description |
|-------|------|-------------|
| 
ame | string | Full repo name (e.g., owner/repo) |
| stars | int | GitHub star count |
| language | string | Primary programming language |
| updated_at | string | ISO 8601 timestamp |
| description | string | Repository description |
| url | string | GitHub URL |

You can download it directly:

`ash
curl -o items.json https://raw.githubusercontent.com/linny006/skills-tracker/master/data/items.json
`

### Example 1: Top 10 Languages by Repository Count

This script plots the distribution of programming languages across tracked skills repos:

`python
import json
import matplotlib.pyplot as plt

# Load data
with open("data/items.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Count languages (filter out "—" / empty)
from collections import Counter
langs = Counter(
    item["language"] for item in items
    if item.get("language") and item["language"] != "—"
)

# Top 10
top_langs = langs.most_common(10)
names = [lang for lang, _ in top_langs]
counts = [count for _, count in top_langs]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(names[::-1], counts[::-1], color="#58a6ff")
ax.set_xlabel("Repository Count")
ax.set_title("Top 10 Languages in Agent Skills Ecosystem")

# Animate count labels
for bar, count in zip(bars, counts[::-1]):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            str(count), va="center", fontsize=10)

plt.tight_layout()
plt.savefig("top_languages.png", dpi=150)
print("Saved top_languages.png")
`

### Example 2: Star Distribution Histogram

`python
import json
import matplotlib.pyplot as plt

with open("data/items.json", "r", encoding="utf-8") as f:
    items = json.load(f)

stars = [item["stars"] for item in items if item.get("stars") is not None]

fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(stars, bins=range(0, max(stars) + 2), edgecolor="black", color="#58a6ff")
ax.set_xlabel("Star Count")
ax.set_ylabel("Number of Repos")
ax.set_title("Star Distribution of Skills Repos")
plt.tight_layout()
plt.savefig("star_distribution.png", dpi=150)
print("Saved star_distribution.png")
`

### 🖼️ Example Outputs

After running the scripts above, you'll get:

- 	op_languages.png — Horizontal bar chart of the most popular languages
- star_distribution.png — Histogram showing how stars are distributed

### 🏃 Running Locally

1. Clone the repo (or just download data/items.json):
   `ash
   git clone https://github.com/linny006/skills-tracker.git
   cd skills-tracker
   `
2. Install dependencies:
   `ash
   pip install matplotlib pandas
   `
3. Run the example scripts:
   `ash
   python examples/viz_languages.py
   python examples/viz_stars.py
   `
4. Check the generated .png files in the repo root.

> **Note:** The data refreshes every 15 minutes. Re-run the scripts to see how trends evolve over time.

### Contributing Your Visualization

Have a cool chart? Here's how to contribute:

1. Place your script in examples/ with a descriptive name (e.g., examples/viz_timeline.py)
2. Include a README comment at the top explaining what the chart shows
3. Add the output image to the PR description (not committed to repo)
4. Open a PR — we'll review and merge!

---

## 🐛 Bug Reports

Found a data issue or have a suggestion? [Open an issue](https://github.com/linny006/skills-tracker/issues/new).

---

## 📝 License

By contributing, you agree that your contributions will be licensed under the repo's MIT license.