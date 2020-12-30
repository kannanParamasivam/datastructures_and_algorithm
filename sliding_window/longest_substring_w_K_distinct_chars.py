from collections import defaultdict
from typing import List
from math import inf



class Solution:


    def longest_substring_w_k_distinct_chars(self, S: str, K: int) -> int:

        if not S or not K:
            return -1

        window_start = 0
        char_freq = defaultdict(int)
        max_len = -inf

        for window_end in range(len(S)):

            char_freq[S[window_end]] += 1

            if len(char_freq) <= K:
                max_len = max(max_len, window_end - window_start + 1)

            while len(char_freq) > K:
                char_freq[S[window_start]] -= 1

                if char_freq[S[window_start]] <= 0:
                    del char_freq[S[window_start]]

                window_start += 1

        return max_len


sol = Solution()
print(sol.longest_substring_w_k_distinct_chars('araaci', 2))
print(sol.longest_substring_w_k_distinct_chars('cbbebi', 3))


        

        

