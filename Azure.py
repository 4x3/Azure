import ccxt
import pandas as pd
import ta  # technical analysis library
import requests
import time
from datetime import datetime
import sys

# Azure Logo and Name
azure_logo = '''
     /\                        
    /  \    _____   _ _ __ ___ 
   / /\ \  |_  / | | | '__/ _ \\
  / ____ \  / /| |_| | | |  __/
 /_/    \_\/___|\__,_|_|  \___|
'''

print(azure_logo)
print("Azure - Crypto Trading Bot\n")

# Binance API keys (Replace these with your own keys)
api_key = 'your_binance_api_key'
api_secret = 'your_binance_api_secret'

# Check if Binance API keys are provided
if not api_key or not api_secret:
    print("Program error: It seems that the user has not provided a Binance API key or secret. Unfortunately, we cannot trade.")
    sys.exit()  # Exit the program if the keys are not provided

# Telegram bot configuration (Replace with your bot's token and chat ID)
telegram_bot_token = 'your_telegram_bot_token'
telegram_chat_id = 'your_chat_id'

# Setup Binance client using ccxt
binance = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

# Function to send Telegram messages
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id}&text={message}'
    requests.get(url)

# Function to calculate RSI and MACD for market analysis
def get_technical_indicators(symbol, timeframe='1h'):
    # Fetch historical market data
    ohlcv = binance.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Calculate RSI (Relative Strength Index)
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    
    # Calculate MACD (Moving Average Convergence Divergence)
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    return df

# Buy decision: Check if the market is oversold and if the MACD is signaling a buy
def should_buy(df):
    if df['rsi'].iloc[-1] < 30 and df['macd'].iloc[-1] > df['macd_signal'].iloc[-1]:
        return True
    return False

# Sell decision: Check if the market is overbought and if the MACD is signaling a sell
def should_sell(df):
    if df['rsi'].iloc[-1] > 70 and df['macd'].iloc[-1] < df['macd_signal'].iloc[-1]:
        return True
    return False

# Function to place a buy or sell order
def execute_order(symbol, side, amount):
    try:
        order = binance.create_market_order(symbol, side, amount)
        send_telegram_message(f'{side.capitalize()} order executed: {order}')
    except Exception as e:
        send_telegram_message(f'Error executing {side} order: {str(e)}')

# Placeholder function for stop-loss and take-profit logic (you can expand it)
def set_stop_loss_take_profit(symbol, stop_loss_pct, take_profit_pct):
    # You can implement stop-loss and take-profit logic here
    pass

# Main trading loop
def main(symbol, amount):
    print("Trading has started... Let's see how the market moves.\n")
    while True:
        df = get_technical_indicators(symbol)
        
        # Check if the bot should buy
        if should_buy(df):
            print("Buying now... RSI is low and MACD is positive.")
            execute_order(symbol, 'buy', amount)
            set_stop_loss_take_profit(symbol, stop_loss_pct=0.02, take_profit_pct=0.05)

        # Check if the bot should sell
        elif should_sell(df):
            print("Selling now... RSI is high and MACD is negative.")
            execute_order(symbol, 'sell', amount)
        
        # Sleep before checking again (e.g., every 10 minutes)
        time.sleep(60 * 10)  # 10 minutes (change if needed)

# Run the bot with specified settings
if __name__ == '__main__':
    symbol = 'BTC/USDT'  # Example trading pair (you can change it)
    amount = 0.001  # Example amount to trade (change as needed)
    
    # Start the bot
    main(symbol, amount)
