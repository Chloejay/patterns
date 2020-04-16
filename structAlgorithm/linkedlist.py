from collections import deque 

def main():
    lst= deque() 
    lst.append('de')
    lst.appendleft('sh')
    return lst 

class Node:
    def __init__(self, data: str, next= None):
        self.data= data
        self.next= next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head= None 

    def prepend(self, data:str):
        self.head= Node(data = data, 
                        next = self.head)

    def append(self, data:str):
        if not self.head:
            self.head = Node(data = data)
            return #exit 

        curNode = self.head 
        while curNode.next is not None:
            curNode= curNode.next 
        curNode.next= Node(data= data) 

    def find(self, data:str): 
        curNode= self.head  
        while curNode is not None:
            if curNode.data != data:
                import logging 
                logger = logging.getLogger()
                logger.setLevel(logging.INFO)
                logging.info('move next')

                curNode= curNode.next 
            else: 
                logging.info('found it')
                return curNode

if __name__=='__main__':
    # main() 
    lst= LinkedList() 
    lst.prepend('city')
    lst.append('de')
    lst.append('sh') 
    assert lst.find('berlin') == False, \
    'the data not found'