# 예측 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

# 2.모델 설명
st.title('유튜브 성과 예측 프로그램')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/positivealexey/youtube-channel-performance-analytics')
st.write(' - 훈련    데이터 : 255건')
st.write(' - 테스트 데이터 : 110건')
st.write(' - 인공지능 모델 정확도 : -0.02')

# 3.데이터 시각화
col1, col2, col3 = st.columns(3)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화3')
      st.image('시각화3.png')   # 이미지 불러오기

# 4.모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력해주세요. 인공지능이 당신의 유튜브 채널의 성과를 예측해드립니다! (음숫값은 입력하지 말아주세요!)')

a = st.number_input(' 구독자 수가 몇 명인가요? ', value=0)      #초기값은 0
b = st.number_input(' 영상의 조회수를 입력해주세요. ', value=0)     # 초기값은 0
c= st.number_input(' 영상의 시청 시간을 입력해주세요. ', value=0.0 )     # 초기값은 0.0


if st.button(' 성과예측(USD)'):            # 사용자가 '성과예측' 버튼을 누르면
        input_data = [[a,b,c]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write('인공지능의 예측 성과는', p)

