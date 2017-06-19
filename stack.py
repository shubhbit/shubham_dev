""""
Module for stack Data-Structure
""""

class Stack(object):
    """
        Class for Stack implementation 
    """
    
    def __init__(self):
        """
        Constructure
        """
        self.st = []
        
    def push(self, elem):
        """
        inserting an element into stack
        """
        self.st.append(elem)
    
    def pop(self):
        """
        Poping the last element of the list
        """
        self.st[len(self.st)-1]
    
    def display(self):
        print self.st
        
    if __name__ == "__main__":
        st = Stack()
        st.display()
        st.push(34)
        st.push(67)
        st.display()
        st.pop()
        st.display()
        
