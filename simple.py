from helium import *
import time
import json

def login():
    # read credentials and login
    data = {}
    with open('env/credentials.json') as f:
        data = json.load(f)
    write(data['user'], into='Username')
    write(data['pass'], into='Password')
    click(Button('Log In'))
    
    # wait until page is fully loaded
    wait_until(Text('BTC/USD').exists, timeout_secs=30)

def open_long():
    sell_button = Button(to_right_of='BTC/USD')
    buy_button = Button(to_right_of=sell_button)

    click(buy_button)

def close_long():
    pass

def main():
    # start browser
    start_chrome('https://trade.brightfunded.com/')

    # try to login
    login()

    # open long
    open_long()

    # close long
    # close_long()

    # debug
    time.sleep(3)

    # stop browser
    kill_browser()

main()