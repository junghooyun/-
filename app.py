import google.generativeai as genai
from google.gemini import types

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="Native English Chatbot",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Native English Conversation Bot")
st.caption("Practice English conversation with Gemini")

# -----------------------------
# API KEY 불러오기
# -----------------------------
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("❌ GEMINI_API_KEY 가 secrets.toml에 설정되지 않았습니다.")
    st.stop()

# -----------------------------
# Gemini Client 생성
# -----------------------------
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"❌ Gemini 클라이언트 생성 오류: {e}")
    st.stop()

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 이전 채팅 출력
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# 사용자 입력
# -----------------------------
user_input = st.chat_input("영어로 자유롭게 대화해보세요!")

# -----------------------------
# 챗봇 동작
# -----------------------------
if user_input:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(user_input)

    # 시스템 프롬프트
    system_prompt = """
    You are a friendly native English conversation partner.

    Rules:
    - Talk naturally like a native speaker.
    - Help the user practice English conversation.
    - Keep responses concise and conversational.
    - Correct awkward English gently.
    - Ask follow-up questions to continue the conversation.
    """

    # Gemini용 history 변환
    history = []

    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"

        history.append(
            types.Content(
                role=role,
                parts=[types.Part(text=msg["content"])]
            )
        )

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=[
                        types.Content(
                            role="user",
                            parts=[types.Part(text=system_prompt)]
                        ),
                        *history
                    ]
                )

                bot_reply = response.text

                st.markdown(bot_reply)

        # 응답 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

    except Exception as e:
        error_message = f"❌ 오류가 발생했습니다: {e}"

        with st.chat_message("assistant"):
            st.error(error_message)

        st.session_state.messages.append({
            "role": "assistant",
            "content": error_message
        })
