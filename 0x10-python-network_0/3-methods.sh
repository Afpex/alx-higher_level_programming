#!/bin/bash
# Get the allowed HTTP methods for a given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
