#!/bin/zsh
arg1=$1
arg2=$2
echo "arg1=$arg1, arg2=$arg2"
if [ $arg1 -lt $arg2 ]; then
    echo "arg1 < arg2"
elif [ $arg1 -eq $arg2 ]; then
    echo "arg1 = arg2"
else
    echo "arg1 > arg2"
fi