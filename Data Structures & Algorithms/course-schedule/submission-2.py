class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crspreq={i: [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            crspreq[crs].append(preq)

        visiting=set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crspreq[crs]==[]:
                return True
            visiting.add(crs)

            for preq in crspreq[crs]:
                if not dfs(preq):
                    return False
            visiting.remove(crs)
            crspreq[crs]=[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True