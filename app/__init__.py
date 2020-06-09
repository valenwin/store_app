from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app import config

app = Flask(__name__)
Bootstrap(app)

app.config.from_object(config.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='Store App', template_mode='bootstrap3')

# Blueprints
from .products import products_page
from .cart import cart_page

# Register Blueprints
app.register_blueprint(products_page, url_prefix='/products')
app.register_blueprint(cart_page, url_prefix='/cart')

from . import views
from .products import views, models
from .cart import views

# Admin register
from app.products.models import Product
admin.add_view(ModelView(Product, db.session))
