from flask import Flask, redirect, url_for, render_template, request, session, Blueprint , flash, make_response



blog_page_bp = Blueprint('blog_page_bp', __name__, template_folder = 'templates')


@blog_page_bp.route("/")
def redirection():
    return render_template("blog_page.html")
