#!/bin/sh
set -eu
dir="${1}"
file="day${1}"
mkdir -p ${dir}
touch ${dir}/${file}.py
touch ${dir}/input.txt
touch ${dir}/example.txt