from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       res = defaultdict(list)
       for word in strs:
           key = ''.join(sorted(word))
           res[key].append(word)
       return list(res.values())

if __name__ == '__main__':
    anagram_finder = Solution()
    res = anagram_finder.groupAnagrams(["act","pots","tops","cat","stop","hat"])
    print(res)

        