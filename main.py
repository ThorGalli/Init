import time
from coin_fetcher import fetch_prices


def fetch_coins():
    fetch_index = 0  # Initialize fetch index
    while True:
        fetch_index += 1  # Increment fetch index
        print(f"\nStarting fetch #{fetch_index}...")
        fetch_prices()
        print(f"Fetch #{fetch_index} complete. Waiting for 60 seconds...\n")
        time.sleep(10)  # Wait for 60 seconds before the next fetch


if __name__ == "__main__":
    fetch_coins()
