import pickle


class ConfigDict(dict):

    _config_directory = '/Users/esj/git/github/python-beyond-the-basics/configs/'  # match local

    def __init__(self, config_name):

        self._config_name = config_name
        self._config_file = self._config_directory + self._config_name + '.pickle'

        try:
            open(self._config_file, 'rb')
            print('Configuration file (.pickle) located successfully.')
        except FileNotFoundError:
            raise FileNotFoundError('Configuration file (.pickle) missing.')

        with open(self._config_file, 'rb') as fh:
            self.unpickled = pickle.load(fh)

        for i in self.unpickled:
            dict.__setitem__(self, i, self.unpickled[i])

    def __setitem__(self, key, value):

        dict.__setitem__(self, key, value)  # store key-value pair

        with open(self._config_file, 'wb') as fh:
            pickle.dump(self, fh)

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
