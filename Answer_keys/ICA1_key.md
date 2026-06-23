# BI621 – In-class assignment 1

For this assignment, answer all the questions and **include the command you used** to obtain the answer. You may edit this assignment online using the edit button in the upper right hand corner of GitHub's online interface: ![image](https://user-images.githubusercontent.com/1646180/232853243-3284cb63-c89e-448d-a20d-30ca9ed8b040.png)

For most future assignments, you will need to use `git` commands via the terminal instead of editing online.

When in editing using [GitHub Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#quoting-code), you can use backticks(\`) to format text as code, or triple backticks (\`\`\`) for code in its own distinct block. Note that GitHub does not wrap text displayed as code: *be sure to insert linebreaks for readability within codeblocks*. You can find more about GitHub Flavored Markdown here: https://help.github.com/articles/basic-writing-and-formatting-syntax/. Also notice that files must have the `.md` extension for GitHub to properly desplay GitHub Markdown.
1.	What is the absolute path to your home (`~`) directory?

    `pwd`

    Varies. Leslie's is:
    ```
    /home/coonrod
    ```
    Note the beginning `/` - very important! All absolute paths must begin with `/`
    
2. What is the absolute path to your data directory within the bgmp PIRG?

    Varies. Leslie's is:
    ```
    /projects/bgmp/coonrod
    ```


3. What is the difference between your home directory (`~`), your data directory (answer to #2), and THE home directory (`/home/`)?

    Your home directory (`~`) is a smaller space (250GB) and where you will be located in the file system when you log in to Talapas. THE home directory (`/home`) is the director which holds ALL users home (`~`) directories.

    Your bgmp pirg directory (`/projects/bgmp/<user>`) is a larger space (we share ~60TB) where we can store bigger datasets/projects.

4.	No need to respond to this question.

5.	Move to the directory `/etc/profile.d/`

    `cd /etc/profile.d/`

    1.	What is the 116th line of the file `y-motd.sh` in the directory `/etc/profile.d/`?
    
        `head -116 y-motd.sh` or `cat -n y-motd.sh`
        ```
        printf "  ${WARN}${BOLD}!  Data on Talapas is NOT backed up.${RESET}  ${DIM}You are responsible for your data.${RESET}\n"
        ```
        
    2.	What is the relative file path to get to `/var/log` from here?
        
        `.cd ../../var/log/`
        
    3.	What is the absolute path?
    
        `/var/log/`
        
        Again, notice that relative paths do no start with `/` while absolute paths do!
    
6.	Move to the directory `/etc/sysconfig`

    `cd /etc/sysconfig` or `cd sysconfig`
    
    1.	What is the contents on line 165 of the `sysstat.ioconf` file?
        
        `head -165 sysstat.ioconf`
        
        ```
        58:lvm:*:0:d:256:*:1:Logical Volume Manager (lvm0..lvm255)
        ```
        
    2.	Without changing directories, what is the second line of the `cpuinfo` file in the proc directory?
    
        `vendor_id	: GenuineIntel`
        
        1.	What is the command to read this file with a relative path?
        
            `head -2 ../../proc/cpuinfo`
        
        2.	An absolute path?
        
            `head -2 /proc/cpuinfo`
            
7.	Move back to the root – what directories do you see? How can you tell they are directories?

    ```
    $ cd /
    $ ls -F
       bin@   dev/  gpfs/  lib@    media/  opt/       proc/      root/  sbin@  sys/  usr/
       boot/  etc/  home@  lib64@  mnt/    packages@  projects@  run/   srv/   tmp/  var/
    ```
    We can use `ls -F` to designate folders. Technically, those that end with `@` are symbolic links to OTHER directories, but we won't "split that hair" here.

8.	Move back home – what are three ways to move from home to the root?
    
    move home: `cd` or `cd ~`
    
    move from home to root: `cd /` or `cd ../..` or `cd -` (specific to how you were asked to move)
    
9.	What do the following options do (use man command)?
    1.	`-1` when using `ls`
    
        list one file per line
    
    2.	`-i` when using `rm`
    
        prompt before every removal
    
    3.	`-I` when using `rm`
    
        prompt once before removing more than three files, or when removing recursively.  Less intrusive than -i, while still giving protection against most mistakes
    
    4.	`-r` when using `rm` (*WARNING!* Be sure you know what you’re doing before running this command)
    
        remove directories and their contents recursively
    
    5.	`-S` when using `less`
    
        Causes lines longer than the screen width to be chopped rather than folded.  That is, the portion of a long line that does not fit in the screen width is not shown.  The default is to fold long lines; that is, display the remainder on the next line.
    
    6.	`-n` when using `cat`
    
        number all output lines
