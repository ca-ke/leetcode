class Solution:
    def newspapers_split(
        self, newspaper_read_times: list[int], num_coworkers: int
    ) -> int:
        low, high = max(newspaper_read_times), sum(newspaper_read_times)
        ans = -1

        def feasible(
            newspaper_read_times: list[int], num_coworkers: int, limit: int
        ) -> bool:
            time, num_workers = 0, 0
            for read_time in newspaper_read_times:
                if time + read_time > limit:
                    time = 0
                    num_workers += 1
                time += read_time

            if time != 0:
                num_workers += 1

            return num_workers <= num_coworkers

        while low <= high:
            mid = (low + high) // 2
            if feasible(newspaper_read_times, num_coworkers, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
