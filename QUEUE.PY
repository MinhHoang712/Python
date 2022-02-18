class Queue(object):
    def __init__(self,limit=5):
        self.que = []
        self.limit = limit 
        self.front = None 
        self.rear = None 
        self.size = 0
    def isEmpty(self):
        return self.size <= 0
    #phương thức thêm một phần tử vào hàng đợi 
    def enQueue(self,item):
        if self.size >= self.limit:
            print("Hàng đợi đầy")
            return 0
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size 
        self.size +=1
        print("Hàng đợi sau khi thêm vào là: ")
        print(self.que)
    #phương thức lấy một phần tử ở hàng đợi
    def deQueue(self):
        if self.size <=0:
            print('Hàng đợi rỗng')
            return 0
        else:
            self.que.pop(0)
            self.size -=1
            if self.size == 0:
                self.front = self.rear = None 
            else:
                self.rear = self.size -1
            print('Hàng đợi sau khi lấy giá trị là: ')
            print(self.que)
    def size(self):
        return self.size 
if __name__ == "__main__":
    queue = Queue(5)
    queue.enQueue(3)
    queue.enQueue(21)
    queue.enQueue(312)
    queue.enQueue(123)
    queue.enQueue(4)
    queue.deQueue()
        
        
        
            