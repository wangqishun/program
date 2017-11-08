package main

import "fmt"

func findMaxConsecutiveOnes(nums []int) int {
	value, maxValue := 0, 0
	if nums == nil || len(nums) == 0 {
		return 0
	}
	for _,val := range nums {
		if val == 1 {
			value += 1
		} else {
			if maxValue < value {
				maxValue = value
			}
			value = 0
		}
	}
	if maxValue < value {
		maxValue = value
	}
	return maxValue
}

func main() {
	fmt.Println(findMaxConsecutiveOnes([]int{}))
}
