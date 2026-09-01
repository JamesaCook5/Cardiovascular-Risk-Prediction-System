import numpy as np

class fullLogisticModel:

    def __init__(self,lr = 0.01,numIters=1000):
        self.lr = lr 
        self.numIters = numIters
        self.weights = None
        self.bias = None
    
    def fit(self, Sample,value):
        #Sample is a numpy nd vector of size NxM where N is the No. of samples
        #and M is the number of features in said sample

        #now we initialise the weights
        numSamples,numParameters = Sample.shape
        #this will unpack the shape of the vector into numSamples (N) and numParameters (M)
        self.weights = np.zeros(numParameters)
        #set the weights to a vector full of 0s with the size of 
        self.bias = 0
        #sets the bias to be 0 

        #gradient descent function
        for _ in range(self.numIters):
            linearModel = np.dot(Sample, self.weights) + self.bias
            #np.dot multiplies the vectors together, creating a linear regression line
            valuePrediction = self.sigmoid(linearModel)
            #approximation

            #Now we update our weights
            dw = (1/numSamples) * np.dot(Sample.T,(valuePrediction - value))
            db = (1/numSamples) * np.sum(valuePrediction-value)

            self.weights -= self.lr * dw #update the weight based on the derivative
            self.bias -= self.lr * db #update the bias based on the derivative



    def predict(self, Sample):
        linearModel = np.dot(Sample, self.weights) + self.bias
        valuePrediction = self.sigmoid(linearModel)
        #creates a probablity the same way that I did earlier in the 'fit' method

        #For simplicity and efficacy sakes, I will implement a binary model 
        #1(cardiovascular disease) , 0(no cardiovascular disease)
        valuePredictionClass = [1 if i>0.5 else 0 for i in valuePrediction]
        #list comprehension for every probability in valuePrediction
        return valuePredictionClass
    
    
    def probability(self,Sample):
        predictionModel = np.dot(Sample,self.weights) + self.bias
        predictionValue = self.sigmoid(predictionModel)
        return predictionValue

    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))
        #sigmoid function of an input 'x'
