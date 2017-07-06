# Pythone v3.6

import os

if not os.path.exists("read.txt"):
    print("[error] read.txt file is not existed.")
else:
    read_file = open("read.txt", "r", encoding = "UTF-8")
    write_file = open("write.txt", "w", encoding = "UTF-8")

    if (read_file == None) or (write_file == None):
        print("[error] file can't open!")
    else:
        for line in read_file.readlines():
            print(line, end = "")
            write_file.write(line)

        read_file.close()
        write_file.close()
