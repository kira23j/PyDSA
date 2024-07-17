class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        prereqs=defaultdict(list)
        for c , p in prerequisites:
            prereqs[c].append(p)
        def cycle(cource , seen):
            if cource in seen:
                return True
            seen.add(cource)
            for p in prereqs[cource]:
                if cycle(p,seen):
                    return True
            prereqs[cource]=[]
            seen.remove(cource)
            return False
        seen=set()
        for cource in range(numCourses):
            if cycle(cource ,seen):
                return False
        return True
        