import os
from natsort import natsorted
import shutil

in_path = r'C:\Users\chris\Documents\DataMovementFolder'
out_path = r'C:\Users\chris\Documents\FullDataset\pass36-41'

img_count = 1
seg_count = 1
depth_count = 1

for scene_folders in natsorted(os.listdir(in_path)):
    print('Scene path is: ' + scene_folders)
    next_path = os.path.join(in_path,scene_folders)
    for image_folders in os.listdir(next_path):
        path = os.path.join(next_path,image_folders)
        print('folder path is:' + path)

        if 'Images' in path:
            print('Image path is:' + path)
            for img in natsorted(os.listdir(path)):
                print('Image file is: ' + img)
                image = os.path.join(path,img)
                shutil.copyfile(image, out_path + r'\all_frames\Frame' + str(img_count) + '.png')
                img_count += 1

        if 'Seg_masks' in path:
            print('Seg_mask path is: ' + path)
            for seg in natsorted(os.listdir(path)):
                print('Seg mask file is: ' + seg)
                seg_img = os.path.join(path,seg)
                shutil.copyfile(seg_img, out_path + r'\all_masks\Mask' + str(seg_count) + '.png')
                seg_count += 1

        if 'Z' in path:
            print('Z_buff path is: ' + path)
            for depth in natsorted(os.listdir(path)):
                print('Depth image file is:' + depth)
                depth_img = os.path.join(path,depth)
                shutil.copyfile(depth_img, out_path + r'\all_zbuffs\Zbuff' + str(depth_count) + '.png')
                depth_count += 1

print('Data movement complete, have a nice day! :)')