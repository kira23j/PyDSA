class Borg:
    _shared_state={}
    def __init__(self):
        self.__dict__=self._shared_state
        
        
        

class Singleton(Borg):
    def __init__(self,**kwargs):
        Borg.__init__(self)
        self._shared_state.update(kwargs)
    
    def __str__(self) -> str:
        return str(self._shared_state)
    
    
x=Singleton(HTTP="hyper text transfer protocol")
print(x)
y=Singleton(LMS="learning management system")
print(y)
z=Singleton(WSL="windows subsystem for linux")
print(z)

#   output
# {'HTTP': 'hyper text transfer protocol'}
# {'HTTP': 'hyper text transfer protocol', 'LMS': 'learning management system'}
# {'HTTP': 'hyper text transfer protocol', 'LMS': 'learning management system', 'WSL': 'windows subsystem for linux'}