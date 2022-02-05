import unittest

class Solution:
    def isBalanced(s):
        stack = []
        d = {')': '(', ']':'[', '}':'{'}
        
        for c in s:
            if not stack:
                stack.append(c)
            elif c not in d:
                stack.append(c)
            elif d[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        if len(stack)==0:
            return 'YES'
        else:
            return 'NO'

class testisBalanced:
    listOfStrings = [
        ('{[()]}', 'YES'), 
        ('{[(])}','NO'), 
        ('{{[[(())]]}}', 'YES'),
        ('{(([])[])[]}', 'YES'),
        ('{(([])[])[]]}', 'NO'),
        ('{(([])[])[]}[]', 'YES')
    ]
    def testisBalanced(self):
        
        for b, expected in self.listOfStrings:
            actual = Solution().isBalanced(b)
            self.assertEqual(actual,expected)
            
if __name__ == '__main__':
    unittest.main()


