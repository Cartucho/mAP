# mAP (mean Average Precision)

[![New](https://img.shields.io/badge/2018-NEW-brightgreen.svg)](https://github.com/Cartucho/mAP/commits/master)
[![GitHub stars](https://img.shields.io/github/stars/Cartucho/mAP.svg?style=social&label=Stars)](https://github.com/Cartucho/mAP)

This code will evaluate the performance of your neural net for object recognition.

<img src="https://user-images.githubusercontent.com/15831541/37559643-6738bcc8-2a21-11e8-8a07-ed836f19c5d9.gif" width="500" height="300" />

In practice, a **higher mAP** value indicates a **better performance** of your neural net, given your ground-truth and set of classes.

## Table of contents

- [Explanation](#explanation)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [Running the code](#running-the-code)
- [Authors](#authors)

## Explanation
The performance of your neural net will be judged using the mAP criterium defined in the [PASCAL VOC 2012 competition](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). We simply adapted the [official Matlab code](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#devkit) into Python (in our tests they both give the same results).

First (**1.**), we calculate the Average Precision (AP), for each of the classes present in the ground-truth. Then (**2.**), we calculate the mean of all the AP's, resulting in an mAP value.

#### 1. Calculate AP for each Class

<img src="https://user-images.githubusercontent.com/15831541/37559147-e45b3dc4-2a18-11e8-8956-1ccccf83d1c8.jpg" width="60%" height="60%" />

#### 2. Calculate mAP

<img src="https://user-images.githubusercontent.com/15831541/37559152-eed3f002-2a18-11e8-83e0-2da3c898194a.jpg" width="60%" height="60%" />

## Prerequisites

You need to install:
- [Python](https://www.python.org/downloads/)

Optional:
- **plot** the results by [installing Matplotlib](https://matplotlib.org/users/installing.html) - Linux, macOS and Windows:
    1. `python -mpip install -U pip`  
    2.  `python -mpip install -U matplotlib`
-  show **animation** by installing [OpenCV](https://www.opencv.org/):
    1. `python -mpip install -U pip`
    2. `python -mpip install -U opencv-python`  

## Quick-start
To start using the mAP you need to clone the repo:

```
git clone https://github.com/Cartucho/mAP
```

## Running the code

Step by step:

  1. [Create the ground-truth files](#create-the-ground-truth-files)
  2. Move the ground-truth files into the folder **ground-truth/**
  3. [Create the predicted objects files](#create-the-predicted-objects-files)
  4. Move the predictions files into the folder **predicted/**
  5. Run the code:
         ```
         python main.py
         ```

Optional (if you want to see the **animation**):

  6. Insert the images into the folder **images/**


#### Create the ground-truth files

- Create a separate ground-truth text file for each image.
- Use **matching names** (e.g. image: "image_1.jpg", ground-truth: "image_1.txt"; "image_2.jpg", "image_2.txt"...).
- In these files, each line should be in the following format:
    ```
    <class_name> <left> <top> <right> <bottom>
    ```
    , where `<class_name>` must have no whitespaces between words.
- E.g. "image_1.txt":
    ```
    tvmonitor 2 10 173 238
    book 439 157 556 241
    book 437 246 518 351
    pottedplant 272 190 316 259
    ```
#### Create the predicted objects files

- Create a separate predicted objects text file for each image.
- Use **matching names** (e.g. image: "image_1.jpg", predicted: "image_1.txt"; "image_2.jpg", "image_2.txt"...).
- In these files, each line should be in the following format:
    ```
    <class_name> <confidence> <left> <top> <right> <bottom>
    ```
    , where `<class_name>` must have no whitespaces between words.
- E.g. "image_1.txt":
    ```
    tvmonitor 0.471781 0 13 174 244
    cup 0.414941 274 226 301 265
    book 0.460851 429 219 528 247
    chair 0.292345 0 199 88 436
    book 0.269833 433 260 506 336
    ```
## Authors:
* **João Cartucho** - Please give me your feedback: to.cartucho@gmail.com

    Feel free to contribute

    [![GitHub contributors](https://img.shields.io/github/contributors/Cartucho/mAP.svg)](https://github.com/Cartucho/mAP/graphs/contributors)
