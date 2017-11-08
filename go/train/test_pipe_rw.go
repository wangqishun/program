package main

import (
	"fmt"
	"time"
	_ "io"
	"os"
)

func main() {
	reader, writer, _ := os.Pipe()
	defer reader.Close()
	defer writer.Close()
	tickerWriter := time.NewTicker(time.Millisecond * 500)
	tickerReader := time.NewTicker(time.Millisecond * 700)
	go func(){
		for {
			for t := range tickerWriter.C {
				writer.Write([]byte(t.String()))
			}
		}
	} ()
	go func(){
		for {
			for range tickerReader.C {
				for {
					var buffer = make([]byte, 100)
					n, _ := reader.Read(buffer)
					fmt.Println(string(buffer[:n]))
				}
			}
		}
	} ()

	time.Sleep(time.Minute)
	tickerReader.Stop()
	tickerWriter.Stop()
}
