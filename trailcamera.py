from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from gpiozero import LED
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
now = datetime.now()

date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
led = LED(17)

while True: 
  pir.wait_for_motion()
  print("Motion detected")
  led.on()
  camera.start_preview()
  camera.capture('/home/pi/trailcam_scripts/photos/image.jpg')
  camera.stop_preview()
  pir.wait_for_no_motion()
  print("Motion stopped")
  led.off()
