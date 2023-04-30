import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv



frekans = 44100
sure = 20

kayit = sd.rec(int(frekans * sure),samplerate=frekans, channels=2)

sd.wait()

write("kayit0.wav",frekans, kayit)

wv.write("kayit1.wav",kayit,frekans,sampwidth=2)