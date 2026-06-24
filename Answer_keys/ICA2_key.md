# BI621 – In-class assignment 2

For each of the following questions, provide the **single command** you used to generate the answers. Be sure to use triple backticks 
(\`\`\`) to set off code. You can find more about GitHub Flavored Markdown here: https://help.github.com/articles/basic-writing-and-formatting-syntax/

You should use the file ```s_1_sequence.fastq``` found in this repository. Be sure to unzip it first (```gunzip s_1_sequence.fastq.gz```). This is a FASTQ file that contains Illumina sequencing reads where the first 5 nucleotides of the sequence are the inline barcode.

NOTE! The correct result from each command is included in the question. If your command does not yeild the correct answer, you should re-consider the command you are using.

1.	Count the number of raw reads (answer: 250,000).
    ```
    wc -l s_1_sequence.fastq                       #and "manually" divide answer by 4
    cat s_1_sequence.fastq | grep ^@HWI | wc -l    #better answer
    ```

    Note that:

    ```cat s_1_sequence.fastq | grep ^@ | wc -l```

    will NOT work!

    <details><summary>WHY???</summary>
    <p>

    Because simply searching for `@` at the beginning of a line will also return qscore lines.


    </p>
    </details>

2.	Count the number of reads with barcode CGATA (answer: 19,501).
    ```
    grep "^CGATA" s_1_sequence.fastq | wc -l     #note that ^ is critical here, we want so search for CGATA at the BEGINNING of sequences, not just anywhere
    ```
3.	Capture all FASTQ records for the barcode ACCAT into a file called sample_01.fq (you should get a file with 18,352 records and 73,408 lines). Report the command used to generate this file AND the command(s) used to confirm the file is of the expected length.
    ```
    grep -A 2 -B 1 "^ACCAT" s_1_sequence.fastq | grep -v "^--" > sample_01.fq     #Remember to capture RECORDS, not just reads

    wc -l sample_01.fq              #Should confirm 73,408 lines
    grep -c "^HWI" sample_01.fq     #Should confirm 18,352 records
    ```
4.	Determine the count of all barcodes in the file.
    ```
    cat s_1_sequence.fastq | grep -A 1 "^@HWI" | grep -v ^@ | grep -v ^-- | cut -c 1-5 | sort | uniq -c | sort -n
    # (or similar, but must include -n or -g in the last sort)
    ```

**Challenge** - What encoding, Phred+33 or Phred+64, is used for the quality scores in this file? How do you know?

<details><summary>Phred+33, click for explanation</summary>

Adapted from https://en.wikipedia.org/wiki/FASTQ_format#Encoding
```
  SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS................................
  .................................JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
  LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL...............................
  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghi
  |                         |    |        |                              |
 33                        59   64       73                            104
  0........................26...31.......40                                
                                    3.....9..............................41 
  0.2......................26...31........41                              

 S - Sanger        Phred+33,  raw reads typically (0, 40)
 J - Illumina 1.5+ Phred+64,  raw reads typically (3, 41)
     with 0=unused, 1=unused, 2=Read Segment Quality Control Indicator (bold) 
     (Note: See discussion above).
 L - Illumina 1.8+ Phred+33,  raw reads typically (0, 41)
```
Looking at an example qscore line from the file (`BBBBBBBB####################################################`) we see that it contains `#`, which can only be Phred+33.
</details>

**Challenge** - What barcodes were actually used when creating this sequencing library? How do you know? Where do the other "barcodes" come from?

There are probably 14 barcodes that were used to create this sequencing library. They are:
```
7900 TCAGA
10659 ACTGC
10931 TGACC
11536 GAGAT
11871 CTGAA
14409 CGGCG
14508 TGGTT
18226 GAAGC
18352 ACCAT
18375 TCGAG
19501 CGATA
23012 AATTT
26336 GCATT
31136 CTAGG
```

Note there is >25x drop to the next most abundant "barcode" (`286 CTAGT`). These barcodes are most likely
- sequencing error in true barcodes
- PhiX spike in ([more info](https://www.illumina.com/content/dam/illumina-marketing/documents/products/technotes/hiseq-phix-control-v3-technical-note.pdf))

Some hints:
1.	Commands we have learned so far: `ls`, `man`, `more`, `less`, `cat`, `wc`, `head`, `cut`, `grep`, `sort`, `uniq`, `>`, `|`
2.	Use head when building a command, cat once the command is working
3.	Look at the `-n` option for the head command, the `-l` option for `wc`
4.	The `^` character means “must occur at the beginning of line” in a grep search
5.	Look at the grep options: `-c`, `-v`, `-A`, `-B`
6.	Read the `man` pages for `sort` and `uniq` to learn how to combine them
