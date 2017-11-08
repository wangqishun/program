package main

import "fmt"

func findLengthOfLCIS(nums []int) int {
	value, maxValue := 1, 1
	if nums == nil || len(nums) == 0 {
		return 0
	}
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i - 1] {
			value += 1
		} else {
			if maxValue < value {
				maxValue = value
			}
			value = 1
		}
	}
	if maxValue < value {
		maxValue = value
	}
	return maxValue
}

func main(){
	fmt.Println(findLengthOfLCIS([]int{2,2,2,2,2}))
}