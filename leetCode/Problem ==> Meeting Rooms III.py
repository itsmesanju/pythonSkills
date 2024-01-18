class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Add the meetings into queue and start assigning to the rooms.
        If room not found, update the meeting/start time based on the end time of occupied rooms and try again
        """
        roomCount, roomAvail = [0] * n, [0] * n
        q = deque(sorted(meetings))

        while q:
            #print(f"Finding rooms for meetings: {q}")
            start, end = q.popleft()
            found = False

            for i in range(n):
                #print(f"Checking Room: {i}")
                if roomAvail[i] <= start:
                    #print(f"Room found for {start, end}")
                    found = True
                    roomCount[i] += 1
                    roomAvail[i] = end
                    break

            if not found:
                #print("No room found")
                minDiff = min(roomAvail) - start
                q.appendleft([start + minDiff, end + minDiff])
                #print(f"Preppeding updated time in the queue: {q[0]}")

        return roomCount.index(max(roomCount))
