import streamlit as st

st.set_page_config(
    page_title="Style Mentor",
    page_icon="🎩",
    layout="wide"
)

st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:3rem;
    font-weight:700;
    color:#222;
}
.sub-title{
    text-align:center;
    color:#666;
    margin-bottom:20px;
}
.card{
    padding:20px;
    border-radius:15px;
    background-color:#f7f7f7;
    border:1px solid #e5e5e5;
}
.tip{
    padding:15px;
    border-radius:10px;
    background:#eef8ff;
    border-left:5px solid #2196F3;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🎩 Style Mentor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">패션 디자이너 아저씨와 함께하는 스타일 가이드</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=600",
        use_container_width=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
        <h3>👨‍🎨 패션 디자이너 아저씨</h3>
        <p>
        안녕하세요! 저는 스타일 멘토입니다.
        사람의 가치를 외모로 평가하지 않고,
        자신에게 어울리는 패션과 자기관리를 찾도록 도와드립니다.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

category = st.selectbox(
    "관심 분야를 선택하세요",
    [
        "패션",
        "헤어스타일",
        "피부관리",
        "자신감"
    ]
)

question = st.text_area(
    "고민이나 궁금한 점을 입력하세요",
    placeholder="예: 교복에 어울리는 스타일이 궁금해요."
)

tips = {
    "패션": """
• 기본 색상 위주로 코디하면 실패가 적습니다.
• 편안함과 활동성을 우선으로 생각하세요.
• 유행보다 자신의 취향을 찾는 것이 중요합니다.
""",
    "헤어스타일": """
• 깔끔한 관리만으로도 좋은 인상을 줄 수 있습니다.
• 관리하기 쉬운 스타일을 선택하세요.
• 정기적인 손질이 중요합니다.
""",
    "피부관리": """
• 충분한 수면과 수분 섭취가 중요합니다.
• 세안은 너무 자주 하지 않는 것이 좋습니다.
• 피부 고민이 심하면 전문가 상담을 고려하세요.
""",
    "자신감": """
• 외모는 사람의 일부일 뿐 전부가 아닙니다.
• 자신의 장점을 찾고 발전시키세요.
• 비교보다 성장에 집중하는 것이 좋습니다.
"""
}

if st.button("조언 받기"):
    if not question.strip():
        st.warning("고민을 입력해주세요.")
    else:
        st.success("스타일 멘토의 조언")

        st.markdown(
            f"""
            <div class="tip">
            {tips.get(category)}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("### ✨ 추가 메시지")
        st.write(
            f"'{question}'에 대해 고민하고 있다면, "
            "자신을 다른 사람과 비교하기보다 자신에게 맞는 스타일을 찾는 데 집중해 보세요."
        )

st.divider()

st.caption(
    "Style Mentor | 교육용 자기관리 및 패션 가이드"
)
