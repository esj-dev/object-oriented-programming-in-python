
from classes_module import MaxSizeList

a = MaxSizeList(2)
b = MaxSizeList(5)

for obj in (a, b):
    obj.push('hey')
    obj.push('yo')
    obj.push('world')
    obj.push('data')
    obj.push('science')
    obj.push('blob')
    obj.push('kayak')

for obj in (a, b):
    print(obj.get_list())
