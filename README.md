# Letter-Recognition-using-Logistic-Regression

###Project Description

<p>The aim of the project is to recognise the hand written digits(from 0-9) from the given pixel data. Logistic regression is used as a learning algorithm to identify the digits.</p>

###Format of the dataset

<p>The given dataset <a href="https://github.com/NandanNayak/Letter-Recognition-using-Logistic-Regression/blob/master/ex3data1.mat">ex3data1.mat</a> has 5000 training examples. Each hand-written digit has 500 training examples. Each training example is a 20 pixel by 20 pixel gray scale image of the digit. Each pixel is represented by a floating point value which represents the intensity at that location. The 20 by 20 pixel data is unrolled into a 400-dimensional vector data. Therefore the dataset is of dimension 5000 by 400, where each row is an example of the handwritten digit. This forms the first part of the dataset. The second part of the dataset contains the 5000 dimensional vector 'Y' that contains labels for the training set. The '0' digit is labelled as '10' whereas the digits from '1-9' are labelled as '1' to '9' in their natural order.</p>

###Algorithm description

<p>The dataset 'X' is inserted a bias variable which is 1. Therefore the dimension of X becomes 5000 by 401. The theta represents the model parameters which is a matrix of 10 by 401. Each row is designated to a digit. Using the concept of Gradient Descent, the model parameters - theta, are repeatedly learnt through iterations.</p>

<img src="https://github.com/NandanNayak/Letter-Recognition-using-Logistic-Regression/blob/master/Matrix%20Computation.png" />

The X0 obtained is given to sigmoid function. The sigmoid function gives 1 or 0 output depending upon whether the computed value is above threshold or not. 

###Running the code

<strong><em>python LetterRecognition.py</em></strong>

###Program Output

<p>The algorithm has a accuracy of 97.82%. When the digit which needs to be identified and the required data regarding the pixel intensities is given, the algorithm does a dot product with the model parameters and the pixel data and recognises the digit based on the highest probability.</p>

<img src="https://github.com/NandanNayak/Letter-Recognition-using-Logistic-Regression/blob/master/Output.png" />
