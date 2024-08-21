import math

def calc_dist(src, dst):
    return math.sqrt(math.pow(src[0]-dst[0],2) + math.pow(src[1]-dst[1],2) + math.pow(src[2]-dst[2],2))

if __name__ == '__main__':
    video_fps = 29.97

    street_lamp_left_poses = [ 
        [0.750207, -1.03877, -3.55228], 
        [0.586235, -0.793863, 0.523832]
    ]

    street_lamp_right_poses = [ 
        [-1.190, -0.811, -2.450], 
        [-1.273, -0.580, 1.653]
    ]

    pixel_distance = calc_dist(street_lamp_left_poses[0], street_lamp_left_poses[1])
    real_distance = 60.6 # meter

    # Ratio를 얼마나 정확하게 구하는 지가 결과에 크게 영향을 미침.
    # 추후에는 수 많은 구간의 거리를 구하여 ratio의 평균값을 가져가는 것도 좋을듯.
    ratio_meter_to_pixel = real_distance / pixel_distance
    print("ratio ==", ratio_meter_to_pixel, "[m/pxls]")

    # x, y, z
    camera_pos = [ 
        [0.109335, 0.460956, 8.06914], # 21
        [0.0822171, 0.422324, 7.32351], # 39
        [0.0765505, 0.435108, 6.83076], # 51
        [0.0821259, 0.426793, 6.34248], # 63
        [0.0817751, 0.316199, 5.63108], # 88 
        [0.0737895, 0.26494, 5.05106], # 96
        [0.063199, 0.238463, 3.81331], # 129
        [0.0603911, 0.197816, 3.26864], # 144
        [0.0466779, 0.164744, 2.73223], # 159
        [0.023697, 0.0898105, 1.46513], # 195
        [0.0218471, 0.0819532, 1.36334], # 198
        [-0.00562497, -0.0104462, -0.288146], # 252
        [-0.0119932, -0.0489406, -0.978953], # 279
        [-0.0136101, -0.0800238, -1.38137], # 297
        [-0.0124651, -0.107869, -1.77669], # 318
        [-0.013698, -0.121416, -1.92592], # 327
        [-0.0150004, -0.127172, -2.02057], # 333
        [-0.0165398, -0.141187, -2.19609], # 345 
        [-0.0187192, -0.152975, -2.35064], # 357
        [-0.0219217, -0.171069, -2.54739], # 375
        [-0.0262896, -0.184652, -2.684], # 390
        [-0.0283192, -0.195721, -2.81574], # 408
        [-0.0289489, -0.201565, -2.89942], # 423
        [-0.0310926, -0.205454, -2.96988] # 441
    ]

    # index
    frame_number = [
        21, 39, 51, 63, 81, 96, 129, 144, 159, 195, 198, 252, 279, 297, 318, 327, 333, 345, 357, 375, 390, 408, 423, 441
    ]
    
    # km/h
    gps_velocity =[
        63, 62, 62, 61, 60, 59, 59, 56, 55, 55, 51, 44, 39, 39, 32, 32, 32, 25, 25, 18, 18, 13, 13
    ]

    for i in range(len(frame_number)-1):
        duration = ((frame_number[i+1] - frame_number[i])/video_fps) / (60 * 60) # hours
        estimated_velocity = (calc_dist(camera_pos[i+1], camera_pos[i]) * ratio_meter_to_pixel / 1000) / duration
        print("(%3d -> %3d) Estimated: %5.2f[km/h]"%(frame_number[i], frame_number[i+1], estimated_velocity), end='')
        print(",  GPS: %d[km/h]"%(gps_velocity[i]))
        
        
'''
오차가 생기는 이유로 GPS의 정확도를 꼽고 싶음.
현재 결과에서는 속도가 높을 수록 정확성이 높은 것으로 나옴.
속도가 높다는 것은 같은 시간 동안 더 먼 거리를 갈 수 있다는 것임.
GPS의 오차는 정해져 있기 때문에 계산 과정에서 거리가 클 수록 오차가 상대적으로 작아져 결과의 정확성이 상대적으로 높아짐.
하지만 속도가 느릴 때는 상대적으로 오차가 크게 느껴지기 때문에 결과가 정확하지 않을 수 있다고 생각함.
'''