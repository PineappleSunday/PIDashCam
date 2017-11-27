import picamera
import RPi.GPIO as GPIO
import time 
import datetime

def Init():
	LED = 20
	camera = picamera.PiCamera()
	camera.resolution =(640,480)
	return camera,LED
def Record(camera,LED):
	date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
	t_end = time.time() + 10 * 1
	camera.start_recording('Video' +date + '.h264')

	while (time.time() < t_end):
		print('Recording')
	camera.stop_recording()

def main():



	camera,LED = Init()
	while True:
		if (True):
			print('I am recording')
			time.sleep(1)
			Record(camera,LED)
if __name__ == "__main__":
	main()