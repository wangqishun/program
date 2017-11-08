package main

import (
	"os"
	"syscall"
	"os/signal"
	"fmt"
)

func handleSignal() {
	recv := make(chan os.Signal)
	signal.Notify(recv, syscall.SIGINT, syscall.SIGQUIT)
	for sig := range recv{
		fmt.Println("recv signal: ", sig)
	}
}

func main() {
	handleSignal()
}
