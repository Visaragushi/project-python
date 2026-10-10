from flask import Flask
from db import init_db
from routes.restaurants import restaurants_bp
from routes.tables import tables_bp
from routes.reservations import reservations_bp

app = Flask(__name__)
init_db(app)

app.register_blueprint(restaurants_bp, url_prefix='/api')
app.register_blueprint(tables_bp, url_prefix='/api')
app.register_blueprint(reservations_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask
from db import init_db

app = Flask(__name__)
init_db(app)

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration (make sure you have the correct URL here)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Your models should go here, for example:
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)

if __name__ == "__main__":
    app.run(debug=True)
