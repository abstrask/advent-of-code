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
