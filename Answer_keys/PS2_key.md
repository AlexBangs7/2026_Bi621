# BI621 – Problem Set 2

Your goal for this assignment is to transform a SAM file (```mouse_C1.concordant_uniq.sam.gz```) into a FASTQ file. Using your knowledge about SAM and FASTQ file formats, craft a single command (probably composed of multiple parts) to make the transformation. Do not unzip the file.

Submit:
1.	The command you used to generate your FASTQ file
    ```
    gzcat mouse_C1.concordant_uniq.sam.gz | grep -v "^@" | cut -f 1,10,11 | sed -E 's/(.+)\t(.+)\t(.+)/@\1\n\2\n+\n\3/' > new_file.fq
    ```
2.	The 1024th record in your new FASTQ file (and the command you used to identify it).
    ```
    cat new_file.fq | head -4096 | tail -4

    @NS500451:154:HWKTMBGXX:1:11101:20675:1544-TACGAACC^GTGATGTC;0^0
    ACACCCGCCTAGCCAGCCAGATCAGCCGAATCAACCCTGGCGATCAATGGGGTGACAGATGTCGCAGCCAG
    +
    EEEEEEEEEEEE<EEEEEEEEEEEEEEEEEEEEEAEAEEEAEEEEEEEEE/E6EEEEEEEEAEEEEEEAEE
    ```
3.	Answers to the following questions:
    1. How many lines are in your FASTQ file?
    
        4,000,000
        
    2. Is there a problem with your FASTQ file?
        
        Header lines are not unique since data was from paired-end exp. 
        
    3. If there is, how can you fix it? If not, how do you know there’s not?'
        
        Could add a “counter” onto ID line.
        
    4. What is the maximum expected value in a quality score?
    
        40 (or 41)
    
    5. What ASCII character encodes that value for your FASTQ file?
        
        I (or J)
        
    6. What is the actual maximum value observed in this file? What is the probability that a base call with this qscore is incorrect?
        
        The maximum qscore observed in the file is encoded by "E", which corresponds to a qscore of 36. We can use the equation
        
        Q = -10 log <sub>10</sub> P
        
        and solve for P. We calculate that the probability of an incorrect basecall with a qscore of 36 is ~0.00025, or roughly 1 in 4000
