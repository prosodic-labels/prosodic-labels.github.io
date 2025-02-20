from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Directory where audio files are stored
AUDIO_DIR = '/speech/krupavathy/INTERSPEECH_krupa_exps/Interspeech-Paper-Kit/hosting_samples/audio_samples/'

@app.route('/')
def index():
    # Get list of audio files
    audio_files = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.mp3') or f.endswith('.wav')]
    return render_template('index.html', audio_files=audio_files)

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
