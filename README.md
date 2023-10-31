# Face Detection using Viola-Jones Algorithm

## Contributors
- Nartozhieva Nigara (Student ID: 12200276)
- Akhrorov Temurbek (Student ID: 12204574)

## Course
- Digital Image Processing by Prof. Kakani Vijay

## Overview
This project focuses on face detection using the Viola-Jones algorithm, involving the creation of a custom XML file for face recognition. We encountered several challenges and learned valuable lessons while building and training our own face detection model.

## Dataset Collection

### Positive Images
For positive face recognition, we gathered a dataset from Kaggle [LFW People Dataset](https://www.kaggle.com/datasets/atulanandjha/lfwpeople/). To simplify the dataset's structure, we used Python with the Pillow library to extract and organize images into a single folder.

### Negative Images
We used the [Intel Image Classification Dataset](https://www.kaggle.com/datasets/puneet6060/intel-image-classification) from Kaggle, which consists of images of various objects, landscapes, and more. Additionally, we included our own negative samples by capturing images of our classroom.

### Image Resizing
To expedite the training process, we resized our positive images to 250x250 pixels using Python.

## Training
After collecting datasets, we trained our face detection model using the Cascade Trainer GUI. The training process took approximately 6 hours with 20 stages.

## Real-Time Face Detection
We implemented real-time face detection using the trained XML file with OpenCV. The detection process uses the trained classifier to identify faces in a video stream.

## Problems Solved

### Problem 1: Finding Minimum Detectable Face Size
We developed a script that dynamically determines the minimum detectable face size by incrementally increasing the size until no faces are detected.

### Problem 2: Finding Maximum Detectable Face Size
Similarly, we identified the maximum detectable face size by decrementing the size until no faces are detected.

### Problem 3: Finding Average Detection Time
We measured the average detection time per image and per face. This valuable insight helps assess the model's performance in real-time.

## Challenges and Solutions

1. **Training Issues**
   - Issue: Failure in image file naming during training. We resolved this problem by renaming all image files sequentially.
   - Issue: OpenCV Error: Bad Argument (Insufficient number of positive images). We adjusted the percentage of Positive Image Usage from 100% to 90% to resolve this issue.

2. **Faces in Negative Image Samples**
   We encountered issues with negative image samples containing small faces, and we developed a script to identify and delete images with faces from the negative dataset.

## Conclusion
This project provided us with a valuable hands-on experience in building and training a face detection model using the Viola-Jones algorithm. We overcame numerous challenges, such as dataset management, image preprocessing, and addressing real-world detection issues. Our journey spanned approximately 5-6 days, and the collaboration among the team members played a crucial role in our success. We gained a deep understanding of object detection and the practical application of machine learning in real-world scenarios.

## Demo Video
For a detailed demonstration, please refer to our demo video.

