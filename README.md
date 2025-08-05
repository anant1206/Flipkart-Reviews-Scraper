# 🛒 Flipkart Review Scraper

A fast and efficient Python script to scrape product reviews from Flipkart using Selenium, BeautifulSoup, and Brave browser.

---

## 🚀 Features

- ✅ Scrapes **all review pages** (not just first few)
- ✅ Uses **headless mode** for faster scraping
- ✅ Cleans up extra text like `READ MORE`
- ✅ Filters out non-review blocks
- ✅ Saves data to CSV
- ✅ Compatible with Brave browser
- ✅ Lightweight and auto-installs compatible ChromeDriver

---

## 📦 Requirements

- Python 3.7+
- Google Chrome or Brave browser
- pip packages:
  - `selenium`
  - `beautifulsoup4`
  - `pandas`
  - `chromedriver-autoinstaller`

---

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
   ```bash
   cd <project-directory>
   ```
   
2. Install required packages:
   ```bash
   pip install -r requirements.txt

3. Make sure Brave browser or Chrome is installed:

    Default path used:
     ```bash
    C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe
    ```
   Modify the brave_path in the script if needed.

---

## 🧠 How It Works
   - Launches a headless Brave browser
   - Navigates to the Flipkart product review page
   - Scrolls (optional) and waits for reviews to load
   - Extracts:
     -- Customer name
     -- Review title
     -- Star rating
   - Comment (with READ MORE removed)
   - Repeats until no "Next" button found
   - Saves to flipkart_reviews_optimized.csv

---

## 🧪 Usage

In the script, update this line with your Flipkart product review URL:

```python
url = "https://www.flipkart.com/your-product-link-product-reviews/itmxxxxxxxxxxxx?pid=PIDXXXXXXXXXXXXX"
```
Then run the script:
You don't need the full link, just paste the link till pid

Output:
  - flipkart_reviews.csv
  - Console log shows scrape progress and time taken
  - The CSV file contains the extracted reviews along with Customer Name, Review Title, Rating, and Review Comment. It is generated upon completion of scraping all pages.

| Part                   | Meaning                               |
| ---------------------- | ------------------------------------- |
| `itmxxxxxxxxxxxXx`     | Backend item ID (used in review URLs) |
| `pid=PIDXXXXXXXXXXXXX` | Product ID used by site/frontend      |

---
## Contributing
Feel free to open issues or contribute to the project. Pull requests are always welcome.




