# This is Assignment 1
# Name Of Author : Chandan Kumar
# This Script will convert an RGB Video to HSV Video
# Then it takes each frame and calculates H, S, V
# The Average is taken out from each color channel
# The Value Channel is rounded up and an image is made by merging them
# We wii get an intuition on how the image looks
# If <70 it is night and >= 70 it is morning/day
# Percentage is calculated 

import numpy as np
import cv2 
import matplotlib.pyplot as plt
import math

def reshape_frames(V_mean_rounded):
    total_frames = len(V_mean_rounded)
    height = math.isqrt(total_frames)
    width = math.ceil(total_frames / height)
    
    V_mean_rounded_reshaped = np.array(V_mean_rounded)
    if len(V_mean_rounded_reshaped) < height * width:
        V_mean_rounded_reshaped = np.pad(V_mean_rounded_reshaped, (0, height * width - len(V_mean_rounded_reshaped)), mode='constant')
    
    V_mean_rounded_reshaped = V_mean_rounded_reshaped.reshape((height, width))
    return V_mean_rounded_reshaped

def rgb_to_hsv(video_path):
    cap = cv2.VideoCapture(video_path)
    H, S, V = [], [], []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV', hsv_frame)

        h, s, v = cv2.split(hsv_frame)
        H.append(h)
        S.append(s)
        V.append(v)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return (H, S, V)

def average_and_round_hsv(H, S, V):
    H_mean, S_mean, V_mean = [], [], []
    for i, j, k in zip(H, S, V):
        H_mean.append(i.mean())
        S_mean.append(j.mean())
        V_mean.append(k.mean())

    H_mean_rounded = np.round(H_mean).astype(int)
    S_mean_rounded = np.round(S_mean).astype(int)
    V_mean_rounded = np.round(V_mean).astype(int)

    return H_mean_rounded, S_mean_rounded, V_mean_rounded

def classify_brightness(value):
    if value >= 70:
        return "Morning"
    elif value < 70:
        return "Night"
    
def classify_time_of_day(video_path):
    (H, S, V) = rgb_to_hsv(video_path)
    (_, _, V_mean_rounded) = average_and_round_hsv(H, S, V)

    morning_count = 0
    night_count = 0

    for v in V_mean_rounded:
        category = classify_brightness(v)
        if category == "Morning":
            morning_count += 1
        elif category == "Night":
            night_count += 1

    total_frames = len(V_mean_rounded)

    morning_percentage = (morning_count / total_frames) * 100
    night_percentage = (night_count / total_frames) * 100

    # V_mean_rounded_reshaped = np.array(V_mean_rounded).reshape((71, 14))
    V_mean_rounded_reshaped = reshape_frames(V_mean_rounded)
    plt.imshow(V_mean_rounded_reshaped, cmap='viridis')
    plt.colorbar()
    plt.title("Brightness Heatmap")
    plt.show()

    print(f"Total Frames: {total_frames}")
    print(f"Morning: {morning_percentage:.2f}%")
    print(f"Night: {night_percentage:.2f}%")


classify_time_of_day('mrng2night2.mp4')