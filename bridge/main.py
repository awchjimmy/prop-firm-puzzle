import pyautogui
import time
from fastapi import FastAPI
from pydantic import BaseModel

# update the co-ordinates to fit your screen
long_button_x, long_button_y = 550, 300
close_button_x, close_button_y = 885, 596
delay_seconds = 0.7

class TradingMessage(BaseModel):
    action: str
    contracts: float
    marketPosition: str
    positionSize: float
    prevMarketPosition: str
    price: float
    symbol: str
    time: str

# fastapi app
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/trading-business/d87fe8c7-fbfa-4104-8230-42a0be573aae")
def trading_business(msg: TradingMessage):
    # Open or close position based on Tradingview signal
    if msg.action == 'buy':
        gui_open_long()
    else:
        gui_close_long()
        
    return {"Hello": "World"}

def gui_open_long():
    pyautogui.moveTo(long_button_x, long_button_y)
    time.sleep(delay_seconds)
    pyautogui.click()
    
def gui_close_long():
    pyautogui.moveTo(close_button_x, close_button_y)
    time.sleep(delay_seconds)
    pyautogui.click()
