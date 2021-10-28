from flask import Flask, redirect, url_for, render_template, request, session, Blueprint , flash, make_response
from datetime import datetime

home_page_bp = Blueprint('home_page_bp', __name__, template_folder = 'templates')


@home_page_bp.route("/")
def redirection():
    return redirect(url_for("home_page_bp.home"))

@home_page_bp.route("/home")
def home():
    return render_template("homepage.html")



