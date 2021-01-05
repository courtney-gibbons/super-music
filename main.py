import time
import array
import math
import board
import digitalio
from audiocore import RawSample
from audioio import AudioOut

def play_tone(freq, duration):
    audio.play(get_sample(freq), loop=True)
    time.sleep(duration)
    audio.stop()  # and then stop.


def get_sample(freq):
    if freq == 0:
        return RawSample(array.array("H",[0]))
    FREQUENCY = freq
    SAMPLERATE = 22050

    length = int(SAMPLERATE * 4 / FREQUENCY)
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i * 4 / length) * (2 ** 15) + 2 ** 15)
    sine_wave_sample = RawSample(sine_wave, sample_rate = SAMPLERATE)
    return sine_wave_sample

# Enable the speaker
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.direction = digitalio.Direction.OUTPUT
speaker_enable.value = True
audio = AudioOut(board.SPEAKER)

frequencies_and_durations = [
    (261,.5), #C
    (261,.5), #C
    (392,.5), #G
    (392,.5), #G
    (440,.5), #A
    (440,.5), #A
    (392,1), #G
    
    (349,.5), #F
    (349,.5), #F
    (329,.5), #E
    (329,.5), #E
    (293,.5), #D
    (293,.5), #D
    (261,1), #C
    
    (392,.5), #G
    (392,.5), #G
    (349,.5), #F
    (349,.5), #F
    (329,.5), #E
    (329,.5), #E
    (293,1), #D
    
    (392,.5), #G
    (392,.5), #G
    (349,.5), #F
    (349,.5), #F
    (329,.5), #E
    (329,.5), #E
    (293,.5), #D
    
    (261,.5), #C
    (261,.5), #C
    (392,.5), #G
    (392,.5), #G
    (440,.5), #A
    (440,.5), #A
    (392,1), #G
    
    (349,.5), #F
    (349,.5), #F
    (329,.5), #E
    (329,.5), #E
    (293,.5), #D
    (293,.5), #D
    (261,1), #C
]

for frequency_and_duration in frequencies_and_durations:
    play_tone(frequency_and_duration[0],frequency_and_duration[1])
