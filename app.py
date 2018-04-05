from flask import Flask, render_template, request, make_response, redirect
import base64
import json
import os

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    result=request.form
    newresult={}
    for k,v in result.iteritems():
        newresult[k]=v
    createfile(**newresult)
    return redirect("http://localhost:8080/")

def createfile(**result):
    with open('output/simpleci.conf','w') as f:
        f.write(render_template("simpleci.conf.template",
            ggithubURL=str(result.get('ggithubURL')),
            glibraryName=str(result.get('glibraryName')),
            gversion=str(result.get('gversion')),
            bproject=str(result.get('bproject')),
            bserverUrl=str(result.get('bserverUrl')),
            busername=str(result.get('busername')),
            bpassword=base64.b64encode(str(result.get('bpassword')))
            # ausername=str(result.get('ausername')),
            # acredentialsId=str(result.get('acredentialsId')),
            # adescription=str(result.get('adescription')),
            # apassword=base64.b64encode(str(result.get('apassword')))
            ))
    return True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
