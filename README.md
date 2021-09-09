# number-plate-recognition


👉Created a model that will detect a car in a live stream or video and recognize characters on number plate of the car . 

👉Secondly , it will use the characters and fetches the owners information using RTO API’s .

👉Created a Web portal where all this information will be displayed (using html,css,and js)

_______________________________________________________________________________________________________

I have seperated the solution into multiple steps.

Step1 - Train car detection model and crop the car image only.

Step2 - The cropped image will send to the car_number_plate_detecton_model where the visible number_plate will be cropped out.

Step3 - Then the cropped image of number plate will be send to Number-detecton model to read the numbera and alphabets

_______________________________________________________________________________________________________

                                                  FRONT-END
                  
-------------------------------------------------------------------------------------------------------

The front-End of the web_app will look similar to the below image. 
The user can upload their image using the upload button and then the whole file will be uplaoded to the server. To make it easy I have used s3 to store the image so that it can be  downloaded from anywhere.

For Securtiy the web_server only have access to the s3.

![front_end](https://user-images.githubusercontent.com/61656756/132627006-b7d86e25-4611-49f9-959b-192b671bcbf5.jpg)




_______________________________________________________________________________________________________

The number plate of the user will then be downloaded in the server after which the character detection model will come into play.


![car_number_recognition](https://user-images.githubusercontent.com/61656756/132623075-0254744b-fc37-4f28-beef-6da47ed78a92.jpg)
As you can see on the right side we have the characters detected as weel as their accuracy!

_______________________________________________________________________________________________________

                                               BEHIND THE SCENES
 
-------------------------------------------------------------------------------------------------------

Car Number plate detection and Extraction
_______________________________________________________________________________________________________


![1s](https://user-images.githubusercontent.com/61656756/132619998-a9c60197-aa2c-4e59-ae16-dad4ae43f7b1.jpg)


A demo of functioning model.

click on it ->  [car_number_Plate_detection](https://user-images.githubusercontent.com/61656756/132624993-95c65540-619d-4ddf-8583-457672114d61.gif)

As you can see the number plates are detected, cropped and then seperated


_______________________________________________________________________________________________________

                                        character Recognition model training

_______________________________________________________________________________________________________

![digit recognition](https://user-images.githubusercontent.com/61656756/132620711-b300ae0e-2e21-416c-9f2c-a1708cfe0477.jpg)

_______________________________________________________________________________________________________

Now that we have trained the character recognition model we are going to use this to extract the characters present in the number plate
_______________________________________________________________________________________________________


![car_number_recognition](https://user-images.githubusercontent.com/61656756/132629921-0e5d8808-9ac2-448d-837d-63af2ab4fa57.jpg)



_______________________________________________________________________________________________________
               
                                    
                                              Thank You
                                    
-------------------------------------------------------------------------------------------------------
              

