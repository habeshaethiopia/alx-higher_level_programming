#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
curl -s -L -X GET "$1?X-School-User-Id=98" 
