from flask import Flask ,request, render_template, jsonify

app = Flask(__name__,static_url_path='') 

@app.route('/') 
def index(): 
    return 'hello!'

@app.route('/ajax', methods=['POST']) 
def ajax(): 
    data = request.get_json()
    print(data)
    
    return jsonify(result = 'success', result2 = data)

if __name__ == '__main__': 
    app.run(debug=True) 