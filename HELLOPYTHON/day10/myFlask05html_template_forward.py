from flask import Flask 
from flask import render_template 

app = Flask('__name__') 

@app.route('/') 
def index(): 
    return render_template('myFlask05html_template.html') 

if __name__ == '__main__': 
    app.run() 
    
#html파일이 꼭 templates파일안에 존재해야함