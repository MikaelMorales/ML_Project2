#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from image_helpers import *
from mask_to_submission import *

def value_to_class(v, foreground_threshold):
    df = np.sum(v)
    if df > foreground_threshold:
        return 1
    else:
        return 0

def predict_and_display_image(model, img, gt, real_img):
    Zi = model.predict(img)
    
    w = gt.shape[0]
    h = gt.shape[1]
    predicted_im = label_to_img(w, h, model.patchSize, model.patchSize, Zi)
    cimg = concatenate_images(real_img, predicted_im)
    fig1 = plt.figure(figsize=(10, 10)) # create a figure with the default size 
    plt.imshow(cimg, cmap='Greys_r')

    new_img = make_img_overlay(real_img, predicted_im)

    plt.imshow(new_img)
    
def predict_test_set_images(filename, model):
    imgs = load_test_images()
    imgs_path = ['../test_set_images/test_'+str(i)+'/test_'+str(i)+'.png' for i in range(1, 51)]
    prediction_filenames = []
    
    for i in range(len(imgs)):
        prediction_filenames.append('predictions/prediction' + str(i+1) + '.png')

    for i in range(len(imgs)):
        Zi = model.predict(imgs_path[i])
        w = imgs[i].shape[0]
        h = imgs[i].shape[1]
        predicted_im = label_to_img(w, h, model.patchSize, model.patchSize, Zi)
        color_mask = np.zeros((w, h, 3), dtype=np.float)
        color_mask[:,:,0] = predicted_im
        color_mask[:,:,1] = predicted_im
        color_mask[:,:,2] = predicted_im

        mpimg.imsave(prediction_filenames[i], color_mask)
    
    masks_to_submission(filename, *prediction_filenames)