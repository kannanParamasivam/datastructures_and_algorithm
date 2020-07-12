'''
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive.
Multiple occurances of a keyword in a review should be considred as a single mention.
If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
'''

from typing import List
from collections import defaultdict
import heapq
from pprint import pprint as pp


class Solution:

    def get_polular_keywrods(self, reviews: List[str], keywords: List[str], k) -> List[str]:

        if not reviews or not keywords or not k:
            return

        fd = {k.lower(): 0 for k in keywords}

        for review in reviews:

            cur_keywords = set()

            for word in review.split():

                if word.lower() in fd:
                    cur_keywords.add(word.lower())

            for word in cur_keywords:
                fd[word.lower()] += 1

        heap = [(-n, k) for k, n in fd.items() if n > 0]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


sol = Solution()
result = sol.get_polular_keywrods(reviews=["I love anacell Best services; Best services provided by anacell",
                                           "betacellular has great services",
                                           "deltacellular provides much better services than betacellular",
                                           "cetracular is worse than anacell",
                                           "Betacellular is better than deltacellular."],
                                  keywords=["anacell", "cetracular", "betacellular"],
                                  k=2)

print(result)
