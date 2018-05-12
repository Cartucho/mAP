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

- ### convert YOLO to our format:

    1) Add class list to the file `class_list.txt`
    2) Insert predicted objects files into **predicted/**
    3) Insert images into **images/**
    4) Run the python script: `python convert_pred_yolo.py`

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

## Rename all classes by replacing spaces with delimiters
Use this option instead of the above option when you have a lot of classes with spaces.
It's useful when renaming classes with spaces become tedious (because you have a lot of them).

1) Add class list to the file `class_list.txt` (the script will search this file for class names with spaces)
2) Run the `remove_space.py` script and specify the `--delimiter` (default: "-") and `--yes` if you want to force confirmation on all yes/no queries, e.g.

`python remove_space.py --delimiter "-" --yes`

## Intersect ground-truth and predicted files
This script ensures same number of files in ground-truth and predicted folder.
When you encounter file not found error, it's usually because you have
mismatched numbers of ground-truth and predicted files.
You can use this script to move ground-truth and predicted files that are
not in the intersection into a backup folder (backup_no_matches_found).
This will retain only files that have the same name in both folders.

1) Prepare `.txt` files in your `ground-truth` and `predicted` folders.
2) Run the `intersect-gt-and-pred.py` script to move non-intersected files into a backup folder (default: `backup_no_matches_found`).

`python intersect-gt-and-pred.py`
