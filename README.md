# mini-utils

mini_grep
---------

Usage:

    ./mini_grep [-q] -e PATTERN [FILE...]

`mini_grep` goes through every argument in FILE and prints the whole
line in which PATTERN is found. By default `mini_grep` also outputs
the line number of each printed line.

- PATTERN has to be a valid regex
- FILE can be zero or more arguments. If zero args are given,
  `mini_grep` will parse entries from the standard input.
- If given, the `-q` options only outputs lines but omits the matching
  line numbers.



mini_ls
-------

Usage

    ./mini_ls [-r] [FILE...]

`mini_ls` lists information about the paths given in FILE. The
information required are: Owner, Permission, Modified Time.

- FILE can be zero or more arguments. If zero args are given,
  `mini_ls` will list information about the current directory.
- If given, the `-r` option will make `mini_ls` run recursively on any
  directory it comes across.


mini_df
-------

Usage:

    ./mini_df [-h] [PATH...]

`mini_df` outputs the file system disk space usage of each entry in
PATH. The information required is: Total Space, Free Space, Used
Space. The result should be in Bytes.

- PATH can be zero or more arguments. IF zero args are given,
  `mini_df` will list the disk space usage of the current directory.
- If given `-h` will output the result in human-readable format.
