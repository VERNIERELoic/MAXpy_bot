# MAXPY BOT FOR SNCF TGVMAX

Author : @Loic VERNIERE

## USE CASE

You can't found a train according to your subscription at MAXJEUNE ? 

Use this bot ! 

**MAXy** will send your email notification when a seat is available based on yout criterials !

## 1.1 Requierement
- Git installed
- Docker/Docker-compose installed
- Internet connection
- Linux OS

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
# clone the priject
git clone https://github.com/VERNIERELoic/MAXpy_bot.git
# Go into the project folder
cd maxpy-bot
# Run the docker compose to start the bot
docker-compose up -d
```

## 1.3 Config file

at the your of the project, edit the ./config/config.ini file to setup your alerts

```ini
[RESEARCH]

DATE = 2022/06/29
FROM = PARIS
TO = LYON
```

To apply modification, you must restart the docker stack as follow : 
```bash
docker-compose restart
```
