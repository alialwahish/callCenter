import call
class callCenter(object):
    def __init__(self):
        self.call=[]
    def add(self,name,phnNum,resnFrCal,idd="55"):
        
        self.call.append(call.Call(name,phnNum,resnFrCal))
        
        return self
    
    def remove(self):
        self.call.pop(0)
        
    def info(self):
        for contInfo in self.call:
            print "Name:",contInfo.calrNam,"Phone Number",contInfo.calPhnNum,contInfo.idd
        print "Queue:",len(self.call)
        return self
    
    
xf=callCenter()
xf.add("ali","444","followin")
xf.add("ryan","666","new customer")
xf.add("mony","555","ads")
xf.info()