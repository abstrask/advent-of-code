package main

import "testing"

func TestPartOne(t *testing.T) {
	g, e, p := part1("example")
	if g != 22 {
		t.Errorf("Expected gamma rate of 22, but got %v", g)
	}
	if e != 9 {
		t.Errorf("Expected epsilon rate of 9, but got %v", e)
	}
	if p != 198 {
		t.Errorf("Expected power consumption of 198, but got %v", p)
	}
}
