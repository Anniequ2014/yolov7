import os
import random
import shutil

# Set the path to the root folder that contains your labeled image dataset,
# as well as the proportion of images to use for validation
#root_folder = '/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/images'
root_folder ='/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/'
img_root_folder = '/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/images'
label_root_folder = '/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/labels'

val_proportion = 0.2

# Create the train and val directories if they don't already exist
os.makedirs(os.path.join(root_folder, 'train/images'), exist_ok=True)
os.makedirs(os.path.join(root_folder, 'train/labels'), exist_ok=True)
os.makedirs(os.path.join(root_folder, 'val/images'), exist_ok=True)
os.makedirs(os.path.join(root_folder, 'val/labels'), exist_ok=True)

# Get a list of all the image files in the root folder
#image_files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(img_root_folder, f))]
image_files = [f for f in os.listdir(img_root_folder) if os.path.isfile(os.path.join(img_root_folder, f))]

# Shuffle the list of image files
random.shuffle(image_files)

# Get the index at which to split the list of image files into train and validation sets
split_index = int(len(image_files) * (1 - val_proportion))
print(split_index)
# Copy the images to the train and val folders based on the split index
for i, image_file in enumerate(image_files):
    img_source_path = os.path.join(img_root_folder, image_file)
    label_source_path = os.path.join(label_root_folder,image_file.split('.')[0]+'.txt')
    if i < split_index:        
        img_destination_path = os.path.join(root_folder, 'train/images', image_file)
        label_destination_path = os.path.join(root_folder, 'train/labels', image_file.split('.')[0]+ '.txt')
    else:
        img_destination_path = os.path.join(root_folder, 'val/images', image_file)
        label_destination_path = os.path.join(root_folder, 'val/labels', image_file.split('.')[0]+ '.txt')
    shutil.copyfile(img_source_path, img_destination_path)
    shutil.copyfile(label_source_path,label_destination_path)   
