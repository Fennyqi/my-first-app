# my-first-class

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env
```

Install packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
SENDGRID_API_KEY="_____"
SENDER_ADDRESS="example.gmail.com"
```


## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
# python app/unemployment.py
python -m app.unemployment
```
Run the stocks report:


```sh
python -m app.stocks
```


Send an example email:


```sh
python app/email_service.py
```

Enlarge a number by 100:

```sh
python app/my_mod.py
```

Get weather information:


```sh
python app/weatherapp.py
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```