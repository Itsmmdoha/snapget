from requests import get, head

class File:
    def __init__(self,url,numberOfThreads):
        File.url = url
        File.numberOfThreads = numberOfThreads

    def getChunk(self,startByte,endByte):
        pass
