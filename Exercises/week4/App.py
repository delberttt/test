from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "This is the home page"

# todo: create more routes for miners and users of blockchain


if __name__ == '__main__':
    pass
