import anvil.server

@anvil.server.callable
def to_bytes(data):
  data = bytes([ord(c) for c in data])
  return data
