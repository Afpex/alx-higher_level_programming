#!/bin/bash
# Takes a URL, sends a request to it & displays the size of the response
curl -s "$1" | wc -c
