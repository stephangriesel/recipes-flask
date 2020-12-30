## Overview

This Flask application displays my family's favorite recipes!

## How to Run

In the top-level directory:

```sh
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

## Installation Instructions

Pull down the source code from this GitLab repository:

```sh
git clone git@gitlab.com:patkennedy79/flask-recipe-app.git
```

Create a new virtual environment:

```sh
$ cd flask-recipe-app
$ python3 -m venv venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

## Configuration

TBD

## Key Python Modules Used

* Flask: micro-framework for web application development

This application is written using Python 3.9.0.

## Unit Testing

To run all the tests:

```sh
(venv) $ pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ pytest --cov-report term-missing --cov=project
```
