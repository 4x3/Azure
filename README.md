# Azure - Crypto Trading Bot

### 🚀 **Azure** - Automated Crypto Trading Bot Using Binance API

A customizable crypto trading bot built with Python. The bot uses **RSI** and **MACD** indicators for trading decisions and implements **stop-loss** and **take-profit** functionality to manage risk. Get alerts via **Telegram** for each trade.

---

### **Features**:

- **Customizable Trading Strategy**: 
  - Uses **RSI** and **MACD** indicators to make buy and sell decisions.
  - Buys when **RSI** is below 30 and **MACD** signals a crossover, and sells when **RSI** is above 70 and **MACD** signals a reversal.
  
- **Risk Management**:
  - Set **stop-loss** and **take-profit** percentages to automatically secure profits and limit losses.
  
- **Telegram Alerts**: 
  - Receive **trade updates** and **alerts** via **Telegram** for every buy and sell action.
  
- **Real-Time Trading**:
  - Trades based on **Binance API**, placing market buy and sell orders in real time.

- **Customizable**:
  - Easily modify trading pairs, timeframe, and risk parameters.
  - Designed to be extended for other strategies or additional features.

---

### **How to Get it Working**:

#### **Step 1: Set Up Your Binance API Keys**

1. Log in to your [Binance account](https://www.binance.com/).
2. Navigate to **API Management** and create a new API key. 
3. Save your **API Key** and **Secret Key**.
4. Enable **Spot Trading** permissions and **Read Info** permissions.

#### **Step 2: Set Up Your Telegram Bot**

1. Open **Telegram** and go to **BotFather**.
2. Create a new bot and save the **Bot Token**.
3. To get your **Chat ID**:
   - Start a chat with your bot.
   - Visit `https://api.telegram.org/bot<Your_Bot_Token>/getUpdates` to find your chat ID.

#### **Step 3: Install Dependencies**

You’ll need to install a few libraries to run the bot:

```bash
pip install ccxt pandas ta requests
