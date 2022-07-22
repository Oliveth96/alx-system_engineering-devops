#!/usr/bin/env bash
#A Bash script that displays Best School 10 times

printMessage=10
until [ $printMessage -lt 1 ]
do
    echo "best School"
    printMessage=$((printMessage - 1))
done
