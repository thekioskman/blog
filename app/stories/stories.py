from flask import Flask, redirect, url_for, render_template, request, session, Blueprint , flash, make_response


stories_page_bp = Blueprint('stories_page_bp', __name__, template_folder = 'templates')

@stories_page_bp.route("/remedy_story")
def stories():
    return render_template("story_page.html" , page_title = "Stories")


@stories_page_bp.route("/short_stories")
def short_stories():
    return render_template("all_short_stories.html" , page_title = "Short Stories")


@stories_page_bp.route("/chapter1")
def chapter_1():
    return render_template("story_chapter_1.html" , page_title = "Remedy Chapter 1")

@stories_page_bp.route("/chapter2")
def chapter_2():
    return render_template("story_chapter_2.html" , page_title = "Remedy Chapter 2")


@stories_page_bp.route('/toggle_theme/<color>')
def toggle_theme(color):

    response = make_response(redirect(url_for("stories_page_bp.stories")))

    response.set_cookie('theme', color)
    print(color)
    return response