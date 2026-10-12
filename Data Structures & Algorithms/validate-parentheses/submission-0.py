class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True

        valid = {
            "]": "[", 
            ")": "(",
            "}": "{"
        }

        stack = Stack()

        # test it
        stack.push("1")
        assert stack.peek() == "1"
        assert not stack.is_empty()
        top = stack.pop()
        assert top == "1"
        assert stack.is_empty()

        stack.push("2")
        stack.push("3")
        assert "3" == stack.pop()
        assert "2" == stack.pop()
        assert stack.pop() is None
        assert stack.is_empty()


        for char in s:
            if char in ["[", "(", "{"]:
                stack.push(char)
            elif char in ["]", ")", "}"]:
                top = stack.peek()
                if valid[char] == top:
                    stack.pop()
                else:
                    return False
            else:
                raise Exception("invalid input")

        # Finally
        if stack.is_empty():
            return True

        return False


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def is_empty(self):
        if len(self.stack) == 0:
            return True

        return False
    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]
    def pop(self):
        if self.is_empty():
            return None
        top = self.stack.pop()
        return top

