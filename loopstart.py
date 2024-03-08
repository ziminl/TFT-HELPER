


import pyautogui
import time

def center_coordinates(rect):
    x = rect[0] + rect[2] // 2
    y = rect[1] + rect[3] // 2
    return x, y

def search_and_click_image(image_path):
    image_location = pyautogui.locateOnScreen(image_path)

    if image_location:
        center_x, center_y = center_coordinates(image_location)
        
        # Click on the center of the image
        pyautogui.click(center_x, center_y)
        print(f"Clicked on the center of {image_path}")
        return True
        
    else:
        print(f" {image_path} not found")
        return False

if __name__ == "__main__":
    image_path = 'img/start2.png'
    num_iterations = 100000
    iteration_delay = 2

    for i in range(num_iterations):
        success = search_and_click_image(image_path)
        if not success:
            print("not started yet. retring")
        time.sleep(iteration_delay)


