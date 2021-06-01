from flask import Flask 
from flask import render_template 

app = Flask('__name__') 

@app.route('/') 
def index(): 
    title = '리스트 보기'
    mylist = ["박예진", "오승엽", "박새봄", "박혁순"]
    return render_template('06reder_list.html', mylist=mylist, title=title) 

if __name__ == '__main__': 
    app.run() 
    
#html파일이 꼭 templates파일안에 존재해야함