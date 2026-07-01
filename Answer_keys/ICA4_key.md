# BI621 – In-class assignment 4

For each question, be sure to include the command used to generate the answer (if applicable).

Download and decompress the following file from HPC:
```
trimmed_reads.fq.gz
```
1.	Determine the length distribution of the trimmed reads (you should be able to do parts i-iii using one line).
    1.	Extract the sequence
    2.	Measure its length
    3.	Compute the distribution of lengths
    ```
    gzcat trimmed_reads.fq.gz | grep -A 1 "^@unbarcoded" | grep -v "^@unbarcoded" | grep -v "^--" | awk '{print length($1)}' | sort -n | uniq -c
    ```
2.	Use your favorite plotting software to plot the distribution of read lengths. What do you conclude from this plot?
![Read lengths plot](../images/ICA4_plot.jpg)

    This plot shows that most reads were not trimmed. Note that plotting on a log scale is not helpful to iterpret the data here. Plots should be have titles and axes labeled. Additionally, Leslie speculates that the lack of read lengths between 86-99 bases suggests that reads needed to have at least 25 bases of adapter sequence present in order to trim, and that the reads were not trimmed based on qscores.

Download the following files from HPC:
```
mouseSaline1_fw.genecount
mouseSaline1_rv.genecount
```
3.	Determine the percentage of reads that mapped to a feature (gene).
    1.	Sum the number of reads that mapped to a feature. (one line command)
    2.	Calculate the total number of reads. (one line command)
    3.	Divide by the number of mapping reads by the total number of reads. (feel free to use a calculator)
    4.	*CHALLENGE* – Condense as many parts as possible to a single line command.
    ```
    $ cat mouseSaline1_fw.genecount | awk '$1~"ENSMUS" {sum += $2} $1~"__" {count += $2} END {print "reads mapped:\t" sum;print "total reads:\t" count+sum;print "% reads mapped:\t"sum/(sum+count)*100"%"}'
    reads mapped:	894086
    total reads:	19177391
    % reads mapped:	4.66219%

    $ cat mouseSaline1_rv.genecount | awk '$1~"ENSMUS" {sum += $2} $1~"__" {count += $2} END {print "reads mapped:\t" sum;print "total reads:\t" count+sum;print "% reads mapped:\t"sum/(sum+count)*100"%"}'
    reads mapped:	14442057
    total reads:	19177391
    % reads mapped:	75.3077%
    ```
4.	Which file had more reads mapping to features?
    ```
    The "reverse" file had more reads mapping to features.
    ```
5.	*CHALLENGE* – What do you hypothesize the difference between the ```fw``` and the ```rv``` file is? (hint: the program used to generate these files is called ```htseq-count```)

    The difference between the two files is due to the strandedness parameter. For paired-end reads, if ```--stranded=yes``` when ```htseq-count``` is run, then the first read must map to the same strand as the feature and the second read has to map to the opposite strand. Reads have to be in the same orientation as the feature. If ```--stranded=reversed```, then the second read has to map to the same strand as the feature and the first read has to map to the opposite strand. Depending on how the library was prepared (i.e. which reads map to which strands, template or opposite), these two ```--stranded``` settings greatly affect the number of mapped reads.
