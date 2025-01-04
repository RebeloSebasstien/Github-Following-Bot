# GitHub Auto-Follower Bot

## Description
The GitHub Auto-Follower Bot is a Python script designed to automatically follow a specified number of random GitHub users. Ideal for exploring new developers or expanding your network on GitHub.

## Features
- Authenticate using your GitHub username and token.
- Follow a specific number of random GitHub users.
- Handles API limits to ensure smooth operation.
- Lightweight and easy to use.

## Requirements
- Python 3.7 or higher
- Installed Python libraries:
  - `requests`
  - `colorama`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/github-auto-follower-bot.git
   cd github-auto-follower-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python follow_bot.py
   ```

2. Enter your GitHub username and token.

3. Specify the number of users you want to follow. The bot will automatically find and follow them.

## Example Usage
```plaintext
Please log in with your GitHub credentials.
GitHub Username: your-username
GitHub Token: your-token
Welcome, your-username! Authentication successful.
How many people would you like to follow: 10
Searching 10 random users...
Followed: user1
Followed: user2
Followed: user3
...
```

## Notes
- Ensure your GitHub token has the `user:follow` scope enabled.
- Be mindful of GitHub's rate limits to avoid temporary restrictions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This tool is for educational purposes only. Please use responsibly and adhere to GitHub's terms of service.
