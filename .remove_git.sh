#!/bin/sh

read -p "Remove .git directory? (y/n) " answer

if [ $answer = "y" ]; then
    echo "Removing .git directory .."
    rm -rf .git
    if [ $? -eq 0 ]; then
        echo "Removed"
    else
        echo "Error removing .git directory"
    fi
else
    echo "Aborted"
fi
