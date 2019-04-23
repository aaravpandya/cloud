from flask import Flask, request, Response, send_file, render_template, flash, redirect, url_for
import yolo
import io
from PIL import Image
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import base64
import json
import urllib.request
from multiprocessing import Process, Value
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
     return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')



yolo.YOLO._defaults['model_path']='model_data/yolo-openimages.h5'
yolo.YOLO._defaults['classes_path']='model_data/openimages.names'
yolo.YOLO._defaults['anchors_path']='model_data/yolo_anchors.txt'
model = yolo.YOLO()
# queue_service = QueueService(account_name="aarav", account_key="ePdwFBIcH0vLcsYSEdKsslt+d2CpM1YRSDN6ZHtkYh5J9xE06Ebj5pSXFhcV15QkG2xm8EXVsxQwo3NxFh9hLA==")
# block_blob_service = BlockBlobService(account_name='aarav', account_key='ePdwFBIcH0vLcsYSEdKsslt+d2CpM1YRSDN6ZHtkYh5J9xE06Ebj5pSXFhcV15QkG2xm8EXVsxQwo3NxFh9hLA==')




    
@app.route('/prediction/image', methods=['POST'])
def image_prediction():
    file = request.files['file']
    try:
        image = Image.open(file)
    except:
        return str("Image Error")
    else:
        image = model.detect_image(image)
        image.save("output.jpg")
        return send_file("output.jpg",mimetype='image/jpeg')
   

# @app.route('/prediction/imagequeue', methods=['GET'])
# def checkQueue(checkQueue_on):
#         while True:
           
#             # queue_service.put_message("jsonqueue","hello world")
#             messages = queue_service.get_messages('jsonqueue', num_messages=1, visibility_timeout=5*60)
#             print(True)
#             d = {}
            
#             for message in messages:
#                 d = json.loads(QueueMessageFormat.text_base64decode(message.content))
#                 print(d["uri"])
#                 urllib.request.urlretrieve(d["uri"], "1.jpg")
#                 image = Image.open("1.jpg")
#                 image = model.detect_image(image)
#                 image.save("output.jpg")
#                 block_blob_service.create_blob_from_path("detectedimages",d["guid"], "1.jpg")
#                 queue_service.delete_message("jsonqueue",message.id,message.pop_receipt) 
if __name__ == '__main__':    
    # app.run(debug=True)
    
    app.run(host='0.0.0.0')    
# app.run(debug=True)