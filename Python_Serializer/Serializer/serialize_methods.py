from abc import ABC, abstractmethod

class SerializeMethods():
    
    @abstractmethod
    def dump(self, obj, fp):
        pass
    @abstractmethod
    def dumps(self, obj):
        pass
    @abstractmethod
    def load(self, fp):
        pass
    @abstractmethod
    def loads(self, s):
        pass