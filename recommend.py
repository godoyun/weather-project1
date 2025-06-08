def recommend_clothing(temp, wind, weather_desc, humidity, month):
    recommendation = ""

    # 계절 감안한 기준
    if temp >= 28:
        recommendation = "민소매, 반바지, 린넨 셔츠"
    elif 23 <= temp < 28:
        recommendation = "반팔, 얇은 셔츠, 면바지"
    elif 17 <= temp < 23:
        recommendation = "긴팔티, 가디건, 청바지"
    elif 10 <= temp < 17:
        recommendation = "자켓, 니트, 면바지"
    elif 4 <= temp < 10:
        recommendation = "코트, 니트, 기모 바지"
    else:
        recommendation = "패딩, 목도리, 장갑, 방한모자"

    # 비/눈 날씨일 경우
    if "비" in weather_desc or "눈" in weather_desc:
        recommendation += ", 우산"

    # 습도 높을 경우: 땀 배출 잘 되는 옷 강조
    if humidity >= 80 and temp >= 20:
        recommendation += " (통기성 좋은 옷 추천)"

    # 강풍일 경우
    if wind >= 8.0:
        recommendation += ", 바람막이"

    # 계절 보정
    if month in [12, 1, 2] and temp <= 10:
        recommendation += " (겨울철, 따뜻하게 입으세요)"
    elif month in [6, 7, 8] and temp >= 28:
        recommendation += " (한여름, 자외선 차단도 고려)"

    return recommendation