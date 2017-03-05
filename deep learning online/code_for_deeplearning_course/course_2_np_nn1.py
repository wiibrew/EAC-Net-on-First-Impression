import numpy as np
#prepare dara
X_0=np.random.multivariate_normal([1,1],[[1,0],[0,1]],(200))
y_0 = np.zeros((200,))
X_1 = np.random.multivariate_normal([1,2],[[1,0],[0,1]],(200))
y_1 = np.ones((200,))

#merge the two data into one
X=np.concatenate((X_0, X_1), axis=0)
y=np.concatenate((y_0, y_1), axis=0)
# print X,y
#shuffle the data
from sklearn.utils import shuffle
print X.shape, y.shape
X,y=shuffle(X,y)

print X,y


#init the parameter
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

X_tr=X[:100]
X_ts=X[100:]
y_tr=y[:100]
y_ts=y[100:]
#train model
# for j in xrange(10000):
    # l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    # l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    # l2_delta = (y - l2)*(l2*(1-l2))
    # l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    # syn1 += l1.T.dot(l2_delta)
    # syn0 += X.T.dot(l1_delta)
    # if j%100==0:print (y-l2)
    