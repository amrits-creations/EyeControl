from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates"
    )
    socketio.init_app(app)
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    return app