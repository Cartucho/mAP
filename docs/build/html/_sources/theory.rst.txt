Theory
======

In this section you will learn about the metrics used to evaluate an object detector.

.. contents:: :local:

Precision and Recall
--------------------

When it comes to object detection, Precision and Recall are the two fundamental concepts.
By the end of this subsection, you should be able to answer the following questions:

#. What is a True/False Positive, and True/False Negative?
#. Why are there no True Negatives in the object detection task?
#. What is Precision and Recall?
#. What is a Precision-Recall curve?

True/False Positive, and True/False Negative
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/theory/hover_cat.jpg
   :alt: map to buried treasure

   Meet `Hover Cat <https://imgur.com/XhME3>`_, he will help you with the theory!

Imagine that your object detector gave you the following output:

.. figure:: images/theory/tp_example.png
   :alt: map to buried treasure
   :scale: 50%

   Example of a True Positive.

This definitely looks like a True Positive, right? Yes! Why? Well, since the object is labeled correctly ("Hover Cat") and the bounding-box (green rectangle) is well adjusted to that object. But how can we be sure that this is, indeed, a True Positive and not a False Posivite?

It's easier to answer this question if we first have a look at the three possible False Positive scenarios:

1. wrong label
2. insufficient overlap (IoU < threshold)
3. multiple detection of the same object

The first type of False Positive is when you get the wrong label (1.):

.. figure:: images/theory/fp_example_label.png
   :alt: map to buried treasure
   :scale: 50%

   False Positive: the "Hover Cat" was wrongly labeled as a "Dog".

No wonder he looks mad, he is not a "Dog"!

The second type of False Positive is when the overlap of the bounding-boxes (the blue and red rectangles in the following image) is not sufficient:

.. figure:: images/theory/fp_example_overlap.png
   :alt: map to buried treasure
   :scale: 50%

   Example of a False Positive, since the overlap between the bounding boxes is insufficient.

This overlap is defined by the Intersection over Union (IoU), as illustrated in the next image. Specifically, we calculate it by diving the area of the bounding-boxe's Intersection (in yellow) by the Union area (in orange):

.. figure:: images/theory/fp_example_iou.png
   :alt: map to buried treasure
   :scale: 50%

   False Positive: The IoU is calculated by dividing the bounding-boxe's Intersection area (in yellow) over the Union area (in orange).

If the IoU score is smaller than a pre-defined threshold value (e.g. IoU < 50%) that detection will be considered a False Positive. The threshold value can be tuned according to one's needs.

The third type of False Positives is multiple detections of the same object:

.. figure:: images/theory/fp_example_multiple_detection.png
   :alt: map to buried treasure
   :scale: 50%

   Example of a False Positive, since the same ground-truth object was detected multiple times.

In this case only one detection will be considered a True Positive. To decide which of them will be considered the True Positive, the detection with higher confidence score will be used (in this case the detection with "confidence:80%"). In other words, there can only be one True Positive associated with each ground-truth object.

But what would happen if the object detector did not detect a single object for this image?

TODO: show image

Then we would get a False Negative. Note that this time we refer to the ground-truth and not to the detection.


Well a True Negative in the case of object detection simply makes no sense since it would correspond to an object that is not in the ground-truth and it was not detected.
True Negative -> there is no cat and no cat was detected. but if you think about it there are infinity number of classes, there is no dog and no dog was deteced, there is no bird and no bird is detected. it makes no sense in this context


TODO: explain why there are no true negatives

In summary, for a detection

Precision
^^^^^^^^^
TODO

Recall
^^^^^^
TODO

Precision-Recall Curve
^^^^^^^^^^^^^^^^^^^^^^
TODO

mean Average Precision
----------------------
TODO

Confusion Matrix
----------------

TODO

ROC Curve
---------
TODO

Log-average Miss Rate
---------------------
TODO


References
----------
