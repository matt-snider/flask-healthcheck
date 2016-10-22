# flask-healthcheck
Flask-Healtcheck is a [Flask](http://flask.pocoo.org/) extension that provides
a simple way of adding healthchecks to a service.

## Example:
```python
from flask import Flask
app = Flask(__name__)
healthcheck = HealthCheck(app)

@app.route('/')
def hello_world():
    return 'Hello world!'


@healthcheck
def connections():
    if len(connections) < 5:
        return False, 'Less than 5 active connections'
    else:
        return True
```

Making a request against this endoint will return a 200 status code and the
following output when the healthcheck passes:
```json
{
  "connections": {
    "healthy": true,
  }
}
```

And, the following if the healthcheck fails:
```json
{
  "connections": {
    "healthy": true,
    "message": "Less than 5 active connections"
  }
}
```

## Built-in Healthchecks
Healthchecks for some popular Flask extensions are already built in and just
need to be activated:
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
healthcheck.add_extension('sqlalchemy', db)
```
Here it's important to call `add_extension()` with the proper extension name
and the extension object.

