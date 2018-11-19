
from features_module import ConfigDict

# create instance of ConfigDict (subclass of dict)

cc = ConfigDict('config.txt')

print(cc['query'])
print(cc['email'])

cc['team'] = 'mtech'  # this writes a new key=value to config.txt

# create instance of dict

my_dict = {'email': 'esj@kayak.com', 'pwd': 'blank', 'mac': 'dkmac44', 'team': 'bi'}

# intro to __setitem__ method

my_dict['pwd'] = '_hidden_'  # call method
my_dict.__setitem__('team', 'mtech')
my_dict.__setitem__('man', 'sji')

# intro to __getitem__ method

my_dict['email']  = 'esj@jkayak.dk'  # call method
my_dict.__getitem__('email')
my_dict.__getitem__('team')

# writing to config.txt

temp_config = open('config.txt', 'a')
temp_config.write('warehouse=vertica' + '\n')
temp_config.close()

temp_config = open('config.txt', 'a')
temp_config.write('cluster=c4sem' + '\n')
temp_config.close()
