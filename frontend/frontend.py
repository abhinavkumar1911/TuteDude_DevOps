from flask import Flask,render_template,request
import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BACKEND_URL = 'http://host.docker.internal:8000'
 ##or 'http://host.docker.internal:8000'
ENDPOINT='/submit'
BREAKPOINT = '/view'



app = Flask(__name__,template_folder='')

@app.route('/')
def home():
    return render_template('Signup.html')

@app.route('/submit',methods=['POST'])
def submit():
    output = dict(request.form)
    requests.post(BACKEND_URL + ENDPOINT, json=output)
    with open ('data.json','w') as json_file:
        print(output,json_file)
    return 'Data Submitted Successfully !'

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL+BREAKPOINT)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
        return response.json()
    
    
    #return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)