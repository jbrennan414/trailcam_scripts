import boto3
import os
import shutil

s3 = boto3.resource("s3")

#list all files
arr = os.listdir('/home/pi/trailcam_scripts/photos')

#upload each file
for file in arr:
  data = open(f'/home/pi/trailcam_scripts/photos/{file}', 'rb')
  s3.Bucket('trailcam-photos').put_object(Key=file, Body=data)


#todo this should be a try/catch...
#delete photos directory
dir_path = '/home/pi/trailcam_scripts/photos'

try:
  shutil.rmtree(dir_path)
except OSError as e:
  print("Ok that didnt work")

#make a new photos directory
os.mkdir(dir_path)
exit()
