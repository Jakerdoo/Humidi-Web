import anvil.server
from anvil import *
import anvil.files
from anvil.files import data_files
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

@anvil.server.callable
def func1(self, file, **event_args):

  import sys
import librosa
from sound_to_midi.monophonic import wave_to_midi
tablerow = app_tables.table_1.search()[0]['Column1']

print("Starting...")
file_in = tablerow
file_out = 'Untitled.mid'
y, sr = librosa.load(file_in, sr=None)
print("Audio file loaded!")
midi = wave_to_midi(y, sr=sr)
print("Conversion finished!")
with open (file_out, 'wb') as f:
    midi.writeFile(f)
print("Done. Exiting!")
  
  
  
