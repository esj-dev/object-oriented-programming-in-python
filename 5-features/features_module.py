
class ConfigDict(dict):

    def __init__(self, filename):

        self._filename = filename  # marking the variable as private using _name

        temp_str = open(self._filename, 'r').read()
        temp_lst = temp_str.split('\n')[:-1]
        temp_lst_pairs = [i.split('=') for i in temp_lst]
        for i in temp_lst_pairs:
            dict.__setitem__(self, i[0], i[1])  # invoking parent method here to avoid our custom __setitem__  below!

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)  # store key-value pair
        file = open(self._filename, 'a')  # open .txt file for writing
        file.write(key + '=' + value + '\n')  # write key-value pairs to .txt
        file.close()  # update .txt
