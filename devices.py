class Devices:
    def __init__(self,name,value,_state):
        self.name = name
        self.value = value
        self.state = _state

    def __str__(self):
        return f"{self.name} ({self.state})"
     
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self,text):
        if text == "Active":
            self._state = "Active"
        
        elif text == "Service":
            self._state = "Service"
        
        elif text == "Reject":
            self._state = "Reject"
        else:
            self._state = "Reject"

    @classmethod
    def create_fromtext(cls,data):
        base = data.split(";")

        name = base[0]
        value = int(base[1])
        state = base[2]
        extra = base[3]

        if extra == "Server":
            return Server(name,value,state,8)
        
        elif extra == "Laptop":
            return WorkStation(name,value,state,"Unknown")
        
        else:
            return cls(name,value,state)
        
class WorkStation(Devices):
    def __init__(self,name,value,state,user):
        super().__init__(name,value,state)
        self.user = user

    def error_report(self):
        print(f"User {self.user}, reported the error on: {self.name}")
    
class Server(Devices):
    def __init__(self,name,value,state,cpu):
        super().__init__(name,value,state)
        self.cpu = cpu

    def error_report(self):
        print(f"CRITICAL ERROR ON SERVER: {self.name}")

           