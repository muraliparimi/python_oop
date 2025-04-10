from collections import defaultdict
from typing import List
class Solution:
    def get_max_beauty(self, d, q):
        try:
            return max([item for sublist in [beauty for price, beauty in d.items() if price <= q] for item in sublist])
        except ValueError:
            return 0

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        price_beauty_dict = defaultdict(list)
        for item in items:
            price_beauty_dict[item[0]].append(item[1])
        #print(price_beauty_dict)
        res = []
        for query in queries:
            res.append(self.get_max_beauty(price_beauty_dict, query))
        return res
    

if __name__ == '__main__':
    s = Solution()
    items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
    queries = [1,2,3,4,5,6]
    print(s.maximumBeauty(items, queries))
    # d = {1: [2], 3: [2, 5], 2: [4], 5: [6]}
    # print(s.get_max_beauty(d, 3))
    # q=3
    # print("{[beauty for price, beauty in d.items() if price <= q]}")

    