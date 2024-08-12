import json 
import utils_math as um 
from ocr import bounding_box
from utils_image import rotate_image
import time
import cv2 

tstart = time.time()
with open('config.json', 'r') as file: 
    config = json.load(file)

print("ocr_started")
start = time.time()
coordinate = bounding_box(config['image_path'], config['vision_api_key'])
end = time.time()
print("ocr_done", end-start)


start = time.time()
car = coordinate['Car']
tires = coordinate['Tires']

breadth = um.distince(car[0]['x'], car[1]['x'], car[0]['y'], car[1]['y'])
length = um.distince(car[0]['x'], car[3]['x'], car[0]['y'], car[3]['y'])

centriod = {
                'x':(car[1]['x'] + car[0]['x'])/2, 
                'y':(car[3]['y'] + car[0]['y'])/2
            }
t1center = {
    'x':(tires[0][1]['x'] + tires[0][0]['x'])/2, 
    'y':(tires[0][3]['y'] + tires[0][0]['y'])/2
}
t2center = {
    'x':(tires[1][1]['x'] + tires[1][0]['x'])/2, 
    'y':(tires[1][3]['y'] + tires[1][0]['y'])/2
}
tcenter = {
    'x':(t1center['x'] + t2center['x'])/2, 
    'y':(t1center['y'] + t2center['y'])/2
}

if length > breadth:
    rotaion_angle, comp_rotation_angle = um.get_angle(car[0], car[3])
    print(f'rotation_angle {rotaion_angle}, count_rotation_angle {comp_rotation_angle}')

    # rotated_image = rotate_image(config['image_path'], rotaion_angle)
    # comp_rotated_image = rotate_image(config['image_path'], comp_rotation_angle)
    end = time.time()
    print("Rotation Angle Time",end-start)

    start = time.time()
    angle = [rotaion_angle, comp_rotation_angle]
    for theta in angle:
        print(f"for angle {theta}")
        rcentroid = um.rotate_point(centriod, theta)
        print(f'original car centroid ={centriod}, rotated centroid={rcentroid}')
        rtcenter = um.rotate_point(tcenter, theta)
        print(f'original tire centroid ={tcenter}, rotated centroid={rtcenter}')
        if rcentroid['y'] >= rtcenter['y']:
            correct_rotation = theta
    end = time.time()
    print(f'correct_rotation: {correct_rotation}') 
    print("time takes for correct rotation calculation", end - start)
    tend = time.time()
    print("total_time:", tend-tstart)
    output_image = rotate_image(config['image_path'], rotaion_angle)
else: 
    config['image_path']

# image = cv2.imread(config['image_path'])
# img = draw_box(image, car)
# for box in tires: 
#     img = draw_box(img, box)










