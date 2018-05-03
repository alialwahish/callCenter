import call
import uuid

class callCenter(object):
    def __init__(self):
        self.call=[]
    def add(self,name,phnNum,resnFrCal):
        uniId=str(uuid.uuid4())
        uniId=uniId[-6:]
        self.call.append(call.Call(name,phnNum,resnFrCal,idd=uniId))
        
        return self
    
    def findAndRem(self,phnNmbr):
        print "deleting record associated with phone number",phnNmbr
        for i in self.call:
            if phnNmbr == i.calPhnNum:
                print "deleted record:",i.calrNam,i.calPhnNum
                self.call.remove(i)
                
    def remove(self):
        self.call.pop(0)
        
    def info(self):
        print
        for contInfo in self.call:
            print "Name:",contInfo.calrNam,"Phone Number",contInfo.calPhnNum
        print "Queue:",len(self.call)
        return self
    
    
xf=callCenter()
xf.add("ali","444","followin")
xf.add("ryan","666","new customer")
xf.add("mony","555","ads")

xf.info()
xf.findAndRem("666")
xf.info()