class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by their start time
        intervals.sort()

        # Initialize result list
        merged_intervals = []

        # Initialize current interval with the first interval
        current_start, current_end = intervals[0]

        # Iterate through remaining intervals
        for interval_start, interval_end in intervals[1:]:
            # Check if current interval and next interval don't overlap
            if current_end < interval_start:
                # No overlap, add current interval to result
                merged_intervals.append([current_start, current_end])
                # Update current interval to the new interval
                current_start, current_end = interval_start, interval_end
            else:
                # Intervals overlap, merge them by extending the end time
                current_end = max(current_end, interval_end)

        # Add the last interval to result
        merged_intervals.append([current_start, current_end])

        return merged_intervals 