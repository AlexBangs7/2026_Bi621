# BI621 – In-class assignment 3

Download and decompress the following file: 

```/projects/bgmp/shared/Bi621/mouse_C1.concordant_uniq.sam.gz```

Remember, you can use ```scp``` to download files from Talapas:

```
scp <yourDuckID>@login.talapas.uoregon.edu:/absolute/path/to/file/on/Talapas /path/on/your/computer
```

This file contains the alignment data for an RNA-seq experiment in mouse, in the SAM file format.

For questions 1-4, record the *single* command you used. Note that questions build upon one another! Be careful to submit the command you used to answer the question, not the command you used to ensure that your command was working (ex: be sure to replace ```head``` with ```cat```)

**Note**: Leslie's commands leave the file zipped and work on a Mac. For an unzipped file, use ```cat```, or, to leave zipped on a Windows/Linux machine, use ```zcat```.

1.	Extract out the alignment lines (1,000,000 sequences).
    ```
    gzcat mouse_C1.concordant_uniq.sam.gz | grep -v "^@"
    ```
2.	Extract out the QNAME and sequence for each read.
    ```
    gzcat mouse_C1.concordant_uniq.sam.gz | grep -v "^@" | cut -f 1,10
    ```
3.	Construct a ```sed``` expression to match the QNAME and sequence. Use sed to reverse the columns.
    ```bash
    gzcat mouse_C1.concordant_uniq.sam.gz | grep -v "^@" | cut -f 1,10 | sed -E 's/(NS500.+)\t([ACTGN]+)/\2\t\1/'

    #or, even more simply - remember, SIMPLER is BETTER:
    gzcat mouse_C1.concordant_uniq.sam.gz | grep -v "^@" | cut -f 1,10 | sed -E 's/(.+)\t(.+)/\2\t\1/'
    ```
4.	Use ```sed``` (or a combination of `sed` and ```tr```) to convert the two column input into a FASTA file. Capture that output in FASTA file called ```mouse_C1.fasta```.
    ```
    gzcat mouse_C1.concordant_uniq.sam.gz | grep -v "^@" | cut -f 1,10 | sed -E 's/(.+)\t(.+)/>\1\n\2/' > mouse_C1.fasta
    ```
5.	What are the last three FASTA records in the file you created?
    ```
    $ tail -6 mouse_C1.fasta

    >NS500451:154:HWKTMBGXX:1:11210:11578:12578-GACATGAG^CGTTGGAT;0^0
    AGAAGATGCTGTCGCCGAGGAGGAGCGGGAGGAGGACGAGGAAGAGGAGAAACCAAGACCCAAACTTACTG
    >NS500451:154:HWKTMBGXX:1:11210:20863:12591-TCGTCATC^CAACGATC;0^0
    CTTGAGATCAACATCAGATTTGAGCAGGCGCAATACAGAATCTGTGAAATGACAATGTCGCAGCAGAGGAA
    >NS500451:154:HWKTMBGXX:1:11210:20863:12591-TCGTCATC^CAACGATC;0^0
    AGCTTTCTAGTGTCGGTGTGACTCATTACCTGTTACTAAAAACTCAAAGGGAAAAGTGGCATCATCATCTC
    ```

## Challenge problems
6.	Is this a single-end or paired-end experiment? How do you know?
    ```
    Paired-end. Many ways to know: matching read names, RNEXT and PNEXT and TLEN have values.
    ```
Some hints:
1.	Use ```ctrl-v tab``` to get a literal tab on the command line.
2.	The ```tr``` command can replace one single character with another. You could use it to replace the ```|``` character with a new line ```\n``` where ```\n``` will create a newline in the output.
