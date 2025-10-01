import numpy as np
class MyArray:
    def __init__(self,value):
        self.shape = value
        self.abc = np.ones(shape=(0,value))
    
    def replace(self,index,value):
            if index < self.shape:
               self.abc[index] = value
            
    def insert(self,index,value):
        if index < self.shape:
            self.abc = np.insert(self.abc,index,value)

    def remove(self,index):
        if index < self.shape:
            self.abc = np.delete(self.abc,index)
    

if __name__ == "__main__":
    arr = MyArray(5)
    arr.insert(index=0,value=10)
    arr.insert(1,20)
    arr.insert(2,30)
    print(f"หลัง insert:",arr.abc)

    arr.replace(1,99)
    print(f"หลัง replace index 1:",arr.abc)

    arr.remove(0)
    print(f"หลัง remove index 0:",arr.abc)