from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from app.routes import users_routes


load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.register_blueprint(users_routes.bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
