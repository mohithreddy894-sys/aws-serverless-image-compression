import boto3
from PIL import Image
import io
import urllib.parse

s3 = boto3.client("s3")

OUTPUT_BUCKET = "output-0-m6"


def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]

    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    print("Input bucket:", bucket)
    print("Input key:", key)

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    image_content = response["Body"].read()

    image = Image.open(io.BytesIO(image_content))

    print("Original format:", image.format)
    print("Original size:", image.size)
    print("Original mode:", image.mode)

    if image.mode != "RGB":
        image = image.convert("RGB")

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="JPEG",
        quality=50,
        optimize=True
    )

    buffer.seek(0)

    filename = key.split("/")[-1]

    filename_without_extension = filename.rsplit(".", 1)[0]

    output_key = (
        "compressed-"
        + filename_without_extension
        + ".jpeg"
    )

    print("Output bucket:", OUTPUT_BUCKET)
    print("Output key:", output_key)

    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=output_key,
        Body=buffer.getvalue(),
        ContentType="image/jpeg"
    )

    print("Image compression completed successfully.")

    return {
        "statusCode": 200,
        "message": "Image compressed successfully",
        "input_bucket": bucket,
        "input_key": key,
        "output_bucket": OUTPUT_BUCKET,
        "output_key": output_key
    }
