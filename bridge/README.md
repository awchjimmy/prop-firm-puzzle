# How to set up localtunnel

### Official guide
1. https://localtunnel.me/
2. https://github.com/localtunnel/localtunnel

----

### Install
```sh
npm install -g localtunnel
```

### Run
1. Start your server behind firewall
```sh
./start-server.sh
```

2. Start localtunnel
```sh
lt --port 8000
```

3. Copy and paste into Tradingview
```sh
# example endpoint
https://all-ducks-tell.loca.lt/trading-business/d87fe8c7-fbfa-4104-8230-42a0be573aae

# example message
{"action":"{{strategy.order.action}}","contracts":"{{strategy.order.contracts}}","marketPosition":"{{strategy.market_position}}","positionSize":"{{strategy.position_size}}","prevMarketPosition":"{{strategy.prev_market_position}}","price":"{{close}}","symbol":"{{ticker}}","time":"{{timenow}}"}
```
