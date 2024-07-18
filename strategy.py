#fast lvup


#n-2 and n-5 up (ex. 3-2 4-2 4-5 5-2) 
# algo : max -4n ==0 -> lv up (8lv will be last)
# to add augmentation based / 



#strategy code logic

#check with ocr, starting champion
#start champion : deck
#calculate the best way.
#to add more things like augmentation 

#ocr logic in line 12


# return what to buy
#list all things in shop+reroll clicking(mabie lv 8 with 3cost 3star/ 5with 1cost 3star / 6,7 with 2
#

###########code############
#pip install pillow pytesseract pygetwindow pyautogui

from PIL import Image
import pytesseract
import pyautogui

# Tesseract setup
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

left = 200
top = 400
width = 200
height = 400
box = (left, top, left + width, top + height)

screenshot = pyautogui.screenshot(region=box)

screenshot.save('captured_region.png')

screenshot = screenshot.convert('L')  # Convert to grayscale

text = pytesseract.image_to_string(screenshot)

print("200~400x200x400 has :", text)
#make deck and collect one by one, but after reroll, capture it again.
