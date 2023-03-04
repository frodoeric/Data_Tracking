import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_alembic import Alembic

connex_app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')

app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/xptotracking_ms_people'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

ma = Marshmallow(app)
db = SQLAlchemy(app)
alembic = Alembic(app)


