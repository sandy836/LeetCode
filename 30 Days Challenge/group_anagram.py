class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _hash = dict()
        for s in strs:
            sorted_string = self.create_sorted_string(s)
            if sorted_string in _hash:
                _hash[sorted_string].append(s)
            else:
                _hash[sorted_string] = [s]
        return _hash.values()
    
    
    def create_sorted_string(self, s):
        return ''.join(sorted(s))