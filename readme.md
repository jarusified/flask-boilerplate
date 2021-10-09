# Flask Boilerplate
A react-native powered mobile application to prevent street cleaning and parking
tickets.

# Backend 

## Requirements
Python3.8 or greater, pip==21.2.4, virtualenv (optional for cleaner environment).

## Install and setup.
Recommendation: Use Python's virtualenv to avoid unnecessary package version conflicts.

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Server
By default, we will fetch APP_PORT from environment. If not specified, default
port is 5000

```
python3 main.py --http {APP_PORT}
```
