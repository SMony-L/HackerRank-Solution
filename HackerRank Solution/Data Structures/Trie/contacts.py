import unittest 
from typing import List

class trieNode:
    def __init__(self):
        self.endOfword = False
        self.children = {}
        self.memo = 0

class Solution:
    
    def add(self,trie, word):
        cursor = trie
        for letter in word:
            if cursor.children.get(letter) is None:
                cursor.children[letter] = trieNode()
            cursor = cursor.children[letter]
            cursor.memo += 1
            
    def find(self,trie,partial):
        cursor = trie
        for letter in partial:
            cursor = cursor.children.get(letter)
            if cursor is None:
                return 0
    
        return cursor.memo
    
    def contacts(self, queries: List[List[int]]) -> List[int]:
    
        # first attemp solution failed a few test cases
        # L = []
        # counterL = []
        # count = 0
        # for i in q:
        #     if i[0] == 'add':
        #         L.append(i[1])
                
        #     elif i[0] == 'find':
        #         substr = i[1]
        #         subLen = len(substr)
                
        #         for j in range(len(L)):
        #             if substr == L[j][:subLen]:
        #                 count +=1 
        #             else:
        #                 continue
        #         counterL.append(count)
        #         count = 0
        
        # return counterL

        # Optimization with a Trie & memoization
        contactList = trieNode()
        countList = []
        for queryType, queryValue in queries:
            if queryType == 'add':
                self.add(contactList, queryValue)
            else:
                count = self.find(contactList, queryValue)
                countList.append(count)
        return countList

class testContacts(unittest.TestCase):
    queries = [
        ([['add', 'ed'], ['add', 'eddie'], ['add', 'edward'], ['find', 'ed'], ['add', 'edwina'], ['find', 'edw'], ['find', 'a']],[3,2,0]),
        ([['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']], [2,0])
    ]
    def testContacts(self):
        for i, expected in self.queries:
            actual = Solution().contacts(i)
            self.assertEqual(actual,expected)
            
if __name__ == '__main__':
    unittest.main()