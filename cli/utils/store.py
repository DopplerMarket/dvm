import json, os.path
import config

class Store:
  
  datastore = {}
  filePath = os.path.join(config.local_directory, config.store_db)
  
  def __init__(self):
    os.makedirs(config.local_directory, exist_ok=True)

    if os.path.exists(self.filePath):
      with open(self.filePath, 'r') as f:
        self.datastore = json.load(f)
        f.close()
    
    else:
      self._update()

  
  def get(self, key, default=None):
    if key in self.datastore:
      return self.datastore[key]
      
    return default
    
    
  def set(self, key, value):
    self.datastore[key] = value
    self._update()
    
  
  def _update(self):
    with open(self.filePath, 'w') as f:
      json.dump(self.datastore, f)
      f.close()


# Export Store
store = Store()