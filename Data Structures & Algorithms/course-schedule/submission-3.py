class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prep_dct = {i:[] for i in range(numCourses)}
        for course, prep in prerequisites:
            prep_dct[course].append(prep)
        
        exploring, completed = set(), set()
        def dfs(course):
            if course in exploring:# detect a loop
                return False
            if course in completed:
                return True
            
            exploring.add(course)
            for prep in prep_dct[course]:
                if not dfs(prep):# any course has a loop
                    return False
            exploring.remove(course)
            completed.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
