from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    a = request.args.get("a","haha")
    return 'Hello {}'.format(a)

if __name__ == '__main__':
    app.run(debug=True)