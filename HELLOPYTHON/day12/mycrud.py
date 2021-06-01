from flask import Flask ,request, render_template, jsonify
from day12.mydao_exam import DaoExam

app = Flask(__name__,static_url_path='') 

@app.route('/') 
@app.route('/list')
def list(): 
    dex = DaoExam()
    mylist = dex.myselect()
    return render_template('examlist.html',mylist=mylist)
@app.route('/add.ajax' ,methods=['POST'])
def ajax_add():
    p = request.get_json()
    dex = DaoExam()
    cnt = dex.myinsert(p['e_id'], p['kor'], p['eng'], p['math'])
    msg = ""
    
    if cnt == 1:
        msg = "ok"
    else :
        msg = "ng"
        
    return jsonify(msg = msg)

@app.route('/upd.ajax' ,methods=['POST'])
def ajax_upd():
    p = request.get_json()
    dex = DaoExam()
    cnt = dex.myupdate(p['kor'], p['eng'], p['math'], p['e_id'])
    msg = ""
    
    if cnt == 1:
        msg = "ok"
    else :
        msg = "ng"
        
    return jsonify(msg = msg)

@app.route('/del.ajax' ,methods=['POST'])
def ajax_del():
    p = request.get_json()
    dex = DaoExam()
    cnt = dex.mydelete(p['e_id'])
    msg = ""
    
    if cnt == 1:
        msg = "ok"
    else :
        msg = "ng"
        
    return jsonify(msg = msg)

if __name__ == '__main__': 
    app.run(debug=True) 