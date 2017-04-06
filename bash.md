### Bash Basics
Create file:
```bash
> file
# or: touch file
```

Create directory:
```bash
mkdir folder
```

Move file
```bash
mv file folder/
```

Rename file
```bash
mv file file.txt
```

Copy file
```bash
cp file.txt ..
# copy with rename: cp file.txt newfile.txt
```

Open file with the default program
```bash
open file.txt     # on Mac
xdg-open file.txt # on Linux
```

Delete file permanently
```bash
rm file.txt # delete specific file
rm fi*      # delete files starting with
```

Delete directory permanently
```bash
rm -r folder
```

More info on a command
```bash
man rm
```

Bonus
```bash
bc    # calculator
cal   # calendar
date  # today's date
```

--------

Redirect  
```bash
# Basic use: redirect standard output to a file
echo hello > hello.txt  # redirect stdout
echo hello 2> hello.txt # redirect stderr
```

Pipe
```bash
# pass the output of a program as an input to an other
man cat | cat > test.txt
# 1: get the man page for the cat method
# 2: pass it as stdin for the second cat
# 3: redirect second cat's output to test.txt

# this was just for example, you could write
# man cat > test.txt
# to do the same
```
To understand why some word's letters are doubled, check out [this link](http://stackoverflow.com/questions/26634497/redirecting-man-page-output-to-file-results-in-double-letters-in-words/26635053#26635053).
