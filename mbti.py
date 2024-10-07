import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Custom MBTI Test", layout="centered")

# 타이틀
st.title("Custom MBTI Personality Test")

# 설명
st.write("""
이 테스트는 당신의 성향을 4가지 유형(W/D, H/L, C/B, M/F)으로 나누어 분석합니다.
각 질문에 대해 당신이 얼마나 동의하는지 선택해 주세요.
""")

# 질문 및 성향 설정
questions = [
    {"text": "나는 대화의 재미보다 그 내용의 도덕적 수위를 훨씬 중요시한다.", "category": "W", "reverse": False},
    {"text": "뚱뚱한 사람을 보면, 그에 걸맞는 별명을 지어주고 싶다.", "category": "D", "reverse": False},
    {"text": "지극히 사소한 잘못을 걸려 불이익을 받았을 때에도, 나는 ‘걸리지만 않았어도’ 라고 아쉬워하기보다는 잘못을 한 것에 대해 반성한다.", "category": "W",
     "reverse": False},
    {"text": "최근 디시인사이드를 일주일에 3일 이상 의도적으로 접속한 적이 있다.", "category": "D", "reverse": False},
    {"text": "지금 당장 내 핸드폰의 모든 SNS 단체대화방 채팅 내역이 교내에 공개되어도, 보고 속으로 나를 이전보다 꺼려할 사람은 솔직히 크게 없다.", "category": "W",
     "reverse": False},
    {"text": "영원히 뒷담화를 하지 않고 살기는 아마 불가능할 것이라고 생각한다.", "category": "D", "reverse": False},
    {"text": "내가 지금 무언가를 하든 하지 않든 미래는 어떻게든 흘러갈 것이며, 나의 행동으로 인한 결과의 차이가 설령 생긴다 하더라도 괜찮다.", "category": "L",
     "reverse": False},
    {"text": "장기적이고 발전적인 계획을 달성하기 위해 자신의 충동을 억제하는 일에 주로 성공하는 편이다.", "category": "H", "reverse": False},
    {"text": "어떠한 일이 멀리 볼 때 나에게 필요하거나 도움이 되더라도, 내면의 흥미와 열정을 불러일으키지 않는다면 그 일에 길게 몰입하기 힘들다.", "category": "L",
     "reverse": False},
    {"text": "최근 생활에 있어, 솔직하게 할 수 있는 것 안에서는 대체로 최선을 다해왔다고 생각한다.", "category": "H", "reverse": False},
    {"text": "나에게 주어진 시간은 당연히 순간마다 내 마음이 가장 하고 싶은 일을 하는데 사용하기 위해 존재한다.", "category": "L", "reverse": False},
    {"text": "만약 임의의 같은 학년 학생이 자신과 완전히 동일한 상황에 놓였었더라도, 시기마다 주어지는 일에 자신보다 더욱 많이 노력했을 가능성은 아무래도 낮을 것이다.", "category": "H",
     "reverse": False},
    {"text": "남들이 통상적인 수준에서 생각지도 못한 말이나 행동으로 종종 웃음을 주곤 한다.", "category": "C", "reverse": False},
    {"text": "사회에는 어느 정도 정해진 원리나 규칙이 있으며, 나나 내 주변에서 그 반례가 나오기 쉽지 않을 것이라 생각한다.", "category": "B", "reverse": False},
    {"text": "실현 불가능해 보이는 일이 가능해 보일 때나 이를 가능하게 만들 때 재미를 느낀다.", "category": "C", "reverse": False},
    {"text": "사람은 사회적으로 위험천만한 일 없이 물처럼 흘러가듯 사는 게 가장 좋은 것이다.", "category": "B", "reverse": False},
    {"text": "나는 내가 일반적인 것에 벗어나 독특하고 기묘한 관점을 떠올리고 제기하는 사람이길 바란다.", "category": "C", "reverse": False},
    {"text": "뇌를 거치지 않고 즉각적으로 나오는 언행이 거의 없다.", "category": "B", "reverse": False},
    {"text": "타의에 의한 동성 간 스킨십이 잦은 편이며 거부감이 적다.", "category": "F", "reverse": False},
    {"text": "내가 보기에 사소한 일에 상대가 기분이 상했음을 표출하는 모습을 보면 ‘그럴 수도 있겠다’는 이해보다는 짜증이 앞선다.", "category": "M", "reverse": False},
    {"text": "같이 대화나 활동을 할 때 그 사람의 성별은 크게 고려 대상이 되지 않는다고 생각한다.", "category": "F", "reverse": False},
    {"text": "마음에 들지 않는 일은 인간관계를 불편하게 만들 가능성이 있을지언정, 마음에 담아두기보다는 해결하고 넘어가야 한다.", "category": "M", "reverse": False},
    {"text": "단호하거나 강압적이어야 할 때 그렇지 못했던 적이 종종 있다.", "category": "F", "reverse": False},
    {"text": "내 인생은 기본적으로 나 홀로 나아가는 것이지, 곁에 기대거나 의지할 사람은 크게 필요하거나 중요한 것은 아니다.", "category": "M", "reverse": False}
]

# 점수 선택지
choices = ['매우 아니다', '아니다', '보통이다', '그렇다', '매우 그렇다']
scores = [0, 2, 5, 7, 10]

# 성향별 점수 초기화
totals = {"W": 0, "D": 0, "H": 0, "L": 0, "C": 0, "B": 0, "M": 0, "F": 0}

# 질문 응답 받기
for q in questions:
    answer = st.radio(q["text"], choices, index=2)  # 기본값: 보통이다
    score = scores[choices.index(answer)]

    # 역순 처리
    if q["reverse"]:
        score = 10 - score

    # 해당 성향의 점수 합산
    totals[q["category"]] += score

# 결과 계산
if st.button("결과 보기"):
    result = ""
    result += "W" if totals["W"] > totals["D"] else "D"
    result += "H" if totals["H"] > totals["L"] else "L"
    result += "C" if totals["C"] > totals["B"] else "B"
    result += "M" if totals["M"] > totals["F"] else "F"

    st.subheader(f"당신의 성향은: {result}")
    st.write(f"총 점수: {totals}")