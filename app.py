from flask import Flask, request, Response, send_file, render_template, flash, redirect, url_for, jsonify
import yolo
import io
from PIL import Image
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import base64
import json
import urllib.request
from io import BytesIO
from azure.storage.blob import BlockBlobService, PublicAccess
import uuid
app = Flask(__name__)

block_blob_service = BlockBlobService(account_name='aarav', account_key='ST3HKEuuKnxOInnZ3sODhrmjT7BawHJTSANOlqTCRWIP6/jj8uBFRROYehub9XPB+WIez/vTsV+zYnny5+XvJQ==')

yolo.YOLO._defaults['model_path']='model_data/yolo-openimages.h5'
yolo.YOLO._defaults['classes_path']='model_data/openimages.names'
yolo.YOLO._defaults['anchors_path']='model_data/yolo_anchors.txt'
model = yolo.YOLO()

@app.route('/', methods=['POST', 'GET'])
def index():
     return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/prediction/image', methods=['POST'])
def image_prediction():
    file = request.files['file']
    try:
        image = Image.open(file)
    except:
        return str("Image Error")
    else:
        image,objects = model.detect_image(image)
        image.save("output.jpg")
        return send_file("output.jpg",mimetype='image/jpeg')
   
@app.route('/predict',methods=['POST'])
def predict():
    file = request.files['file']
    try:
        image = Image.open(file)
    except:
        return str("Image Error")
    else:
        image,objects = model.detect_image(image)
        image.save("output.jpg")
        guid = uuid.uuid1()
        filename = str(guid) + "output.jpg"
        block_blob_service.create_blob_from_path("images",filename, "output.jpg")
        d = {}
        d["image"] = block_blob_service.make_blob_url("images",filename)
        d["objects"] = objects
        r = json.dumps(d)
        return r
if __name__ == '__main__':    
    # app.run(debug=True)
    app.run(host='0.0.0.0')
# app.run(debug=True)
