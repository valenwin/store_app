from flask import render_template

from . import products_page
from .models import Product


@products_page.route('product/<product_id>', methods=['GET', 'POST'])
def view_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    return render_template('products/view-product.html',
                           product=product)
