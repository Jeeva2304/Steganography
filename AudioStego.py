from abc import ABC, abstractmethod

class AudioStego(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def EncodeAudio(self, audioLocation, stringToEncode) -> str:
        pass
    
    @abstractmethod
    def DecodeAudio(self, audioLocation) -> str:
        pass
    
    @abstractmethod
    def ConvertToByteArray(self, audio):
        pass
    
    @abstractmethod
    def SaveToLoaction(self, audioArray, location) -> str:
        pass
