#!/bin/bash
# Get the allowed HTTP methods for a given URL
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | awk '{print $2}'
