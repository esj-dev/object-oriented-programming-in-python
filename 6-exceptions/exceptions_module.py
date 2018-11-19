
class ConfigDict(dict):

    def __init__(self, filename):

        self._filename = filename  # marking the variable as private using _name

        try:
            temp_str = open(self._filename, 'r').read()
            print('Text file found successfully.')
        except FileNotFoundError:
            raise FileNotFoundError('File or path does not exist.')

        temp_lst = temp_str.split('\n')[:-1]
        temp_lst_pairs = [i.split('=') for i in temp_lst]
        for i in temp_lst_pairs:
            dict.__setitem__(self, i[0], i[1])  # invoking parent method here to avoid our custom __setitem__  below!

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)  # store key-value pair
        file = open(self._filename, 'a')  # open .txt file for writing
        file.write(key + '=' + value + '\n')  # write key-value pairs to .txt
        file.close()  # update .txt

    def __getitem__(self, key):  # overwriting __getitem__ method inherited from dict!

        try:
            dict.__getitem__(self, key)
        except KeyError:
            key_list = self.keys()
            raise ConfigKeyError(key, key_list)
        return dict.__getitem__(self, key)


class ConfigKeyError(Exception):

    def __init__(self, key, key_list):
        self._bad_key = key
        self._key_list = key_list

    def __str__(self):
        return("The key '{0}' does not exist in this ConfigDict instance. Available keys are {1}".
               format(self._bad_key,
                      tuple(self._key_list)
                      )
               )
