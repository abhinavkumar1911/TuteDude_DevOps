from flask import Flask, request , jsonify
from dotenv import load_dotenv
import os
import pymongo
import json
import bson
from bson.json_util import dumps
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)



load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')
##client = pymongo.MongoClient("mongodb+srv://abhinav:<password>@learn.da9e7l6.mongodb.net/?retryWrites=true&w=majority&appName=learn")
client = pymongo.MongoClient(MONGO_URI)
db = client.learn
collection = db['Assignment-1']
app = Flask(__name__,template_folder='')


@app.route('/submit',methods=['POST'])
def submit():
   
   output = dict(request.json)
   collection.insert_one(output)
   data = list(collection.find())
   json_data = dumps(data,indent=4)
   with open ("data.json","w") as outfile :
      outfile.write(str(json_data))
   
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
    return jsonify(data)




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)