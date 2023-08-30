# Godspeed Aircraft Defect Detection

Godspeed is a Flask based web-app that uses a model to detect defects on the exterior of an aircraft. The model was trained on a Roboflow dataset using the YOLOv5 architecture.

The model was trained on Google Collab and we were able to achieve a 0.95 mAP score on the test set. The model was trained for 100 epochs with a batch size of 16. 
We also attempted to deploy the model on IBM Watson Studio but were unable to do so due to model specification compatibility problems. The jupyter notebooks used for training and deployment can be found in the `notebooks` folder.

Database integration, Security and Confidentiality of uploaded images and Report generation for repair is pending.

# Pre-requisites:
- !pip install roboflow

Dataset used: https://universe.roboflow.com/dibya-dillip/aircraft-skin-defects-classification-new-dataset/model/3

