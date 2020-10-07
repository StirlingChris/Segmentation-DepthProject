import os
import numpy as np
import cv2
import glob

## This script should be run from within your ID_masks folder ##

path = os.getcwd() # Change this to path of folder to ID Masks. You should also run this script from inside your ID Mask folder
out_path = 'C:/Users/chris/Documents/DatasetRenders/pass41/Seg_masks/' # Change this to output folder, make sure there is a forward slash at end of string to denote new folder
np.random.seed(5)

left_masks = []
l_apple_masks = []
l_avocado_masks = []
l_carrot_masks = []
l_corn_masks = []
l_courgette_masks = []
l_foodfight_masks = []
l_garlic_masks = []
l_ginger_masks = []
l_kiwi_masks = []
l_lemon_masks = []
l_muffin_masks = []
l_parsnip_masks = []
l_playmobil_masks = []
l_plum_masks = []
l_pomegranate_masks = []
l_robin_masks = []
l_roll_masks = []
l_scone_masks = []
l_seeded_masks = []
l_sprout_masks = []
l_thor_masks = []
l_tomato_masks = []
l_ralphie_masks = []
l_corn2_masks = []

right_masks = []
r_apple_masks = []
r_avocado_masks = []
r_carrot_masks = []
r_corn_masks = []
r_courgette_masks = []
r_foodfight_masks = []
r_garlic_masks = []
r_ginger_masks = []
r_kiwi_masks = []
r_lemon_masks = []
r_muffin_masks = []
r_parsnip_masks = []
r_playmobil_masks = []
r_plum_masks = []
r_pomegranate_masks = []
r_ralphie_masks = []
r_robin_masks = []
r_roll_masks = []
r_scone_masks = []
r_seeded_masks = []
r_sprout_masks = []
r_thor_masks = []
r_tomato_masks = []
r_corn2_masks = []

print(path)
for entry in os.listdir(path):

    if entry.find('_L') != -1:
        left_masks.append(entry)
        if entry.find('Apple') != -1:
            l_apple_masks.append(entry)
        if entry.find('Avocado') != -1:
            l_avocado_masks.append(entry)
        if entry.find('Carrot') != -1:
            l_carrot_masks.append(entry)
        if entry.find('Corn') != -1:
            l_corn_masks.append(entry)
        if entry.find('Courgette') != -1:
            l_courgette_masks.append(entry)
        if entry.find('Foodfight') != -1:
            l_foodfight_masks.append(entry)
        if entry.find('Garlic') != -1:
            l_garlic_masks.append(entry)
        if entry.find('Ginger') != -1:
            l_ginger_masks.append(entry)
        if entry.find('Kiwi') != -1:
            l_kiwi_masks.append(entry)
        if entry.find('Lemon') != -1:
            l_lemon_masks.append(entry)
        if entry.find('Muffin') != -1:
            l_muffin_masks.append(entry)
        if entry.find('Parsnip') != -1:
            l_parsnip_masks.append(entry)
        if entry.find('Playmobil') != -1:
            l_playmobil_masks.append(entry)
        if entry.find('Plum') != -1:
            l_plum_masks.append(entry)
        if entry.find('Pomegranate') != -1:
            l_pomegranate_masks.append(entry)
        if entry.find('Robin') != -1:
            l_robin_masks.append(entry)
        if entry.find('Roll') != -1:
            l_roll_masks.append(entry)
        if entry.find('Scone') != -1:
            l_scone_masks.append(entry)
        if entry.find('Seeded') != -1:
            l_seeded_masks.append(entry)
        if entry.find('Sprout') != -1:
            l_sprout_masks.append(entry)
        if entry.find('Thor') != -1:
            l_thor_masks.append(entry)
        if entry.find('Tomato') != -1:
            l_tomato_masks.append(entry)
        if entry.find('Ralphie') != -1:
            l_ralphie_masks.append(entry)
        if entry.find('Corn2') != -1:
            l_corn2_masks.append(entry)

    if entry.find('_R') != -1:
        right_masks.append(entry)
        if entry.find('Apple') != -1:
            r_apple_masks.append(entry)
        if entry.find('Avocado') != -1:
            r_avocado_masks.append(entry)
        if entry.find('Carrot') != -1:
            r_carrot_masks.append(entry)
        if entry.find('Corn') != -1:
            r_corn_masks.append(entry)
        if entry.find('Courgette') != -1:
            r_courgette_masks.append(entry)
        if entry.find('Foodfight') != -1:
            r_foodfight_masks.append(entry)
        if entry.find('Garlic') != -1:
            r_garlic_masks.append(entry)
        if entry.find('Ginger') != -1:
            r_ginger_masks.append(entry)
        if entry.find('Kiwi') != -1:
            r_kiwi_masks.append(entry)
        if entry.find('Lemon') != -1:
            r_lemon_masks.append(entry)
        if entry.find('Muffin') != -1:
            r_muffin_masks.append(entry)
        if entry.find('Parsnip') != -1:
            r_parsnip_masks.append(entry)
        if entry.find('Playmobil') != -1:
            r_playmobil_masks.append(entry)
        if entry.find('Plum') != -1:
            r_plum_masks.append(entry)
        if entry.find('Pomegranate') != -1:
            r_pomegranate_masks.append(entry)
        if entry.find('Robin') != -1:
            r_robin_masks.append(entry)
        if entry.find('Roll') != -1:
            r_roll_masks.append(entry)
        if entry.find('Scone') != -1:
            r_scone_masks.append(entry)
        if entry.find('Seeded') != -1:
            r_seeded_masks.append(entry)
        if entry.find('Sprout') != -1:
            r_sprout_masks.append(entry)
        if entry.find('Thor') != -1:
            r_thor_masks.append(entry)
        if entry.find('Tomato') != -1:
            r_tomato_masks.append(entry)
        if entry.find('Ralphie') != -1:
            r_ralphie_masks.append(entry)
        if entry.find('Corn2') != -1:
            r_corn2_masks.append(entry)


