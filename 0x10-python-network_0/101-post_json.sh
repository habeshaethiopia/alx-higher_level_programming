#!/bin/bash
#send JSON post request
curl -s -X POST -H "content-type: application/json" -d @"$2" $1
