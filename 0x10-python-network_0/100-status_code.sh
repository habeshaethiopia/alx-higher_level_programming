#!/bin/bash
#displays only the status code of the response.
curl -s -I -L "$1" | grep HTTP | cut -d " " -f2
