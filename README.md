Certainly! Here's the revised README.md with the integration of the additional information within the content:

```markdown
# Image Assistant using AWS

## Overview

The Image Assistant project aims to provide a user-friendly web platform for image analysis and editing. It leverages a combination of front-end technologies such as HTML, CSS Bootstrap, and back-end framework Django Python. The project integrates various AWS services to enhance its functionality, including S3 for object storage, Lambda functions for serverless image processing, API Gateway for secure interaction, Rekognition for image analysis, EC2 for computational capabilities, and CloudWatch for monitoring resource usage.

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

Before setting up the API, Lambda, and dependencies, ensure that you have configured your AWS credentials. You can set your `aws_access_key_id` and `aws_secret_access_key` using the AWS Command Line Interface (CLI) or by creating a credentials file.

```bash
aws configure
```

## Setting up API, Lambda, and Dependencies

1. **API Gateway:** Create a new API in the API Gateway console to define the HTTP endpoints for your application.

2. **Lambda Functions:** Set up Lambda functions to handle various image processing tasks and integrate them with your API.

3. **AWS S3:** Use S3 buckets for storing essential dependencies such as EasyOCR, OpenCV, Skimage, and numpy within the Image Assistant framework.

4. **AWS Rekognition:** Leverage Rekognition services for predicting labels, classes, and bounding boxes within uploaded images.

5. **AWS EC2:** Utilize EC2 instances to augment the computational capabilities of the Image Assistant architecture.

6. **AWS CloudWatch:** Set up CloudWatch for monitoring resource usage and expenditure, ensuring cost-effective operation of the Image Assistant website.

7. **Dependencies:** Ensure all necessary libraries and frameworks, such as EasyOCR, OpenCV, and skimage Python, are properly installed and configured within the project environment.

For detailed instructions on setting up the API, Lambda functions, and dependencies, please refer to the project's documentation or the AWS documentation.

## References

The document contains a list of references to AWS documentation, libraries, and frameworks used in the project.

For a more detailed understanding of the project and its technical aspects, please refer to the provided LaTeX document or visit the GitHub repository at [GitHub Repository](https://github.com/huyhoang-mike/image_assistant).
```

This revised README.md now includes detailed information on how to clone the project, configure AWS credentials, and set up the API, Lambda functions, and dependencies. If there are any further modifications or specific details you'd like to add, feel free to let me know!
