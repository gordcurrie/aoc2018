package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"time"
)

var (
	vals  []int
	val   int  = 0
	loop  int  = 0
	found bool = false
	data  []int
)

func main() {
	start := time.Now()
	file, err := os.Open("data.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		data = append(data, i)
	}

	for !found {
		for _, v := range data {
			val = val + v
			if contains(val, vals) {
				fmt.Println(time.Since(start))
				log.Fatal(val)
			}
			vals = append(vals, val)
		}
	}
}

func contains(val int, vals []int) bool {
	for _, v := range vals {
		if v == val {
			return true
		}
	}
	return false
}
