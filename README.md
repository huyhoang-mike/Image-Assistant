# Image Assistant using AWS

## Overview

The Image Assistant project aims to provide a user-friendly web platform for image analysis and editing. It leverages a combination of front-end technologies such as HTML, CSS, Javascript, and back-end framework Django Python. The project integrates various AWS services to enhance its functionality, including S3 for object storage, Lambda functions for serverless image processing, API Gateway for secure interaction, Rekognition for image analysis, EC2 for computational capabilities, and CloudWatch for monitoring resource usage.

## Functionality

The website offers the following functionalities:
- **Image Editing:** Provides features for applying filters, noise reduction, scaling, and rotation to images.
- **Text Extraction:** Utilizes the EasyOCR library to extract text from images with high accuracy.
- **Image Comparison:** Employs the Structural Similarity Index (SSI) algorithm to compare uploaded images.
- **Object Detection:** Utilizes AWS Rekognition for automatic annotations and object detection.
- **Image Upload and Download:** Users can upload images, perform editing and analysis, and download the results.

## Cloning the Project

To clone the project, use the following command:
```bash
git clone https://github.com/huyhoang-mike/image_assistant.git
```
## Configuring AWS Credentials

Before setting up the API, Lambda, and dependencies, ensure that you have configured your AWS credentials. You can set your `aws_access_key_id` and `aws_secret_access_key` directly on the code. Then run the command to runserver as well as make the forward port 8000 public.

```bash
python3 manage.py runserver 0.0.0.0:8000
```


For detailed instructions on setting up the API, Lambda functions, and dependencies, please refer to the project's documentation or the AWS documentation.

## Implementation


https://github.com/huyhoang-mike/Image-Assistant/assets/109945762/d68a8eef-ff6e-451b-9aff-63bebcbf9340




