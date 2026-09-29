# AWS Serverless Image Compression

A serverless project that automatically compresses images uploaded to Amazon S3 using AWS Lambda and Python Pillow.

## How it works

1. An image is uploaded to the input bucket `input-0-m6`.
2. The S3 `ObjectCreated` event triggers the `image-compresser` Lambda function.
3. Lambda compresses the image as a JPEG (quality 50) using Pillow.
4. The result is saved to the output bucket `output-0-m6` as `compressed-<name>.jpeg`.

## Tech stack

AWS Lambda, Amazon S3, IAM, CloudWatch Logs, Python, Boto3, Pillow (Lambda layer)

## Files

- `lambda_function.py`: Lambda source code
- `iam-policy.json`: least-privilege IAM policy for the Lambda role
- `test-event.json`: sample S3 event for testing in the Lambda console
- `AWS_Serverless_Image_Compression_Documentation.pdf`: full project documentation

## Author

Vanticheruku Mohith Reddy ([@mohithreddy894-sys](https://github.com/mohithreddy894-sys))
