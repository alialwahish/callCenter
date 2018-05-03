from datetime import datetime
class Call(object):
    def __init__(self,calrNam,calPhnNum,resnFrCal,idd="55"):
        self.idd=""
        self.calrNam=calrNam
        self.calPhnNum=calPhnNum
        self.timCal=datetime.now().strftime('%Y-%m-d %H: %M:%S')    
        self.resnFrCal=resnFrCal
    def display(self):
        print self.idd,self.calrNam,self.calPhnNum,self.timCal,self.resnFrCal
    def getClrNam(self):
        return self.calrNam
        
    def getPhnNum(self):
        return self.calPhnNum

