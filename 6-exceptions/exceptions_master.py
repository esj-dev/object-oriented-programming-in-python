
import exceptions_module
import importlib

importlib.reload(exceptions_module)

cc = exceptions_module.ConfigDict('config.txt')

print(cc['query'])
print(cc['email'])

cc['mistake']
