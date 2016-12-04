import sys

def config():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print 'pyhub lib is running! and encoding is %s'% str(sys.getdefaultencoding())
