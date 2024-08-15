# SPL Generator Library
## A Python Library for easily generating programs in the Shakespeare Programming Language
### About
A work-in-progress library to make the esoteric [Shakespeare Programming Language](https://shakespearelang.com/1.0/) more accessible by allowing users to generate SPL code using builder objects in Python. Use `python test.py` as an example, and append the result to a .spl file (the title section is not included yet, as I am still working on implementing Acts and Scenes). Then, you can run the program with `shakespeare run first_play.spl` (assuming you've added the title section to the spl file - it is a work in progress)

### **Important** note when running your shakespeare program
For the [SPL interpreter that I'm using](https://github.com/zmbc/shakespearelang/), the current version on the main branch has some issues with python 3.10+ and other issues I've noticed with certain nouns and adjectives such as "summer's day" and "fat-kidneyed", so please use the first release candidate version 1.0.0rc1 of the interpreter (found [here](https://pypi.org/project/shakespearelang/1.0.0rc1/)) when using this library. 
