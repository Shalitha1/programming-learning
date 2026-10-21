// fmt.Println(lengthOfLongestSubstring("abcabcbb")) // 3
package main

import "fmt"

func main() {
	fmt.Println(lengthOfLongestSubstring("abxcabcbb"))
}

func lengthOfLongestSubstring(s string) int {
	left := 0
	maxLength := 0
	seen := make(map[byte]bool)

	for right := 0; right < len(s); right++ {
		for seen[s[right]] {
			delete(seen, s[left])
			left++
		}

		seen[s[right]] = true

		currentLength := right - left + 1
		if currentLength > maxLength {
			maxLength = currentLength
		}
	}

	return maxLength

}
