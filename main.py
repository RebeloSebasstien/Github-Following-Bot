import os
import requests
from colorama import Fore, Style, init
import time
import random
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def auth():
    print(Fore.CYAN + "Please log in with your GitHub credentials.")
    username = input(Fore.YELLOW + "GitHub Username: ")
    token = input(Fore.YELLOW + "GitHub Token: ")
    response = requests.get("https://api.github.com/user", auth=(username, token))
    if response.status_code == 200:
        print(Fore.GREEN + f"Welcome, {username}! Authentication successful.")
        return username, token
    else:
        print(Fore.RED + "Authentication failed. Please check your credentials and try again.")
        return None, None
    
def follow(user, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.put(f"https://api.github.com/user/following/{user}", headers=headers)
    if response.status_code == 204:
        print(Fore.GREEN + f"Followed: {user}")
        return True
    else:
        print(Fore.RED + f"Failed: {user}")
        return False

def fetch(token, num):
    headers = {"Authorization": f"token {token}"}
    users = []
    page = 1

    while len(users) < num:
        response = requests.get(f"https://api.github.com/users?per_page=100&page={page}", headers=headers)

        if response.status_code != 200:
            break
        
        nn = [user["login"] for user in response.json()]
        if not nn:
            break

        users.extend(nn)
        page += 1
        time.sleep(1)  # Avoid hitting the rate limit

    return random.sample(users, min(len(users), num))

def main():
    clear()
    username, token = None, None

    while not username or not token:
        username, token = auth()

    clear()

    try:
        num = int(input(Fore.YELLOW + "How many people would you like to follow: "))
        if num <= 0:
            print(Fore.RED + "Please enter a positive number.")
            return

        print(Fore.CYAN + f"Searching {num} random users...")
        u2f = fetch(token, num)

        for user in u2f:
            follow(user, token)
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
