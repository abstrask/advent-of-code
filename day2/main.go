package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {

	// Part One
	_, _, part1Answer := part1("input")
	fmt.Println("Part One:", part1Answer)

}

func part1(filename string) (int, int, int) {

	readFile, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var pos, depth int

	for fileScanner.Scan() {
		i := strings.Split(fileScanner.Text(), " ")
		o := i[0]                    // operation
		d, err := strconv.Atoi(i[1]) // delta
		if err != nil {
			log.Fatal(err)
		}

		switch o {
		case "forward":
			pos += d
		case "down":
			depth += d
		case "up":
			depth -= d
		}
	}

	return pos, depth, pos * depth

}
