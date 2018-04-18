# Compatibility Python 3

# Import project files

# Import External Packages
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn import linear_modle

# torch packages
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F




class LeastSquares:
    # fits gathered data to the form
    # x_(t+1) = Ax + Bu

    def __init__(self):
        self.reg = linear_model.LinearRegression()

    def train(self, change_states, states_actions_prev):
        # need to make sure data here is normalized AND the states are all
        # formed as change of state, rather than arbitary values (this makes sure
        # that the features are not fit to large vlaues)

        # Xw = y
        # this works if we stack a array
        #       z = [x, u]
        # then can make a matrix
        #       w ~ [A, B]
        Z = np.hstack(states_actions_prev[:,0],states_actions_prev[:,1])
        y = change_states

        self.reg.fit(Z,y)
        return self.reg.coef_

    def predict(self, states_actions_prev):
        # predicts next state of a state, action pairing
        # works if it is a list element, or a pre-concatenated array

        if (len(states_actions_prev) == 2):
            vect = np.hstack(states_actions_prev[0],states_actions_prev[1])
            pred = self.reg.predict(vect)
        else:
            pred = self.reg.predict(states_actions_prev)
        return pred

class NeuralNet:
    # NOTE

    def __init__(self, D_in, D_out, layers, dims):
        # layers is a list of layer types to initialize the NN to
        if (len(layers) != len(dims)):
            raise ValueError('Passed a not matching neural net layers with corresponding dimensions')

        n_lay = len(layers)
        for (i,l) in enumerate(layers):
            if (i==0):
                self.lay


class GaussianProcess:
    # TODO

def ComputeAccuracy(truth,prediction):
