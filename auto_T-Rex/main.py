import cv2
import mss
import numpy as np
import keyboard as kb
import time

def show(img):
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def get_center_of_dino():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        screenshot = np.array(sct.grab(monitor), dtype=np.uint8)

    dino = cv2.imread('dino.png')

    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    sample = cv2.matchTemplate(screenshot, dino, cv2.TM_CCOEFF_NORMED)

    max_loc = cv2.minMaxLoc(sample)[3]

    threshold = 0.8

    is_dinosaur_present = sample[max_loc[1], max_loc[0]] > threshold

    if is_dinosaur_present:
        dino_height, dino_width = dino.shape[:2]

        center_x = max_loc[0] + dino_width // 2
        center_y = max_loc[1] + dino_height // 2

        return(center_x, center_y)
    else:
        print("Can't find dino")
    
def game(x, y):
    tsleep = 3
    forward_danger_zone = {"top": y-53, "left": x+60, "width": 100, "height": 47}
    down_save_zone = {"top": y, "left": x, "width": 142, "height": 5}
    print(f'You have {tsleep}sec')

    time.sleep(tsleep)
    kb.press('space')
    while True:
        with mss.mss() as sct:
            danger_zone = np.array(sct.grab(forward_danger_zone), dtype=np.uint8)
            save_zone = np.array(sct.grab(down_save_zone), dtype=np.uint8)

            if save_zone.mean()>240:
                kb.press('down')
                time.sleep(0.17)
            if danger_zone[-1, :, 0].mean()<235:
                kb.release('down')
                kb.press('space')                                                                       
     
if  __name__ == "__main__":
    coords_center_of_dino = get_center_of_dino()
    if coords_center_of_dino:
        game(coords_center_of_dino[0], coords_center_of_dino[1])