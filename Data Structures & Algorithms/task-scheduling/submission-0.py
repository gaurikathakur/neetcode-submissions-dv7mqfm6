from collections import deque,Counter
from typing import List
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=Counter(tasks)
        max_heap=[-cnt for cnt in counts. values()]
        heapq.heapify(max_heap)
        time=0
        cool_down=deque()
        while max_heap or cool_down:
            time+=1
            if max_heap:
                rem_count=heapq.heappop(max_heap)+1
                if rem_count<0:
                    cool_down.append((rem_count,time+n))
            if cool_down and cool_down[0][1]==time:
                ready_task_count,_=cool_down.popleft()
                heapq.heappush(max_heap,ready_task_count)
        return time



            


        