class StackOverflowException(Exception):
    """自定义一个栈溢出异常"""
    pass

class StackEmptyException(Exception):
    """自定义一个栈空出异常"""
    pass

class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit
        
    def push(self, element):
        """进栈，向栈压入一个元素"""
        if len(self.stack) >= self.limit:
            raise StackOverflowException("Stack Overflow Exception")
        else:
            self.stack.append(element)
    
    def pop(self):
        """退栈，从栈中弹出一个元素"""
        if self.stack:
            self.stack.pop()
        else:
            raise StackEmptyException("Stack Empty Exception")
    
    def is_empty(self):
        """判断栈是否为空"""
        return not bool(self.stack)
    
    def peek(self):
        """查看栈顶元素"""
        if self.stack:
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        """查看栈的大小"""
        return len(self.stack)
    
    def clear(self):
        """清空栈中的元素"""
        self.stack = []
    
    def __str__(self):
        return "<Stack>" + str(self.stack)