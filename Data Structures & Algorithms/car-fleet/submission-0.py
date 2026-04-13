class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0]*n

        for i in range(n):
            time[i]=(target-position[i])/speed[i]
        
        mem = []
        for i, pos in enumerate(position):
            mem.append([pos, time[i]])
        mem = sorted(mem, reverse=True)
        
        res = 1
        prev_t = mem[0][1]
        for tp in mem:
            if tp[1]<=prev_t:
                continue
            else:
                res+=1
            prev_t = tp[1]
        return res

