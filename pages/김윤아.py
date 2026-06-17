import streamlit as st

st.set_page_config(
    page_title="Color Me Better",
    page_icon="🌈",
    layout="centered"
)

st.title("🌈 Color Me Better")
st.subheader("나에게 가장 잘 어울리는 색을 찾아보자!")

st.markdown("""
이 앱은 퍼스널컬러를 간단하게 진단하여
자신에게 어울리는 색조와 스타일을 추천해줍니다.

💡 외모는 '좋고 나쁨'이 아니라 '어울림의 차이'입니다.
""")

st.divider()

# 입력 받기
skin = st.selectbox(
    "피부톤을 선택하세요",
    [
        "밝고 핑크빛",
        "밝고 노란빛",
        "중간톤",
        "어두운톤"
    ]
)

hair = st.selectbox(
    "머리카락 색을 선택하세요",
    [
        "밝은 갈색",
        "중간 갈색",
        "짙은 갈색",
        "검정색"
    ]
)

eyes = st.selectbox(
    "눈동자 색을 선택하세요",
    [
        "밝은 갈색",
        "갈색",
        "진한 갈색",
        "검정색"
    ]
)

def get_personal_color(skin, hair, eyes):
    # 매우 단순하고 안정적인 규칙 기반 진단

    if skin == "밝고 핑크빛":
        return "봄 웜톤"

    if skin == "밝고 노란빛":
        return "가을 웜톤"

    if skin == "중간톤":
        if hair in ["짙은 갈색", "검정색"]:
            return "겨울 쿨톤"
        return "여름 쿨톤"

    if skin == "어두운톤":
        return "가을 웜톤"

    return "여름 쿨톤"


if st.button("퍼스널컬러 진단하기"):
    try:
        result = get_personal_color(skin, hair, eyes)

        st.success(f"당신의 추천 퍼스널컬러는 👉 {result}")

        if result == "봄 웜톤":
            colors = [
                ("코랄", "#FF7F50"),
                ("피치", "#FFDAB9"),
                ("옐로우", "#FFD700")
            ]

            makeup = """
- 립: 코랄, 피치
- 블러셔: 살구빛
- 아이섀도우: 골드 브라운
"""

            fashion = """
- 밝고 화사한 색상을 활용하세요.
- 크림색, 아이보리 계열이 잘 어울립니다.
"""

            avoid = "회색, 차가운 블루"

        elif result == "여름 쿨톤":
            colors = [
                ("라벤더", "#E6E6FA"),
                ("로즈핑크", "#FFB6C1"),
                ("스카이블루", "#87CEEB")
            ]

            makeup = """
- 립: 로즈핑크
- 블러셔: 소프트 핑크
- 아이섀도우: 모브 계열
"""

            fashion = """
- 부드럽고 은은한 색상을 활용하세요.
- 파스텔 계열이 잘 어울립니다.
"""

            avoid = "강한 오렌지"

        elif result == "가을 웜톤":
            colors = [
                ("카멜", "#C19A6B"),
                ("올리브", "#808000"),
                ("브라운", "#8B4513")
            ]

            makeup = """
- 립: 브릭 레드
- 블러셔: 베이지 코랄
- 아이섀도우: 브라운 계열
"""

            fashion = """
- 차분하고 깊은 색상이 잘 어울립니다.
- 베이지, 카키, 브라운을 추천합니다.
"""

            avoid = "형광색"

        else:
            colors = [
                ("버건디", "#800020"),
                ("네이비", "#000080"),
                ("블랙", "#000000")
            ]

            makeup = """
- 립: 체리 레드
- 블러셔: 플럼 계열
- 아이섀도우: 쿨 브라운
"""

            fashion = """
- 대비감 있는 색상이 잘 어울립니다.
- 블랙과 화이트 조합을 추천합니다.
"""

            avoid = "탁한 베이지"

        st.subheader("🎨 추천 색상")

        cols = st.columns(len(colors))

        for col, (name, color) in zip(cols, colors):
            with col:
                st.markdown(
                    f"""
                    <div style="
                    background-color:{color};
                    height:80px;
                    border-radius:10px;">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.caption(name)

        st.subheader("💄 색조 사용법")
        st.markdown(makeup)

        st.subheader("👕 패션 추천")
        st.markdown(fashion)

        st.subheader("⚠️ 피하면 좋은 색상")
        st.info(avoid)

        st.subheader("🌟 자신감 메시지")

        st.success(
            """
당신의 매력은 특정 외모 기준이 아니라
자신에게 어울리는 스타일을 찾는 과정에서 더욱 빛납니다.

퍼스널컬러는 자신을 바꾸는 것이 아니라
자신의 장점을 발견하는 도구입니다.
"""
        )

    except Exception as e:
        st.error("진단 중 오류가 발생했습니다.")