all_rights = [[r_apple_masks], [r_avocado_masks], [r_muffin_masks], [r_lemon_masks], [r_ginger_masks], [r_garlic_masks],
              [r_carrot_masks], [r_foodfight_masks], [r_ralphie_masks], [r_corn_masks], [r_courgette_masks], [r_kiwi_masks],
              [r_parsnip_masks], [r_playmobil_masks], [r_plum_masks], [r_pomegranate_masks], [r_robin_masks], [r_roll_masks],
              [r_scone_masks], [r_seeded_masks], [r_sprout_masks], [r_thor_masks], [r_tomato_masks], [r_corn2_masks]]

all_lefts = [[l_apple_masks], [l_avocado_masks], [l_muffin_masks], [l_lemon_masks], [l_ginger_masks], [l_garlic_masks],
             [l_carrot_masks], [l_foodfight_masks], [l_ralphie_masks], [l_corn_masks], [l_courgette_masks], [l_kiwi_masks],
             [l_parsnip_masks], [l_playmobil_masks], [l_plum_masks], [l_pomegranate_masks], [l_robin_masks], [l_roll_masks],
             [l_scone_masks], [l_seeded_masks], [l_sprout_masks], [l_thor_masks], [l_tomato_masks], [l_corn2_masks]]



frame_total = len(l_apple_masks)

new_mask_r = [item for item in all_rights]
new_mask_l = [item for item in all_lefts]
print(len(l_apple_masks), type(new_mask_l[0][0]))


height, width = 1080, 1920
new_image_l = np.zeros((height, width, 3), dtype=np.uint8)
new_image_r = np.zeros((height, width, 3), dtype=np.uint8)


blue_vals = [np.random.randint(0, 255) for item in range(len(all_rights))]
green_vals = [np.random.randint(0, 255) for item in range(len(all_rights))]
red_vals = [np.random.randint(0, 255) for item in range(len(all_rights))]
mask_codes = ['Apple', 'Avocado', 'Muffin', 'Lemon', 'Ginger', 'Garlic', 'Carrot', 'Foodfight', 'Ralphie', 'Corn', 'Courgette',
              'Kiwi', 'Parsnip', 'Playmobil', 'Plum', 'Pomegranate', 'Robin', 'Roll', 'Scone', 'Seeded', 'Sprout', 'Thor', 'Tomato', 'Corn2']


colour_vals = zip(blue_vals,green_vals,red_vals,mask_codes)
for col in colour_vals:
    print(col)

idx = 0
for frame in range(frame_total):
    new_image_l = np.zeros((height, width, 3), dtype=np.uint8)
    new_image_r = np.zeros((height, width, 3), dtype=np.uint8)
    idx += 1
    for i in range(len(all_lefts)):
        mask = cv2.imread(new_mask_l[i][0][frame])
        mask_pic = mask.copy()    # Prevents altering of original image
        new_image = cv2.add(new_image_l, mask_pic)
        new_image_l[:, :, 0] = np.where(mask_pic[:, :, 0] < 255, new_image_l[:, :, 0], blue_vals[i])
        new_image_l[:, :, 1] = np.where(mask_pic[:, :, 1] < 255, new_image_l[:, :, 1], green_vals[i])
        new_image_l[:, :, 2] = np.where(mask_pic[:, :, 2] < 255, new_image_l[:, :, 2], red_vals[i])
        cv2.imwrite(out_path + 'ObjectMask00'+ str(idx) +'_L.png', new_image_l) # Change the output path
    print('Left Mask {0} finished'.format(idx))
    for i in range(len(all_rights)):
        mask = cv2.imread(new_mask_r[i][0][frame])
        mask_pic = mask.copy()    # Prevents altering of original image
        new_image = cv2.add(new_image_r, mask_pic)
        new_image_r[:, :, 0] = np.where(mask_pic[:, :, 0] < 255, new_image_r[:, :, 0], blue_vals[i])
        new_image_r[:, :, 1] = np.where(mask_pic[:, :, 1] < 255, new_image_r[:, :, 1], green_vals[i])
        new_image_r[:, :, 2] = np.where(mask_pic[:, :, 2] < 255, new_image_r[:, :, 2], red_vals[i])
        cv2.imwrite(out_path + 'ObjectMask00'+ str(idx) +'_R.png', new_image_r) # Change the output path
    print('Right Mask {0} finished'.format(idx))
    print(str(idx), 'out of ', frame_total, ' finished')

print('Masking Finished')

