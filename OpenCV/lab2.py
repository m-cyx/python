import cv2

# Создать объект захвата видео, второй аргумент тут для того, чтобы не видеть ошибку.
input_cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Проверка на то, открылся ли видеопоток
if(input_cam.isOpened() == False):
	print("Ошибка при открытии видеопотока")

# Получаем высоту и ширину кадра, устанавливаем фпс.
# Объект input_cam имеет метод get() для получения метаданных. 3 и 4 это номера данных
# CAP_PROP_FRAME_WIDTH =3, CAP_PROP_FRAME_HEIGHT =4  Длина и ширина соответственно
frame_width = int(input_cam.get(3))
frame_height = int(input_cam.get(4))
frame_size = (frame_width,frame_height)
fps = 20


# Создаем объект записи видео
output = cv2.VideoWriter(   'record.avi', 
                            cv2.VideoWriter_fourcc('M','J','P','G'), #для mp4 другой аргумент
                            fps, 
                            frame_size)


# Начало записи
while(input_cam.isOpened()):      
	ret, frame = input_cam.read() # Метод input_cam.read() возвращают кортеж (логическое значение, кадр)
                                  # Переменные получают значения из кортежа
	if ret == True:
		output.write(frame)       # Записал фрейм
		cv2.imshow("Frame",frame) # Показал фрейм в окошке
		key = cv2.waitKey(20)     # Ждём 20 мс нажатия кнопки
		if (key == 27):           # 27 - код кдавиши Esc в ASCII
			break                 # Кнопочка выхода
	else:
		print('Веб-камера отключена')
		break


# Освобождаю объекты захвата и вывода видео. Это нужно как бы для обнуления указателей.
# Например, если бы мы два потока одновременно запустили, то они бы ругались.
input_cam.release()
output.release()
cv2.destroyAllWindows()


