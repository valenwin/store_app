from flask import render_template

from . import products_page


@products_page.route('/', methods=['GET', 'POST'])
def product():
    return render_template('products/view-product.html')
