import cv2

def rotate_image(image_path, angle): 
    image = cv2.imread(image_path)
    (h, w)= image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    # cv2.imshow("rotated_image", rotated)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return rotated_image

def draw_box(image, box):
    top_left = (int(box[0]['x']*image.shape[1]), int(box[0]['y']*image.shape[0]))
    bottom_right = (int(box[2]['x']*image.shape[1]), int(box[2]['y']*image.shape[0]))
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    return image

