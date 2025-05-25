from flask import Flask
import socket

helloworld = Flask(__name__)

@helloworld.route("/")
def run():
    hostname = socket.gethostname()  # gets container/pod hostname
    return {
        "message": "Hello World Python From Jenkins",
        "hostname": hostname
    }

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=5000, debug=True)
