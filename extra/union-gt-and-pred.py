import sys
import os
import glob

## This script ensures same number of files in ground-truth and predicted folder.
## When you encounter file not found error, it's usually because you have
## mismatched numbers of ground-truth and predicted files.
## You can use this script to create missing files as empty file. The rationale 
## behind is the following:
##  - if a file is missing from the ground truth but is present among the 
##    predictions it means that we have false positives
##  - if a file is missing from the predictions but is present in the ground
##    truth it means that we have a false negative

# change directory to the one with the files to be changed
path_to_gt = '../ground-truth'
path_to_pred = '../predicted'

os.chdir(path_to_gt)
gt_files = glob.glob('*.txt')
if len(gt_files) == 0:
    print("Error: no .txt files found in", path_to_gt)
    sys.exit()
os.chdir(path_to_pred)
pred_files = glob.glob('*.txt')
if len(pred_files) == 0:
    print("Error: no .txt files found in", path_to_pred)
    sys.exit()

gt_files = set(gt_files)
pred_files = set(pred_files)
print('total ground-truth files:', len(gt_files))
print('total predicted files:', len(pred_files))

gt_backup = gt_files - pred_files
pred_backup = pred_files - gt_files

def backup(src_folder, backup_files, dst_folder):
    # non-intersection files (txt format) will be moved to a backup folder
    if not backup_files:
        print('No missing file in', dst_folder)
        return
    os.chdir(src_folder)
    ## create the backup dir if it doesn't exist already
    for file in backup_files:
        open(dst_folder + '/' + file, 'w').close()
    
backup(path_to_gt, gt_backup, path_to_pred)
backup(path_to_pred, pred_backup, path_to_gt)
if gt_backup:
    print('total predicted added files:', len(gt_backup))
if pred_backup:
    print('total ground-truth added files:', len(pred_backup))

union = gt_files | pred_files
print('total union files:', len(union))
print("Union completed!")
