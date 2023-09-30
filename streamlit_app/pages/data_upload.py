from pathlib import Path

import streamlit as st
import os
from dotenv import load_dotenv
import asyncio
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))

from ingest import main as ingest_main

load_dotenv()

source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')

file_extensions = [
    ".csv",
    ".docx",
    ".doc",
    ".enex",
    ".eml",
    ".epub",
    ".html",
    ".md",
    ".msg",
    ".odt",
    ".pdf",
    ".pptx",
    ".ppt",
    ".txt"
]


async def main():
    st.set_page_config(page_title="Data upload", page_icon="📥")
    st.header('Upload training data file\n\n')

    uploaded_file = st.file_uploader("Choose a file", type=file_extensions)
    if uploaded_file:
        path = Path(__file__).resolve().parent
        parent_path = path.parents[1]
        filename = f"{parent_path}/{source_directory}/{uploaded_file.name}"

        with open(filename, "wb") as file:
            file.write(uploaded_file.read())

        ingest_main()

    st.write("""
    The supported extensions are:

       - `.csv`: CSV,
       - `.docx`: Word Document,
       - `.doc`: Word Document,
       - `.enex`: EverNote,
       - `.eml`: Email,
       - `.epub`: EPub,
       - `.html`: HTML File,
       - `.md`: Markdown,
       - `.msg`: Outlook Message,
       - `.odt`: Open Document Text,
       - `.pdf`: Portable Document Format (PDF),
       - `.pptx` : PowerPoint Document,
       - `.ppt` : PowerPoint Document,
       - `.txt`: Text file (UTF-8),
    """)


if __name__ == "__main__":
    asyncio.run(main())
