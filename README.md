# pyzip

pyzip is a python program to zip a file with password.

### Usages
Usage:
```
--input <input file>
--i <input file>
--output <output file>
--o <output file>
--password <password>
--pw <password>
```

Example1:
```
python pyzip.py --input ./Text.txt --output ./output.zip --password PSW
```
Example2:
```
python pyzip.py --i ./Text.txt --o ./output.zip --pw PSW
```

If you are trying to zip a directory,
you need to compress whole directory using normal zipper then set password using this.
