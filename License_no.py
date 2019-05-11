#Importing all required libraries
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import model_from_json
import cv2
import glob
import numpy as np

def model_creator():
    # loading  json and hdfs and creating  model
    json_file = open('model1.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()   
    model = model_from_json(loaded_model_json)
    model.load_weights("model1.h5")

    #Compiling the model
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics = ['accuracy'])
    return model

def class_gen():
    #Generating the label of all the classes
    from keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

    test_datagen = ImageDataGenerator(rescale = 1./255)

    training_set = train_datagen.flow_from_directory('English/train',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')


    generator = train_datagen.flow_from_directory("English/train", batch_size=36)
    label_map = (generator.class_indices)
    return label_map


def plate_no(model=model_creator(),label_map=class_gen()):
    #Loading the images of the segmented character and identifying the number
    length=len(glob.glob("roi/*.png"))
    strng=""
    #global str
    for i in range(length):
    
        strn="roi/roi"+str(i)+".png"
        image=cv2.imread(strn)
        image = cv2.resize(image,(64,64))
        image = np.reshape(image,[1,64,64,3])
        classes=model.predict_classes(image)
        for key,val in label_map.items():
            if val==classes:
                strng=strng+key
    lst = list()
    for ch in strng:
        lst.append(ch)
   
    return lst




    
    
