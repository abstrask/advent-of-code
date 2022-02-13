package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	// Part One
	_, _, part1Answer := part1("example")
	fmt.Println("Part One:", part1Answer)
}

func part1(filename string) (int, int, int) {
	text := readFile(filename)
	lines := strings.Split(text, "\n")

	bits := []string{}

	// Append each bit to the same position in a string slice, as their position on the input line
	for _, l := range lines {
		for j, c := range l {
			bits[j] += string(c)
		}
	}

	fmt.Println(bits)

	return 1, 1, 1
}

func readFile(filename string) string {
	bs, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(bs)
}
