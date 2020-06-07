from flask import Blueprint

products_page = Blueprint('products_page', __name__)

from app.products import views