# autoxecuter
This script will continously be executing any program file whenever the content of the source file will be changed.

* Step 1 :
```bash
[username@host]$ git clone https://github.com/nowshad-hossain-rahat/autoxecuter
```
* Step 2 :
```bash
[username@host]$ cd autoxecuter
```

* Step 3 :
```bash
[username@host]$ ./run

[#]-> Welcome to Auto Executer!
[#]-> Author : Nowshad Hossain Rahat
[#]-> Git repo : https://github.com/nowshad-hossain-rahat/autoxecuter
[#]-> Select Executer :
  [0]-> Node.js
  [1]-> Python
  [2]-> PHP
  [3]-> Ruby
  [4]-> Perl
  [5]-> TypeScript
  [6]-> C++ (GCC)
  [7]-> Bash
[#]-> Enter the ID : 6
[#]-> File name : [PATH/TO/YOUR/FILE]
[#]-> Execution started...
```

Now just write code to that file and whenever you'll save it the Auto Executer will detect that and execute that file. Then the output will be printed into your console.

* Press ```Ctrl + C``` to stop
```bash
^C[#]-> Auto Executer stopped!
```

# To install as a command
If you want to install this Auto Executer as a command like you do ```node``` or ```php``` i mean if you want it to run from anywhere of your Linux system like ```autoxecuter``` then follow the steps below

* To install
```bash
[username@host]$ ./install
```
* To run
```bash
[username@host]$ autoxecuter
```

* To uninstall
Go into the ```autoxecuter``` folder you cloned from github
```bash
[username@host]$ cd autoxecuter
```
then
```bash
[username@host]$ ./uninstall
```

