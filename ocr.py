# import json
# import time 
import requests 
import base64



def bounding_box(img_path, api_key):
    with open(img_path, 'rb') as file: 
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
        'key': api_key
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
    return coordinates_dict
