#!/bin/bash

# Set Git username and token for authentication
GITHUB_USERNAME="MUSTAFA892"
GITHUB_TOKEN="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"

# Push the committed changes to the remote repository
git push https://$GITHUB_USERNAME:$GITHUB_TOKEN@$(git config --get remote.origin.url | sed 's/https:\/\///') 

