from flask import Flask, request
from Exercises.week4 import handlers

app = Flask(__name__)


internal_storage = {
    "Public_key": "Default",
    "Private_key": "Default",
    "Neighbour_nodes": []
}


@app.route('/')
def homePage():
    welcome = "Welcome to KDCoin!<br>" \
           "Statistics:<br><br>" \
           "Currently logged in as: {}<br>" \
           "Neighbour nodes registered: {}<br>" \
           "".format(
        internal_storage["Public_key"],
        internal_storage["Neighbour_nodes"])

    if internal_storage["Public_key"] == "Default":
        welcome = "Please log in:"

    loginPage = open("Mainpage.html").read()

    return welcome + loginPage


@app.route('/login', methods=['POST'])
def loginAPI():
    internal_storage["Public_key"] = request.values.get("pub_key")
    internal_storage["Private_key"] = request.values.get("priv_key")

    # re-routes back to homepage
    return homePage()


@app.route('/new')
def newUser():
    pub, priv = handlers.createNewKeyPair()
    return "Public Key: {}<br>" \
           "Private Key: {}<br>" \
           "Please save these 2 (They are unrecoverable)".format(pub, priv)


@app.route('/pay/<recv_addr>')
def payTo(recv_addr):
    # todo: handler to pay from sender to recv
    pass


# todo: create more routes for miners and users of blockchain


if __name__ == '__main__':
    app.run()
