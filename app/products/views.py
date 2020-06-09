from flask import render_template, session

from app.cart.forms import AddToCart
from . import products_page
from .models import Product


@products_page.route('product/<product_id>', methods=['GET', 'POST'])
def view_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    form = AddToCart()
    return render_template('products/view-product.html',
                           product=product,
                           form=form)


def handle_cart():
    products = []
    grand_total = 0
    index = 0
    quantity_total = 0

    for item in session['cart']:
        product = Product.query.filter_by(id=item['id']).first()

        quantity = int(item['quantity'])
        total = quantity * product.price
        grand_total += total

        quantity_total += quantity

        products.append({'id': product.id,
                         'name': product.name,
                         'price': product.price,
                         'image': product.image,
                         'quantity': quantity,
                         'total': total,
                         'index': index})
        index += 1

    grand_total_plus_shipping = grand_total + 1000

    return products, grand_total, grand_total_plus_shipping, quantity_total
