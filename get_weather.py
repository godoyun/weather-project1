import requests
import pandas as pd
from datetime import datetime


API_KEY = '1709f085c6bdcd327ebde8ea73e05452'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric', 
        'lang': 'kr'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"[ 에러] 지역 '{city}' 검색 실패: {data.get('message')}")
            return None

    
        weather_info = {
            '지역명': data['name'],
            '현재 기온': data['main']['temp'],
            '체감 온도': data['main']['feels_like'],
            '습도': data['main']['humidity'],
            '풍속': data['wind']['speed'],
            '날씨 상태': data['weather'][0]['description'],
            '요청 시각': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            '위도': data['coord']['lat'],
            '경도': data['coord']['lon']
        }

        return pd.DataFrame([weather_info])

    except Exception as e:
        print("[예외 발생]", e)
        return None

def save_to_csv(df, city):
    filename = f"{city}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"[저장 완료] {filename}")

if __name__ == "__main__":
    print(f"현재 API 키: {API_KEY}")
    city = input("지역명을 입력하세요: ")
    df = get_weather(city)
    if df is not None:
        save_to_csv(df, city)