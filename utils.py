def get_korean_city_name(english_name):
    mapping = {
        # 🇰🇷 대한민국 (행정명칭 기준)
        "Seoul": "서울특별시",
        "Busan": "부산광역시",
        "Incheon": "인천광역시",
        "Daegu": "대구광역시",
        "Daejeon": "대전광역시",
        "Gwangju": "광주광역시",
        "Ulsan": "울산광역시",
        "Sejong": "세종특별자치시",

        "Suwon": "수원시",
        "Goyang": "고양시",
        "Yongin": "용인시",
        "Seongnam": "성남시",
        "Cheongju": "청주시",
        "Jeonju": "전주시",
        "Cheonan": "천안시",
        "Changwon": "창원시",
        "Gimhae": "김해시",
        "Pohang": "포항시",
        "Jeju": "제주시",
        "Gangneung": "강릉시",
        "Andong": "안동시",
        "Chuncheon": "춘천시",
        "Wonju": "원주시",
        "Mokpo": "목포시",
        "Gunsan": "군산시",
        "Geoje": "거제시",
        "Namyangju": "남양주시",
        "Pyeongtaek": "평택시",
        "Hwaseong": "화성시",
        "Uijeongbu": "의정부시",
        "Gimpo": "김포시",

        # 🇯🇵 일본
        "Tokyo": "도쿄",
        "Osaka": "오사카",
        "Kyoto": "교토",
        "Nagoya": "나고야",
        "Fukuoka": "후쿠오카",
        "Sapporo": "삿포로",

        # 🇺🇸 미국
        "New York": "뉴욕",
        "Los Angeles": "로스앤젤레스",
        "Chicago": "시카고",
        "San Francisco": "샌프란시스코",
        "Seattle": "시애틀",
        "Boston": "보스턴",
        "Houston": "휴스턴",
        "Atlanta": "애틀랜타",

        # 🇬🇧 유럽/기타
        "London": "런던",
        "Paris": "파리",
        "Berlin": "베를린",
        "Rome": "로마",
        "Madrid": "마드리드",
        "Amsterdam": "암스테르담",
        "Vienna": "빈",
        "Bangkok": "방콕",
        "Singapore": "싱가포르",
        "Sydney": "시드니",
        "Toronto": "토론토",
        "Vancouver": "밴쿠버",
        "Istanbul": "이스탄불"
    }

    return mapping.get(english_name.strip(), english_name)