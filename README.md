# azure - crypto trading bot

### 🚀 **azure** - automated crypto trading bot using binance api

a customizable crypto trading bot built with python. the bot uses **rsi** and **macd** indicators for trading decisions and implements **stop-loss** and **take-profit** functionality to manage risk. get alerts via **telegram** for each trade.

---

### **features**:

- **customizable trading strategy**: 
  - uses **rsi** and **macd** indicators to make buy and sell decisions.
  - buys when **rsi** is below 30 and **macd** signals a crossover, and sells when **rsi** is above 70 and **macd** signals a reversal.
  
- **risk management**:
  - set **stop-loss** and **take-profit** percentages to automatically secure profits and limit losses.
  
- **telegram alerts**: 
  - receive **trade updates** and **alerts** via **telegram** for every buy and sell action.
  
- **real-time trading**:
  - trades based on **binance api**, placing market buy and sell orders in real time.

- **customizable**:
  - easily modify trading pairs, timeframe, and risk parameters.
  - designed to be extended for other strategies or additional features.

---

### **how to get it working**:

#### **step 1: set up your binance api keys**

1. log in to your [binance account](https://www.binance.com/).
2. navigate to **api management** and create a new api key. 
3. save your **api key** and **secret key**.
4. enable **spot trading** permissions and **read info** permissions.

#### **step 2: set up your telegram bot**

1. open **telegram** and go to **botfather**.
2. create a new bot and save the **bot token**.
3. to get your **chat id**:
   - start a chat with your bot.
   - visit `https://api.telegram.org/bot<your_bot_token>/getupdates` to find your chat id.

#### **step 3: install dependencies**

you’ll need to install a few libraries to run the bot:

```bash
pip install ccxt pandas ta requests
