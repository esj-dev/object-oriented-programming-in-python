
class MaxSizeList(object):

    def __init__(self, par):
        self.lst = []
        self.mlength = par

    def push(self, string):
        self.lst.append(string)
        if len(self.lst) > self.mlength:
            self.lst.pop(0)

    def get_list(self):
        return self.lst
