# import json
# import time 
import requests 
import base64

class Vision():
    def __init__(self, api_key):
        self.api_key = api_key 
    
    def process_image(self, image_path, ocr_type, filter = 0.8): 
        if ocr_type == "OBJECT_LOCALIZATION":
            return self.bounding_box(image_path)
        if ocr_type == "LABEL_DETECTION":
            return self.label_detection(image_path, filter)

    def bounding_box(self, image_path):
        with open(image_path, 'rb') as file: 
            content =  base64.b64encode(file.read()).decode('utf-8')
        request_payload = {
            "requests": [
                {
                "image": {
                    "content": content
                },
                "features": [
                    {
                    "type": "OBJECT_LOCALIZATION"
                    },
                ]
                }
            ]
        }
        url = 'https://vision.googleapis.com/v1/images:annotate'
        params = {
            'key': self.api_key
        }
        # start = time.time()
        response = requests.post(url, params=params, json=request_payload)
        if response.status_code != 200: 
            print('Error', response.status_code)
            print(response.text)
        else: 
            annotation = response.json()
        # end = time.time()
        # print("ocr_done time_take = ", end-start)
        coordinates_dict = {
        'Car': None,
        'Tires': []
        }
        for annotate in annotation['responses'][0]['localizedObjectAnnotations']:
            if annotate['name'] == 'Car':
                coordinates_dict['Car'] = annotate['boundingPoly']['normalizedVertices']
            elif annotate['name'] == 'Tire':
                coordinates_dict['Tires'].append(annotate['boundingPoly']['normalizedVertices'])
        print(coordinates_dict)                
        return coordinates_dict

    def label_detection(self, image_path, filter): 
        with open(image_path, 'rb') as file: 
            content =  base64.b64encode(file.read()).decode('utf-8')
        request_payload = {
        "requests": [
                {
                "image": {
                    "content": content
                },
                "features": [
                    {
                    "type": "LABEL_DETECTION", 
                    "maxResults":30
                    },
                ]
                }
            ]
        }
        url = 'https://vision.googleapis.com/v1/images:annotate'
        params = {
            'key': self.api_key
        }
        # start = time.time()
        response = requests.post(url, params=params, json=request_payload)
        if response.status_code != 200: 
            print('Error', response.status_code)
            print(response.text)
        else: 
            annotation = response.json()
        labels = []
        # print(annotation)
        for annotate in annotation['responses'][0]['labelAnnotations']:
            if annotate['score'] >= filter:
                # labels.append({
                #     'description': annotate['description'], 
                #     'score':annotate['score']
                # })
                labels.append(annotate['description'])
        return labels
