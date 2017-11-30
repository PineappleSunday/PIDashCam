import picamera
import RPi.GPIO as GPIO
import time 
import datetime

def Init():
	print('Initializing Pi and Camera Settings')
	LED = 20
	camera = picamera.PiCamera()
	camera.resolution =(640,480)
	camera.hflip = True
	camera.vflip = True
	return camera,LED
def Record(camera,LED):
	date = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
	t_end = time.time() * 60 * 10
	camera.start_recording(date + '.h264')

	while (time.time() < t_end):
		continue
	camera.stop_recording()
	print('Camera has stopped recording')
	
def main():
    camera,LED = Init()

    while (True):

        if (True):
           Record(camera,LED)
if __name__ == "__main__":
	main()
