import streamlit as st

try:
    from google import genai
except:
    genai = None

# ------------------------
# 페이지 설정
# ------------------------

st.set_page_config(
    page_title="마음 성장 연구소",
    page_icon="🌱",
    layout="centered"
)

# ------------------------
# Gemini 함수
# ------------------------

def ask_gemini(user_input):

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

        client = genai.Client(api_key=api_key)

        prompt = f"""
당신은 학생들의 자기존중감 향상을 돕는 상담사입니다.

규칙
- 외모를 평가하지 말 것
- 외모 비교를 부추기지 말 것
- 공감 중심으로 답변
- 학생 눈높이에 맞게 답변
- 300자 이내

학생 고민:
{user_input}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI 응답 생성 중 오류가 발생했습니다.\n\n{e}"

# ------------------------
# 제목
# ------------------------

st.title("🌱 마음 성장 연구소")

st.markdown("""
### 외모보다 더 소중한 나를 발견하는 공간

누구나 외모 때문에 고민할 수 있습니다.

하지만 사람의 가치는 외모 하나로 결정되지 않습니다.

오늘은 나의 장점과 가능성을 함께 찾아보세요.
""")

st.divider()

# ------------------------
# 자기 발견
# ------------------------

st.header("💡 나의 장점 발견하기")

good1 = st.text_input("내가 잘하는 것")
good2 = st.text_input("친구들이 좋아하는 나의 모습")
good3 = st.text_input("최근 칭찬받은 일")

if st.button("장점 정리하기"):

    strengths = [x for x in [good1, good2, good3] if x.strip()]

    if strengths:

        st.success("당신의 강점 카드")

        for item in strengths:
            st.write(f"✅ {item}")

        st.info(
            "이 장점들은 외모와 상관없이 당신을 특별하게 만드는 소중한 가치입니다."
        )

    else:
        st.warning("한 가지 이상 입력해주세요.")

st.divider()

# ------------------------
# 가치 지도
# ------------------------

st.header("🌟 나의 가치 지도")

kindness = st.slider("친절함", 0, 10, 5)
effort = st.slider("노력", 0, 10, 5)
humor = st.slider("유머감각", 0, 10, 5)
creativity = st.slider("창의성", 0, 10, 5)
responsibility = st.slider("책임감", 0, 10, 5)

avg = (
    kindness +
    effort +
    humor +
    creativity +
    responsibility
) / 5

st.progress(avg / 10)

st.caption(
    "외모 외에도 다양한 가치가 당신을 구성하고 있습니다."
)

st.divider()

# ------------------------
# 마음 상태 체크
# ------------------------

st.header("📈 오늘의 마음 체크")

confidence = st.slider("오늘의 자신감", 0, 10, 5)
happiness = st.slider("오늘의 행복감", 0, 10, 5)
satisfaction = st.slider("오늘의 만족감", 0, 10, 5)

mind_score = round(
    (confidence + happiness + satisfaction) / 3,
    1
)

st.metric(
    "오늘의 마음 점수",
    f"{mind_score}/10"
)

st.divider()

# ------------------------
# AI 고민 상담
# ------------------------

st.header("🧑‍🏫 상담사 아저씨와 이야기하기")

st.image(
    "counselor.png",
    width=200,
    caption="마음 성장 연구소 상담사"
)

st.info(
    """
안녕!

나는 마음 성장 연구소의 상담사야 😊

외모 때문에 속상하거나 고민되는 일이 있으면
편하게 이야기해 줘.

함께 생각해 보자!
"""
)

user_worry = st.text_area(
    "고민을 적어보세요."
)

if st.button("상담 받기"):

    if not user_worry.strip():
        st.warning("고민을 입력해주세요.")

    else:
        with st.spinner("상담사 아저씨가 생각 중입니다..."):

            answer = ask_gemini(user_worry)

        st.chat_message("assistant").write(answer)

# ------------------------
# 응원 편지
# ------------------------

st.header("💌 나를 위한 응원 편지")

nickname = st.text_input("이름 또는 별명")

if st.button("응원 편지 받기"):

    if nickname.strip():

        st.info(
            f"""
{nickname}님,

당신은 외모만으로 설명될 수 없는 소중한 사람입니다.

조금 부족하게 느껴지는 날이 있더라도
그것이 당신의 가치를 결정하지는 않습니다.

당신의 친절함, 노력, 성실함,
그리고 성장하려는 마음이
당신을 더욱 빛나게 만듭니다.

오늘도 스스로를 응원해주세요. 🌱
"""
        )

    else:
        st.warning("이름 또는 별명을 입력해주세요.")

st.divider()

st.caption("🌱 마음 성장 연구소")
