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
              
<!--

# Installation


[(Back to top)](#table-of-contents)

1. Install git (preferably, version >= 2.0) and python (preferably, version >=3.6)
 [(windows)](https://www.maketecheasier.com/install-git-bash-on-windows/)
 For Linux :
 ```bash
    sudo yum instal git -y
    sudo yum install python -y
 ```
 
2. Copy the github url from the repository : 

 ```bash
 https://github.com/SiddharthaShandilya/Face_recognition_task_EC2-What-sAPP.git
 ```

3. Select a Directory in local system and use 

  ```bash 
  git clone https://github.com/SiddharthaShandilya/Face_recognition_task_EC2-What-sAPP.git           
  ```

    *Note for `git clone command`  Please make sure that you have proper internet connection. *

    *Note for `python` Please try to anaconda for running the app.*  

4. Create a seperate virtual environment to avoid conflict between python libraries :
    ```bash
    python3 -m venv new-env 
    ```

5. Activate the virtual env: 👉 [(click Here)](https://www.programshelp.com/help/python/activate_virtual_environment_python_windows_10.html)
6. Install all the libraries for the application.
```bash
pip3 install -r requirements.txt
```

6. Have a look at [Recommended configurations](#recommended-configurations) and [Custom configurations](#custom-configurations).


</br></br>


# Recommended configurations

[(Back to top)](#table-of-contents)

<!--

1. To add some short command (say, `lc`) with some flag options (say, `-l`, `-A`, `--sd`) by default, add this to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.) :
    ```sh
    alias lc='colorls -lA --sd'
    ```

2. For changing the icon(s) to other unicode icons of choice (select icons from [here](https://nerdfonts.com/)), change the YAML files in a text editor of your choice (say, `subl`)

    ```sh
    subl $(dirname $(gem which colorls))/yaml
    ```

</br></br>
-->
<!--

# Custom configurations

[(Back to top)](#table-of-contents)

<!--
You can overwrite the existing icons and colors mapping by copying the yaml files from `$(dirname $(gem which colorls))/yaml` into `~/.config/colorls`, and changing them.

- To overwrite color mapping :

  Please have a look at the [list of supported color names](https://github.com/sickill/rainbow#color-list). You may also use a color hex code as long as it is quoted within the YAML file and prefaced with a `#` symbol.

  Let's say that you're using the dark color scheme and would like to change the color of untracked file (`??`) in the `--git-status` flag to yellow. Copy the defaut `dark_colors.yaml` and change it.

  ```sh
  cp $(dirname $(gem which colorls))/yaml/dark_colors.yaml ~/.config/colorls/dark_colors.yaml
  ```

  In the `~/.config/colorls/dark_colors.yaml` file, change the color set for `untracked` from `darkorange` to `yellow`, and save the change.

  ```
  untracked: yellow
  ```

  Or, using hex color codes:

  ```
  untracked: '#FFFF00'
  ```

- To overwrite icon mapping :

  Please have a look at the [list of supported icons](https://nerdfonts.com/). Let's say you want to add an icon for swift files. Copy the default `files.yaml` and change it.

  ```sh
  cp $(dirname $(gem which colorls))/yaml/files.yaml ~/.config/colorls/files.yaml`
  ```

  In the `~/.config/colorls/files.yaml` file, add a new icon / change an existing icon, and save the change.


  ```
  swift: "\uF179"
  ```

- User contributed alias configurations :

  - [@rjhilgefort](https://gist.github.com/rjhilgefort/51ea47dd91bcd90cd6d9b3b199188c16)


</br></br>

# Updating

[(Back to top)](#table-of-contents)

Want to update to the latest version of `chat_app`?

<!--
```sh
gem update colorls
```



</br></br>

# Uninstallation

[(Back to top)](#table-of-contents)

Want to uninstall and revert back to the old style? No issues (sob). Please feel free to open an issue regarding how we can enhance `chat_app`.

<!--
```sh
gem uninstall colorls
```


</br></br>

# Contributing

[(Back to top)](#table-of-contents)

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first. :tada:


</br>

# Future Scope
[(Back to top)](#table-of-contents)

Adding Voice chat app will make it more user friendly





-->
