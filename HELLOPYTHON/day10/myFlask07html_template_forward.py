from flask import Flask 
from flask import render_template 

app = Flask('__name__') 

@app.route('/') 
def index(): 
    title = '리스트 보기'
    mylist = ["박예진", "유은지", "정유진", "최윤성"]
    objlist = []
    objlist.append({'e_id':'test01', 'e_name':'박예진', 'birth':'1998'})
    objlist.append({'e_id':'test02', 'e_name':'유은지', 'birth':'1993'})
    return render_template('07reder_list.html', mylist=mylist, title=title, objlist=objlist) 

if __name__ == '__main__': 
    app.run() 
    
#html파일이 꼭 templates파일안에 존재해야함