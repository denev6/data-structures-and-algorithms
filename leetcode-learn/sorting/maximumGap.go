// You must write an algorithm
// that runs in linear time and uses linear extra space.

func maximumGap(nums []int) int {
	if len(nums) == 1 {
		return 0
	}

	// Counting Sort: O(N)
	maxValue := slices.Max(nums)
	shift := slices.Min(nums)
	count := make([]int, maxValue-shift+1)
	for _, n := range nums {
		count[n-shift] += 1
	}
	// find max diff
	maxDiff := 0
	prev := shift
	for n, c := range count {
		if c == 0 {
			continue
		}
		diff := n - prev
		if diff > maxDiff {
			maxDiff = diff
		}
		prev = n
	}
	return maxDiff
} // -> fatal error: runtime: out of memory