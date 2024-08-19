import cv2
import numpy as np 

def rotate_image(image_path, angle): 
    image = cv2.imread(image_path)
    (h, w)= image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]
    rotated_image = cv2.warpAffine(image, M, (new_w, new_h))
    # cv2.imshow("rotated_image", rotated)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return rotated_image

def draw_box(image, box):
    top_left = (int(box[0]['x']*image.shape[1]), int(box[0]['y']*image.shape[0]))
    bottom_right = (int(box[2]['x']*image.shape[1]), int(box[2]['y']*image.shape[0]))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    return image

def draw_image_coordinate(image, plot:list):
    for i, cor in enumerate(plot): 
        x = cor['x']
        y = cor['y']
        height, width, _ = image.shape
        cv2.line(image, (0,0), (width, 0), (0, 255, 0), 2)
        cv2.line(image, (0,0), (0, height), (255, 0, 0), 2)
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(image, f'cor["text"]:{x}, {y}', (x+15, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
