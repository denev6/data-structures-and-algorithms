// Reverse Words in a String III

func reverseWords(s string) string {
	words := strings.Split(s, " ")
	for i, word := range words {
		words[i] = reverse(word)
	}
	return strings.Join(words, " ")
}

func reverse(s string) string {
	runes := []rune(s)
	lenStr := len(runes)
	for i := 0; i < lenStr/2; i++ {
		runes[i], runes[lenStr-i-1] = runes[lenStr-i-1], runes[i]
	}
	return string(runes)
}