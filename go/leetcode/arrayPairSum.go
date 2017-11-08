package main

import (
	"sort"
	"fmt"
)

func findComplement(num int) int {
	return ^num + 1
}

func sum(num []int) int {
	s := 0
	for i:=0; i < len(num); i+=2 {
		s += num[i]
	}
	return s
}

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	return sum(nums)
}

func main() {
	nums:= []int{1,4,3,2}
	fmt.Print(arrayPairSum(nums))
	fmt.Print(findComplement(1))
	fmt.Printf("nums:%v", nums)
}