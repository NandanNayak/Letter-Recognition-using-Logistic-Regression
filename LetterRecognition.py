"""
Aim : To recognise the letter using the given pixel data
Author : Nandan Nayak
Date : 18/July/2016
"""

#import all modules
from __future__ import division
import scipy.io as spio
import numpy as np



#define global variables
doc="ex3data1.mat"
myPrediction={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

#define functions
def sigmoid(val,digit,isprint=0):
     val=1/(1+np.exp(-val))
     if isprint==1:
          print val
     if val>=0.6:
          if digit==0:
               return 10
          else:
               return digit
     else:
          return 0

def sigmoid2(val,digit,isprint=0):
     val=1/(1+np.exp(-val))
     return val


#define main
if __name__=="__main__":
     myfile=spio.loadmat(doc)
     digits=10
     rows=500
     cols=401
     X=np.array(myfile["X"])
     X=np.insert(X,0,1,axis=1)
     X=X.reshape((digits,rows,cols))
     Y=np.array(myfile["y"]).reshape((digits,rows)).T
     theta=np.zeros((digits,cols))
     diff=np.zeros(rows)
     hyp=np.empty((rows,digits))
     z=np.empty(rows)

     loops=100
     alpha=0.001
     m=rows

     for k in range(loops):
         for j in range(digits):
              for i in range(rows):
                   z[i]=np.dot(theta[j],X[j][i])
                   hyp[i][j]=sigmoid(z[i],j)

              for l in range(cols):
                   diff=(hyp[:,j]-Y[:,j])*X[j][:,l]
                   theta[j][l]=theta[j][l]-(alpha/m*(diff.sum()))



     count=0
     for j in range(digits):
          for i in range(rows):
               if hyp[i][j]!=Y[i][j]:
                    count+=1

     error=count/(rows*digits)
     accuracy=1-error
     print "The accuracy of the algorithm is",accuracy


     flag=True
     while(flag):
          try:
               choice_dig=int(raw_input("\nEnter the digit to be recognised : "))
               choice_row=int(raw_input("\nEnter a row no. of the pixel data sample(0-499):"))
               X_in=X[choice_dig][choice_row]
               Y_in=Y[choice_row][choice_dig]

               
               out=np.zeros(digits)
               for i in range(digits):
                    u=np.dot(theta[i],X_in)
                    out[i]=sigmoid2(u,Y_in,1)
                    
               print "\nThe probability of a digit given the pixel data:"
               for i in range(10):
                    myPrediction[i]=out[i]
               print myPrediction
               
               max_val=max(out)
               print
               for i in range(digits):
                    if out[i]==max_val:
                         index=i
                         break
               print "The predicted digit based on highest probability is",index

               choice=raw_input("\nDo you want to continue(y/n)?")
               if choice=="n":
                    flag=False
          except:
               print "\nInvalid input, try again\n"
        
    
    
