package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	// Part One
	fmt.Println("Part One:", part1("input"))

	// Part Two
	fmt.Println("Part Two:", part2("input"))

}

func part1(filename string) int {

	readFile, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var previous, current, increases int

	for fileScanner.Scan() {
		current, err = strconv.Atoi(fileScanner.Text())
		if err != nil {
			log.Fatal(err)
		}
		if previous > 0 {
			if current > previous {
				increases++
			}
		}
		previous = current
	}

	return increases

}

func part2(filename string) int {

	readFile, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	// Sliding window of 3
	var sw [3]int
	var cv, ps, i, increases int

	for fileScanner.Scan() {
		cv, err = strconv.Atoi(fileScanner.Text())
		if err != nil {
			log.Fatal(err)
		}

		// Store current value in next place in the sw array
		index := i % len(sw)
		sw[index] = cv

		// Calculate current sum of sw, if this is 3rd number or greater
		cs := 0
		if i >= 2 {
			for _, v := range sw {
				cs += v
			}

			// If previous sum is registered, and current sum is higher, increment increases
			if ps > 0 {
				if cs > ps {
					increases++
				}
			}

			ps = cs

		}

		i++

	}

	return increases

}
