from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Amazon scraping function
def amazon_data(product_response):
    soup = BeautifulSoup(product_response.content, 'html.parser')
    names = [tag.get_text().strip() for tag in soup.find_all("span", {"class": 'a-size-medium a-color-base a-text-normal'})]
    prices = [tag.get_text().strip() for tag in soup.find_all("span", {"class": 'a-price-whole'})]
    ratings = [tag.get_text().strip().replace('out of 5 stars', '') for tag in soup.find_all("span", {"class": 'a-icon-alt'})]
    rating_counts = []
    for div in soup.find_all("div", {"class": "a-row a-size-small"}):
        rating_count_element = div.find("span", {"class": "a-size-base"})
        if rating_count_element:
            rating_count_text = rating_count_element.get_text().strip()
            rating_count = rating_count_text.split()[0].replace(',', '')
            rating_counts.append(rating_count)
        else:
            rating_counts.append('0')
    original_prices = []
    for span in soup.find_all("span", {"class": "a-price a-text-price"}):
        original_price_span = span.find("span", {"class": 'a-offscreen'})
        if original_price_span:
            original_prices.append(original_price_span.get_text().strip())
        else:
            original_prices.append(None)
    return names, prices, ratings, original_prices, rating_counts

# Snapdeal scraping function
def scrape_snapdeal(product_name):
    base_url = "https://www.snapdeal.com/search?keyword={}&santizedKeyword={}&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
    formatted_product_name = '+'.join(product_name.split())
    url = base_url.format(formatted_product_name, formatted_product_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all("div", class_="product-tuple-listing")
    data = []
    for product in products:
        title = product.find("p", class_="product-title").text.strip()
        price_tag = product.find("span", class_="product-price").text.strip()
        price = int(price_tag.split()[1].replace(',', ''))
        original_price_tag = product.find("span", class_="product-desc-price strike")
        if original_price_tag:
            original_price = int(original_price_tag.text.strip().split()[1].replace(',', ''))
        else:
            original_price = int(price / (1 - int(product.find("div", class_="product-discount").text.strip().split('%')[0]) / 100))
        discount_tag = product.find("div", class_="product-discount")
        if discount_tag:
            discount = int(discount_tag.text.strip().split('%')[0])
        else:
            discount = None
        rating_tag = product.find("div", class_="filled-stars")
        if (rating_tag):
            rating = float(rating_tag['style'].split(":")[-1].split("%")[0]) / 20
        else:
            rating = None
        rating_count_tag = product.find("p", class_="product-rating-count")
        if (rating_count_tag):
            rating_count = int(rating_count_tag.text.strip()[1:-1])
        else:
            rating_count = None
        product_url_tag = product.find("a", class_="dp-widget-link")
        product_url = product_url_tag['href'] if product_url_tag else None
        data.append({
            "Name": title,
            "Price": price,
            "Original_Price": original_price,
            "Discount (%)": discount,
            "Rating": rating if rating else None,
            "Rating_Count": rating_count if rating_count else None,
            "Source": 'Snapdeal',
            "URL": product_url
        })
    df = pd.DataFrame(data)
    return df

# ShopClues scraping function
def shopclue_data(product_response):
    soup = BeautifulSoup(product_response.content, 'html.parser')
    names = [tag.get_text(strip=True) for tag in soup.findAll("h2", {"class": ''})]
    price_elements = soup.findAll("span", {"class": "p_price"})
    price_lines = [price_element.get_text(strip=True) for price_element in price_elements]
    original_price_elements = soup.findAll("span", {"class": "old_prices"})
    original_prices = [original_price_element.get_text(strip=True) if original_price_element.find("span") else None for original_price_element in original_price_elements]
    discount_elements = soup.findAll("span", {"class": "prd_discount"})
    discounts = [discount_element.get_text(strip=True) if discount_element else None for discount_element in discount_elements]
    star_elements = soup.findAll("div", {"class": "rtnrew"})
    stars = []
    for star_element in star_elements:
        star_span = star_element.find("span", {"style": True})
        if star_span:
            width = float(star_span['style'].split(":")[1].replace('px', '').strip())
            stars.append(width / 20)
        else:
            stars.append(None)
    return names, price_lines, original_prices, discounts, stars

# Flipkart scraping function
def scrape_flipkart(product_name):
    base_url = "https://www.flipkart.com/search?q={}"
    formatted_product_name = '+'.join(product_name.split())
    url = base_url.format(formatted_product_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all("div", class_="_1AtVbE")
    data = []
    for product in products:
        title = product.find("a", class_="IRpwTa")
        if not title:
            continue
        title = title.get_text().strip()
        price_tag = product.find("div", class_="_30jeq3")
        if not price_tag:
            continue
        price = int(price_tag.get_text().strip().replace('₹', '').replace(',', ''))
        original_price_tag = product.find("div", class_="_3I9_wc")
        if original_price_tag:
            original_price = int(original_price_tag.get_text().strip().replace('₹', '').replace(',', ''))
        else:
            original_price = price
        discount_tag = product.find("div", class_="_3Ay6Sb")
        if discount_tag:
            discount = int(discount_tag.get_text().strip().replace('% off', ''))
        else:
            discount = 0
        rating_tag = product.find("div", class_="_3LWZlK")
        if rating_tag:
            rating = float(rating_tag.get_text().strip())
        else:
            rating = 0
        rating_count_tag = product.find("span", class_="_2_R_DZ")
        if rating_count_tag:
            rating_count = int(rating_count_tag.get_text().strip().split()[0].replace(',', ''))
        else:
            rating_count = 0
        product_url_tag = product.find("a", class_="_1fQZEK")
        product_url = "https://www.flipkart.com" + product_url_tag['href'] if product_url_tag else None
        data.append({
            "Name": title,
            "Price": price,
            "Original_Price": original_price,
            "Discount (%)": discount,
            "Rating": rating,
            "Rating_Count": rating_count,
            "Source": 'Flipkart',
            "URL": product_url
        })
    df = pd.DataFrame(data)
    return df

# TataCliq scraping function
def scrape_tatacliq(product_name):
    base_url = "https://www.tatacliq.com/search/?searchCategory=all&text={}"
    formatted_product_name = '+'.join(product_name.split())
    url = base_url.format(formatted_product_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all("div", class_="ProductModule__container")
    data = []
    for product in products:
        title = product.find("div", class_="ProductModule__name").get_text().strip()
        price_tag = product.find("span", class_="ProductModule__price")
        if not price_tag:
            continue
        price = int(price_tag.get_text().strip().replace('₹', '').replace(',', ''))
        original_price_tag = product.find("span", class_="ProductModule__mrp")
        if original_price_tag:
            original_price = int(original_price_tag.get_text().strip().replace('₹', '').replace(',', ''))
        else:
            original_price = price
        discount_tag = product.find("span", class_="ProductModule__discount")
        if discount_tag:
            discount = int(discount_tag.get_text().strip().replace('% off', ''))
        else:
            discount = 0
        rating_tag = product.find("span", class_="ProductModule__rating__score")
        if rating_tag:
            rating = float(rating_tag.get_text().strip())
        else:
            rating = 0
        rating_count_tag = product.find("span", class_="ProductModule__rating__count")
        if rating_count_tag:
            rating_count = int(rating_count_tag.get_text().strip().replace('(', '').replace(')', ''))
        else:
            rating_count = 0
        product_url_tag = product.find("a", class_="ProductModule__product-image")
        product_url = "https://www.tatacliq.com" + product_url_tag['href'] if product_url_tag else None
        data.append({
            "Name": title,
            "Price": price,
            "Original_Price": original_price,
            "Discount (%)": discount,
            "Rating": rating,
            "Rating_Count": rating_count,
            "Source": 'TataCliq',
            "URL": product_url
        })
    df = pd.DataFrame(data)
    return df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    product_name = request.form['product']
    base_url = 'https://www.amazon.in'
    url = f'https://www.amazon.in/s?k={product_name}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    base_response = requests.get(base_url, headers=headers)
    cookies = base_response.cookies
    product_response = requests.get(url, headers=headers, cookies=cookies)
    names, prices, ratings, original_prices, rating_counts = amazon_data(product_response)
    min_length = min(len(names), len(prices), len(ratings), len(original_prices), len(rating_counts))
    names = names[:min_length]
    prices = prices[:min_length]
    ratings = ratings[:min_length]
    original_prices = original_prices[:min_length]
    rating_counts = rating_counts[:min_length]
    prices_numeric = [int(price.replace(',', '')) for price in prices]
    original_prices_numeric = [int(original_price.replace('₹', '').replace(',', '')) if original_price else None for original_price in original_prices]
    discounts = [int(round(((original_price - price) / original_price) * 100)) if original_price else None for original_price, price in zip(original_prices_numeric, prices_numeric)]
    source = ['Amazon'] * min_length
    urls = [url] * min_length
    data = {
        'Name': names,
        'Price': prices_numeric,
        'Original_Price': original_prices_numeric,
        'Discount (%)': discounts,
        'Rating': ratings,
        'Rating_Count': rating_counts,
        'Source': source,
        'URL': urls
    }
    df1 = pd.DataFrame(data)
    
    # Scraping data from Snapdeal
    df_snapdeal = scrape_snapdeal(product_name)

    # Scraping data from ShopClues
    base_url = 'https://www.shopclues.com/'
    url = f'https://www.shopclues.com/search?q={product_name}'
    base_response = requests.get(base_url, headers=headers)
    cookies = base_response.cookies
    product_response = requests.get(url, headers=headers, cookies=cookies)
    names, price_lines, original_prices, discounts, stars = shopclue_data(product_response)
    min_length = min(len(names), len(price_lines), len(original_prices), len(discounts), len(stars))
    names = names[:min_length]
    price_lines = price_lines[:min_length]
    original_prices = original_prices[:min_length]
    discounts = discounts[:min_length]
    stars = stars[:min_length]
    prices_numeric = [int(price.replace('₹', '').replace(',', '')) for price in price_lines]
    original_prices_numeric = [int(original_price.replace('₹', '').replace(',', '')) if original_price else None for original_price in original_prices]
    discounts_numeric = [int(discount.replace('% Off', '').strip()) if discount else None for discount in discounts]
    source = ['ShopClues'] * min_length
    urls = [url] * min_length
    data = {
        'Name': names,
        'Price': prices_numeric,
        'Original_Price': original_prices_numeric,
        'Discount (%)': discounts_numeric,
        'Rating': stars,
        'Source': source,
        'URL': urls
    }
    df_shopclues = pd.DataFrame(data)

    # Scraping data from Flipkart
    df_flipkart = scrape_flipkart(product_name)

    # Scraping data from TataCliq
    df_tatacliq = scrape_tatacliq(product_name)

    # Combining all dataframes
    combined_df = pd.concat([df1, df_snapdeal, df_shopclues, df_flipkart, df_tatacliq], ignore_index=True)
    
    # Normalizing and calculating the score
    data = combined_df.fillna(0)
    scaler = MinMaxScaler()
    data[['Price', 'Original_Price', 'Discount (%)', 'Rating', 'Rating_Count']] = scaler.fit_transform(
        data[['Price', 'Original_Price', 'Discount (%)', 'Rating', 'Rating_Count']])
    data['Score'] = data['Rating'] * data['Rating_Count'] * data['Discount (%)'] / data['Price']
    data = data.sort_values(by='Score', ascending=False)

    def recommend_products(data, top_n=5):
        recommended_products = data.head(top_n).copy()
        recommended_products['Price'] = recommended_products['Price'] * (data['Price'].max() - data['Price'].min()) + data['Price'].min()
        recommended_products['Original_Price'] = recommended_products['Original_Price'] * (data['Original_Price'].max() - data['Original_Price'].min()) + data['Original_Price'].min()
        index_list = recommended_products.index.tolist()
        return recommended_products[['Name', 'Score', 'Price', 'Discount (%)', 'Original_Price', 'Source', 'URL', 'Rating', 'Rating_Count']], index_list

    top_products_original, index_list = recommend_products(data, top_n=5)
    specific_rows = combined_df.iloc[index_list]
    return render_template('results.html', tables=specific_rows.to_html(classes='data', header="true", index=False))

if __name__ == '__main__':
    app.run(debug=True)
