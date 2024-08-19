import json 
import utils_math as um 
from ocr import bounding_box
from utils_image import rotate_image, draw_box
import time
import cv2 
from PIL import Image
tstart = time.time()
with open('config.json', 'r') as file: 
    config = json.load(file)

print("ocr_started")
start = time.time()
coordinate = bounding_box(config['image_path'], config['vision_api_key'])
end = time.time()
print(coordinate)
print("ocr_done", end-start)


start = time.time()
car = coordinate['Car']
tires = coordinate['Tires']
img = cv2.imread(config['image_path'])
img = draw_box(img, car)
print(f'car coordeinates: {car}')
for tire in tires: 
    print(f'tire coordinates {tire}')
    img = draw_box(img, tire)
# cv2.imshow("bounding_boxes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
breadth = um.distince(car[0]['x'], car[1]['x'], car[0]['y'], car[1]['y'])
length = um.distince(car[0]['x'], car[3]['x'], car[0]['y'], car[3]['y'])

centriod = {
                'x':(car[1]['x'] + car[0]['x'])/2, 
                'y':(car[3]['y'] + car[0]['y'])/2
            }
print(f'centroid {centriod}')
t1center = {
    'x':(tires[0][3]['x'] + tires[0][2]['x'])/2, 
    'y':(tires[0][3]['y'] + tires[0][2]['y'])/2
}
print(f't1 center is:{t1center}')
t2center = {
    'x':(tires[1][3]['x'] + tires[1][2]['x'])/2, 
    'y':(tires[1][3]['y'] + tires[1][2]['y'])/2
}
print(f't2 center is:{t2center}')
tcenter = {
    'x':(t1center['x'] + t2center['x'])/2, 
    'y':(t1center['y'] + t2center['y'])/2
}
print(f'The avg center of tires = {tcenter}')
if t1center['y'] != t2center['y']:
    start = time.time()
    rotation_angle, comp_rotation_angle = um.get_angle(t1center, t2center)
    end = time.time()
    print("rotation angle time", end-start)
    print(f'rotation_ange: {rotation_angle}, comp_rotation_angle: {comp_rotation_angle}')
    angle = [rotation_angle, comp_rotation_angle]
    for theta in angle: 
        print(f'for angke {theta}')
        rcentroid = um.rotate_point(centriod, theta)
        print(f'original car centroid ={centriod}, rotated centroid={rcentroid}')
        rtcenter = um.rotate_point(tcenter, theta)
        print(f'original tire centroid ={tcenter}, rotated centroid={rtcenter}')
        for i in range(4): 
            print(f'no {i} car coord: {um.rotate_point(car[i], theta)}')
            print(f'no {i} tire coord: {um.rotate_point(tire[i], theta)}')

        if rcentroid['y'] < rtcenter['y']:
            corect_rotation = theta
    
    print(f'Correct_rotation {corect_rotation}')
    if corect_rotation > 0:         
        output_image = rotate_image(config['image_path'], corect_rotation)
    else: 
        output_image = rotate_image(config['image_path'],360- corect_rotation)

    # cv2.imshow("correct_rotated_image", output_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

else: 
    config['image_path']
tend = time.time()
print("total time takes:", tend-tstart)
# image = cv2.imread(config['image_path'])
# img = draw_box(image, car)
# for box in tires: 
#     img = draw_box(img, box)










