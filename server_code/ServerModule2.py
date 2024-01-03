import anvil.server
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

@anvil.server.callable
def func1(file, file_list):

  import sys
import librosa
from sound_to_midi.monophonic import wave_to_midi

print("Starting...")
file_in = file_list
file_out = 'Untitled.mid'
y, sr = librosa.load(file_in, sr=None)
print("Audio file loaded!")
midi = wave_to_midi(y, sr=sr)
print("Conversion finished!")
with open (file_out, 'wb') as f:
    midi.writeFile(f)
print("Done. Exiting!")
  
  
  
