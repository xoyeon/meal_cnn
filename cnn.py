
import streamlit as st
import numpy as np
import pandas as pd
import joblib

from keras.models import load_model
from PIL import Image, ImageOps
from keras.preprocessing import image
from tensorflow import keras

def welcome():
    st.title('오늘 몇 칼로리?')
    st.subheader('오늘의 식사를 이미지 파일로 업로드 해 주세요.')
    
    st.image('급식93.svg',use_column_width=True)

    st.subheader('성인 하루 권장 칼로리는')
    col1, col2 = st.columns(2)
    col1.metric("성인 남성", "체중(kg)X1.0X24", "평균 2700kcal")
    col2.metric("성인 여성", "체중(kg)X0.9X24", "평균 2000kcal")


### photo

def photo():
    st.title('식사를 보여주세요')
    uploaded_file = st.file_uploader("이미지파일선택",type = ["jpg","png","jpeg"])
    
    try:
      if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='선택된 이미지.', use_column_width=True)
        st.write("")
        st.write("어떤 종류의 밥일까요?")



        model2= keras.models.load_model("keras_model.h5")
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = image

            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

            #turn the image into a numpy array
        image_array = np.asarray(image)
            # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            # Load the image into the array
        data[0] = normalized_image_array

            # run the inference
        prediction = model2.predict(data)
        # st.write(prediction)

        label_ = 0
        result1 = "어떤 종류의 밥일까요?"

        label_ = np.argmax(prediction[0])


        if label_ == 0:
              result1 = "백미입니다. (130kcal / 100g)"
        if label_ == 1:
              result1 =  "현미입니다. (110.9kcal / 100g)"
        if label_ == 2:
              result1 = "흑미입니다. (330kcal / 100g)"
        if label_ == 3:
              result1 = "짜장밥입니다. (493.9kcal / 370g)"
        if label_ == 4:
              result1 = "카레밥입니다. (544kcal / 400g)"

        st.write("오늘 내가 먹은 밥은?: "+ result1)
      
    except:
        st.error('밥 사진을 다시 올려주세요.')



### video

def video():
    st.title('사진촬영')
    img_file_buffer = st.camera_input("오늘도 잊지말고 기록해주세요!")

    try:
      if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='선택된 이미지.', use_column_width=True)
        st.write("")
        st.write("어떤 종류의 밥일까요?")



        model2= keras.models.load_model("keras_model.h5")
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = image

            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

            #turn the image into a numpy array
        image_array = np.asarray(image)
            # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            # Load the image into the array
        data[0] = normalized_image_array

            # run the inference
        prediction = model2.predict(data)
        # st.write(prediction)

        label_ = 0
        result1 = "어떤 종류의 밥일까요?"

        label_ = np.argmax(prediction[0])


        if label_ == 0:
              result1 = "백미입니다. (130kcal / 100g)"
        if label_ == 1:
              result1 =  "현미입니다. (110.9kcal / 100g)"
        if label_ == 2:
              result1 = "흑미입니다. (330kcal / 100g)"
        if label_ == 3:
              result1 = "짜장밥입니다. (493.9kcal / 370g)"
        if label_ == 4:
              result1 = "카레밥입니다. (544kcal / 400g)"

        st.write("오늘 내가 먹은 밥은?: "+ result1)
      
    except:
        st.error('밥 사진을 다시 올려주세요.')


selected_box = st.sidebar.selectbox('오늘도 잊지말고 기록해주세요',('원하시는 방식을 선택해주세요','사진업로드', '사진촬영'))
    
if selected_box == '원하시는 방식을 선택해주세요':
    welcome()
    st.sidebar.write("칼로리, 대신 계산해드립니다.")
if selected_box == '사진업로드':
    photo()
    st.sidebar.write("뭐 드셨는지만 보여주세요! ")
if selected_box == '사진촬영':
    video()
    st.sidebar.write("뭐 드시는지만 알려주세요!")
