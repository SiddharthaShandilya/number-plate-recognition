
import boto3
import time # for delaying time so that aws can extract texts
import logging
import threading # for multi-threading
from botocore.exceptions import ClientError
import cv2, numpy


model = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
#model_car = cv2.CascadeClassifier('cars_detection.xml')

#####################################################################################################################

def car_detection(cap): # here we detect the plate, crop it and save into another image
    while True:
        ret,photo = cap.read()
        photo = cv2.resize(photo,(1800,1800))
        if len(photo)==0:
            pass
        else:
            #faces = model_car.detectMultiScale(photo)
            faces = model.detectMultiScale(photo)
            faces = numpy.asarray(faces)
            #print(faces.shape)
            #print(photo)
    
            for i in range(faces.shape[0]):
                if len(faces) != 0:
                    x1 = faces[i][0]
                    y1 = faces[i][1]
                    x2 = x1 + faces[i][2]
                    y2 = y1 + faces[i][3]
                    cropped_pic = cv2.rectangle(photo,(x1,y1),(x2,y2),[0,220,0],5)
                    
        
        
                else:
                    #cropped_pic = photo
                    time.sleep(5)
                    pass
        #s3_img=mpl.imshow(cropped_pic[y1:y2,x1:x2])
        #print(type(s3_img))
        cv2.imwrite('for_s3_image.jpg', cropped_pic[y1:y2,x1:x2])
        #time.sleep(5)# to slow the image processing rate as it takes time to upload s3 bucket
        
#___________________________________________________________________________________________

def upload_file(file_name, bucket, object_name=None): # we take the cropped image and upload it into S3 bucket for aws rekognition to process it
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        #logging.error(e)
        return False
    return True
#___________________________________________________________________________________________________________________________________________________
def detect_text(photo, bucket):# here we reachout to aws rekognition and give it the bucket name and take the text as output
    total_number_plate={}

    client=boto3.client('rekognition')

    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                       
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            #print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            #print ('Id: {}'.format(text['Id']))
            #if 'ParentId' in text:
                #print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            
            total_number_plate[text['Id']] = text['DetectedText']
            print(total_number_plate)
            
    return len(textDetections)
#_________________________________________________________________________________________________________
"""
def threading(cap,bucket,photo):
    
    upload_file_thread = threading.Thread(target=upload_file, args=(photo,bucket,))
    detect_text_thread = threading.Thread(target=detect_text, args=(photo, bucket,))
    car_detection_thread.start()
    
    upload_file_thread.start()
    detect_text_thread.start()

"""
#______________________________________________________________________________
def main():
    
    bucket='text-recognition-project' # here u need to give your bucket list to store the images from the video
    photo='for_s3_image.jpg'
    
    cap = cv2.VideoCapture('car_video.mp4')
    car_detection_thread = threading.Thread(target=car_detection, args=(cap,))
    car_detection_thread.start()
    while True:
        if upload_file(photo,bucket):
            text_count=detect_text(photo,bucket)
            
        else:
            pass
            
        #print("Text detected: " + str(text_count))
        #print(text_count['DetectedText'])
        


if __name__ == "__main__":
        main()
        
