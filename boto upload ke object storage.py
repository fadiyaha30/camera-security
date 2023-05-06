import boto3  #package python boto untuk upload ke storage s3

hostname = "agungsurya.is3.cloudhost.id" #nama hostname tempat penyedia storage s3 untuk nyimpen video
secret_key = "ofWnaJUWRSkZ1AgquPDgCyq6exLgXNFeclAZCpOZ" 
access_key = "M8ZGSA5AWHHOVRXQMDGX" 


################### deklarasi ###################
session = boto3.session.Session()
client = session.client('s3', **{
    "region_name": hostname.split('.')[0],
    "endpoint_url": "https://" + hostname,
    "aws_access_key_id": access_key,
    "aws_secret_access_key": secret_key
})
#################################################


with open('data/video.mp4', 'rb') as file: #untuk buka folder/video.mp4 
    response = client.put_object(Bucket='agungsurya', Key='video.mp4', Body=file, ACL='private') 
    #untuk tujuan ke bucket storage s3 agungsurya 

print(response) #respond dari server s3 storage









#response = client.list_objects(Bucket='dbwhadgw')
#print(response)


#response = client.list_buckets()
#print(response)
