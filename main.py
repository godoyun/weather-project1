from get_weather import get_weather, save_to_csv
from recommend import recommend_clothing
from datetime import datetime

if __name__ == "__main__":
    city = input("지역명을 입력하세요: ")
    df = get_weather(city)

    if df is not None:
        save_to_csv(df, city)

        #디버깅용 출력 추가
        print("[DEBUG] DataFrame 열 목록:", df.columns.tolist())
        print("[DEBUG] DataFrame 첫 행:\n", df.loc[0])

        # 데이터 추출
        temp = float(df.loc[0, '현재 기온'])
        wind = float(df.loc[0, '풍속'])
        desc = str(df.loc[0, '날씨 상태'])
        humidity = int(df.loc[0, '습도'])
        month = datetime.now().month

        clothes = recommend_clothing(temp, wind, desc, humidity, month)
        print(f"\n[추천 옷차림] {clothes}")
