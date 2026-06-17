import streamlit as st

st.set_page_config(
    page_title="Style Mentor",
    page_icon="🎩",
    layout="wide"
)

# -------------------
# 스타일
# -------------------
st.markdown("""
<style>
.main-title {
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:#222;
}
.subtitle {
    text-align:center;
    font-size:1.2rem;
    color:#666;
}
.tip-box {
    background:#f5f7fa;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #4CAF50;
}
</style>
""", unsafe_allow_html=True)

# -------------------
# 헤더
# -------------------
st.markdown('<div class="main-title">🎩 Style Mentor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">패션 디자이너 아저씨가 알려주는 스타일 가이드</div>',
    unsafe_allow_html=True
)

# -------------------
# 캐릭터
# -------------------
st.markdown("## 👨‍🎨 패션 디자이너 아저씨")

st.markdown("""
```text
      _________
     /         \\
    |  ◉   ◉   |
    |     ^    |
    |   \\___/  |
     \\  ===== /
      \\_____/ 
        |||
     ___|||___
    | Fashion |
    | Designer|
