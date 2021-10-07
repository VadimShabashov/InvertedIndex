# InvertedIndex

## This repository provides functionality for the construction of the Inverted Index of an arbitrary document. By passing the words into the program, a user will be able to search and highlight the found words in the text.


### Example of the working code:

1. Compilation of the program:

```
$ python3 main.py
```

3. One will be offered to pass names of the files:

```
Enter file names: 1.txt 7.txt
```

There Inverted Index was constructed for the provided documents.

3. Finally, one will be offered to pass the words:

```
Enter term(s) to search: книгоиздательство
```

The text, containing these words, will be displayed with the words highlighted.

![Alt text](example.png?raw=true "Optional Title")



## Things to revise:

Highlighting doesn't work properly, since, for example, the word "cat" in "cats" will be highlighted, which is not expected behavior.



## Original version:

This is a modified version of the (https://medium.com/@fro_g/writing-a-simple-inverted-index-in-python-3c8bcb52169a)
