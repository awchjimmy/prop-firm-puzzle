from helium import *
from time import sleep
import json
from fastapi import FastAPI
from pydantic import BaseModel

class TradingviewSignal(BaseModel):
    action: str
    contracts: str
    marketPosition: str
    positionSize: str
    prevMarketPosition: str
    price: str
    symbol: str
    time: str

app = FastAPI()

def login():
    # read credentials and login
    data = {}
    with open('.env') as f:
        data = json.load(f)
    write(data['user'], into='Username')
    write(data['pass'], into='Password')
    click(Button('Log In'))
    
    # wait until page is fully loaded
    wait_until(Text('BTC/USD').exists, timeout_secs=20)

def open_long():
    # locate "BTC/USD" in watchlist view
    sleep(1)
    rightclick(Text('BTC/USD'))

    sleep(1)
    click(Text('Buy Order'))

    sleep(1)
    click(Text('Send Order'))

    # wait for the popup message
    sleep(3)


def close_long():
    # locate "-" in position view
    sleep(1)
    rightclick(Text('—'))

    sleep(1)
    click(Text('Close Position'))

    # wait for the popup message
    sleep(3)

def tradingview_trigger_buy():
    # start browser
    start_chrome('https://trade.brightfunded.com/', headless=False)

    # try to login
    login()

    # open long
    open_long()

    # stop browser
    kill_browser()

def tradingview_trigger_sell():
    # start browser
    start_chrome('https://trade.brightfunded.com/', headless=False)

    # try to login
    login()

    # close long
    close_long()

    # stop browser
    kill_browser()

@app.post("/tradingview-signal/a46bac4c-ded8-498b-b49f-80d2c5e7fd92")
def handle_signal(signal: TradingviewSignal):
    if signal.action == 'buy':
        tradingview_trigger_buy()
    elif signal.action == 'sell':
        tradingview_trigger_sell()
    else:
        print('Unknown action from tradingview.')
