from abc import ABC, abstractmethod

class BaseCollector(ABC):
    
    @abstractmethod
    def get_aircraft(self):
        pass