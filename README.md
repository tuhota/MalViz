#  📈 MalViz

## Python/C API:
wrapper.cpp makes use of this API to interact with Python3 scripts

It can also call Python functions directly within the program

[Documentation](https://docs.python.org/3/c-api/veryhigh.html)



## Dependencies
Install python-dev/devel for your distro and ```$locate Python.h ``` to ensure installation was successful



## g++ compiler directives:
```g++ wrapper.cpp -o wrapper -I/usr/include/python3.X -lpython3.X```

X = replace with your current Python3 version


<hr>

# 🔨 TODO:
1. Integrate more visualisation scripts
2. Exception handling and logging
3. Option to write visualisations to file
