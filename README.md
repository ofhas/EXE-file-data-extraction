# EXE-file-data-extraction

In this project we'll demonstrate the use of the subprocess module, list comprehension, sets and python simulated webserver, the main purpose of this project is to extract the output of the exe file that spits out differet data, some of the data is a json object which has 3 properties, data, events and duration, we'll count the number of different events and data and display it by using list comprehension and the subprocess module on a localhost page.
  
you'll need to preform the following steps in order to run the process successfuly:
1, save all the files: big.py and webserver.py files and generator-windows-amd64.exe file at the same folder.
2, run the webserver.py file first and then run the big.py file, keep both processes running togather.
3, open a localhost:8080 at your browser.  
The data of the output extraction should appear at the localhost page you've open, in order to get the updated data you should refresh the page every time.
