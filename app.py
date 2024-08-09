from flask import Flask, render_template, request, url_for
import random
import json

app = Flask(__name__)

with open('something.json', 'r') as file:
    balanceData = json.load(file)
    balance = balanceData["balance"]

@app.route('/', methods = ['GET', 'POST'])
def theCasino():   
    return render_template('index.html', balance = balance)

@app.route('/coinflip', methods = ['GET', 'POST'])
def coinFlip():

    from app import balance
    from app import balanceData

    coin = ["heads", "tails"]
    didYouWin = 'no!'
    winningSide = ""
    headsOrTails = ""

    if request.method == 'POST':
        headsOrTails = request.form['headsOrTails']
        betAmount = int(request.form['betAmount'])
        winningSide = random.choice(coin)

        with open('something.json', 'r') as file:
            balanceData = json.load(file)
            balance = balanceData["balance"]


        
        with open("something.json") as file:
            balanceData = json.load(file)
            balanceData["betAmount"] = betAmount

        with open('something.json', 'w') as file:
                json.dump(balanceData,  file, indent=4)
        

        if betAmount > balance:
            didYouWin = "Insuficiant balance!"
        elif betAmount < 0:
            didYouWin = "No neagtive valiues!"
        elif winningSide == headsOrTails:
            didYouWin = "yes!"
            with open('something.json') as file:
                balanceData = json.load(file)
                balanceData["balance"] = balance + betAmount
            
            with open('something.json', 'w') as file:
                json.dump(balanceData,  file, indent=4)

        elif winningSide != headsOrTails:
            didYouWin = "no!"
            with open('something.json') as file:
                balanceData = json.load(file)
                balanceData["balance"] = balance - betAmount
            
            with open('something.json', 'w') as file:
                json.dump(balanceData,  file, indent=4)
        
        balance = balanceData["balance"]
            
        
    return render_template('coinFlip.html', url=url_for('coinFlip'), didYouWin = didYouWin, winningSide = winningSide, headsOrTails = headsOrTails, balance = balance)

@app.route('/error', methods = ['GET', 'POST'])
def error(): 

    return render_template('error.html', balance = balance)

@app.route('/addfunds', methods = ['GET', 'POST'])
def addFunds():   

    from app import balance
    from app import balanceData  

    if request.method == "POST":
        
        amountAdded = int(request.form['amountAdded'])

        with open("something.json") as file:
            balanceData = json.load(file)
            balanceData["balance"] = balance + amountAdded

        with open('something.json', 'w') as file:
                json.dump(balanceData,  file, indent=4)

    return render_template('addFunds.html', url = url_for, balance = balance, amountAdded = amountAdded )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)