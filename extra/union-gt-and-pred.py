import sys
import os
import glob

## This script ensures same number of files in ground-truth and predicted folder.
## When you encounter file not found error, it's usually because you have
## mismatched numbers of ground-truth and predicted files.
## You can use this script to move ground-truth and predicted files that are
## not in the intersection into a backup folder (backup_no_matches_found).
## This will retain only files that have the same name in both folders.

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
print()

gt_backup = gt_files - pred_files
pred_backup = pred_files - gt_files

print("gt_backup:", gt_backup)
print("pre_backup:", pred_backup)

def backup(src_folder, backup_files, dst_folder):
    # non-intersection files (txt format) will be moved to a backup folder
    if not backup_files:
        print('No backup required for', src_folder)
        return
    os.chdir(src_folder)
    ## create the backup dir if it doesn't exist already
    for file in backup_files:
        open(dst_folder + '/' + file, 'w').close()
    
backup(path_to_gt, gt_backup, path_to_pred)
backup(path_to_pred, pred_backup, path_to_gt)
if gt_backup:
    print('total ground-truth backup files:', len(gt_backup))
if pred_backup:
    print('total predicted backup files:', len(pred_backup))

intersection = gt_files | pred_files
print('total union files:', len(intersection))
print("Union completed!")
