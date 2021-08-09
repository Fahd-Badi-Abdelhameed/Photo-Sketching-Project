###############################################################################	
# File Name    	: 	Photo Sketching.py    		                              #
# Author       	: 	Fahd Badi                                                 #
# Version      	: 	1.0.0                                                     #
# Origin Date  	: 	26/05/2020                                                #   
# Notes        	: 	None                                                      #
###############################################################################

from matplotlib import pyplot as plt
import numpy as np
import cv2

#Input image
input_img = cv2.imread('Mo_Salah.jpg')
 
#Convert the BGR to RGB because used plt.imshow() function. 
b, g, r = cv2.split(input_img)
input_img = cv2.merge([r, g, b])  
                                 
#convert the RGB color image to greyscale image
grey_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
       
#Invert the greyscale image to get a negative
invert_img = 255-grey_img 

#Gaussian blur to the negative from invert image
blur_img = cv2.GaussianBlur(invert_img, (21,21), 15)

#Blend the greyscale image with the Gaussian blur image using a color dodge
def dodgeColour(image, mask):
    return cv2.divide(image, 255-mask, scale=256)      
pencil = dodgeColour(grey_img, blur_img)
 
#show input image and output image  
plt.subplot(121), plt.imshow(input_img, cmap="gray"), plt.title('Input image')
plt.subplot(122), plt.imshow(pencil, cmap="gray"), plt.title('Pencil sketch')
plt.show()


###############################################################################
################################ END OF PROGRAM ###############################
###############################################################################