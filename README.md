# Mede.tech

INTRODUCTION: 

Using deep convolutional neural networks, this project seeks to categorize the emotion on a person's face into one of seven categories.
The model was developed using the FER-2013 dataset, which was presented at the International Conference on Machine Learning (ICML). This dataset includes 35887 grayscale, 48x48 sized facial photos displaying seven emotions: angry, disgusted, afraid, pleased, neutral, sad, and astonished.
 
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
