package main

import (
	"os/exec"
	"fmt"
	_ "io"
	_ "bytes"
	"bufio"
	"io"
)

func main() {
	cmdO := exec.Command("echo", "-n", "My First command. \n Hello world")
	stdoutO, err := cmdO.StdoutPipe();
	if err != nil {
		fmt.Println("error occurs: ", err)
		return
	}
	if err := cmdO.Start(); err != nil {
		fmt.Println("error occurs: ", err)
		return
	}
	/*
	var buffer bytes.Buffer
	for {
		outputO := make([]byte, 5)
		n, err := stdoutO.Read(outputO);
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println("error occurs: ", err)
			return
		}
		if n > 0 {
			buffer.Write(outputO[:n])
		}
	}
	fmt.Println(buffer.String())
	*/
	buffer := bufio.NewReader(stdoutO)
	for {
		outputO, _, err := buffer.ReadLine()
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println("error occurs: ", err)
			return
		}
		fmt.Println(string(outputO))
	}

}