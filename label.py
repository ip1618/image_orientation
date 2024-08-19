import json 
import time 
from ocr import Vision

with open('config.json', 'r') as file: 
    config = json.load(file)

print("image_path", config['image_path'])
start = time.time()
ocr = Vision(config['vision_api_key'])
end = time.time()
labels = ocr.process_image(config['image_path'], 'LABEL_DETECTION', 0.85)
print('Label detection time take', end - start)
print(labels)

plate = 0 
tail_light = 0
if 'Vehicle registration plate' in labels: 
    plate = 1
    if 'Automotive tail & brake light' in labels: 
        tail_light = 1 
if plate ==1:
    if tail_light ==1:
        print("rear")
    else: 
        print("front")
if plate ==0: 
    print("side")




