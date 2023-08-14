#!/bin/bash
echo "# This file lists all AirBnB Clone Authors of this repository \n
To generate or add new list of authors use generateAUTHORS.sh file" > AUTHORS
echo >> AUTHORS


git log --format="%aN <%aE>" | sort -uf >> AUTHORS
