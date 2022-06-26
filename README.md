# Mede.tech

INTRODUCTION: 

This project aims to classify the emotion on a person's face into one of seven categories, using deep convolutional neural networks. 
The model is trained on the FER-2013 dataset which was published on International Conference on Machine Learning (ICML). This dataset consists of 35887 grayscale, 
48x48 sized face images with seven emotions - angry, disgusted, fearful, happy, neutral, sad and surprised.
 
 DEPENDENCIES: 
 
 Python 3, OpenCV, Tensorflow
 
DATA PREPERATION 

The original FER2013 dataset in Kaggle is available as a single csv file. 
We had converted into a dataset of images in the PNG format for training/testing and provided this as the dataset in the previous section.

If you are looking to experiment with new datasets, you may have to deal with data in the csv format. We have provided the code we wrote for data preprocessing in the dataset_prepare.py file which can be used for reference.


ALGORITHM : --

First, the haar cascade method is used to detect faces in each frame of the webcam feed.

The region of image containing the face is resized to 48x48 and is passed as input to the CNN.

The network outputs a list of softmax scores for the seven classes of emotions.

The emotion with maximum score is displayed on the screen.
