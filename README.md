# Segmentation-DepthProject
This repository hosts code used througout the development of the stereo vision segmentation and depth deep learning system. 

MaskCreation.py creates the semantic segmentation masks from the binary object masks created by Blender when rendering scenes. The masks are colour-coded consistently across scenes. The code, when run, prints out the colour codes used to code the objects masks but note that seeing as these masks are created using OpenCV these values are BGR as opposed to RGB so depending on how you pre-process your data you may need to reverse the contents of each tuple in order to get consistent results.

DataSort.py sorts raw data generated from Blender. It iterates through the 'images','seg_masks' & 'z_buffs' folders in each scene folder and saves the images in them into new folders called 'all_frames', 'all_masks' & 'all_zbuffs'. This simply streamlines the data upload to the universitys servers and the train/validation/test split but can realistically be done after upload while the data is still in it's original format.

RGB-DNetwork.py is a stereo vision deep learning model that is trained using two RGB images and a ground-truth depth map to semantically segment objects in both images and to estimate a depth map using featurs from all 3 input images.
