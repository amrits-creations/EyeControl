from app import create_app, socketio

app = create_app()

if __name__ == "__main__":
    # Bind to localhost so you can browse to http://127.0.0.1:5000
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)