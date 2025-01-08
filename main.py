import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('\n\n')
st.write('안녕하세요. 저는 이수호입니다.')
st.write('저의 이메일 주소는 24_11012@daejin.sen.hs.kr')

import streamlit as st
import random
import urllib.parse

# 운세 리스트
fortunes = [
    "오늘은 기분 좋은 일이 생길 거예요!",
    "도전하지 않으면 기회는 오지 않습니다. 용기를 내보세요!",
    "잠시 쉬어가는 것도 중요한 하루입니다.",
    "주변 사람들에게 따뜻한 말 한마디를 건네보세요.",
    "생각지도 못한 행운이 찾아올 것입니다!",
    "약간의 어려움이 예상되지만, 이를 극복하면 큰 성과가 있을 거예요.",
    "가족과의 시간을 보내며 에너지를 충전해 보세요.",
    "모든 일이 잘 풀리는 하루가 될 것입니다!",
    "당신의 노력이 결실을 맺을 날이 가까워지고 있습니다.",
    "오늘은 평소보다 자신감이 넘치는 날이에요. 도전해보세요!"
]

# 앱 제목
st.title("📜 재미있는 운세 보기 앱")

# 이름 입력
name = st.text_input("이름을 입력하세요:", placeholder="홍길동")

# 생일 입력
birthday = st.date_input("생일을 선택하세요:")

# 버튼
if st.button("운세 보기"):
    if name:
        # 랜덤 운세 선택
        fortune = random.choice(fortunes)
        fortune_message = f"✨ {name}님의 오늘의 운세는: '{fortune}' ✨"
        st.success(fortune_message)
        
        # 공유 링크 생성
        encoded_fortune = urllib.parse.quote(fortune_message)
        
        # SNS 공유 버튼
        st.markdown("### 운세 공유하기!")
        
        # 페이스북 공유 링크
        fb_url = f"https://www.facebook.com/sharer/sharer.php?u={encoded_fortune}"
        st.markdown(f"[페이스북에 공유하기](https://www.facebook.com/sharer/sharer.php?u={encoded_fortune})")
        
        # 트위터 공유 링크
        twitter_url = f"https://twitter.com/intent/tweet?text={encoded_fortune}"
        st.markdown(f"[트위터에 공유하기](https://twitter.com/intent/tweet?text={encoded_fortune})")

        # 카카오톡 공유 링크 (카카오톡의 URL scheme을 사용하여 링크 구성)
        kakao_url = f"https://ka.kakao.com/share?url={encoded_fortune}"
        st.markdown(f"[카카오톡에 공유하기](https://ka.kakao.com/share?url={encoded_fortune})")

         # 패들렛 공유 링크 (카카오톡의 URL scheme을 사용하여 링크 구성)
        padlet_url = f"https://padlet.com/t0025/breakout-link/eXwgvw5lad6y2ybR-jA7rbnJknQJJb498={encoded_fortune}"
        st.markdown(f"[패들렛에 공유하기](https://padlet.com/t0025/breakout-link/eXwgvw5lad6y2ybR-jA7rbnJknQJJb498={encoded_fortune})")
        
    else:
        st.warning("이름을 입력해주세요!")

# 추가 요소: 오늘 날짜 표시
st.sidebar.write("😊 즐거운 하루 되세요!")

