from flask import Blueprint, render_template, request, send_from_directory

bp = Blueprint("home", __name__)


@bp.route("/")
def index():

    return render_template("home/index.html")


@bp.route("/about")
def about():

    return render_template("home/about.html")
