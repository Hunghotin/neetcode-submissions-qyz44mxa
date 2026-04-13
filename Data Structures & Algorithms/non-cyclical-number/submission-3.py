class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        n_str = str(n)
        fast = 0
        for s in n_str:
            fast+=int(s)**2

        while slow!=fast:
            fast_str = str(fast)
            fast = 0
            for s in fast_str:
                fast+=int(s)**2
            
            fast_str = str(fast)
            fast = 0
            for s in fast_str:
                fast+=int(s)**2

            slow_str = str(slow)
            slow = 0
            for s in slow_str:
                slow+=int(s)**2
        return True if fast==1 else False
            
