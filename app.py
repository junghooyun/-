import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💌"
)

st.title("💌 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# API KEY 불러오기
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)

except Exception:
    st.error("❌ secrets.toml 에 GEMINI_API_KEY를 설정해주세요.")
    st.stop()

# 모델 생성
try:
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

except Exception as e:
    st.error(f"❌ 모델 생성 실패: {str(e)}")
    st.stop()

# 시스템 프롬프트
SYSTEM_PROMPT = """
너는 따뜻하고 공감 능력이 뛰어난 연애상담 챗봇이다.

규칙:
- 사용자의 감정을 존중한다.
- 현실적이고 균형 잡힌 조언을 제공한다.
- 공격적이거나 단정짓지 않는다.
- 친근한 한국어로 답변한다.
"""

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 채팅 출력
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 입력창
user_input = st.chat_input("고민을 이야기해보세요...")

if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI 응답
    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        try:
            # 대화 기록 구성
            chat_history = SYSTEM_PROMPT + "\n\n"

            for msg in st.session_state.messages:
                role = "사용자" if msg["role"] == "user" else "상담사"
                chat_history += f"{role}: {msg['content']}\n"

            # Gemini 응답 생성
            response = model.generate_content(chat_history)

            assistant_reply = response.text

            # 출력
            message_placeholder.markdown(assistant_reply)

            # 기록 저장
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_reply
            })

        except Exception as e:

            error_message = (
                "❌ 오류가 발생했습니다.\n\n"
                f"에러 내용:\n{str(e)}"
            )

            message_placeholder.error(error_message)
