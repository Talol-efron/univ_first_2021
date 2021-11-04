#!/bin/zsh
a=1
b=2
c='expr $a+$b'
d="expr $a+$b"
e=`expr $a+$b`
f=`expr $a + $b`
echo c=$c
echo d=$d
echo e=$e
echo f=$f