import anvil.server
import anvil.media
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import sys
import librosa
from sound_to_midi.monophonic import wave_to_midi


@anvil.server.callable
def access_files(file, files_list):


  file_in = (file)
  file_out = 'Untitled.mid'
  y, sr = librosa.load(file_in, sr=None)
  print("Audio file loaded!")
  midi = wave_to_midi(y, sr=sr)
  print("Conversion finished!")
  with open (file_out, 'wb') as f:
    midi.writeFile(f)
  print("Done. Exiting!")


