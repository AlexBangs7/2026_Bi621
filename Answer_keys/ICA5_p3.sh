#!/usr/bin/env bash

ls -1 *.fq | while read line;
	do echo $line
	cat $line | wc -l
	cat $line >> all_reads.fastq		##WARNING! Running this script >1x will create a file that is TOO BIG
done
wc -l all_reads.fastq
exit
