class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_dict = dict()
        self.cur_mru_key = None
        self.cur_lru_key = None

    def _move_to_latest(self, key):
        if key not in self.lru_dict:
            raise AssertionError(f"invalid key is specified, key: {key}")
        if self.lru_dict[key][1] is None:
            return
        s_lru = self.lru_dict[key]
        s_next_key = s_lru[1]
        s_prev_key = s_lru[2]

        if s_next_key is not None:
            self.lru_dict[s_next_key][2] = s_prev_key
        if s_prev_key is not None:
            self.lru_dict[s_prev_key][1] = s_next_key
        elif s_next_key is not None:
            self.cur_lru_key = s_next_key

        s_lru[1] = None
        s_lru[2] = self.cur_mru_key
        self.lru_dict[self.cur_mru_key][1] = key
        self.cur_mru_key = key

    def get(self, key: int) -> int:
        if key not in self.lru_dict:
            return -1
        self._move_to_latest(key)
        return self.lru_dict[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dict:
            self.lru_dict[key][0] = value
            self._move_to_latest(key)
            return
        if len(self.lru_dict.keys()) == self.capacity:
            if self.capacity == 1:
                del self.lru_dict[self.cur_lru_key]
                self.cur_lru_key = None
                self.cur_mru_key = None
            else:
                next_lru_key = self.lru_dict[self.cur_lru_key][1]
                self.lru_dict[next_lru_key][2] = None
                del self.lru_dict[self.cur_lru_key]
                self.cur_lru_key = next_lru_key
        self.lru_dict[key] = [value, None, self.cur_mru_key]
        prev_mru_key = self.cur_mru_key
        if prev_mru_key is not None:
            self.lru_dict[prev_mru_key][1] = key
        if self.cur_lru_key is None:
            self.cur_lru_key = key
        self.cur_mru_key = key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
