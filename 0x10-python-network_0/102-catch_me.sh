#!/bin/bash
# causes the server to respond with a message containing You got me!
curl -s -d "You got me!" http://0.0.0.0:5000/catch_me
