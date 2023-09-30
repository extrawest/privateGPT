from pathlib import Path

import streamlit as st
import asyncio
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from privateGPT import get_answer


async def main():
    st.set_page_config(page_title="Interactive chat", page_icon="🗨️")
    st.header("Interactive chat\n\n")

    prompt = st.chat_input("Send a message")
    if prompt:
        answer, docs, time_for_answer = get_answer(prompt)
        st.write(f"Docs: {len(docs)}")
        for item in docs:
            st.write(f"{item}\n")

        st.write(f"Time: {time_for_answer} s")
        st.write(f"Question: {prompt}\n")
        st.write(f"Answer:  {answer}\n")




if __name__ == "__main__":
    asyncio.run(main())
