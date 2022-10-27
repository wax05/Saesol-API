from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import gov_api

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('main.html')

@app.route('/api/docs')
def docs_page():
    return render_template('docs.html')

@app.route('/api/geb/<date>')
def geb_api(date:int):
    data = gov_api.get_geb_info(date)
    return jsonify(data)
    
@app.route('/api/schinfo/<name>')
def schoolinfo_api(name:str):
    data = gov_api.get_school_info(name)
    return jsonify(data)

@app.route('/api/time/<grade>/<class_>/<date>')
def time_api(grade:int, class_:int, date:int):
    data = gov_api.get_school_time('J10',7531374,grade,class_,date)
    return jsonify(data)

@app.route('/test')
def test():
    return render_template('test.html')