class Solution:
    def countElements(self, arr: List[int]) -> int:
        element_count = dict()
        count = 0
        for num in arr:
            element_count[num] = element_count.get(num, 0)+1
        
        for ele, occur in element_count.items():
            if ele+1 in element_count.keys():
                count += occur
        return count