from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enter = deque()
        self.exit = deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.exit.append(x)
        while(len(self.exit) > 1):
            self.enter.append(self.exit.popleft())
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        top = self.exit.popleft()
        while(len(self.enter) > 1):
            self.exit.append(self.enter.popleft())
        self.exit, self.enter = self.enter, self.exit
        return top
        
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.exit[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.exit) == 0 and len(self.enter) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()