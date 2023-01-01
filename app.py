import pyautogui
import tkinter as tk
from tkinter import ttk
from pynput import mouse, keyboard
from PIL import Image
import pytesseract # https://www.youtube.com/watch?v=L8q-KCbXybc, https://ddolcat.tistory.com/954 (에러 해결, 한글 데이터 셋 자료 링크)
# import easyocr
import win32clipboard as clip
import win32con
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# reader = easyocr.Reader(['ko', 'en'])

# IMAGE_SUBTITME = "subtitle_screenshot.png"
IMAGE_VIDEO = "video_screenshot.png"

# Global variables to store the start and end coordinates of the region
# subtitle_start_x = 0
# subtitle_start_y = 0
# subtitle_end_x = 0
# subtitle_end_y = 0
# subtitle_width = 0
# subtitle_height = 0

video_start_x = 0
video_start_y = 0
video_end_x = 0
video_end_y = 0
video_width = 0
video_height = 0

# Create the main window
window = tk.Tk()

# Subtitle
# label title
# label_subtitle_title = tk.Label(window, text="Subtitle Capture: F4", font=("Arial Bold", 20))
# label_subtitle_title.pack()

# subtitle start point
# is_input_subtitle_start_point = False
# def reverse_is_input_subtitle_start_point():
#   global is_input_subtitle_start_point
#   is_input_subtitle_start_point = not is_input_subtitle_start_point
# button_subtitle_start_point = tk.Button(window, text="Setup Start Point", command=reverse_is_input_subtitle_start_point)
# label_subtitle_start_point = tk.Label(window, text="Click and drag to capture a region")
# button_subtitle_start_point.pack()
# label_subtitle_start_point.pack()

# subtitle end point
# is_input_subtitle_end_point = False
# def reverse_is_input_subtitle_end_point():
#   global is_input_subtitle_end_point
#   is_input_subtitle_end_point = not is_input_subtitle_end_point
# button_subtitle_end_point = tk.Button(window, text="Setup End Point", command=reverse_is_input_subtitle_end_point)
# label_subtitle_end_point = tk.Label(window, text="Click and drag to capture a region")
# button_subtitle_end_point.pack()
# label_subtitle_end_point.pack()

# def calculateSubtitleDimensions():
#   global subtitle_start_x, subtitle_start_y, subtitle_end_x, subtitle_end_y, subtitle_width, subtitle_height
#   # Calculate the dimensions of the region
#   print("Start point: ({}, {})".format(subtitle_start_x, subtitle_start_y))
#   print("End point: ({}, {})".format(subtitle_end_x, subtitle_end_y))
#   subtitle_width = subtitle_end_x - subtitle_start_x
#   subtitle_height = subtitle_end_y - subtitle_start_y
#   print ("Dimensions: ({}, {})".format(subtitle_width, subtitle_height))
#   label_subtitle_dimensions.config(text="Dimensions: ({}, {})".format(subtitle_width, subtitle_height))

# button_subtitle_calculate = tk.Button(window, text="Calculate Capture Region", command=calculateSubtitleDimensions)
# label_subtitle_dimensions = tk.Label(window, text="Dimensions: ({}, {})".format(subtitle_width, subtitle_height))
# button_subtitle_calculate.pack()
# label_subtitle_dimensions.pack()

# def captureSubtitleRegion():
#   global subtitle_start_x, subtitle_start_y, subtitle_width, subtitle_height
#   image = pyautogui.screenshot(region=(subtitle_start_x, subtitle_start_y, subtitle_width, subtitle_height))
#   image.save(IMAGE_SUBTITME)
#   return image
# button_subtitle_capture = tk.Button(window, text="Test Capture Region", command=captureSubtitleRegion)
# button_subtitle_capture.pack()

# separator = ttk.Separator(window, orient='horizontal')
# separator.pack(fill='x')

# Video
label_video_title = tk.Label(window, text="Video Capture: F2", font=("Arial Bold", 20))
label_video_title.pack()

# video start point
is_input_video_start_point = False
def reverse_is_input_video_start_point():
  global is_input_video_start_point
  is_input_video_start_point = not is_input_video_start_point
button_video_start_point = tk.Button(window, text="Setup Start Point", command=reverse_is_input_video_start_point)
label_video_start_point = tk.Label(window, text="Click and drag to capture a region")
button_video_start_point.pack()
label_video_start_point.pack()

# video end point
is_input_video_end_point = False
def reverse_is_input_video_end_point():
  global is_input_video_end_point
  is_input_video_end_point = not is_input_video_end_point
button_video_end_point = tk.Button(window, text="Setup End Point", command=reverse_is_input_video_end_point)
label_video_end_point = tk.Label(window, text="Click and drag to capture a region")
button_video_end_point.pack()
label_video_end_point.pack()

def calculateVideoDimensions():
  global video_start_x, video_start_y, video_end_x, video_end_y, video_width, video_height
  # Calculate the dimensions of the region
  print("Start point: ({}, {})".format(video_start_x, video_start_y))
  print("End point: ({}, {})".format(video_end_x, video_end_y))
  video_width = video_end_x - video_start_x
  video_height = video_end_y - video_start_y
  print ("Dimensions: ({}, {})".format(video_width, video_height))
  label_video_dimensions.config(text="Dimensions: ({}, {})".format(video_width, video_height))

