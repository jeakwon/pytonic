import pyabf
import matplotlib.pyplot as plt

class ABF(pyabf.ABF):
    def __init__(self,abfFilePath):
        super().__init__(abfFilePath)

    def plot(self):
        plt.plot(self.data)
        plt.show()

if __name__ == "__main__":
    f = r'C:\Users\jeakwon\Desktop\f1.abf'
    abf = ABF(f)
    import pprint
    pprint.pprint(dir(abf))