from flask import Blueprint, render_template, request


bp = Blueprint("order", __name__, url_prefix="/order")


@bp.route("/<int:transaction_id>")
def order(transaction_id):
    return render_template("order.html", transaction_id=transaction_id)


@bp.route("/make-order", methods=["POST"])
def make_order():
    if request.method == "POST":
        transaction_id = None
        user_id = None
        menu_id = None
        ordered = True
