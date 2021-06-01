from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/<a>')
def aParam(a):
    return f'{a}!'
if __name__ == '__main__':
    app.run(debug=True)