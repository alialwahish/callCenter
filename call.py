from datetime import datetime
class Call(object):
    def __init__(self,calrNam,calPhnNum,resnFrCal,idd):
        self.idd=idd
        self.calrNam=calrNam
        self.calPhnNum=calPhnNum
        self.timCal=datetime.now().strftime('%Y-%m-d %H: %M:%S')    
        self.resnFrCal=resnFrCal
    def display(self):
        print self.calrNam,self.calPhnNum,self.timCal,self.resnFrCal   

