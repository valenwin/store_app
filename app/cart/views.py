from flask import session, redirect, url_for, render_template

from . import cart_page
from .forms import AddToCart
from ..products.views import handle_cart


@cart_page.route('/')
def cart():
    products, grand_total, grand_total_plus_shipping, quantity_total = handle_cart()

    return render_template('cart/cart.html',
                           products=products,
                           grand_total=grand_total,
                           grand_total_plus_shipping=grand_total_plus_shipping,
                           quantity_total=quantity_total)


@cart_page.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = []

    form = AddToCart()

    if form.validate_on_submit():
        session['cart'].append({'id': form.id.data, 'quantity': form.quantity.data})
        session.modified = True

    return redirect(url_for('cart_page.cart'))


@cart_page.route('/quick-add/<id>')
def quick_add(id):
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({'id': id, 'quantity': 1})

    session.modified = True

    return redirect(url_for('cart_page.cart'))


@cart_page.route('/remove-from-cart/<id>')
def remove_from_cart(id):
    session['cart'].pop(int(id))
    session.modified = True
    return redirect(url_for('cart_page.cart'))
