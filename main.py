import cv2
import time
import random

cap = cv2.VideoCapture('muyaho.mp4')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output_%s.mp4' % time.time(), fourcc, cap.get(cv2.CAP_PROP_FPS) / 2, (w, h))

# cap.set(1, 900) # 무야호 시작

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    if random.random() > 0.9:
        theta = random.randint(-3, 3)
        x, y = random.randint(-10, 10), random.randint(-10, 10)

        M = cv2.getRotationMatrix2D(center=(w // 2, h // 2), angle=theta, scale=1.0)
        M[0, 2] += x
        M[1, 2] += y

        img = cv2.warpAffine(img, M=M, dsize=(w, h))

    img = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=0)

    '''
    sigma_s: Range between 0 to 200. Default 60.
    sigma_r: Range between 0 to 1. Default 0.07.
    shade_factor: Range between 0 to 0.1. Default 0.02.
    '''
    gray, color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.05, shade_factor=0.015)


    cv2.imshow('gray', gray)
    # cv2.imshow('color', color)

    out.write(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
