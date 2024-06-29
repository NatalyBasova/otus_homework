from flask import Blueprint, render_template, request, send_from_directory
from .utils import *

bp = Blueprint("home", __name__)


@bp.route("/")
def index():
    mc = set_menu("home")
    return render_template("home/index.html",mc=mc)


@bp.route("/about/")
def about():

    mc = set_menu("about")
    return render_template("home/about.html",mc=mc)
