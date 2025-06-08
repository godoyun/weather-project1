import streamlit as st
from get_weather import get_weather
from recommend import recommend_clothing
from PIL import Image
from datetime import datetime

st.title("👕 날씨 기반 옷차림 추천 시스템")

# 사용자 입력
city = st.text_input("지역명을 입력하세요:")

# 입력이 있을 경우
if city:
    df = get_weather(city)

    if df is not None:
        # 입력 시각 저장
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        st.subheader(f"🌍 지역: {df.loc[0, '지역명']}")
        st.write(f"🌡️ 현재 기온: {df.loc[0, '현재 기온']}℃")
        st.write(f"🤒 체감 온도: {df.loc[0, '체감 온도']}℃")
        st.write(f"💧 습도: {df.loc[0, '습도']}%")
        st.write(f"🍃 풍속: {df.loc[0, '풍속']} m/s")
        st.write(f"⛅ 날씨 상태: {df.loc[0, '날씨 상태']}")
        st.write(f"🕒 입력 시각: {now}")

        # 추천 옷차림
        temp = float(df.loc[0, '현재 기온'])
        wind = float(df.loc[0, '풍속'])
        desc = str(df.loc[0, '날씨 상태'])
        humidity = int(df.loc[0, '습도'])
        month = datetime.now().month

        recommendation = recommend_clothing(temp, wind, desc, humidity, month)

        st.subheader("👗 추천 옷차림")
        st.markdown(f"✅ {recommendation}")

        # (선택) 이미지 출력
        st.subheader("🖼️ 이미지로 보기")
        try:
            for item in recommendation.replace(",", "").split():
                img_path = f"images/{item.strip()}.png"
                img = Image.open(img_path)
                st.image(img, caption=item.strip(), width=150)
        except:
            st.warning("일부 이미지가 없습니다.")
    else:
        st.error("날씨 정보를 불러오지 못했습니다.")

