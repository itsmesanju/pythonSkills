class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        """
        The algorithm calculates the minimum number of semesters required to complete all courses given prerequisite relations.
        It iteratively filters relations based on available courses, checks for unfulfilled prerequisites, updates the set of available courses, and increments the semester count until all courses are taken or it's not possible to proceed. 
        
        If all courses can be taken, the algorithm returns the minimum number of semesters; otherwise, it returns -1.
        """
        courses = set(range(1, n+1))
        count = 0

        while relations:
            filtered_relations = []

            for x, y in relations:
                if x in courses:
                    filtered_relations.append([x, y])
            relations = filtered_relations

            reqs = set()
            for x, y in filtered_relations:
                reqs.add(y)

            #calculates the symmetric difference, which is the set of elements that are in either of the sets, but not in both.
            if not courses ^ reqs:
                return -1
            courses = reqs
            count += 1

        return count
