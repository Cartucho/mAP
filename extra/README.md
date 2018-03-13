# Extra

## Ground-Truth:
- ### convert YOLO to PASCAL VOC format:

    1) Add class list to the file `class_list.txt`
    2) Insert ground-truth files into **ground-truth/**
    3) Insert images into **images/**
    4) Run the python script: `python convert_yolo_format_to_voc.py`
    
## Find the files that contain a specific class of objects

1) Run the python script and specify the **class** and **path** as arguments, e.g. `python find_class.py chair ../ground-truth`
