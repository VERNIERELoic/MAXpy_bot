# MAXPY BOT FOR SNCF TGVMAX

Author : @Loic VERNIERE

## USE CASE

You can't found a train according to your MAXJEUNE subscription ? 

Use this bot ! 

**MAXy** will send telegram notification when a seat is available based on yout criterials !

## 1.1 Requierement
- Git
- Docker/Docker-compose
- Internet connection

import list : 
```py
import json, telegram, sys, os, requests, configparser
```
package list : 
```py
json
python-telegram-bot
requests
configparser
```


## 1.2 Deploy

```bash
# clone the project
git clone https://github.com/VERNIERELoic/MAXpy_bot.git
# Go into the project folder
cd maxpy-bot
# Run the docker compose to start the bot
docker-compose up -d
```

## 1.3 Config file

at the your of the project, edit the ./config/config.ini file to setup your alerts

```ini
[TRAVEL1]
DATE = 2022/07/01
FROM = PARIS
TO = LYON

[TRAVEL2]
DATE = 2022/07/03
FROM = PARIS
TO = LYON
```

To apply modification, you must restart the docker stack as follow : 
```bash
docker-compose restart
```
