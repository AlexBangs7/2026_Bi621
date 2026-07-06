#!/usr/bin/env bash

ls -1 *.genecount | while read line;
	do echo $line
	cat $line | grep "ENSMUSG00000020848"
done
exit
