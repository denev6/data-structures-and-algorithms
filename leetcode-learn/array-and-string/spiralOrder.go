func spiralOrder(matrix [][]int) []int {
	nRow := len(matrix)
	nCol := len(matrix[0])
	ans := make([]int, nRow*nCol)

	// init
	firstRow := 0
	firstCol := 0
	lastRow := nRow - 1
	lastCol := nCol - 1

	row := 0
	col := 0

	// move right at first
	dRow := 0
	dCol := 1

	for i := 0; i < len(ans); i++ {
		ans[i] = matrix[row][col]

		row += dRow
		col += dCol

		// out-of-bound
		if row > lastRow { // bottom
			dRow = 0
			dCol = -1
			row--
			col--
			lastCol--
		}
		if col > lastCol { // right
			dRow = 1
			dCol = 0
			row++
			col--
			firstRow++
		}
		if row < firstRow { // top
			dRow = 0
			dCol = 1
			row++
			col++
			firstCol++
		}
		if col < firstCol { // left
			dRow = -1
			dCol = 0
			row--
			col++
			lastRow--
		}
	}
	return ans
}