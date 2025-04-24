# Web Scraper Example

This project is a Python-based web scraper designed to demonstrate web scraping skills. The scraper extracts product details, such as title, price, image URL, and product URL, from e-commerce websites like Amazon (used as a sample). It shows how to interact with a website, parse its content, and filter out unwanted results.

**Note:** The scraper is not specifically targeting Amazon, but rather it’s an example of how to use web scraping techniques in Python. The Amazon UK page is used here for demonstration purposes.

## Features

- Scrapes product information from an e-commerce website (Amazon UK in this case).
- Excludes sponsored products.
- Configured headers to prevent blocking by Amazon.

## Requirements

1. **Python 3.x**
2. **Libraries**:
   - `beautifulsoup4`
   - `requests`

To install the necessary libraries, follow the steps below.

## Setup and Installation

### 1. Setting Up the Virtual Environment and Installing Dependencies

To isolate dependencies, it's recommended to use a virtual environment.

````bash
# Navigate to your project folder
cd /path/to/your/project

# Create a virtual environment (you can replace 'scrap_env' with any name)
python3 -m venv scrap_env
source scrap_env/bin/activate

# Install Dependencies
pip install beautifulsoup4 requests

# Run the Scraper
python scraper.py

````

## 2. Discord Integration

This project also integrates with Discord. To use the Discord bot functionality, follow the steps below:

### Create a Discord Bot:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and add a bot.
3. Get the bot token from the "Bot" tab.

### Run the Discord Bot:

The bot listens for a specific message (`!scrape`) to scrape products and send them to your Discord channel.

The bot responds to `!scrape` by scraping product details from Amazon and sends the results as rich embeds to the Discord channel.

Discord reference link below:
[Discord Developers](https://discord.com/developers/build)
[DiscordPy](https://discordpy.readthedocs.io/en/stable/)

