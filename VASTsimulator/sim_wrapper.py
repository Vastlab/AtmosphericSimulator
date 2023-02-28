'''
Code adopted from the following paper:

Z. Mao, N. Chimitt, and S. H. Chan, "Accerlerating Atmospheric Turbulence
Simulation via Learned Phase-to-Space Transform", ICCV 2021

Arxiv: https://arxiv.org/abs/2107.11627

Zhiyuan Mao, Nicholas Chimitt, and Stanley H. Chan
Copyright 2021
Purdue University, West Lafayette, IN, USA


Ripon - I'm Using demo.py to generate the Turbulence Images using same strength.

'''



from torch import int8
from VASTsimulator.simulator import Simulator
from VASTsimulator.turbStats import tilt_mat, corr_mat
import matplotlib.pyplot as plt
import torch
import glob
import numpy as np
from PIL import Image
import cv2
import os
import os.path as path
import shutil
from sys import exit
import pathlib



class SimWrapper:
    def __init__(self, data_path, gpu='0', str_list=(1,2,3,4)):
        self.device = torch.device(f'cuda:{gpu}') if torch.cuda.is_available() else torch.device('CPU')
        self.data_path = data_path
        correlation = -.1
        self.simulator_array = [Simulator(strength, 112, data_path=self.data_path).to(self.device, dtype=torch.float32) for strength in str_list]
                                
        for sim in self.simulator_array:
            sim.eval()
        

    def simulate(self, input_img):
        # expects numpy.ndarray of shape (112,112,3)
        out_img_list = []
        input_img = input_img.transpose((2,0,1))
        input_img = torch.tensor(input_img, device =self.device, dtype=torch.float32)
        for simulator in self.simulator_array:
            img = simulator(input_img.clone()).detach().cpu().numpy()
            img = img.transpose((1,2,0))
            img = np.clip(img, 0, 255)
            out_img_list.append(img)
        self.img_list = out_img_list
        return out_img_list
    
    def save(self):
        for i,img in zip((1,2,3,4), self.img_list):
            plt.imsave(f'sample_{i}.jpg', img/255)




