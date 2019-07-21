# mAP (mean Average Precision)

[![GitHub stars](https://img.shields.io/github/stars/Cartucho/mAP.svg?style=social&label=Stars)](https://github.com/Cartucho/mAP)

This python code will evaluate the performance of your **object detector**. All the documentation is in the `docs/` directory and online at (TODO: add link to Read the Docs).

<p align="center">
  <img src="https://user-images.githubusercontent.com/15831541/37559643-6738bcc8-2a21-11e8-8a07-ed836f19c5d9.gif" width="450" height="300" />
</p>

The uniqueness of this tool is that it allows you to quick and easily visualize your results. This allows you to understand how good your object detector really is and when is it failing.

In practice, a higher mAP value indicates a better performance of your neural-network. However, the mAP score is not enough. Therefore, the **goal of this repo** is not only to calculate the mAP score but also other metrics like *ROC curve*, *confusion matrix*, *log average miss-rate* and others!

## Latest Features

- [ ] Calculate the confusion matrix.
- [ ] Draw False Negatives.
- [x] Feb 2019: allow multiple input formats!
- [x] Jan 2019: added log-average miss ratio metric!

## Table of contents

- [Theoretical Explanation](#theoretical-explanation)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [Running the code](#running-the-code)
- [Authors](#authors)

## Theoretical Explanation
Currently the most used metric to evaluate an object detector in the literature is the mAP score. In specific, the mAP criterion defined in the [PASCAL VOC 2012 competition](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/). This project started from an adaptation of the [official Matlab code](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#devkit) into Python.

To calculate the mAP score, first (**1.**), we calculate the Average Precision (AP) for each of the classes. Then (**2.**), we obtain the final mAP score by merely calculating the arithmetic mean of the AP values of all the classes of objects.

#### 1. Calculate AP

For each class (e.g. `person`, `car`):

First, your **detection-results** are sorted by decreasing confidence values.

(TODO: Add example image of objects sorted by decreasing confidence score)

Then, each of these detections (from higher to lower confidence) is assigned to a **ground-truth** object. We have a true positive when they share the **same label** and a significant overlap **IoU >= 0.5** (Intersection over Union greater than 50%).

(TODO: improve this image)
<img src="https://user-images.githubusercontent.com/15831541/37725175-45b9e1a6-2d2a-11e8-8c15-2fb4d716ca9a.png" width="35%" height="35%" />

Note that we also want to avoid multiple detections of the same object. Therefore, a repeated detection of a ground-truth object is a false positive.

(TODO: add example image to assist explanation)

Using this criterion, we calculate the precision/recall curve. E.g.:

(TODO: improve this image)
<img src="https://user-images.githubusercontent.com/15831541/43008995-64dd53ce-8c34-11e8-8a2c-4567b1311910.png" width="45%" height="45%" />

Then we compute a version of the measured precision/recall curve with **precision monotonically decreasing** (shown in light red), by setting the precision for recall `r` to the maximum precision obtained for any recall `r' > r`.

Finally, we compute the AP as the **area under this curve** (shown in light blue) by numerical integration.
No approximation is involved since the curve is piecewise constant.

#### 2. Calculate mAP

We calculate the mean of all the AP's, resulting in an mAP value from 0 to 100%. E.g:

<img src="https://user-images.githubusercontent.com/15831541/38933241-5f9556ae-4310-11e8-9d47-cb205f9b103b.png"/>

<img src="https://user-images.githubusercontent.com/15831541/38933180-366b6fca-4310-11e8-99b9-17ad4b159b86.png" />

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

TODO: add a quick way to install everything and add tqdm and numpy

## Quick-start

(TODO: add a release version)
To start using the mAP you need to clone the repo:

```
git clone https://github.com/Cartucho/mAP
```

## Running the code

We made this code as flexible as possible for you, so for running the code it really depends on the object detector that you are using.
Please select the object detector that you are using from one of the following options:

<details>
  <summary><b>AlexeyAB/darknet</b></summary>
  <p><br>Step-by-step:</p>
  <ol>
    <li>Edit the file <code>class.names</code> in the directory <code>mAP/input/</code> to your own set of classes (one per line)</li>
    <li>Create the <code>ground-truth</code> files (explained below)</li>
    <li>Copy the <code>ground-truth</code> files (one per image) to the directory <code>mAP/input/ground-truth/</code></li>
    <li>Create the <code>results.txt</code> file (explained below)</li>
    <li>Copy the <code>resuts.txt</code> file to the directory <code>mAP/input/detection-results/</code></li>
    <li>(optional) Copy the relevant images to the directory <code>mAP/input/images-optional/</code></li>
    <li>Run the code: <code>python main.py</code></li>
  </ol>
  <h5>2. Create the ground-truth files</h5>
  <p>The AlexeyAB's training/test files are already in the YOLO format (one of the formats that we support). So you can just jump to step 3. Additionally, if you need to label a new set of pictures in the YOLO format you can use this tool in Python: <a href="https://github.com/Cartucho/OpenLabeling">OpenLabeling</a>.</p>
  <h5>4. Create the results.txt file</h5>
  <p>As explained in the AlexeyAB repo's README you can run the detector on a set of images and save the detection-results to a single <code>result.txt</code> file. An example is shown below:</p>
  <pre>
    <code>
    # Example: forward all images in data/train.txt using yolov3 coco and output to the file result.txt
    darknet.exe detector test cfg/coco.data yolov3.cfg yolov3.weights -dont_show -ext_output &lt; data/train.txt &gt; result.txt
    </code>
  </pre>
</details>
<details>
  <summary><b>Darkflow</b></summary>
  <p><br>Step-by-step:</p>
  <ol>
    <li>Create the <code>ground-truth</code> files (explained below)</li>
    <li>Copy the <code>ground-truth</code> files (one per image) to the directory <code>mAP/input/ground-truth/</code></li>
    <li>Create the <code>detection-results</code> JSON files (explained below)</li>
    <li>Copy the JSON files (one per image) to the directory <code>mAP/input/detection-results/</code></li>
    <li>(optional) Copy the relevant images to the directory <code>mAP/input/images-optional/</code></li>
    <li>Run the code: <code>python main.py</code></li>
  </ol>
  <h5>1. Create the ground-truth files</h5>
  <p>The Darkflow training/test files are already in the PASCAL VOC format (one of the formats that we support). So you can just jump to step 2. Additionally, if you need to label a new set of pictures in the PASCAL VOC format you can use this tool in Python: <a href="https://github.com/Cartucho/OpenLabeling">OpenLabeling</a>.</p>
  <h5>3. Create the detection-results JSON files</h5>
  <p>As explained in the Darkflow repo's README you can run the detector on a set of images and save the detection-results to multiple JSON files (one of the formats that we support). So you can just jump to step 4 after running a command like:</p>
  <pre>
    <code>
    # Example: forward all images in sample_img/ using tiny yolo and JSON output
    flow --imgdir sample_img/ --model cfg/tiny-yolo.cfg --load bin/tiny-yolo.weights --json
    </code>
  </pre>
</details>
<details>
  <summary><b>PASCAL VOC</b></summary>
  <p><br>Step-by-step:</p>
  <ol>
    <li>Create the <code>ground-truth</code> files (explained below)</li>
    <li>Copy the <code>ground-truth</code> files (one per image) to the directory <code>mAP/input/ground-truth/</code></li>
    <li>Create the <code>detection-results</code> files (explained below)</li>
    <li>Copy the <code>detection-results</code> files (one per image) to the directory <code>mAP/input/detection-results/</code></li>
    <li>(optional) Copy the relevant images to the directory <code>mAP/input/images-optional/</code></li>
    <li>Run the code: <code>python main.py</code></li>
  </ol>
  <p>To run the code you must have one (1) <code>ground-truth</code> and one (1) <code>detection-results</code> file for each picture. These files must all have the same basename when without the extension (<code>.jpg</code>, <code>.txt</code>). For example <code>ground-truth/image_1.txt</code>, <code>detection-results/image_1.txt</code>, <code>image-optional/image_1.jpg</code> all share the same basename <code>image_1</code>.</p>
  <h5>1. Create the ground-truth files</h5>
  <p>The PASCAL VOC format is one of the formats that we support. So you can just jump to step 2. Additionally, if you need to label a new set of pictures in the PASCAL VOC format you can use this tool in Python: <a href="https://github.com/Cartucho/OpenLabeling">OpenLabeling</a>.</p>
  <h5>3. Create the detection-results files</h5>
  <p>The <code>detection-results</code> files can also be in the PASCAL VOC format.</p>
</details>
<details>
  <summary><b>pjreddie/darknet</b></summary>
  <p><br>Step-by-step:</p>
  <ol>
    <li>Edit the file <code>class.names</code> in the directory <code>mAP/input/</code> to your own set of classes (one per line)</li>
    <li>Create the <code>ground-truth</code> files (explained below)</li>
    <li>Copy the <code>ground-truth</code> files (one per image) to the directory <code>mAP/input/ground-truth/</code></li>
    <li>Create the <code>detection-results</code> files (explained below)</li>
    <li>Copy the <code>detection-results</code> files (one per image) to the directory <code>mAP/input/detection-results/</code></li>
    <li>(optional) Copy the relevant images to the directory <code>mAP/input/images-optional/</code></li>
    <li>Run the code: <code>python main.py</code></li>
  </ol>
  <h5>2. Create the ground-truth files</h5>
  <p>The pjreddie's training/test files are already in the YOLO format (one of the formats that we support). So you can just jump to step 3. Additionally, if you need to label a new set of pictures in the YOLO format you can use this tool in Python: <a href="https://github.com/Cartucho/OpenLabeling">OpenLabeling</a>.</p>
  <h5>4. Create the detection-results files</h5>
  <p>To store the <code>detection-results</code> files just copy the file <code>save_darknet_detection_results.py</code> in the directory <code>mAP/scripts/create_input_files/</code> to the <code>pjreddie/darknet/python</code> directory.</p>
  <p>Then just run that script inside the <code>pjreddie/darknet</code> directory:</p>
  <pre>
    <code>
    # Example: forward all images in data/image_folder/ using YOLOv2_VOC (you can also specify the --output folder, by default it will be darknet/results/)
    python python/save_darknet_detection_results.py --cfg 'cfg/yolov2-voc.cfg' --weights 'yolov2-voc.weights' --data 'cfg/voc.data' --input_dir data/image_folder
    </code>
  </pre>
</details>
<details>
  <summary><b>TODO: keras-yolo3</b></summary>
  <p>TODO If there is any keras-yolo3 user out there please open an issue and we will add this format! (:</p>
</details>
<details>
  <p><br>Step-by-step:</p>
  <ol>
    <li>Edit the file <code>class.names</code> in the directory <code>mAP/input/</code> to your own set of classes (one per line)</li>
    <li>Create the <code>ground-truth</code> files (explained below)</li>
    <li>Copy the <code>ground-truth</code> files (one per image) to the directory <code>mAP/input/ground-truth/</code></li>
    <li>Create the <code>detection-results</code> files (explained below)</li>
    <li>Copy the <code>detection-results</code> files (one per image) to the directory <code>mAP/input/detection-results/</code></li>
    <li>(optional) Copy the relevant images to the directory <code>mAP/input/images-optional/</code></li>
    <li>Run the code: <code>python main.py</code></li>
  </ol>
  <summary><b>other</b></summary>
  <p>To run the code you must have one (1) <code>ground-truth</code> and one (1) <code>detection-results</code> file for each picture. These files must all have the same basename when without the extension (<code>.jpg</code>, <code>.txt</code>). For example <code>ground-truth/image_1.txt</code>, <code>detection-results/image_1.txt</code>, <code>image-optional/image_1.jpg</code> all share the same basename <code>image_1</code>.</p>
  <p>The <code>ground-truth</code> and the <code>detection-results</code> files can be in multiple formats. Here we will explain one of them, the YOLO format, in detail. In the YOLO format, inside each <code>.txt</code> file there is one line for each object in an image.</p>
  <h5>2. Create the ground-truth files</h5>
  <p>Darknet YOLO wants a .txt file for each image with a line for each ground-truth object in the image that looks like:</p>
  <pre><code>&lt;class_index&gt; &lt;x_center&gt; &lt;y_center&gt; &lt;width&gt; &lt;height&gt;</code></pre>
  <p>, where <code>&lt;class_index&gt;</code> corresponds to index of the object's class from <code>0</code> to <code>#classes - 1</code> (remember that you first need to edit the file <code>input/class.names</code> to your own set of classes). The other values  <code>&lt;x_center&gt; &lt;y_center&gt; &lt;width&gt; &lt;height&gt;</code> correspond to the bounding box of each object. These dimensions are calculated relatively to the width and height of the image, so note that the values can range between 0 and 1.0. Also note that <code>&lt;x_center&gt; &lt;y_center&gt;</code> are the center of the bounding-box and not the top-left corner.</p>
  <p>If you need a tool to create the ground-truth you can use <a href="https://github.com/Cartucho/OpenLabeling">OpenLabeling</a>.</p>
  <p>E.g. <code>ground-truth/image_1.txt</code>:</p>
  <pre><code>
  19 0.504222905636 0.575432434082 0.376204467773 0.267504302979
  0  0.402410387993 0.424330688477 0.386157307943 0.353413604736
  1  0.413456357572 0.575212434082 0.376204467773 0.313203102979</code></pre>
  <h5>4. Create the detection-results files</h5>
  <p>The <code>detection-results</code> files have 1 (one) additional parameter when compared to the <code>ground-truth</code> files: the <code>&lt;confidence&gt;</code> score. This value represents the confidence score for each of the detected objects, so note that the values can range between 0 and 1.0.</p>
  <pre><code>&lt;class-index&gt; &lt;confidence&gt; &lt;x_center&gt; &lt;y_center&gt; &lt;width&gt; &lt;height&gt;</code></pre>
  <p>E.g. <code>detection-results/image_1.txt</code>:</p>
  <pre>
    <code>
      14 0.872790455818 0.325253814697 0.490553100586 0.421687042236 0.819358723958
      14 0.869335949421 0.499317230225 0.532302449544 0.2415572052 0.636518513997</code></pre>
</details>

## Authors:
* **João Cartucho** - Please give me your feedback via GitHub issues.

    Feel free to contribute

    [![GitHub contributors](https://img.shields.io/github/contributors/Cartucho/mAP.svg)](https://github.com/Cartucho/mAP/graphs/contributors)
