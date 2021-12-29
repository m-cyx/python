import cv2
import pytesseract

# Путь для подключения tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Подключение фото
img = cv2.imread('C:/Users/Pixel/Desktop/lab6/crop2.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Будет выведен весь текст с картинки
config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=config))

# Отображаем фото
cv2.imshow('Result', img)
cv2.waitKey(0)