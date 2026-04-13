class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = []
        for i,num in enumerate(nums):
            if cache ==[]:
                cache.append([1,num])
            else:
                flag = True
                for j in range(len(cache)):
                    if num == cache[j][1]:
                        cache[j][0]+=1
                        flag = False
                if flag:
                    cache.append([1,num])
        
        cache.sort()
        print(cache)
        result = []
        for i in range(1,k+1):
            result.append(cache[-i][1])
        return result
