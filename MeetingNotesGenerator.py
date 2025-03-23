import re
import streamlit as st
from SpeechToText import SpeechToText
from Summarizer import Summarizer

def main():
    FileUpload().get_audio()

class FileUpload:

    def get_audio(self):
        #upload the file through streamlit
        audio_file = st.file_uploader(label = "Upload meeting audio,", type=["wav","mp3"])
        transcriber = SpeechToText()
        summarizer = Summarizer()

        if audio_file is not None:
            st.audio(audio_file)

            meeting_text = transcriber.transcribe_text(audio_file) #transcribe audio to text
            summary = summarizer.summarize_text(meeting_text) #summarize the text using DeepSeek-R1
            cleaned_summary = re.sub(r'<think>.*?</think>', '', summary, flags=re.DOTALL) #Remove the thinking done by deepseek

            st.write(cleaned_summary) #write the summary to streamlit


if __name__ == '__main__':
    main()