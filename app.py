import streamlit as st
from google import genai

# -----------------------------
# 기본 설정
# -----------------------------

st.set_page_config(
    page_title="Style Mentor AI",
    page_icon="🎩",
    layout="wide"
)


# -----------------------------
# 디자인
# -----------------------------

st.markdown(
    """
<style>

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#666;
}

.box {
    background:#f5f5f5;
    padding:20px;
    border-radius:15px;
}

</style>
""",
    unsafe_allow_html=True
)


st.markdown(
    "<div class='title'>🎩 Style Mentor AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>콧수염 패션 디자이너 AI 아저씨의 스타일 상담</div>",
    unsafe_allow_html=True
)


# -----------------------------
# 캐릭터
# -----------------------------

col1, col2 = st.columns(2)


with col1:

    st.image(
        "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
        width=300
    )


with col2:

    st.markdown(
        """
<div class="box">

👨‍🎨 안녕하세요!

저는 Style Mentor AI입니다.

외모를 평가하지 않고,
나에게 어울리는 패션,
헤어스타일,
생활 습관을 함께 찾아드립니다.

</div>
""",
        unsafe_allow_html=True
    )



st.divider()



# -----------------------------
# Gemini 연결
# -----------------------------

def ask_ai(message):

    try:

        api_key = st.secrets["GEMINI_API_KEY"]

        client = genai.Client(
            api_key=api_key
        )


        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
너는 친절한 패션 디자이너 아저씨 AI이다.

대상:
사춘기 청소년

역할:
- 패션
- 헤어스타일
- 자기관리
- 자신감 향상

에 대해 조언한다.

주의:
외모 평가 금지.
외모 점수 금지.
비교 금지.

사용자 고민:
{message}

따뜻하고 구체적으로 답변해줘.
"""
        )


        return response.text


    except Exception as e:

        return (
            "AI 연결 중 문제가 발생했습니다.\n\n"
            "잠시 후 다시 시도해주세요.\n\n"
            f"오류 정보: {str(e)}"
        )



# -----------------------------
# 사용자 입력
# -----------------------------


category = st.selectbox(
    "상담 분야",
    [
        "패션",
        "헤어스타일",
        "피부관리",
        "자신감",
        "전체 상담"
    ]
)


question = st.text_area(
    "고민을 입력하세요",
    placeholder="예: 친구들에게 잘 어울리는 옷 스타일이 궁금해요."
)



if st.button("🎩 AI 디자이너에게 조언 받기"):


    if question.strip() == "":

        st.warning(
            "고민 내용을 입력해주세요."
        )


    else:

        final_question = (
            f"분야: {category}\n"
            f"고민: {question}"
        )


        with st.spinner(
            "AI 디자이너가 생각 중입니다..."
        ):

            answer = ask_ai(final_question)



        st.success(
            "🎩 디자이너 아저씨의 답변"
        )


        st.markdown(answer)



st.divider()


st.caption(
    "Style Mentor AI | 긍정적인 자기관리와 스타일 조언 서비스"
)
