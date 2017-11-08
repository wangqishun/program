package main

import "fmt"

type MagicDictionary struct {
	m_dic map[int][]string
}


/** Initialize your data structure here. */
func Constructor() MagicDictionary {
	dic := MagicDictionary{}
	dic.m_dic = make(map[int][]string)
	return dic
}


/** Build a dictionary through a list of words */
func (this *MagicDictionary) BuildDict(dict []string)  {
	for _, str := range dict {
		this.m_dic[len(str)] = append(this.m_dic[len(str)], str)
	}
}

func isTwoStringSimilar(str1 string, str2 string) bool {
	chance := 1
	for i:=0; i < len(str1); i++ {
		if str1[i] != str2[i] {
			if chance == 0 {
				return false
			}
			chance --
		}
	}
	if chance == 1 {
		return false
	}
	return true
}

/** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
func (this *MagicDictionary) Search(word string) bool {
	strs, isFind := this.m_dic[len(word)]
	if !isFind{
		return false
	}
	for _, str := range(strs) {
		if isTwoStringSimilar(str, word) {
			return true
		}
	}
	return false
}

func main() {
	dict := []string{"hello", "leetcode"}
	word := "hhllo"
	obj := Constructor();
	obj.BuildDict(dict);
	param := obj.Search(word);
	fmt.Println(param)
}
/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dict);
 * param_2 := obj.Search(word);
 */
