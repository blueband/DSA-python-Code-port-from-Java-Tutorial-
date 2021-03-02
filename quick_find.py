class QuickFind():
    ids = []
    def __init__(self, N):
        # Buiding the element of the list object here
        counter = 0
        while counter < N:
            QuickFind.ids.append(counter)
            counter += 1
    
    def getArraylenght(self):
        return len(QuickFind.ids)
    
    def getArraybyElement(self, index):
        objlength = self.getArraylenght()
        """Given an index, the method return the element at position

        Args:
            index (int): [description]
        """
        if index > objlength:
            print('out of indexing.........')
        elif index == object:
            return QuickFind.ids[index - 1]
        else:
            return QuickFind.ids[index]
    
    def getArrayIndex(self, element):
        """Generate index of the given elemnt

        Args:
            element (mixed type): [description]

        Returns:
            [type]: [description]
        """
        # print('this is element were are looking for now ', element)
        # print('this current content of our list ',QuickFind.ids)
        if element not in QuickFind.ids:
            return None
        else:
            return QuickFind.ids.index(element)
    
    
    def root(self, element_index):
        """
        This function return element at particular
        index number 
        """
        objlength = self.getArraylenght()
        if type(element_index) == str:
            element_index = self.getArrayIndex(element_index)
        
        """chase parent pointer until reach the root

        Args:
            index ([type]): [description]

        Returns:
            int: element at given index or
            None if the data has been modify
        """
        if element_index != None:
            if element_index > objlength:
                print('out of indexing.........')
            elif element_index == objlength:
                return QuickFind.ids[element_index - 1]
            else:
                return QuickFind.ids[element_index]
        else:
            return False
        
    def connected(self, p, q):
        """At moment, only the index of 
        the elemnt can be use as parameter to
        check if p and q has same root
        
        TODO #  grab the mofifying node and build a 
        disctionary object for later refence

        Args:
            int p (int): index of element
            int q (int): index of element

        Returns:
            bool: [description]
        """
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        """
        change root of p to point of root q
        (depth of p and q array access)
        """
        pid = self.getArrayIndex(p)
        print('this is pid : ', pid)
        qid = self.getArrayIndex(q)
        print('this is qid : ', qid)

        if pid == None or qid == None:
            print(None)
        else:
            for index in QuickFind.ids:
                if self.getArrayIndex(index) == pid:  # Problem is here
                    QuickFind.ids[self.getArrayIndex(index)] = qid
        print('this is Array after union operation :', QuickFind.ids) 
        
    def find(self, p, q):
        if self.connected(p, q):
            print(self.getArrayIndex(p), " is connected to ", self.getArrayIndex(q))
        else:
            print(self.getArrayIndex(p), " is not connected to ", self.getArrayIndex(q))
    
# Test case
    
searchUF = QuickFind(10)
searchUF.ids.append('g')
searchUF.ids.append('l')
searchUF.ids.append('m')
searchUF.ids.append('z')

# print(searchUF.getArrayIndex(0))
searchUF.union('m',1)
nodeconnected = searchUF.connected('m',1)
# print('the node connect is : ', nodeconnected)

print(searchUF.find(12, 1))