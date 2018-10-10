from flask import Flask, request

app = Flask(__name__)

miners_list = []


@app.route('/')
def setupServer():
    return str(miners_list)


@app.route('/add/<miner>')
def addNewMiner(miner):
    global miners_list
    if miner not in miners_list:
        miners_list.append(miner)
    return setupServer()


if __name__ == '__main__':
    app.run(port=8080)
