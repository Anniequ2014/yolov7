import os
import random
import shutil

cwd = os.getcwd()
print(cwd)

def split_dataset(image_folder, annotation_folder, train_ratio, val_ratio, test_ratio):
    assert train_ratio + val_ratio + test_ratio == 1, "Ratios should add up to 1"

    # Create train, val, and test folders
    train_dir=os.makedirs("/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/train", exist_ok=True)
    print(train_dir)   
    val_dir=os.makedirs("/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/val", exist_ok=True)
    print(val_dir)
    test_dir = os.makedirs("/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/test", exist_ok=True)

    # Get list of file names in the image folder
    file_names = os.listdir(image_folder)

    # Shuffle the file names randomly
    random.shuffle(file_names)

    # Calculate the number of files for each split
    num_files = len(file_names)
    train_size = int(num_files * train_ratio)
    val_size = int(num_files * val_ratio)
    test_size = num_files - train_size - val_size

    # Split the files into train, val, and test sets
    train_files = file_names[:train_size]
    val_files = file_names[train_size : train_size + val_size]
    test_files = file_names[train_size + val_size :]

    # Move images and annotations to their respective folders
    move_files(train_files, image_folder, annotation_folder, "train")
    move_files(val_files, image_folder, annotation_folder, "val")
    move_files(test_files, image_folder, annotation_folder, "test")

def move_files(files, image_folder, annotation_folder, destination_folder):
    for file in files:
        # Move image file
        image_path = os.path.join(image_folder, file)
        new_image_path = os.path.join(destination_folder, "images", file)
        shutil.copy(image_path, new_image_path)

        # Move annotation file
        annotation_file = os.path.splitext(file)[0] + ".txt"
        annotation_path = os.path.join(annotation_folder, annotation_file)
        new_annotation_path = os.path.join(destination_folder, "annotations", annotation_file)
        shutil.copy(annotation_path, new_annotation_path)

    image_folder = "/home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/images"
    annotation_folder = "home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/labels"
    train_ratio = 0.7
    val_ratio = 0.2
    test_ratio = 0.1

    split_dataset(image_folder, annotation_folder, train_ratio, val_ratio, test_ratio)
