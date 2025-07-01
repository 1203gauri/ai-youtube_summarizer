# import streamlit as st
# from utils import extract_video_id
# from summarizer import get_transcript, summarize_text
# from document_export import save_summary_as_pdf, save_summary_as_docx

# st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")
# st.title("📬 YouTube Video Summarizer")

# url = st.text_input("Enter YouTube Video URL")

# if st.button("Summarize"):
#     try:
#         video_id = extract_video_id(url)
#         with st.spinner("Fetching Transcript..."):
#             transcript = get_transcript(video_id)
#         with st.spinner("Summarizing Transcript..."):
#             summary = summarize_text(transcript)

#         st.subheader("📝 Summary")
#         st.text_area("Video Summary:", summary, height=300)

#         st.download_button("Download as PDF", save_summary_as_pdf(summary), file_name="summary.pdf")
#         st.download_button("Download as DOCX", save_summary_as_docx(summary), file_name="summary.docx")
#     except Exception as e:
#         st.error(f"Error: {e}")



# app.py
import streamlit as st
from utils import extract_video_id
from summarizer import get_transcript, summarize_text_as_notes
from document_export import save_notes_as_pdf
from dotenv import load_dotenv
import os

load_dotenv()
st.set_page_config(page_title="YouTube Study Notes Generator", layout="wide")
st.title("📚 AI-Powered YouTube Study Notes Generator")

st.markdown("""
Enter a YouTube video URL. The AI will extract the transcript, convert it into structured study notes, 
and let you download them as a clean PDF.
""")

url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Study Notes"):
    try:
        video_id = extract_video_id(url)
        with st.spinner("Fetching Transcript..."):
            transcript = get_transcript(video_id)
        with st.spinner("Generating Study Notes with Gemini AI..."):
            notes = summarize_text_as_notes(transcript)

        st.subheader("📝 Generated Study Notes")
        st.text_area("Notes:", notes, height=400)

        st.download_button("📄 Download Notes as PDF", data=save_notes_as_pdf(notes), file_name="study_notes.pdf", mime="application/pdf")

    except Exception as e:
        st.error(f"Error: {e}")
