from flask import Flask, request
import handlers
import miner
import keyPair

import ecdsa


app = Flask(__name__)


internal_storage = {
    "Public_key": None,
    "Private_key": None,
    "Neighbour_nodes": [],
    "User": None,
}


@app.route('/')
def homePage():
    if internal_storage["Public_key"] is None:
        welcome = "Please log in:"
    else:
        welcome = "Welcome to KDCoin!<br>" \
               "Statistics:<br><br>" \
               "Currently logged in as: {}<br>" \
               "Neighbour nodes registered: {}<br>" \
               "".format(
            internal_storage["Public_key"].to_string().hex(),
            internal_storage["Neighbour_nodes"])

    loginPage = open("Mainpage.html").read()

    return welcome + loginPage


@app.route('/login', methods=['POST'])
def loginAPI():
    pub_hex = request.values.get("pub_key")
    import pdb;pdb.set_trace()
    pub_key = ecdsa.SigningKey(bytes.fromhex(pub_hex))
    internal_storage["Public_key"] = pub_key

    priv_hex = request.values.get("priv_key")
    priv_key = ecdsa.VerifyingKey(bytes.fromhex(priv_hex))
    internal_storage["Private_key"] = priv_key

    internal_storage["User"] = miner.Miner.new(internal_storage["Public_key"])

    # re-routes back to homepage
    return homePage()


@app.route('/new')
def newUser():
    priv, pub = keyPair.GenerateKeyPair()
    internal_storage["Private_key"] = priv
    internal_storage["Public_key"] = pub

    return "Public Key: {}<br>" \
           "Private Key: {}<br>" \
           "Please save these 2 (They are unrecoverable)".\
        format(pub.to_string().hex(), priv.to_string().hex())


@app.route('/blockchain')
def getCurrentBlockchain():
    # this API is here for other miners joining in to request the current blockchain
    return internal_storage["User"].blockchain


@app.route('/pay/<recv_addr>')
def payTo(recv_addr):
    # todo: handler to pay from sender to recv
    sender = internal_storage["Public_key"]
    recv = recv_addr

    pass


# todo: create more routes for miners and users of blockchain


if __name__ == '__main__':
    app.run()
