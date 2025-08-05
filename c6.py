import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# Install the matching ChromeDriver
chromedriver_autoinstaller.install()
start = time.time()

# Path to Brave browser
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# Configure Chrome options
options = Options()
options.binary_location = brave_path
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

def scrape_flipkart_reviews(product_url):
    all_reviews = []
    page = 1

    while True:
        paged_url = f"{product_url}&page={page}"
        print(f"Scraping page {page}: {paged_url}")
        driver.get(paged_url)

        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cPHDOP"))
            )

            # Optional: reduce or remove if Flipkart loads fully on page load
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            review_blocks = soup.find_all('div', class_='cPHDOP')

            # Filter out blocks missing key elements
            valid_blocks = [
                block for block in review_blocks
                if block.find('div', class_='XQDdHH') and block.find('p', class_='z9E0IG')
            ]

            if not valid_blocks:
                print("No valid reviews found.")
                break

            for review in valid_blocks:
                rating_div = review.find('div', class_='XQDdHH')
                title_p = review.find('p', class_='z9E0IG')
                comment_div_container = review.find('div', class_='ZmyHeo')
                name_p = review.find('p', class_='_2NsDsF')

                # Skip if any essential field is missing
                if not all([rating_div, title_p, comment_div_container, name_p]):
                    continue

                rating = rating_div.get_text(strip=True)
                title = title_p.get_text(strip=True)

                inner_div = comment_div_container.find('div')
                comment = inner_div.get_text(strip=True) if inner_div else 'No Comment'
                comment = comment.replace('READ MORE', '').strip()

                name = name_p.get_text(strip=True)

                all_reviews.append({
                    'Customer_Name': name,
                    'Review_Title': title,
                    'Rating': rating,
                    'Comment': comment
                })

            # Check for "Next" button to continue
            next_button = soup.find('a', string='Next')
            if not next_button:
                print("Reached last page.")
                break

            page += 1
            time.sleep(0.5)  # Small delay to avoid hitting rate limits

        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    driver.quit()
    return pd.DataFrame(all_reviews)


if __name__ == "__main__":
    url = "https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/product-reviews/itm7c1831ce25509?pid=COMH9ZWQCJGMZGXE"
    df = scrape_flipkart_reviews(url)

    if not df.empty:
        df.to_csv("flipkart_reviews.csv", index=False)
        print(f"\nScraped {len(df)} reviews")
        print("🕒 Time taken:", round(time.time() - start, 2), "seconds")
        print("Saved to flipkart_reviews.csv")
    else:
        print("No reviews found.")
