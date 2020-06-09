from flask import Blueprint

cart_page = Blueprint('cart_page', __name__)

from app.cart import views