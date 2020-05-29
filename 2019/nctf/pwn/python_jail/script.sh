#!/bin/sh

while true
do 
  read lol
  echo $lol | nc prob.vulnerable.kr 20001
done
