from helium import *
from time import sleep
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
    wait_until(Text('BTC/USD').exists, timeout_secs=10)

def open_long():
    sleep(1)
    rightclick(Text('BTC/USD'))

    sleep(1)
    click(Text('Buy Order'))

    sleep(1)
    click(Text('Send Order'))

    sleep(3)


def close_long():
    sleep(1)
    rightclick(Text('—'))

    sleep(1)
    click(Text('Close Position'))

    sleep(3)

def main():
    # start browser
    start_chrome('https://trade.brightfunded.com/')

    # try to login
    login()

    # open long
    # open_long()

    # close long
    close_long()

    # stop browser
    kill_browser()

main()