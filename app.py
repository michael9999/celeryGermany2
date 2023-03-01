import os
from flask import Flask, flash, render_template, redirect, request, jsonify
from tasks import add, runFullSearch
import json
# testing, testing

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', "super-secret")


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/add', methods=['POST'])
def add_inputs():
    x = int(request.form['x'] or 0)
    y = int(request.form['y'] or 0)
    add.delay(x, y)
    flash("Your addition job has been submitted.")
    return redirect('/')


# my changes from here

@app.route('/fullSearch', methods=['POST'])
def goFullSearch():

    headers = request.headers
    auth = headers.get("X-Api-Key")

    if auth == 'asoidewfoef':
        print("goFullSearch running")

        searchpapi = request.get_json().get('searchname', '')

        #searchname = (searchpapi,)
        #testVar = "michael"
        #task = run_FullSearch.apply_async(searchname, countdown=10)
        runFullSearch.delay(searchpapi)

        #task = run_FullSearch.apply_async(countdown=10)
      
        test_id = "done"

        return test_id

    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    
    return "done"