class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Compare each interval's start with the previous interval's end
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False  # Overlap found

        return True  # No overlaps
