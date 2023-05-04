# Image similarity search using deep learning
This project demonstrates, how we can make use of deep learning to do state-of-the-art image similarity search. I have used tensorflow and some publicly available datasets.

## Results
![alt text](https://cdn-images-1.medium.com/max/800/1*dd0QDhLZAjBKD5JZgJCI9w.png)
![alt text](https://cdn-images-1.medium.com/max/800/0*ziXWbDIrdW_qJMCL.png)
![alt text](https://cdn-images-1.medium.com/max/800/0*gL9UZQFdwFk-9smY.png)

## Environment

==**compiler**==: python 3.11

==**packages**==:  Flask 	PyQt5 	numpy 	tensorflow 	Flask-HTTPAuth 	scipy 	imageio 	matplotlib 	sklearn

==**editor**==: Visual Studio Code

==**programming language**==: html( css, javascript ), python

## How to run

1. Download [imagenet](https://drive.google.com/open?id=1UOyZ8166qM3SzxGvaUeWpBzSUfoQLUjJ) folder, extraxt and keep it in server directory
2. Download datasets for [footwares](http://vision.cs.utexas.edu/projects/finegrained/utzap50k/), [apparels](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion/InShopRetrieval.html) keep them inside a directory under upload folder. Final folder strcture will be as below
```
├─.idea
│  └─inspectionProfiles
├─.vscode
├─assets
└─server
    ├─database
    │  ├─dataset
    │  └─tags
    ├─imagenet
    ├─images
    ├─static
    │  ├─images
    │  └─result
    ├─templates
    ├─uploads
    └─__pycache__
```
3. Run image vectorizer which passes each data through an inception-v3 model and collects the bottleneck layer vectors and stores in disc. Edit dataset paths accordingly indide the image_vectorizer.py
```
  python server/image_vectorizer.py 
```
   This will generate two files namely, image_list.pickle and saved_features.txt. Keep them inside lib folder where search.py script is available.

4. Start the server by running rest-server.py. This project uses flask based REST implementation for UI
```
  python server/rest-server.py 
```
5. Once the server starts up, access the url 127.0.0.1:5000 to get the UI. Now upload any file and see 9 similar images. You can change the value of K from 9 to any values, but dont foreget to update the html file accordingly for displaying.
   

