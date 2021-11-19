class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.cnt = 0
        self.prev = None
        self.next = None


class LinkedList:

    """
    DATA_STRUCTURE

    FreqList  ==> implemented using the defaultdict(linkedlist)
        frequency   :  LinkedList
    {
        frequency1 :  head->Node1->node2->tail
        frequency2 :  head->Node1->node2->tail
        ......
    }

    cache(capacity)
        key : node
        {
            key1 : node1
            key2 : node2
            key3 : node3
        }

    """

    """ ## maintains the nodes as linkedlist with head and tail pointers, Internally implements LRU
         LRU implementation
            ==> if any operation occurs (either get or put) then frequency of that key node is updated,and 
                node is deleted from that linkedlist 
            ==> Any New Nodes are psuhed at first.
            ==> When page Fault oocurs then node with least frequency is removed.
            ==> if multiple nodes with least frequency are their then, last node is removed because it is least recently used LRU
    """

    def __init__(
        self,
    ):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertFront(self, node):
        headnxt = self.head.next  # node after head
        headnxt.prev = node
        node.next = headnxt
        node.prev = self.head
        self.head.next = node
        self.size += 1

    def removeNode(self, node):  # used during upadation
        nodeprev = node.prev
        nodenext = node.next
        nodeprev.next = nodenext
        nodenext.prev = nodeprev
        self.size -= 1

    def removeTail(self):  # used when page fault occurs
        prevtail = self.tail.prev
        self.removeNode(prevtail)
        return prevtail


class LFU:
    def __init__(self, capacity):
        from collections import defaultdict

        self.capacity = capacity
        self.cache = {}  # holds the key and address of node
        self.minfreq = 0  # always holds the minfreq
        self.freqlst = defaultdict(
            LinkedList
        )  # Automatically creates objects of Linkedlist

    def put(self, key, value):
        if not self.capacity:
            return
        if key in self.cache:
            self.update(key, value)
        else:
            if len(self.cache) == self.capacity:
                prevtail = self.freqlst[self.minfreq].removeTail()
                # print(prevtail.key)
                del self.cache[prevtail.key]
                # print(self.cache)
            newnode = Node(key, value)
            newnode.cnt += 1
            self.cache[key] = newnode
            self.freqlst[newnode.cnt].insertFront(newnode)
            self.minfreq = 1

    def get(self, key):
        if key not in self.cache:
            return -1
        return self.update(key, self.cache[key].val)

    def displayLinkedList(self, head):
        ptr = head
        while ptr != None:
            print(ptr.key, "==>", ptr.val, "==>", ptr.cnt)
            ptr = ptr.next

    def getData(self):
        print("Entire data")
        print("key==>value==>frequency")
        for each in self.freqlst:
            print("LinkedList at frequency : ", each)
            self.displayLinkedList(self.freqlst[each].head)

    def update(self, key, value):
        node = self.cache[key]
        node.val = value
        prevfreq = node.cnt
        self.freqlst[prevfreq].removeNode(node)
        node.cnt += 1
        self.freqlst[node.cnt].insertFront(node)

        if prevfreq == self.minfreq and self.freqlst[prevfreq].size == 0:
            self.minfreq += 1
        return node.val


obj = LFU(3)
obj.put(1, 10)
obj.put(2, 20)
obj.put(3, 30)
obj.put(4, 40)
obj.getData()
# print("getting value of a key 1 :", obj.get(1))
# obj.getData()
# print("getting value of a key 2 :", obj.get(2))
# obj.getData()
