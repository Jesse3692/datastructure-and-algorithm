# 数据结构与算法

数据结构（data structure）是计算机存储、组织数据的方式。数据结构是指相互之间存在一种或者多种特定关系的数据元素的集合。

算法（Algorithm）是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令，算法代表着用系统的方法描述解决问题的策略机制。

程序是一组计算机能够识别和执行的指令，可以简单的理解为程序 = 数据结构 + 算法



**为什么学习数据结构？**

数据结构所表现的是：如何对现实问题进行建模，并且采用合适的算法高效解决问题。这是一种计算思维，与语言无关，与工具无关，它是我们从现实世界走向计算机世界的桥梁。

## 常用的数据结构

### 1. 栈

栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。



![栈](.\static\img\stack.png)

栈允许进行插入和删除操作的一端称为栈顶(top)，另一端称为栈底（bottom）；栈底固定，而栈顶浮动；栈中元素个数为零时称为空栈。插入一般称为进栈（push），删除则称为退栈（pop）。

由于堆叠数据结构只允许在一端进行操作，因而按照后进先出（LIFO，Last In First Out）的原理运作。栈也称为后进先出表。

**复杂度分析**：

栈属于常见的一种线性结构，对于进栈和退栈而言，时间复杂度都为O(1)。

**主要代码实现：**

```python
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
```

**其他功能实现：**

```python
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
```

**完整代码：**

[数据结构-栈](./Stack.py)

**栈的应用：**

![栈的应用](.\static\img\{A0096DD1-8162-486B-B4FE-F904C726835D}_20200423152344.jpg)

**括号匹配：**

> **有效括号字符串**需满足：
>
> - 左括号必须用相同类型的右括号闭合。
> - 左括号必须以正确的顺序闭合。
> - 注意空字符串可被认为是有效字符串。
>
> **举例：**
>
> ((())): True
>
> ((()): False
>
> (())): False
>
> **目标：**
>
> 1. 使用一个堆栈作为数据结构
> 2. 来检查括号字符串是否完全匹配

**主要代码实现：**

```python
def balanced_parentheses(parentheses):
    limit = len(parentheses)
    stack = Stack(limit=limit)
    for i in parentheses:
        if i == '(':
            # 如果是左括号则进栈
            stack.push(i)
        elif i == ')':
            # 如果是右括号则退栈
            if not stack.is_empty():
                stack.pop()
            else:
                return False
    else:
        return True
```

**完整代码：**[栈的应用-括号匹配](.\exercises\balanced_parentheses.py)

**算法思想：**

判断一个表达式的”(“和”）”是否匹配，思路是这样的：遇到”（“则入栈，遇到”）”则从栈顶弹出”（“与之配成一对，当整个表达式扫描完毕时：

（1） 若栈内为空，则说明（与）是匹配的。

（2） 若表达式扫描完毕，栈内仍有（则说明左括号是多的。

（3） 若当）被扫描到，栈里却没有（能弹出了，说明）多，表达式中）也是多的。

