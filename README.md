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

## License

```
Atbash and Caesar cipher Flask app
Copyright (C) 2020  Abigail Marticio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```