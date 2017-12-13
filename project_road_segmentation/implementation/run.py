import numpy as np
import matplotlib.pyplot as plt
import os,sys
from image_helpers import *
from classification import *
from cnn_model import CNN
from classification import predict_test_set_images

def main():
    #Global variables
    image_dir = "../training/images/"
    gt_dir = "../training/groundtruth/"
    files = os.listdir(image_dir)

    patch_size = 16
    foregroud_threshold = 0.25

    # Loading a set of images with their groundtruth
    imgs, gt_imgs = load_n_images_groundtruth(image_dir, gt_dir, 100, rotate=True)

    model = CNN(patch_size, foregroud_threshold)

    try:
        model.train(imgs, gt_imgs)
    except KeyboardInterrupt:
        pass

    model.save_weights('test_regularizer.h5')

    #Predict and Display image
    #img_idx = 6
    #Z = model.predict(imgs[img_idx])
    #print(Z)
    #predict_and_display_image(model, imgs[img_idx], gt_imgs[img_idx], imgs[img_idx])

    predict_test_set_images('test_regularizer.csv', model, cnn=True)

if __name__ == "__main__":
    main()
