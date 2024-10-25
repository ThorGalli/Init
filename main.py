import time
from coin_fetcher import fetch_prices


def fetch_coins():
    fetch_index = 0
    while True:
        fetch_index += 1
        print(f"\nStarting fetch #{fetch_index}...")
        fetch_prices()
        print(f"Fetch #{fetch_index} complete. Waiting for 10 seconds...\n")
        time.sleep(10)


if __name__ == "__main__":
    fetch_coins()
