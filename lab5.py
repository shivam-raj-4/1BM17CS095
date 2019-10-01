class calldetail:
    def __init__(self):
        self.caller=None
        self.reciever=None
        self.time=None
        self.t=None
    def detail(self,caller,reciever,time,t):
        self.caller=caller
        self.reciever=reciever
        self.time=time
        self.t=t
    def display(self,i):
        print("Detail no.",i)
        print("Caller :",self.caller)
        print("Reciever :",self.reciever)
        print("Time :",self.time)
        print("Type of Call :",self.t)
        print("")
class Util:
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=list_of_call_string
        i=0
        for a in self.list_of_call_objects:
            y=a.split(",")
            o=calldetail()
            o.detail(y[0],y[1],y[2],y[3])
            i=i+1
            o.display(i)
call1='9990000001,9330000001,23,STD'
call2='9990000011,9330000011,25,LOCAL'
list_of_call_string=[call1,call2]
Util().parse_customer(list_of_call_string)
