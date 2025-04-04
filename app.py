from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage,AIMessage
import os

def llm(messages,question):
    # ここにAIの処理を実装します
    # 例: OpenAI APIを使用して応答を生成する
    
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0,streaming=True)

    messages.append(HumanMessage(content=question))

    result = llm(messages)

    return result.content

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

messages = []

st.title("OpenAIとStreamlitをつかったアプリ")

st.write("##### 動作モード1: アニメ専門家によるAI解答")
st.write("アニメを選択することで、アニメに関する質問をAIが解答します。")
st.write("##### 動作モード2: 消防専門家によるAI解答")
st.write("消防を選択することで、消防に関する質問をAIが解答します。")

selected_item = st.radio(
    "専門AIを選んでください",
    ["アニメ", "消防"]
)

if selected_item == "アニメ":
    st.write("アニメ専門家によるAI解答")
    st.write("アニメに関する質問をしてください。")
    question = st.text_input("質問を入力してください")
    if st.button("質問する"):
        if question:
            st.write(f"質問: {question}")
            # AIの回答をここに表示
            messages.append(SystemMessage(content="あなたはアニメの専門家です。質問に対して関西弁で答えてください"))
            response = llm(messages, question)
            st.write(f"AIの回答: {response}")
        else:
            st.warning("質問を入力してください。")
elif selected_item == "消防":
    st.write("消防専門家によるAI解答")
    st.write("消防に関する質問をしてください。")
    question = st.text_input("質問を入力してください")
    if st.button("質問する"):
        if question:
            st.write(f"質問: {question}")
            # AIの回答をここに表示
            messages.append(SystemMessage(content="あなたは消防の専門家です。質問に対して広島弁で答えてください"))
            response = llm(messages, question)
            st.write(f"AIの回答: {response}")

        else:
            st.warning("質問を入力してください。")

