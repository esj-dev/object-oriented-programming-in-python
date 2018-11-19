
from inheritance_module import LogFile, DelimFile

my_log = LogFile('log.txt')
my_log.write('this is a log message')
my_log.write('this is another log message')
my_log.file.close()  # necessary to cache .txt file

my_delim = DelimFile('data.csv', ',')
my_delim.write(['a', 'b', 'c', 'd'])
my_delim.write(['1', '2', '3', '4'])
my_delim.file.close()  # necessary to cache .csv file
