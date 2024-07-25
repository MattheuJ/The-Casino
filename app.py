from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def theCasino():
    return render_template('index.html')

@app.route('/coinflip', methods = ['GET', 'POST'])
def coinFlip():
    return render_template('coinFlip.html')

@app.route('/error', methods = ['GET', 'POST'])
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)