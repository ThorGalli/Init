import json
import random
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import selenium


def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def load_existing_prices(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []


def save_prices(file_path, prices):
    with open(file_path, 'w') as f:
        json.dump(prices, f, indent=4)


def fetch_prices():
    print(selenium.__version__)
    config = load_config('config.json')  # Load the config from the JSON file
    BASE_URL = config['BASE_URL']
    COIN_ROUTES = config['COIN_ROUTES']

    prices = load_existing_prices('moeda_precos.json')

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(BASE_URL)
        print("Fetching cryptocurrency prices...")

        total_coins = len(COIN_ROUTES)  # Get the total number of coins

        for index, route in enumerate(COIN_ROUTES):
            coin_name = route[12:-1]
            print(
                f"[{index + 1}/{total_coins}] Fetching price for {coin_name.capitalize()}...")
            driver.get(BASE_URL + route)

            timestamp = datetime.now().isoformat()

            try:
                price_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//span[contains(@class,"price") or @data-test="text-cdp-price-display"]'))
                )
                price = price_element.text.replace('$', '')

                coin_data = next(
                    (item for item in prices if item['coinName'].lower() == coin_name), None)

                if coin_data:
                    coin_data['values'].append({
                        "isoTimeStamp": timestamp,
                        "valueInDollars": price
                    })
                    print(
                        f"L Updated price for {coin_name.capitalize()}: ${price}\n")
                else:
                    prices.append({
                        "coinName": coin_name.capitalize(),
                        "values": [
                            {
                                "isoTimeStamp": timestamp,
                                "valueInDollars": price
                            }
                        ]
                    })
                    print(
                        f"Added new entry for {coin_name.capitalize()}: ${price}")

            except Exception as e:
                print(
                    f"Error fetching price for {coin_name.capitalize()}: {e}")

            time.sleep(random.randint(1, 6))

        print("\nSaving data to JSON file...")
        save_prices('moeda_precos.json', prices)
        print("Data saved successfully!")

    finally:
        driver.quit()
