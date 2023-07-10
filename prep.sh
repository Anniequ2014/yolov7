#!/bin/bash

# Run train_val.py
#python train_val.py

# Update train, val, and test addresses in mycoco.yaml
sed -i 's~train:.*$~train: /home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/train/images/~' data/mycoco.yaml
sed -i 's~val:.*$~val: /home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/val/images/~' data/mycoco.yaml
sed -i 's~test:.*$~test: /home/annie/Desktop/dev/yolov7/data/datasets/toolboxes/test/images/~' data/mycoco.yaml
