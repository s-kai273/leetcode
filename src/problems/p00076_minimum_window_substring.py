from collections import deque


class Solution:
    def contains_all_ch(self, window_dict, s_dict) -> bool:
        for key in s_dict.keys():
            if key not in window_dict or window_dict[key] < s_dict[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_count_dict = dict()
        for i in range(len(t)):
            ch = t[i]
            t_count_dict[ch] = t_count_dict.get(ch, 0) + 1
        left = 0
        while left < len(s) and s[left] not in t_count_dict:
            left += 1
            if left == len(s):
                return ""
        pos_list = deque()
        pos_list.append(left)
        window_count_dict = dict()
        window_count_dict[s[left]] = window_count_dict.get(s[left], 0) + 1
        if self.contains_all_ch(window_count_dict, t_count_dict):
            return s[left]
        right = left + 1
        while right < len(s):
            ch = s[right]
            if ch in t_count_dict:
                pos_list.append(right)
                window_count_dict[ch] = window_count_dict.get(ch, 0) + 1
            if self.contains_all_ch(window_count_dict, t_count_dict):
                break
            right += 1
        if not self.contains_all_ch(window_count_dict, t_count_dict):
            return ""
        min_s_pointers = (left, right)

        while self.contains_all_ch(window_count_dict, t_count_dict):
            if right - left < min_s_pointers[1] - min_s_pointers[0]:
                min_s_pointers = (left, right)
            window_count_dict[s[left]] -= 1
            pos_list.popleft()
            left = pos_list[0]

        right += 1
        while right < len(s):
            ch = s[right]
            if ch in t_count_dict:
                pos_list.append(right)
                window_count_dict[ch] = window_count_dict.get(ch, 0) + 1
            if self.contains_all_ch(window_count_dict, t_count_dict):
                if right - left < min_s_pointers[1] - min_s_pointers[0]:
                    min_s_pointers = (left, right)
                while self.contains_all_ch(window_count_dict, t_count_dict):
                    if right - left < min_s_pointers[1] - min_s_pointers[0]:
                        min_s_pointers = (left, right)
                    window_count_dict[s[left]] -= 1
                    pos_list.popleft()
                    left = pos_list[0]

            right += 1
        return s[min_s_pointers[0] : min_s_pointers[1] + 1]
