from flask import Flask
from app.util.util import gzipped


# Define the WSGI application object
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 2628000           # This caches all static files (1 month)
app.config.from_object('config')


# Import a module / component using its blueprint handler variable (labels) -> Import all the controllers
from app.db.database import db_setup as database_route
from app.sunburst.main import sunburst as sunburst_route
from app.queries.main import queries as queries_route
from app.util.compress import compress as static_compress


# Register blueprint(s)
app.register_blueprint(database_route)                         # ZeiDB database
app.register_blueprint(sunburst_route)                         # Sunburst Pie routes
app.register_blueprint(queries_route)                          # Dashboard queries route
app.register_blueprint(static_compress)                        # Compressing static files
