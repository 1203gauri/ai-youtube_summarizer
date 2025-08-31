📚 YouTube Video Summarizer with Gemini AI


Tired of watching long videos for revision? This AI-powered tool extracts the transcript from any YouTube video and uses Google's powerful Gemini AI to generate clean, structured, and downloadable study notes. Learn smarter, not harder.

✨ Live Demo (Coming Soon!) - The app is currently being deployed. Stay tuned!



✨ Features
🔗 Simple Input: Just paste the YouTube video URL and let the AI do the rest.

🤖 AI-Powered Summarization: Leverages Google's Gemini Pro model to understand context and generate coherent, bullet-pointed notes.

📄 Transcript Extraction: Automatically fetches the complete transcript using the youtube-transcript-api.

📥 Export to PDF: Download your beautifully formatted study notes as a PDF for offline use with one click.

🚀 Streamlit UI: Built with Streamlit for an intuitive and clean user interface.

🔒 Secure: API keys are managed securely using python-dotenv.

🛠️ Tech Stack
Frontend & Framework: Streamlit

AI & Language Model: Google Gemini API (Gemini Pro)

Transcript Fetching: youtube-transcript-api

PDF Generation: FPDF

Environment Management: python-dotenv

Language: Python 3.9+

📦 Installation & Setup
Follow these steps to run the project locally on your machine.

Clone the repository

bash
git clone https://github.com/your-username/youtube-video-summarizer.git
cd youtube-video-summarizer
Create a Virtual Environment (Recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
pip install -r requirements.txt
Get Your Google Gemini API Key

Visit Google AI Studio.

Sign in with your Google account.

Generate an API key for the Gemini Pro model.

Set Up Environment Variables

Create a new file named .env in the project root directory.

Add your API key to this file:

env
GEMINI_API_KEY=your_actual_api_key_here
Replace your_actual_api_key_here with the key you obtained from Google AI Studio.

Run the Streamlit App

bash
streamlit run app.py
Open your browser and go to the local URL shown in the terminal (usually http://localhost:8501).

🚀 How to Use
Enter YouTube URL: Paste the link of the YouTube video you want to summarize into the input box.

Generate Notes: Click the "Generate Notes" button. The app will fetch the transcript and send it to Gemini AI for processing.

Review & Download: The AI-generated summary will appear on the screen. Click the "Download PDF" button to save your notes.

📂 Project Structure
text
youtube-video-summarizer/
├── app.py                 # Main Streamlit application logic
├── .env                  # Environment variables (gitignored, you create it)
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── assets/             # Directory for demo images/GIFs (optional)
💡 Why This Matters
This project is a practical example of how AI can transform education and productivity. By automating the note-taking process from long-form video content, we can:

Save countless hours of manual work.

Improve focus on understanding concepts rather than transcribing.

Make learning more accessible and efficient for everyone.

It demonstrates the potential of leveraging powerful AI APIs like Gemini to build impactful tools that solve real-world problems.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page or open a Pull Request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request


🙋‍♂️ Author
Gauri Pandey
LinkedIn
https://www.linkedin.com/in/gauri-pandey-90a848252/

GitHub
https://github.com/1203gauri
🌟 Acknowledgments
Google DeepMind for the Gemini API.

The Streamlit team for making app development incredibly simple.

All the contributors and users of the youtube-transcript-api and FPDF libraries
