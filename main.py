import streamlit as st
import random
import base64

# 로컬 이미지 경로 설정
image_path = "C:/Users/user/Desktop/이수호.jpeg"  # 실제 파일 경로로 변경하세요.

# 이미지 파일을 base64로 인코딩
with open(image_path, "rb") as img_file:
    b64 = base64.b64encode(img_file.read()).decode()

# CSS 스타일 설정
background_style = f"""
    <style>
    body {{
        background-color: #f0f8ff; /* 배경 색상 설정 (예: 옅은 파랑) */
        font-family: 'Arial', sans-serif;
    }}
    .stApp {{
        background: url(data:image/jpeg;base64,{b64}) no-repeat center center fixed; /* 로컬 이미지 */
        background-size: cover; /* 이미지가 화면을 덮도록 설정 */
    }}
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)

# 앱 제목
st.title("나의 첫번째 앱")
st.text('\n\n')
st.write('안녕하세요. 저는 이수호입니다.')
st.write('저의 이메일 주소는 24_11012@daejin.sen.hs.kr')

# 운세 리스트
fortunes = {
    "연애운": [
        "오늘은 상대방과 가까워질 좋은 기회가 올 것입니다.",
        "자신감을 가지고 다가가세요. 운명이 당신을 돕고 있습니다.",
        "너무 조급하게 생각하지 말고, 천천히 상대를 알아가세요.",
        "상대방의 마음을 알게 될 중요한 단서가 생길 것입니다.",
        "연애에서 새로운 시작을 맞이할 좋은 날입니다."
    ],
    "재물운": [
        "오늘은 새로운 재정적 기회가 찾아올 것입니다.",
        "상당한 이득을 볼 수 있는 기회가 오지만, 신중하게 결정하세요.",
        "과거의 노력 덕분에 재정적으로 안정될 것입니다.",
        "금전적으로 조금 더 절약하는 것이 도움이 될 것입니다.",
        "소소한 재정적 행운이 따르는 하루입니다."
    ],
    "건강운": [
        "오늘은 활력이 넘치고 에너지가 가득한 하루입니다.",
        "피로를 느낀다면 잠시 휴식을 취하는 것이 중요합니다.",
        "건강을 위해 운동을 시작하는 것이 좋은 날입니다.",
        "스트레스 해소를 위한 활동이 필요해 보입니다.",
        "건강상 작은 변화가 예상되지만, 크게 걱정할 필요는 없습니다."
    ]
}

# 운세 카테고리 선택
fortune_category = st.selectbox(
    "운세 카테고리를 선택하세요:",
    options=["연애운", "재물운", "건강운"]
)

# 버튼 클릭 시 운세 결과 출력
if st.button("운세 뽑기"):
    name = st.text_input("이름을 입력하세요:", placeholder="홍길동")
    if name:
        # 선택된 카테고리에 맞는 운세 뽑기
        selected_fortunes = fortunes[fortune_category]
        fortune = random.choice(selected_fortunes)
        fortune_message = f"✨ {name}님의 {fortune_category}은: '{fortune}' ✨"
        st.success(fortune_message)

        st.markdown("### 운세 Padlet에 공유하기!")
        st.markdown(f"Padlet에 운세를 공유하려면 아래 링크를 클릭하고, 메시지를 추가하세요!")
        
        # 공유 링크 제공
        padlet_url = "https://padlet.com/t0025/breakout-link/eXwgvw5lad6y2ybR-jA7rbnJknQJJb498"
        st.markdown(f"[Padlet에 운세 공유하기]({padlet_url})")

  
