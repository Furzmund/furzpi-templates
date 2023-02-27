#!/bin/sh

read -p "Remove .git directory? (y/n) " answer

if [ $answer = "y" ]; then
    echo "Removing .git directory .."
    rm -rf .git
    if [ $? -eq 0 ]; then
        echo "Removed"
        exit 0
    else
        echo "Error removing .git directory"
        exit 1
    fi
else
    echo "Aborted"
    exit 1
fi
