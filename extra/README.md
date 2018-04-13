# Extra

## Ground-Truth:
- ### convert `xml` to our format:

    1) Insert ground-truth xml files into **ground-truth/**
    2) Run the python script: `python convert_gt_xml.py`

- ### convert YOLO to our format:

    1) Add class list to the file `class_list.txt`
    2) Insert ground-truth files into **ground-truth/**
    3) Insert images into **images/**
    4) Run the python script: `python convert_gt_yolo.py`

## Predicted:
- ### convert darkflow `json` to our format:

    1) Insert result json files into **predicted/**
    2) Run the python script: `python convert_pred_darkflow_json.py`

## Remove specific char delimiter from files

E.g. remove `;` from:

`<class_name>;<left>;<top>;<right>;<bottom>`

to:

`<class_name> <left> <top> <right> <bottom>`

In the case you have the `--ground-truth` or `--predicted` files in the right format but with a specific char being used as a delimiter (e.g. `";"`), you can remove it by running:

`python remove_delimiter_char.py --char ";" --ground-truth`

## Find the files that contain a specific class of objects

1) Run the `find_class.py` script and specify the **class** as argument, e.g.
`python find_class.py chair`

## Remove all the instances of a specific class of objects

1) Run the `remove_class.py` script and specify the **class** as argument, e.g.
`python remove_class.py chair`

## Rename a specific class of objects

1) Run the `rename_class.py` script and specify the `--current-class-name` and `--new-class-name` as arguments, e.g.

`python rename_class.py --current-class-name Picture Frame --new-class-name PictureFrame`
