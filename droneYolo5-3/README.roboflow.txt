
droneYolo5 - v3 2023-02-23 11:29am
==============================

This dataset was exported via roboflow.com on February 23, 2023 at 11:29 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 810 images.
Drones are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Fit (white edges))

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -15 and +15 degrees
* Salt and pepper noise was applied to 5 percent of pixels


