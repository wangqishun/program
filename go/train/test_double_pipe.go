package main

import (
	"os/exec"
	"fmt"
	"bytes"
)

func main() {
	cmd1 := exec.Command("ps", "aux")
	cmd2 := exec.Command("grep", "bash")
	var outputBuf1 bytes.Buffer
	cmd1.Stdout = & outputBuf1
	if err := cmd1.Start(); err != nil {
		fmt.Println("error occurs: ", err)
		return
	}
	if err := cmd1.Wait(); err != nil {
		fmt.Println("error occurs: ", err)
		return
	}
	cmd2.Stdin = &outputBuf1
	var outputBuf2 bytes.Buffer
	cmd2.Stdout = &outputBuf2
	if err := cmd2.Start(); err != nil {
		fmt.Println("error occurs: ", err)
		return
	}
	if err := cmd2.Wait(); err != nil {
		fmt.Println("error occurs: ", err)
		return
	}
	fmt.Println(outputBuf2.String())
}
