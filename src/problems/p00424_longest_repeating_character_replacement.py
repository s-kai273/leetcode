from collections import deque


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        target_ch_list = list(set(s))
        for target in target_ch_list:
            start_i = 0
            replace_index_list = deque()
            for i in range(len(s)):
                ch = s[i]
                if ch != target:
                    replace_index_list.append(i)
                if len(replace_index_list) > k:
                    start_i = replace_index_list.popleft() + 1
                answer = max(answer, i - start_i + 1)
        return answer
