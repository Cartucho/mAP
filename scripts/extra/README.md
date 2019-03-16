# Extra

## ground-truth:
- ### convert `xml` to our format:

    1) Insert ground-truth xml files into **ground-truth/**
    2) Run the python script: `python convert_gt_xml.py`

- ### convert YOLO to our format:

    1) Add class list to the file `class_list.txt`
    2) Insert ground-truth files into **ground-truth/**
    3) Insert images into **images/**
    4) Run the python script: `python convert_gt_yolo.py`

- ### convert keras-yolo3 to our format:

    1) Add or update the class list to the file `class_list.txt`
    2) Use the parameter `--gt` to set the **ground-truth** source.
    3) Run the python script: `python3 convert_keras-yolo3.py --gt <gt_file_path>`
        1) Supports only python 3.
        2) This code can handle recursive annotation structure. Just use the `-r` parameter.
        3) The converted annotation is placed by default in a new from_kerasyolo3 folder. You can change that with the parameter `-o`.
        4) The format is defined according with github.com/qqwweee/keras-yolo3

## detection-results:
- ### convert darkflow `json` to our format:

    1) Insert result json files into **detection-results/**
    2) Run the python script: `python convert_dr_darkflow_json.py`

- ### convert YOLO to our format:

    After runnuning darknet on a list of images, e.g.: `darknet.exe detector test data/voc.data yolo-voc.cfg yolo-voc.weights -dont_show -ext_output < data/test.txt > result.txt`

    1) Copy the file `result.txt` to the folder `extra/`
    2) Run the python script: `python convert_dr_yolo.py`

- ### convert keras-yolo3 to our format:

    1) Add or update the class list to the file `class_list.txt`
    2) Use the parameter `--dr` to set the **detection-results** source.
    3) Run the python script: `python3 convert_keras-yolo3.py --dr <dr_file_path>`
        1) Supports only python 3.
        2) This code can handle recursive annotation structure. Just use the `-r` parameter.
        3) The converted annotation is placed by default in a new from_kerasyolo3 folder. You can change that with the parameter `-o`.
        4) The format is defined according with github.com/gustavovaliati/keras-yolo3

## Find the files that contain a specific class of objects

1) Run the `find_class.py` script and specify the **class** as argument, e.g.
`python find_class.py chair`

## Intersect ground-truth and detection-results files
This script ensures same number of files in ground-truth and detection-results folder.
When you encounter file not found error, it's usually because you have
mismatched numbers of ground-truth and detection-results files.
You can use this script to move ground-truth and detection-results files that are
not in the intersection into a backup folder (backup_no_matches_found).
This will retain only files that have the same name in both folders.

1) Prepare `.txt` files in your `ground-truth` and `detection-results` folders.
2) Run the `intersect-gt-and-dr.py` script to move non-intersected files into a backup folder (default: `backup_no_matches_found`).

`python intersect-gt-and-dr.py`
