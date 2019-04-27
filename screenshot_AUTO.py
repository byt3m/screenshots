import time, os, ctypes
import keyboard as k
from pynput import keyboard
from PIL import ImageGrab


def FormatearFecha(cadena):
	if len(list(cadena)) == 1:
		cadena = "0" + cadena
		return cadena
	else:
		return cadena


def GrabImage(n, ruta, nombre):
	try:
		#ImageGrab.grab().save(ruta) 
		ImageGrab.grab(bbox=(530, 230, 1380, 885)).save(ruta)  # bbox = left, bottom, right, top
		print("Screenshot saved as %s" % nombre)
	except:
		print("An error ocurred while generating the screenshot.")
		ctypes.windll.user32.MessageBoxA(0, b"An error ocurred while generating the screenshot.", b"ERROR", 0x0)
		exit(1)


def start():
	fecha = time.localtime()
	ano = str(fecha.tm_year)
	mes = FormatearFecha(str(fecha.tm_mon))
	dia = FormatearFecha(str(fecha.tm_mday))
	'''hora = FormatearFecha(str(fecha.tm_hour))
	minutos = FormatearFecha(str(fecha.tm_min))
	segundos = FormatearFecha(str(fecha.tm_sec))'''
	nuevaruta = 'screenshotsAUTO' + "\\" + ano + mes + dia
	if not os.path.exists(nuevaruta):
		os.makedirs(nuevaruta)

	n = 1
	KB = keyboard.Controller()

	while(True):
		nombre = str(n) + ".png"
		ruta = nuevaruta + "\\" + nombre
		GrabImage(n, ruta, nombre)

		time.sleep(0.4)
		KB.press(keyboard.Key.page_down)
		time.sleep(0.4)
		n += 1

		if k.is_pressed("F11"):
			exit(1)

		time.sleep(0.1)


def on_press(key):
    if key == keyboard.Key.f7:
        start()
        return False


print("Press F7 to start.\nPress F11 to exit at any moment.")

with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()        
    except Exception as e:
        print("ERROR: %s" % e)
        os.system("pause")