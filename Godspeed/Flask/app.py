# !pip install flask
# !pip install roboflow

import os
from roboflow import Roboflow
from flask import flask, redirect, url_for, render_template, request


app = Flask(__name__)


# load the model

rf = Roboflow(api_key="xre6Oh1WiOhT8issq01D")
project = rf.workspace().project("aircraft-skin-defects-classification-new-dataset")
model = project.version(3).model

# / is the index/home page

@app.route("/", methods=["GET"]) 
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def upload(): 
    if request.method==="POST":
        f=request.files["image"] # this is the name of the input field in the form
        basepath=os.path.dirname(__file__) # this is the path to the directory
        filepath=os.path.join(basepath, "uploads", f.filename) # this is the path to the image
        f.save(filepath) # save the image to the uploads folder
        text = model.predict(filepath).json()
        print(text)
        model.predict(filepath).save("prediction.jpg") # save image on server

        # TO DO : Generate result and report page here and return it  
    return render_template("result.html", text)

if __name__ == "__main__":
    app.run(debug=False, threaded=False, port=5000)







