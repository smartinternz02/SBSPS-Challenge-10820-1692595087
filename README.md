# Team Godspeed-Aircraft Skin Health Diagnosis with Aircraft API

AeroSpace is a web-application aims to provide a assistance to the aerospace industry to diagnos aircraft skin health. The model detect defects on the exterior of an aircraft, was trained on a Roboflow dataset using the YOLOv5 architecture.

The model was trained on Google Collab and we were able to achieve a 0.95 mAP score on the test set. The model was trained for 100 epochs with a batch size of 16. 
We also attempted to deploy the model on IBM Watson Studio but were unable to do so due to model specification compatibility problems. The jupyter notebooks used for training and deployment can be found in the `notebooks` folder.

Database integration, Security and Confidentiality of uploaded images and Report generation are some of the major features of our project.

Also visualization of reports that provide great insights and are easy to understand are one of the catch of our project.

We also maintain a issues faced database to provide which parts have faced the most wear and tear, paint-offs, dents and cracks so that the future manufacturers can take notes on which parts need what sort of sturdy development.

We aim to provide a one stop application that not only compares the past reports, but also provides the statistics of the health state of every part of airplane skin.

Our future scope includes to deep dive into the cause of defect in more accuracy, which as of now we only estimate.

Dataset used: https://universe.roboflow.com/dibya-dillip/aircraft-skin-defects-classification-new-dataset/model/3

Video Link: https://youtu.be/eogXJz_2UEw?feature=shared

