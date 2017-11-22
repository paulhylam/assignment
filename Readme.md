This program will return the following information based on the dataset news.

Prerequisites to running the program:
1. To start on this program, you'll need database software (provided by a Linux virtual machine) and the data to analyze.
2. This instruction assumes the use of the same Linux-based virtual machine (VM) - i.e. Vagrant and VirtualBox.
3. If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
4. Next, download newsdata.sql and put this file into the vagrant directory.
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5. Make sure all the other python files are saved under the same directory in /vagrant

Once the VM is up and running the following commands in the BASH Shell:
1. Run 'psql -d news -f newsdata.sql'
2. Run 'Python Organize_data.py'
3. Run 'Python Output.py'

If you would like to run the codes again you will need to reset the tables and re-run step 1 above:
1. Run 'Python Reset_tables.py'
2. Run 'psql -d news -f newsdata.sql'
3. Run 'Python Organize_data.py'
4. Run 'Python Output.py'
