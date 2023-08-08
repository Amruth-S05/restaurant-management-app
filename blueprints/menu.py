from flask import Blueprint, render_template


bp = Blueprint("item", __name__, url_prefix="/item")


@bp.route("/<int:item_id>")
def item(item_id):
    item_name, item_price = None, None  # get from database
    return render_template("item.html",
                           item_name=item_name,
                           item_price=item_price
                           )
