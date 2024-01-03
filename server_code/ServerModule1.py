import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def to_bytes(data):
  data = bytes([ord(c) for c in data])
  return data
