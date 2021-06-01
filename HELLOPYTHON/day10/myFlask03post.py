from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    a = request.form.get("a","haha")
    return 'Hello {}'.format(a)

if __name__ == '__main__':
    app.run(debug=True)