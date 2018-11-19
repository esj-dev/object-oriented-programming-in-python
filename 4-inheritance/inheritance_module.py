import abc
import datetime
import os


class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, filename, delimiter=','):

        if not os.path.exists('files'):
            os.mkdir('files')

        self.file = open('files/' + filename, 'w+')
        self.delimiter = delimiter

    @abc.abstractmethod
    def write(self, par):  # here, par is a string and list, respectively
        return


class LogFile(WriteFile):

    def write(self, par):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.file.write(dt_str + ' ' + par + '\n')


class DelimFile(WriteFile):

    def write(self, par):

        string = self.delimiter.join(par)
        self.file.write(string + '\n')
