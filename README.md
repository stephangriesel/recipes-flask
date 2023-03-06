## Overview

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

## Run the Development Server

Run development server to serve the Flask application:

```sh
(venv) $ flask --app app --debug run
```

Navigate to 'http://127.0.0.1:5000/' in your favorite web browser to view the website!

## Key Python Modules Used

- **Flask**: micro-framework for web application development which includes the following dependencies:
  - click: package for creating command-line interfaces (CLI)
  - itsdangerous: cryptographically sign data
  - Jinja2: templating engine
  - MarkupSafe: escapes characters so text is safe to use in HTML and XML
  - Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server
- **Frozen-Flask** - generates static files from Flask routes
- **Markdown** - text-to-HTML conversion tool
- **pytest**: framework for testing Python projects
- **pytest-cov**: pytest extension for running coverage.py to check code coverage of tests
- **flake8**: static analysis tool

This application is written using Python 3.11.0.

## Unit Testing

To run all the tests:

```sh
(venv) $ python -m pytest
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project
```

## Adding a New Recipe

1. Add the new image to _project/static/img/_.
2. Copy _project/recipes/template/markdown/recipe_starter.md_ to a new file in the same directory with the recipe name as the filename.
3. Update the new _project/recipes/template/markdown/<recipe_name>.md_ file with the recipe description, ingredients, and steps.
4. Generate the HTML file for the new recipe:

```sh
$ python project/recipes/templates/md_to_html.py
```

5. Add a new section to the applicable recipe section HTML file (i.e. _project/recipes/template/recipes/baked_good.html_, _project/recipes/template/recipes/dinner.html_, etc.).
6. Add the recipe name to the top of _project/recipes/routes.py_.
7. Update the number of recipes for the applicable recipe section in _project/recipes/template/recipes/recipes.html_.

Lastly, run the tests to make sure everything is working as expected:

```sh
(venv) $ python -m pytest
```

### Build the Static Files

In the top-level directory, run the build script:

```sh
(venv) $ python build.py
```

The static files are generated in the _/project/build/_ directory, which can then be hosted on Netlify.
