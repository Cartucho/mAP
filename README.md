# mAP (mean Average Precision)

(This code is under construction)

This code will evaluate the performance of your neural net for object recognition.
The performance will be judged using the mAP criterium defined in the PASCAL VOC 2012 competition.

### Explanation:
First (**1.**), we calculate the Average Precision (AP), for each of the classes present in the ground-truth. Then (**2.**), we calculate the mean of all the AP's, resulting in a mAP value. A higher mAP value indicates a better performance of your neural net, given your ground-truth.

##### 1. Calculate AP for each Class

##### 2. Calculate mAP

### Usage

##### Ground-truth

A separate text file of ground-truth should be generated for each image. In these files, each line should be in the following format:
<class_name> <left> <top> <right> <bottom>
