import sys

def config():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print 'pyhub lib is running!'
    print 'encodig is '+str(sys.getdefaultencoding())
        
