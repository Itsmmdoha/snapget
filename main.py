from requests import get, head

class File:
    def __init__(self,url,numberOfThreads):
        File.url = url
        File.numberOfThreads = numberOfThreads
    def chunkSize(self):
        pass

    def getFileName(self):
        pass

    def getChunk(self,startByte,endByte):
        pass
