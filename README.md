# Atbash and Caesar Cipher Flask

## Overview

An implementation of Atbash and Caesar cipher algorithm as a Flask application.

## Usage

In this repository, Python 3.8.2 was used and it is recommended to create a virtual environment to isolate the dependencies used by this module.
```
$ virtualenv cipher-env
$ source ./cipher-env/Scripts/activate
$ pip install -r requirements.txt
```

We implement the Atbash and Caesar cipher algorithms. To use these algorithms, we have the following view functions:

* `/atbash/encrypt` for Atbash encryption. The request parameter for this function is `text`.
* `/atbash/decrypt` for Atbash decryption. The request parameter for this function is `text`.
* `/caesar/encrypt` for Caesar encryption. The request parameters for this function are `text` and `key`.
* `/caesar/decrypt` for Caesar decryption. The request parameters for this function are `text` and `key`.

To run this app, we can use flask command
```
$ export FLASK_APP=api.py
$ flask run
```

We can also use python -m flask
```
$ export FLASK_APP=api.py
$ python -m flask run
```

or simply use python command
```
$ python api.py
```

And head over to 
```
http//127.0.0.1:5000/atbash/encrypt?text=hello
```

We can also test out our API using curl command
```
$ curl http://localhost:5000/atbash/encrypt?text=hello
```