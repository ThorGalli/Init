import time
import threading
from coin_fetcher import fetch_prices
from colorama import init, Fore, Style

# Initialize colorama
init()

auto_fetcher_started = f"\n{Fore.CYAN}|-|-| Auto Fetcher started |-|-|{Style.RESET_ALL}\n"
exit_info = f"{Fore.YELLOW}| You can press [Enter] any time to return to the menu |{Style.RESET_ALL}\n"

stop_event = threading.Event()  # Create a threading event to control the loop


def display_progress_bar(seconds):
    bar_length = 40  # Length of the progress bar
    for i in range(seconds):
        if stop_event.is_set():  # Check if the stop event is set
            break
        time.sleep(1)
        filled_length = int(bar_length * (i + 1) // seconds)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f'\r|{bar}| {i + 1}/{seconds} seconds', end='')
    print()  # New line after the bar completes


def input_handler():
    input()  # Wait for Enter key press
    stop_event.set()  # Set the event to stop the progress bar


def fetch_coins():
    while True:
        print(f"{Fore.GREEN}\nStarting fetch...{Style.RESET_ALL}")
        fetch_prices()
        print(
            f"{Fore.GREEN}Fetch complete. Waiting for 60 seconds...{Style.RESET_ALL}\n")
        print(exit_info)

        # Start the progress bar in a separate thread
        progress_thread = threading.Thread(
            target=display_progress_bar, args=(60,))
        progress_thread.start()

        # Start the input handler in a separate thread
        input_thread = threading.Thread(target=input_handler)
        input_thread.start()

        # Wait for the progress thread to finish
        progress_thread.join()
        input_thread.join()  # Ensure the input thread has completed

        if stop_event.is_set():  # Check if the stop event was triggered
            print(f"{Fore.GREEN}Fetching stopped.{Style.RESET_ALL}")
            break

        print(f"{Fore.GREEN}Resuming fetching...{Style.RESET_ALL}")


def start_fetching():
    global fetching
    fetching = True
    fetch_thread = threading.Thread(target=fetch_coins)
    fetch_thread.start()

    input(auto_fetcher_started)

    fetching = False
    stop_event.set()  # Signal to stop the fetching
    fetch_thread.join()
    print(f"{Fore.RED}Fetching stopped.{Style.RESET_ALL}")


def coin_stats():
    print(f"{Fore.MAGENTA}Coin stats feature is not yet implemented.{Style.RESET_ALL}")


def pretty_print_menu():
    menu_border = Fore.BLUE + "=" * 30 + Style.RESET_ALL
    print(menu_border)
    print(f"{Fore.YELLOW}{' ' * 5}=== Main Menu ==={' ' * 5}{Style.RESET_ALL}")
    print(menu_border)
    print(f"{Fore.CYAN}| 1. Start Fetching!          |{Style.RESET_ALL}")
    print(f"{Fore.CYAN}| 2. Coin Stats               |{Style.RESET_ALL}")
    print(f"{Fore.CYAN}| 0. Exit                     |{Style.RESET_ALL}")
    print(menu_border)


def main_menu():
    while True:
        pretty_print_menu()
        choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")

        if choice == '1':
            start_fetching()
        elif choice == '2':
            coin_stats()
        elif choice == '0':
            print(f"{Fore.RED}Exiting program. Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    fetching = False
    main_menu()
