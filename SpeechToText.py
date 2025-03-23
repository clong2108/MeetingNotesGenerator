import os
import sys
import tempfile
import whisper

class SpeechToText:
    def transcribe_text(self, audio_file):
        model = whisper.load_model('base')

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_path = tmp_file.name

        result = model.transcribe(audio=tmp_path, fp16=False)

        os.unlink(tmp_path)

        return result['text']
