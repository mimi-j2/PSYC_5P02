
**Question 1:** 

**a)** What command would you use in a terminal shell if you wanted to list the files in your current directory, sorted in reverse order of when they were last edited?

*ls -rt*
rt reverses the order of the sorting by time (so it starts from oldest and ends on most recent file edited)

**b)** How would you expand on this command to also provide the date and time the file was last edited?

*ls -lrt*
by adding l it gives you additional information on each file such as date and time it was last edited. It also gives you additonal information like size of file, file owner, group, date modified, and who can access and edit the file.

**c)** Provide the manual description of at least one of the options required to produce this result.

- l = use a long listing format
- r =  reverse order while sorting
- t = sort by time, newest first;

**Question 2:** If your "home directory" is ```/users/yourname/```, provide three different commands that you can use to navigate from the directory ```/users/yourname/documents/``` to your home directory: 
  
      cd ~/
      cd home 
      cd ../ (if you do this it will take you to the directory above which is the home directory)
      or can also do cd /users/yourname/ to get to the home directory

**Question 3:** Provide the commands to do the following (in order):
- Make a directory called 'Data' 
*mkdir Data*

* Create a file called 'subj01.txt'
*touch subj01.txt*

* Create four copies of the file you just created for subject 2 - 5, as well as 11.

      cp subj01.txt subj02.txt
      cp subj01.txt subj03.txt
      cp subj01.txt subj04.txt
      cp subj01.txt subj05.txt
      cp subj01.txt subj11.txt

- Move all of the files into the 'Data' directory

        mv subj01.txt Data
        mv subj02.txt Data
        mv subj03.txt Data
        mv subj04.txt Data
        mv subj05.txt Data
        mv subj11.txt Data

- Delete all .txt files from the Data directory **except** for subj11.txt

        cd Data
        rm subj01.txt
        rm subj02.txt
        rm subj03.txt
        rm subj04.txt
        rm subj05.txt

**Question 4:** Using the manual to learn about the function, create a _pipe_ that uses the ```tee``` command. Describe the task you're aiming to perform, and provide any and all code needed to complete it. Be sure to upload any files that you needed to run this code.

I did:
**df -h | tee disk_usage.txt**

df reports the file systems space usage, and the -h option makes it human-readable (print sizes in powers of 1024, basically converts things like 1K-blocks to Size in GB which is more understandable)

*tee - read from standard input and writes it to the standard output and one or more files at the same time*

so this takes the report of space usage on my system and then using the tee command gives me the output and puts it to a file disk_usage.txt

Got the information on how a tee is used and examples from this website:
https://linuxize.com/post/linux-tee-command/

**Question 5:** Using the ```screen`` command, open up a screen. Using the ```history``` command and a pipe, write your command history to a file. Then exit the screen, and write your history to a new file again.  (Be sure to name them something obvious and upload both files as part of this assignment.)
1. screen
2. history | tee command_history.txt
3. Ctrl-a-d
4. history | tee no_screen_command_history.txt

**Are these files the same? Why or why not?**

it is not the same - when it comes to creating files or going to specific areas on my personal computer on the screen it will not put the creation of personal fiels or locations of personal whereabouts in the command history. I think this could be to protect personal and sensitive information on a personal computer. The ClassFiles things are still there but that may be because it is connected to a remote repository - so things that are not connected to a remote repository won't be shown in screen. But everything created in the Data directory and eveyr command associated with that is not present, and I think it is because it is not connected to anything remote.

**Question 6:** Complete the Introduction to Github tutorial at https://skills.github.com/. Screenshot the message you receive when you complete the tutorial, and insert the image into your markdown file. Hint: your image will need to exist in the same path as your saved markdown file, and your code will take the form of something like: ``![This is a picture of my screenshot](screenshot.jpg)``

[This a picture of my tutorial completion](Finished_Intro_to_Git.png)

**Question 7:** Go to the class respository (https://github.com/SMEmrich/PSYC-5P02-2025). Using the *fork* button at the top of the page, create a fork of the class respository. 

After it has been forked, clone the repository to your computer using the code git clone git@github.com:[yourusername]/PSYC-5P02-2025.git (You may need a slightly different address if you are using https instead of ssh.) Be sure to put this somewhere that makes sense - this repo will have all course materials from this point on. Take a screenshot of your terminal window listing the files of your local repo. Add the screenshot to the markdown file.

[This is a picture of my PSYC 5P02 local repo](PSYC_5P02_Repo.png)

Question 8: Uplaod all files to github (inluding your markdown file and the files created in Question 5 - 7). Be sure to add me to the repo as a collaborator under Settings (user: SMEmrich). Use the history command to write only the commands you used to commit your files to git. (hint: you may need to use the head command --- or possibly the opposite of head). What was the command you used to the create the final file?. Lastly, commit that file and your final markdown file with responses to all questions to the github repository.

**history | grep "git commit" | tail -n 6 | tee git_commit_history.txt**

1. first I use historywhich brings up the command history 
2. Next I use pipe which ties it to the next command so once I am asking it to pull up history. It will combine that will my next command.
3. My next command that I am piping together is grep "git commit" which looks for the pattern of lines that have the words "git commit" in them and prints it, so it is looking at my history of commands with the words "git commit" in them,
4. Next I am using a tee command to give me the output and put it into a new text file called git_commit_history.txt. 
5. Lastly I am finishing it with tail -n 6 which gives me the output of the last part of the files, followed by -n 6 which means it will only return my last 6 "git commit" lines. 








