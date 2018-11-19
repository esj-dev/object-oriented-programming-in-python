
import importlib
import serialization_module

importlib.reload(serialization_module)

cc = serialization_module.ConfigDict('my_config')

cc['query']
cc['email']

cc['team'] = 'mtech'
