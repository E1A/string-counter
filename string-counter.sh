#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi
 
tr ' ' '\n' < "$1" | sort | uniq -c | sort -nr | head
