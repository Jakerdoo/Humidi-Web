from ._anvil_designer import FileDragAndDropTemplate
from anvil import *
import anvil.server

class FileDragAndDrop(FileDragAndDropTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def drag_drop_upload(self, content_type, data, name):
    # JS sent this data over as a "byte string", ie a string whose codepoints match the bytes in the file
    # Transfrom from a  it into a byte string for Python 3
    data = anvil.server.call('to_bytes', data)
    print('Original file bytes:', data)
    print('Original file content type:', content_type)
    print('Original file name:', name)

    dropped_file = BlobMedia(content_type, data, name=name)

    print('Anvil BlobMedia object bytes:', dropped_file.get_bytes())
    print('Anvil BlobMedia object content type:', dropped_file.content_type)
    print('Anvil BlobMedia object name:', dropped_file.name)
    print('Anvil BlobMedia object length:', dropped_file.length)
    
    self.file_loader_1.files.append(dropped_file)
    self.file_uploaded(dropped_file)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.file_uploaded(file)
    
  def file_uploaded(self, file):
    print('File uploaded, either by drag-and-drop or using the built-in file dialog: ', file.name)
