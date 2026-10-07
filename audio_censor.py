import os
from pydub import AudioSegment
from pydub.generators import WhiteNoise

def audio_censor(wav_filepath):
    """
    Censors the audio
    """
    try:
        # Load the audio file
        audio = AudioSegment.from_file(wav_filepath, format="wav")

        #Band-pass filter
        audio = audio.low_pass_filter(2500).high_pass_filter(400)

        # Generate white noise
        noise = WhiteNoise().to_audio_segment(duration=len(audio)) - 25  
        audio = audio.overlay(noise)

        # Increase the volume of the audio by 5 dB  
        audio = audio + 5 

        #Overwrite the original audio file with the censored version
        audio.export(wav_filepath, format="wav")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to censor audio: {e}")
        return False
    