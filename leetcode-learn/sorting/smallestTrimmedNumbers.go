func smallestTrimmedNumbers(nums []string, queries [][]int) []int {
	// format as {trim: [(i, k)...]}
	lenItem := len(nums[0])
	kIdxs := make([][][]int, lenItem+1)
	for i, q := range queries {
		k, trim := q[0], q[1]
		kIdxs[trim] = append(kIdxs[trim], []int{i, k})
	}
	// init index(nums pointer)
	numsIdx := make([]int, len(nums))
	for i, _ := range numsIdx {
		numsIdx[i] = i
	}
	// find index
	ans := make([]int, len(queries))
	for trim, iks := range kIdxs {
		if trim == 0 {
			continue
		} // empty
		numsIdx = radixSort(nums, numsIdx, trim)
		for _, ik := range iks {
			i, k := ik[0], ik[1]
			ans[i] = numsIdx[k-1]
		}
	}
	return ans
}

func radixSort(nums []string, numsIdx []int, trim int) []int {
	lenItem := len(nums[0])
	unit := lenItem - trim
	sort.SliceStable(numsIdx, func(i, j int) bool {
		return nums[numsIdx[i]][unit] < nums[numsIdx[j]][unit]
	})
	return numsIdx
}