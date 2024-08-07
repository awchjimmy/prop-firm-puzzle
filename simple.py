from helium import *
import time
import json

def login():
    data = {}
    with open('env/credentials.json') as f:
        data = json.load(f)
    
    write(data['user'], into='Username')
    write(data['pass'], into='Password')
    click(Button('Log In'))
    
    # Wait actually 15 secs even if page the page is completely loaded.
    # Or else the script might result in undesire behavior.
    time.sleep(15)

def main():
    # start browser
    start_chrome('https://trade.brightfunded.com/')

    # log in
    login()

    # buy button
    print(Text('BTC/USD').exists())
    print(Button(to_right_of='BTC/USD').is_enabled())

    # stop browser
    kill_browser()
    

main()