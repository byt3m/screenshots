import keyboard, time, ctypes, os
from PIL import ImageGrab


def FormatearFecha(cadena):
	if len(list(cadena)) == 1:
		cadena = "0" + cadena
		return cadena
	else:
		return cadena

n = 1

print("Press 'F7' to grab a screenshot.")

while True:	

	if keyboard.is_pressed("F7"):

		fecha = time.localtime()
		ano = str(fecha.tm_year)
		mes = FormatearFecha(str(fecha.tm_mon))
		dia = FormatearFecha(str(fecha.tm_mday))
		hora = FormatearFecha(str(fecha.tm_hour))
		minutos = FormatearFecha(str(fecha.tm_min))
		segundos = FormatearFecha(str(fecha.tm_sec))

		nuevaruta = 'screenshots' + "\\" + ano + mes + dia
		if not os.path.exists(nuevaruta):
			os.makedirs(nuevaruta)

		name = "screenshot_" + hora + minutos + segundos + "_" + str(n) + ".png"
		ruta = nuevaruta + "\\" + name

		try:
			#ImageGrab.grab().save(ruta) 
			ImageGrab.grab(bbox=(530, 230, 1380, 885)).save(ruta) # bbox = left, bottom, right, top
			print("Screenshot saved as %s" % name)
			texto = "Screenshot saved as " + name
			texto = bytes(texto, encoding="UTF-8")
			ctypes.windll.user32.MessageBoxA(0, texto, b"Screenshot", 0x0)
			n += 1
		except Exception as e:
			print("An error ocurred while generating the screenshot.")
			print(e)
			ctypes.windll.user32.MessageBoxA(0, b"An error ocurred while generating the screenshot.", b"ERROR", 0x0)
		
	time.sleep(0.01)