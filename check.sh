#!/bin/bash
for f in $(ls *.jpg); do n=$(md5sum $f | cut -d" " -f 1); echo "$n.jpg $f" >> solution.txt; done
