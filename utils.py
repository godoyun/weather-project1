def get_korean_city_name(english_name):
    cleaned = english_name.strip().lower()
    cleaned = cleaned.replace("-si", "").replace("-gun", "").replace("-eup", "").replace("-myeon", "").replace("-city", "")

    mapping = {
        # 🇰🇷 대한민국 - 특별시/광역시/특별자치시
        "seoul": "서울특별시",
        "busan": "부산광역시",
        "incheon": "인천광역시",
        "daegu": "대구광역시",
        "daejeon": "대전광역시",
        "gwangju": "광주광역시",
        "ulsan": "울산광역시",
        # 세종은 특별자치시말고 세종시로
        "sejong": "세종특별자치시",

        # 제주 안됨
        "jeju": "제주특별자치도",
        "seogwipo": "서귀포시",

        # 주요 도 단위 시
        "suwon": "수원시",
        "goyang": "고양시",
        "yongin": "용인시",
        "seongnam": "성남시",
        "cheongju": "청주시",
        "jeonju": "전주시",
        "cheonan": "천안시",
        "changwon": "창원시",
        "gimhae": "김해시",
        "pohang": "포항시",
        "gangneung": "강릉시",
        "andong": "안동시",
        "chuncheon": "춘천시",
        "wonju": "원주시",
        "mokpo": "목포시",
        "gunsan": "군산시",
        "geoje": "거제시",
        "namyangju": "남양주시",
        "pyeongtaek": "평택시",
        "hwaseong": "화성시",
        "uijeongbu": "의정부시",
        "gimpo": "김포시",
        "anyang": "안양시",
        "ansan": "안산시",
        "gunpo": "군포시",
        "jecheon": "제천시",
        "gumi": "구미시",
        "yeosu": "여수시",
        "suncheon": "순천시",
        "sokcho": "속초시",

        # 군 단위 (대표 지역만)
        "gapyeong": "가평군",
        "yangyang": "양양군",
        "yeoncheon": "연천군",
        "goesan": "괴산군",
        "jinan": "진안군",
        "cheorwon": "철원군",
        "jeongseon": "정선군",
        "boseong": "보성군",
        "goryeong": "고령군",

        # 읍/면 단위 (실사용 예시 중심)
        "iljuk": "일죽면",
        "ando": "안도면",

        # 🇯🇵 일본
        "tokyo": "도쿄",
        "osaka": "오사카",
        "kyoto": "교토",
        "nagoya": "나고야",
        "fukuoka": "후쿠오카",
        "sapporo": "삿포로",

        # 🇺🇸 미국
        "new york": "뉴욕",
        "los angeles": "로스앤젤레스",
        "chicago": "시카고",
        "san francisco": "샌프란시스코",
        "seattle": "시애틀",
        "boston": "보스턴",
        "houston": "휴스턴",
        "atlanta": "애틀랜타",

        # 🇪🇺 유럽/기타
        "london": "런던",
        "paris": "파리",
        "berlin": "베를린",
        "rome": "로마",
        "madrid": "마드리드",
        "amsterdam": "암스테르담",
        "vienna": "빈",
        "bangkok": "방콕",
        "singapore": "싱가포르",
        "sydney": "시드니",
        "toronto": "토론토",
        "vancouver": "밴쿠버",
        "istanbul": "이스탄불"
    }

    return mapping.get(cleaned, english_name)