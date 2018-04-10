import sys
from PyQt5.QtWidgets import QDesktopWidget


def config():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print 'pyhub lib is running! and encoding is %s'% str(sys.getdefaultencoding())

def centerWidget(self):
    screen=QDesktopWidget().screenGeometry()
    size=self.geometry()
    half_width=(screen.width()-size.width())/2
    half_height=(screen.height()-size.height())/2
    self.move(half_width,half_height)
#from left to right,top to bottom

def paixu_maopao(lst):
    b = []
    l = len()
    for i in range(l):
        j = i
        for j in range(l):
            if (lst[i][0] < lst[j][0]):
                lst[i], lst[j] = lst[j], lst[i]
            if (lst[i][1] > lst[j][1]):
                lst[i], lst[j] = lst[j], lst[i]

    for k in range(len(lst)):
        b.append(lst[k])
    return b
