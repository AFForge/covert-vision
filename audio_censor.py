import os
from pedalboard.io import AudioFile
from pedalboard import Pedalboard, PitchShift, HighpassFilter, LowpassFilter

def audio_censor(wav_filepath):
    """
    Censors the audio 
    """
    try:
        # Load the audio file
        with AudioFile(wav_filepath) as f:
            audio = f.read(f.frames)
            samplerate = f.samplerate

        # Create a pedalboard with the desired effects
        board = Pedalboard([
            HighpassFilter(cutoff_frequency_hz=150.0),
            LowpassFilter(cutoff_frequency_hz=3500.0),
            PitchShift(semitones=-7.0)
        ])

        # Process the audio
        processed_audio = board(audio, samplerate)

        # Save the processed audio back to the file
        with AudioFile(wav_filepath, 'w', samplerate, processed_audio.shape[0]) as f:
            f.write(processed_audio)

        return True

    except Exception as e:
        print(f"[ERROR] Failed to censor audio: {e}")
        return False
    