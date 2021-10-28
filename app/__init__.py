from flask import Flask
from flask.helpers import url_for
from flask_pymongo import PyMongo


def init_app():
    app = Flask(__name__ , instance_relative_config=False)
    app.config.from_object("config.Config")
    
    #app core
    with app.app_context():
        #import all files that are needed for the application
        from app.home import home
        from app.stories import stories
        from app.blog import blog

        #load all the blueprints
        app.register_blueprint(home.home_page_bp, url_prefix = '/')
        app.register_blueprint(stories.stories_page_bp , url_prefix = '/stories' )
        app.register_blueprint(blog.blog_page_bp , url_prefix = '/blog')

        return app