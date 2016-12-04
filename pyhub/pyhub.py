import sys

class pyhub(object):
    def __init__(self):
        print 'pyhub lib is running!'
    @staticmethod
    def config():
        reload(sys)
        sys.setdefaultencoding('utf-8')
        
