import streamlit as st
from get_weather import get_weather
from recommend import recommend_clothing
from PIL import Image
from datetime import datetime
from utils import get_korean_city_name

st.set_page_config(page_title="날씨 옷차림 추천", page_icon="☁️")
st.title("☁️ 날씨 기반 옷차림 추천 시스템")

# 사용자 입력
city = st.text_input("지역명을 입력하세요:")

# 입력이 있을 경우
if city:
    df = get_weather(city)

    if df is not None:
        # 입력 시각 저장
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 한글 도시명 변환
        eng_name = df.loc[0, '지역명']
        kor_name = get_korean_city_name(eng_name)

        temp = float(df.loc[0, '현재 기온'])
        feels_like = float(df.loc[0, '체감 온도'])
        humidity = int(df.loc[0, '습도'])
        wind = float(df.loc[0, '풍속'])
        desc = df.loc[0, '날씨 상태']

        # 💡 날씨 정보 카드 박스
        st.markdown(f"""<div style='background-color:#f0f8ff;padding:20px;border-radius:12px'><h2>📍 {kor_name}</h2><p><b>⛅ 날씨 상태 : </b> {desc}</p><p><b>🕒 조회 시각 : </b> {now}</p><div style='display:flex;flex-wrap:wrap;gap:10px;margin-top:15px'><div style='flex:1;min-width:120px;background-color:#ffffff;border-radius:8px;padding:10px;display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font-size:28px'>🌡️</div><div style='font-size:16px;font-weight:bold;margin-top:4px'>현재 기온</div><p style='font-size:20px;margin-top:8px'><b>{temp}℃</b></p></div><div style='flex:1;min-width:120px;background-color:#ffffff;border-radius:8px;padding:10px;display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font-size:28px'>🤒</div><div style='font-size:16px;font-weight:bold;margin-top:4px'>체감 기온</div><p style='font-size:20px;margin-top:8px'><b>{feels_like}℃</b></p></div><div style='flex:1;min-width:120px;background-color:#ffffff;border-radius:8px;padding:10px;display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font-size:28px'>💧</div><div style='font-size:16px;font-weight:bold;margin-top:4px'>습도</div><p style='font-size:20px;margin-top:8px'><b>{humidity}%</b></p></div><div style='flex:1;min-width:120px;background-color:#ffffff;border-radius:8px;padding:10px;display:flex;flex-direction:column;align-items:center;justify-content:center'><div style='font-size:28px'>🍃</div><div style='font-size:16px;font-weight:bold;margin-top:4px'>풍속</div><p style='font-size:20px;margin-top:8px'><b>{wind} m/s</b></p></div></div></div>""", unsafe_allow_html=True)

        # 여백 추가
        st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)

        # ✅ 우산 알림
        if "비" in desc or "소나기" in desc or "눈" in desc or humidity >= 90:
            st.warning("☔ 오늘은 우산을 챙기는 게 좋겠어요!")
        else:
            st.info("🌤️ 오늘은 우산 걱정 없이 가볍게 나가도 괜찮아요!")

        # 💡 추천 옷차림 카드 박스
        temp = float(df.loc[0, '현재 기온'])
        wind = float(df.loc[0, '풍속'])
        desc = str(df.loc[0, '날씨 상태'])
        humidity = int(df.loc[0, '습도'])
        month = datetime.now().month

        recommendation = recommend_clothing(temp, wind, desc, humidity, month)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="background-color:#fff3cd;padding:20px;border-radius:10px">
                <h3>👕 추천 옷차림</h3>
                <p style="font-size:18px">✅ <b>{recommendation}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 💡 이미지 섹션
        st.markdown("<br><h4>🖼️ 추천 옷차림 이미지 보기</h4>", unsafe_allow_html=True)
        for item in recommendation.split(","):
            key = item.strip()
            img_path = f"images/{key}.png"
            try:
                img = Image.open(img_path)
                st.image(img, caption=key, width=150)
            except:
                st.warning(f"'{key}' 이미지가 없습니다.")
    else:
        st.error("❌ 날씨 정보를 불러오지 못했습니다.")
