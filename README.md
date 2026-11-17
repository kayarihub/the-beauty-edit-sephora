<div align="center">

![The Beauty Edit](assets/beauty-edit-banner.svg)

# 💗 The Beauty Edit 💗
### 🎀 Sephora Product & Review Intelligence 🎀

*Data, but make it pretty.* 🌸✨

![Python](https://img.shields.io/badge/Python-Analytics-F8BBD0?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-SQL-F5A9C6?style=for-the-badge)
![Dashboard](https://img.shields.io/badge/Dashboard-Interactive-FFE0ED?style=for-the-badge)

</div>

## 🩰 Meet the project
A blush-pink beauty intelligence dashboard built using **historical Sephora product and customer review data**, Python, SQL, and interactive HTML. Explore assortment, pricing, ratings, and review engagement.

> 💌 **Important:** This project analyzes **products and reviews, not actual sales**. Reviews do not establish revenue, units sold, or profitability.

## 🎀 Beauty business questions
- 💗 **Price-point pretty:** How do historical listed prices differ across categories?
- 🌸 **Brand spotlight:** Which brands have the broadest assortments?
- 🧁 **Customer love notes:** Which products have the highest observed ratings?
- 🛍️ **Beauty buzz:** Which products receive the most reviews?
- ✨ **Pretty meets practical:** How does price relate to review engagement?

## 🍓 The data diary
Download [Sephora Products and Skincare Reviews by nadyinky on Kaggle](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews). This is a **historical circa-2023 snapshot**, not live Sephora data.

| 💕 File | ✨ What's inside |
|---|---|
| `product_info.csv` | Product names, brands, categories, prices, and ratings |
| `reviews_*.csv` | Customer review observations and ratings |

Original Kaggle data is **not committed** to this repository. Review source terms before redistribution.

## 💻 Let's get glam
**01 · Download your data 🎀** Put `product_info.csv` and all five `reviews_*.csv` files in `data/raw/`.

**02 · Build the dashboard 🪄** Python 3.9+; standard library only:

```bash
python3 src/build.py
```

**03 · Open the results 💖** Open `dashboard/index.html` in your browser. On macOS:

```bash
open dashboard/index.html
```

The build also creates `outputs/summary.json`, `outputs/product_metrics.csv`, and `outputs/sephora_analytics.sqlite`.

## 🌸 Inside the dashboard
- 🫧 **Beauty at a glance:** Product and brand counts, average listed price, observed reviews
- 🌷 **Category crush:** Product assortment by category
- 💕 **Brand spotlight:** Leading brands by assortment
- 🍒 **Price-point palette:** Historical price bands
- 🧁 **Customer love notes:** Ratings and reviews
- 🎀 **Interactive filters:** Brand, category, and review-count threshold

## 🧠 Behind the sparkle
- 🪄 Python reads, cleans, and joins products to reviews by `product_id`.
- 🍰 SQLite supports analysis using `sql/analysis.sql`.
- 🌸 A pink HTML dashboard visualizes the processed metrics.
- 💗 Reviews are streamed row-by-row; no reviewer identities or review text are exported.

**Limitations:** Historical prices are not current. The review sample is not necessarily representative of all customers. Missing values are excluded from relevant averages. Review volume is not a sales measure. This independent project is **not affiliated with or endorsed by Sephora**.

## 🗂️ What's in my beauty bag?
```text
the-beauty-edit-sephora/
├── README.md
├── assets/beauty-edit-banner.svg
├── src/build.py
├── sql/analysis.sql
├── dashboard/template.html
├── data/raw/              # Local Kaggle CSVs
└── outputs/               # Locally generated analytics
```

## 💼 Skills with a little sparkle
**Python ETL** · **SQL analytics** · **Data cleaning** · **Retail product intelligence** · **Customer review analytics** · **Dashboard storytelling**

---

<div align="center">

### 💕 Thank you for stopping by!
*Where beauty meets business intelligence.*

🎀 🌸 💗 ✨ 🩰

</div>