package main

import "testing"

func TestPartOne(t *testing.T) {
	pos, depth, answer := part1("example")
	if pos != 15 {
		t.Errorf("Expected hoz. position of 15, but got %v", pos)
	}
	if depth != 10 {
		t.Errorf("Expected depth of 10, but got %v", depth)
	}
	if answer != 150 {
		t.Errorf("Expected answer of 150, but got %v", answer)
	}
}

func TestPartTwo(t *testing.T) {
	pos, depth, answer := part2("example")
	if pos != 15 {
		t.Errorf("Expected hoz. position of 15, but got %v", pos)
	}
	if depth != 60 {
		t.Errorf("Expected depth of 60, but got %v", depth)
	}
	if answer != 900 {
		t.Errorf("Expected answer of 900, but got %v", answer)
	}
}
