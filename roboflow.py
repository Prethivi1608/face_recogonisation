from inference_sdk import InferenceHTTPClient

# create an inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="YOUR_API_KEY"
)

# run inference on a local image
print(CLIENT.infer(
    "your_image.jpg", 
    model_id="prethivi-hand/1"
))