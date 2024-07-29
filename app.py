from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

Balance = 5000

@app.route('/', methods = ['GET', 'POST'])
def theCasino():   
    return render_template('index.html', Balance = Balance)

@app.route('/coinflip', methods = ['GET', 'POST'])
def coinFlip():
    coin = ["heads", "tails"]
    didYouWin = 'no!'
    winningSide = ""
    headsOrTails = ""

    if request.method == 'POST':
        headsOrTails = request.form['headsOrTails']
        betAmount = request.form['betAmount']
        winningSide = random.choice(coin)

        if betAmount > Balance:
            errorMessage = "Inusuffciant balance"

        if winningSide == headsOrTails:
            didYouWin = "yes!"
        else:
            didYouWin = "no!"
        
    return render_template('coinFlip.html', url=url_for('coinFlip'), didYouWin = didYouWin, winningSide = winningSide, headsOrTails = headsOrTails, Balance = Balance)

@app.route('/error', methods = ['GET', 'POST'])
def error(): 

    return render_template('error.html', Balance = Balance)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)