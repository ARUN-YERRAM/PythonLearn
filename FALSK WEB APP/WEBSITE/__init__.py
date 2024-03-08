from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjvv gjv'

    from .views import views
    from .path import path

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(path,url_prefix='/')

    
    return app

