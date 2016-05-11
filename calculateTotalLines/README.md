###NAME
    lc - calculate line count<br>

###SYNOPSIS
    lc [OPTION]... [DIR]

###DESCRIPTION
    Calculate total line count of all files in the specific directory.(Current working directory as default).

**TODO**:
    -r, --recursive
        calculate the files in the subdirectory.

    -e, --extension
        only calculate the specific extension(type) of the files.

    -i, --ignore
        ignore the sepcific extension(type) of the file. 

###DEMOS:
    1. 
    ```
    lc
    ```
    2. 
    ```
    lc /home/lxw
    ```
    3.
    ```
    lc -r /home/lxw 
    or
    lc --recursive /home/lxw    #Whole Name
    ```
    4.
    ```
    lc -e py /home/lxw
    or
    lc -e .py /home/lxw         #"."(point) is allowed.
    ```
    5.
    ```
    lc -ri .py /home/lxw
    or
    lc -re .py /home/lxw
    or
    lc --recursive --extension .py /home/lxw    #Whole Name
    or
    lc --ignore .py --recursive /home/lxw       #Order means nothing.
    ```
    6.
    **NOTE**:
    ```
    lc -ei .py /home/lxw
    when -e & -i conflicts, it equals to 
    lc /home/lxw
    ```
    7.
    8.
    9. 


###AUTHOR
    Written by Xiaowei Liu.

###ANOUNCEMENT
    Distribution of the program is NOT limited(totally free).

###Note:
    os.walk(): calculates in each directory recursively. 
