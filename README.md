# Project Title

Automatic License Plate Recognition System (ALPR)


## Installing virtual env and necessary packages

Create and activate virtual env.

```bash
python3 -m venv ALPR
```


Activating the virtual env


```bash
source ALPR/bin/activate
```


Installing necessary packages

```bash
pip3 install tensorflow
```

## Compile & Run
Run the below codes in sequence to process the image and train the model for character recognition.


```bash
python3 Image_Preprocessing.py

```

```bash
python3 Number_Plate_Detection.py 
```


```bash
python3 Character_Segmentation.py 
```

```bash
python3 Character_Recognition.py 
```

```bash
python3 Character_Recognition_Better.py 
```


## Use

ALPR uses image processing and recognition technology. It employs Convulational Neural Network (CNN) model for better predictablity of the numbers and digits.

Libraries used:

Tensorflow's Keras API

OpenCV

numpy
## Screenshots

Input image

![e6002d41-dff1-4f96-8fae-9f13e8f756f5](https://github.com/rkirtii/Automatic-License-Plate-Recognition/assets/142138548/a7796f8e-63b7-42ad-a5e1-4cee06d29f21)


Processed image

![711a4559-bc75-49ce-8eaf-1902f4bab553](https://github.com/rkirtii/Automatic-License-Plate-Recognition/assets/142138548/0a0ac0d3-9dde-45c0-8553-4d397430172b)


Final output

![3aca8a8b-2524-474f-b788-9958a3ee5dad](https://github.com/rkirtii/Automatic-License-Plate-Recognition/assets/142138548/06efbdb3-d851-44e0-a502-4a11b09cbb10)