button_video_calculate = tk.Button(window, text="Calculate Capture Region", command=calculateVideoDimensions)
label_video_dimensions = tk.Label(window, text="Dimensions: ({}, {})".format(video_width, video_height))
button_video_calculate.pack()
label_video_dimensions.pack()

def captureVideoRegion():
  print('captureVideoRegion')
  global video_start_x, video_start_y, video_width, video_height
  image = pyautogui.screenshot(region=(video_start_x, video_start_y, video_width, video_height))
  image.save(IMAGE_VIDEO)
  return image
button_video_capture = tk.Button(window, text="Test Capture Region", command=captureVideoRegion)
button_video_capture.pack()


separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x')


# setup mouse click position
is_input_mouse_click_position = False
mouse_start_x = 0
mouse_start_y = 0
def reverse_is_input_mouse_click_position():
  global is_input_mouse_click_position
  is_input_mouse_click_position = not is_input_mouse_click_position
button_mouse_click_position = tk.Button(window, text="Setup Mouse Click Position", command=reverse_is_input_mouse_click_position)
label_mouse_position = tk.Label(window, text="Click to set mouse click position")
button_mouse_click_position.pack()
label_mouse_position.pack()


# Define a function to handle mouse clicks
def on_mouse_click(x, y, button, pressed):
  try:
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    # global is_input_subtitle_start_point, subtitle_start_x, subtitle_start_y, is_input_subtitle_end_point, subtitle_end_x, subtitle_end_y
    global is_input_video_start_point, video_start_x, video_start_y, is_input_video_end_point, video_end_x, video_end_y
    global is_input_mouse_click_position, mouse_start_x, mouse_start_y
    # if is_input_subtitle_start_point:
    #   subtitle_start_x = x
    #   subtitle_start_y = y
    #   label_subtitle_start_point.config(text="Start point: ({}, {})".format(subtitle_start_x, subtitle_start_y))
    #   reverse_is_input_subtitle_start_point()
    # if is_input_subtitle_end_point:
    #   subtitle_end_x = x
    #   subtitle_end_y = y
    #   label_subtitle_end_point.config(text="End point: ({}, {})".format(subtitle_end_x, subtitle_end_y))
    #   reverse_is_input_subtitle_end_point()
    if is_input_video_start_point:
      video_start_x = x
      video_start_y = y
      label_video_start_point.config(text="Start point: ({}, {})".format(video_start_x, video_start_y))
      reverse_is_input_video_start_point()
    if is_input_video_end_point:
      video_end_x = x
      video_end_y = y
      label_video_end_point.config(text="End point: ({}, {})".format(video_end_x, video_end_y))
      reverse_is_input_video_end_point()
    if is_input_mouse_click_position:
      mouse_start_x = x
      mouse_start_y = y
      label_mouse_position.config(text="Mouse click position: ({}, {})".format(mouse_start_x, mouse_start_y))
      reverse_is_input_mouse_click_position()
    # if not pressed:
        # Stop listener
        # return False
  except:
    print('Error: on_mouse_click')


# ...or, in a non-blocking fashion:
mouseListener = mouse.Listener(on_click=on_mouse_click)
mouseListener.start()

def on_keyboard_press(key):
  try:
    print('{0} pressed'.format(key))
    # if key == keyboard.Key.f4: # subtitle capture
    #   print('f2 pressed: capture subtitle region')
    #   image = captureSubtitleRegion()
    #   copyToClipboard(image)
    #   # result = pytesseract.image_to_string(image, lang='kor+eng')
    #   # print(result)
    #   # textsFromImage =  reader.readtext(image)
    #   pyautogui.click()
    #   pyautogui.hotkey('ctrl', 'v')
    if key == keyboard.Key.f2: # video capture
      print('f2 pressed: capture video region')
      image = captureVideoRegion()
      copyToClipboard(image)
      # pyautogui.click()
      pyautogui.hotkey('ctrl', 'v')
    if key == keyboard.Key.f4:
      print('f4 pressed: stop or start video')
      pyautogui.click(mouse_start_x, mouse_start_y)
    if key == keyboard.Key.esc:
      # Stop listener
      return False
  except:
    print("An exception occurred")

# @see https://github.com/asweigart/pyperclip/issues/198
def copyToClipboard(image):
  output = BytesIO()
  image.convert('RGB').save(output, 'BMP')
  data = output.getvalue()[14:]
  output.close()
  clip.OpenClipboard()
  clip.EmptyClipboard()
  clip.SetClipboardData(win32con.CF_DIB, data)
  clip.CloseClipboard()


keyboardListener = keyboard.Listener(on_press=on_keyboard_press)
keyboardListener.start()

window.title("Lecture Tool")
window.geometry("400x700")
window.wm_attributes("-topmost", 1)
window.resizable(False, False)




# Start the event loop
window.mainloop()