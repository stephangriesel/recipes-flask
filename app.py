from project import create_app, freezer

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()
freezer.freeze()
