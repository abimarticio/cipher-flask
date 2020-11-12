# Atbash and Caesar Cipher Flask

## Overview

An implementation of Atbash and Caesar cipher algorithm as a Flask application.

## Pre-requisites

This project has the following dependencies,

* Python 3.8.2
* Flask 1.1.2

## Usage

In this repository, we implement the Atbash and Caesar cipher algorithms. To use these algorithms, we have the following view functions:

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
export FLASK_APP=api.py
python -m flask run
```

And head over to 
```
http//127.0.0.1:5000/atbash/encrypt?text=hello
```
