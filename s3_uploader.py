import boto3

s3 = boto3.resource("s3")

#for bucket in s3.buckets.all():
#  print(bucket.name)

data = open('/home/pi/trailcam_scripts/photos/image.jpg', 'rb')
s3.Bucket('trailcam-photos').put_object(Key='image.jpg', Body=data)
