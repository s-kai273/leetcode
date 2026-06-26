class TimeMap:
    def __init__(self):
        self.time_dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""
        key_data = self.time_dict[key]
        if timestamp < key_data[0][0]:
            return ""
        if timestamp >= key_data[-1][0]:
            return key_data[-1][1]
        left = 0
        right = len(key_data) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if key_data[mid][0] > timestamp:
                right = mid
            else:
                left = mid
        return (
            key_data[right][1] if timestamp == key_data[right][0] else key_data[left][1]
        )


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
