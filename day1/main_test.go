package main

import "testing"

func TestPartOne(t *testing.T) {
	example := part1("example")
	if example != 7 {
		t.Errorf("Expected 7 increases, but got %v", example)
	}
}

func TestPartTwo(t *testing.T) {
	example := part2("example")
	if example != 5 {
		t.Errorf("Expected 5 larger sums, but got %v", example)
	}
}
