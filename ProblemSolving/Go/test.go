package main

import (
	"fmt"
	"math"
	"os"
)

func main() {
	fmt.Print("Enter a number: ")
	var f float64
	_, err := fmt.Scan(&f)
	if err != nil {
		fmt.Println("Your entry could not be parsed as a valid number.")
		os.Exit(1)
	}
	if f < math.MinInt64 || f > math.MaxInt64 {
		fmt.Println("Your number is too large to be truncated")
		os.Exit(1)
	}
	fmt.Printf("Your truncated number: %d", int64(f))
}