from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from flask_migrate import Migrate

BASE_DIR = Path(__file__).parent

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'students.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Learner(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    final_test = db.Column(db.Boolean, nullable=False)

    def __repr__(self) -> str:
        return f"Learner({self.id}: {self.name}|{self.final_test})"



if __name__ == '__main__':
    app.run(debug=True)