import streamlit as st
import asyncio


async def main():
    st.set_page_config(page_title="Main", page_icon="💻")
    st.header("Main\n\n")

    st.markdown("### Data Upload")
    st.write("""
    On this page, you can upload a file for model training. 
    We support one-file uploads at a time, and your file is also saved 
    on your local computer. Once uploaded, the document undergoes processing,
    which may take some time depending on the size and complexity of the file. 
    Upload your file now to get started!
    """)
    st.markdown("### Interactive Chat")
    st.write("""
    On this page, you can submit a text query, and after a pause, 
    the response will be generated. The processing time may vary depending 
    on your computer's performance. Once complete, you will receive the answer,
     execution time, and associated documents related to the response. 
     Try entering your query and explore the results.
    """)


if __name__ == "__main__":
    asyncio.run(main())
