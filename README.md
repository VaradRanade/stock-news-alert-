# stock-news-alert-
# 📈 Stock Trading News Alert

An automated Python tool that monitors stock price volatility and tracks down relevant context. Whenever a specified stock ticker rises or falls by more than 1% compared to its previous closing price, the script instantly searches for and surfaces the top 3 relevant breaking news articles.

## ✨ Features
- **Volatility Tracking**: Automatically tracks stock movements using real-time opening/closing differentials.
- **Automated Article Selection**: Filters news outputs to isolate relevant, active headlines.
- **De-duplication & Formatting**: Cleans up identical headlines and structures them into highly readable visual cards.
- **Security-First Design**: Completely sanitizes system logs to hide private tokens and safely structures parameters using `python-dotenv`.

## 🛠️ Tech Stack
- **Language**: Python 3.14+
- **APIs**: [Alpha Vantage](https://alphavantage.co) (Stock Prices), [NewsAPI](https://newsapi.org) (Financial News Headlines)

## 🚀 Installation & Setup

1. **Clone the repository** (or download the source files):
   ```bash
   git clone https://github.com
   cd stock-news-alert
   ```

2. **Install the required packages**:
   ```bash
   pip install requests python-dotenv
   ```

3. **Configure Environment Variables**:
   Create a hidden file named `.env` in the root of your project directory to store your private API keys:
   ```text
   STOCK_API_KEY=your_alpha_vantage_key_here
   NEWS_API_KEY=your_news_api_key_here
   ```

4. **Run the program**:
   ```bash
   python main.py
   ```

## 🔒 Security Configuration
This repository utilizes a `.gitignore` profile mapping to permanently block `.env` credential files from syncing to public web servers. Never hardcode live secrets into your `main.py` control loop.
