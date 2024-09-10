from flask import Flask, request,render_template
from dotenv import load_dotenv
import os
import pymongo
from bson import json_util, ObjectId
import json



load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')
##client = pymongo.MongoClient("mongodb+srv://abhinav:<password>@learn.da9e7l6.mongodb.net/?retryWrites=true&w=majority&appName=learn")
client = pymongo.MongoClient(MONGO_URI)
db = client.learn
collection = db['Assignment-1']
app = Flask(__name__,template_folder='FrontEnd')


@app.route('/')
def home():
    return render_template('Signup.html')

@app.route('/submit',methods=['POST'])
def submit():
   
   ##output = request.form.to_dict()
   ##email = output["email"]
   ##psw = output["psw"]

    #password = request.form.get(password)
   ##return render_template('submit.html',email = email,password = psw)
   #return 'Hello, ' +email+'!'
   output = dict(request.form)
   collection.insert_one(output)
   return 'data submitted successfully'
@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
     print(item)
     del item ['_id']
     data ={
        'data' : data
     }
    return data



if __name__ == '__main__':
    app.run(debug=True)