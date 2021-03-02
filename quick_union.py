class QuickUnion():
    ids = []
    def __init__(self, N):
        # Buiding the element of the list object here
        counter = 0
        while counter < N:
            QuickUnion.ids.append(counter)
            counter += 1
    
    def getArraylenght(self):
        return len(QuickUnion.ids)
            
    def root(self, element_index):
        objlength = self.getArraylenght()
        """chase parent pointer until reach the root

        Args:
            index ([type]): [description]

        Returns:
            [type]: [description]
        """
        if element_index > objlength:
            print('out of indexing.........')
        elif element_index == object:
            return QuickUnion.ids[element_index - 1]
        else:
            return QuickUnion.ids[element_index]
        
    def connected(self, p, q):
        """[summary]
        chek if p and q has same root

        Args:
            int p (int): [description]
            int q (int): [description]

        Returns:
            bool: [description]
        """
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        """
        change root of p to point of root q
        (depth of p and q array access)
        """
        i = self.root(p)
        j = self.root(q)

        QuickUnion.ids.insert(i, j)
         
        
    
    
# Test case
    
searchUF = QuickUnion(10)
searchUF.union(5,1)
print(searchUF.connected(5,1))