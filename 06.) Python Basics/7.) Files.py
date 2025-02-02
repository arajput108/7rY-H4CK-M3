In Python, you can read and write from files. We've seen that in cyber security, it's common to 
write a script and import or export it from a file; whether that be as a way to store the output 
of your script or to import a list of 100's of websites from a file to enumerate. Let's dive 
straight into an example:

  f = open("file_name", "r")
  print(f.read())

To open the file, we use the built-in open() function, and the "r" parameter stands for "read" and 
is used as we're reading the contents of the file. The variable has a read() method for reading the 
contents of the file. You can also use the readlines() method and loop over each line in the file; 
useful if you have a list where each item is on a new line. In the example above, the file is in the 
same folder as the Python script; if it were elsewhere, you would need to specify the full path of the file.

You can also create and write files. If you're writing to an existing file, you open the file first 
and use the "a" in the open function after the filename call (which stands for append). If you're 
writing to a new file, you use "w" (write) instead of "a". See the examples below for clarity:

   f = open("demofile1.txt", "a") # Append to an existing file
   f.write("The file will include more text..")
   f.close()

   f = open("demofile2.txt", "w") # Creating and writing to a new file
   f.write("demofile2 file created, with this content in!")
   f.close()
Notice we use the close() method after writing to a file; this closes the file so no more writing 
to the file (within the program) can occur.


Answer the questions below:
1.) In the code editor, write Python code to read the flag.txt file. What is the flag in this file?
Code: f = open("flag.txt", "r")
      print(f.read())

Flag: THM{F1LE_R3AD}

