# # from youtube_transcript_api import YouTubeTranscriptApi
# # from transformers import pipeline

# # summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# # def get_transcript(video_id):
# #     transcript = YouTubeTranscriptApi.get_transcript(video_id)
# #     return ' '.join([segment['text'] for segment in transcript])

# # def summarize_text(text, max_chunk=1000):
# #     chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
# #     summary = ''
# #     for chunk in chunks:
# #         out = summarizer_pipeline(chunk, max_length=150, min_length=50, do_sample=False)
# #         summary += out[0]['summary_text'] + '\n'
# #     return summary.strip()
# import openai
# import os
# from youtube_transcript_api import YouTubeTranscriptApi
# from dotenv import load_dotenv



# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to set this environment variable

# def get_transcript(video_id):
#     transcript = YouTubeTranscriptApi.get_transcript(video_id)
#     return ' '.join([segment['text'] for segment in transcript])

# def summarize_text_as_notes(transcript_text):
#     prompt = (
#         "Summarize the following YouTube transcript into well-structured study notes. "
#         "Use bullet points, subheadings, and make it easy to revise for students.\n\n"
#         f"Transcript: {transcript_text}\n\n"
#         "Notes:"
#     )

#     response = openai.ChatCompletion.create(
#         model="gemini-2.0-flash",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.5,
#         max_tokens=1500
#     )

#     return response["choices"][0]["message"]["content"].strip()



# summarizer.py
import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def get_transcript(video_id):
    """Fetches transcript from YouTube video."""
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return ' '.join([segment['text'] for segment in transcript])

def summarize_text_as_notes(transcript_text):
    """Summarize transcript text using Gemini AI."""
    prompt = (
        "Summarize the following YouTube transcript into well-structured study notes. "
        "Use bullet points, subheadings, and make it easy to revise for students.\n\n"
        f"Transcript: {transcript_text}\n\n"
        "Notes:"
    )
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating summary: {e}"
