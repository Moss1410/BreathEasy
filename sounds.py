import numpy as np
import simpleaudio as sa

def playSound(freq, sec):
    frequency = freq  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = sec  # Note duration of 3 seconds   

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, int(seconds * fs), False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done() 

def player():
    A_freq = 440
    Csh_freq = A_freq * 2 ** (4 / 12)
    E_freq = A_freq * 2 ** (7 / 12)

    # get timesteps for each sample, T is note duration in seconds
    sample_rate = 44100
    T = 0.5
    t = np.linspace(0, T, int(T * sample_rate), False)

    # generate sine wave notes
    A_note = np.sin(A_freq * t * 2 * np.pi)
    Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
    E_note = np.sin(E_freq * t * 2 * np.pi)

    # mix audio together
    audio = np.zeros((44100, 2))
    n = len(t)
    offset = 0
    audio[0 + offset: n + offset, 0] += A_note
    audio[0 + offset: n + offset, 1] += 0.125 * A_note
    offset = 5500
    audio[0 + offset: n + offset, 0] += 0.5 * Csh_note
    audio[0 + offset: n + offset, 1] += 0.5 * Csh_note
    offset = 11000
    audio[0 + offset: n + offset, 0] += 0.125 * E_note
    audio[0 + offset: n + offset, 1] += E_note

    # normalize to 16-bit range
    audio *= 32767 / np.max(np.abs(audio))
    # convert to 16-bit data
    audio = audio.astype(np.int16)

    # start playback
    play_obj = sa.play_buffer(audio, 2, 2, sample_rate)

    # wait for playback to finish before exiting
    play_obj.wait_done()       

def ascending():
    f = 400
    while f < 1000:
        playSound(f, 0.05)
        f += 10

player()