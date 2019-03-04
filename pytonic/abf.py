import pyabf

class ABF(pyabf.ABF):
    def __init__(self,abfFilePath):
        super().__init__(abfFilePath)

if __name__ == "__main__":
    f = r'C:\Users\jeakwon\Desktop\f1.abf'
    ABF(f)