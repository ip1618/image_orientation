import numpy as np 

def distince(x1, x2, y1, y2):
    dis = np.sqrt(np.square(y2 -y1) + np.square(x2-x1))
    return dis 

def rotate_point(point:dict, angle)->dict: 
    angle_rad = np.deg2rad(angle)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)], 
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])
    rotated_point = np.dot(rotation_matrix, np.array([point['x'], point['y']]))
    return {'x': rotated_point[0], 'y': rotated_point[1]}

def get_angle(cor1, cor2): 
    angle_rad = np.arctan2(cor2['y'] - cor1['y'], cor2['x'] - cor1['x'])
    angle_deg = np.degrees(angle_rad)
    count_angle_deg = angle_deg + 180 if angle_deg < 0 else angle_deg - 180 
    return angle_deg, count_angle_deg 