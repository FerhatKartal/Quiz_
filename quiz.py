from flask import Flask,render_template,request
from gevent.pywsgi import WSGIServer
from database import connect_database_sonuclar,connect_database_cevaplar,connect_database_kayit

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    arr=[]
    dogru=0
    if(request.method=='POST'):
        arr.append(request.form["cevap1"])
        arr.append(request.form["cevap2"])
        arr.append(request.form["cevap3"])
        arr.append(request.form["cevap4"])
        arr.append(request.form["cevap5"])
       
        cevaplar=connect_database_cevaplar()

        for i in range(len(cevaplar)):
            if(arr[i]==cevaplar[i]):
                dogru+=(100/len(cevaplar))

        connect_database_kayit(dogru)
        puan=max(connect_database_sonuclar())
        
        return render_template("/quizPage.html",puan=puan)
    else:
        return render_template("quizPage.html")

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('localhost', 5000), app)
    http_server.serve_forever()