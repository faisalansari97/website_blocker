WEBSITE_BLOCKER

Have you ever been distracted from the social media websites or some other websites from web while executing your work. You need to figure out the way to overcome these distractions. If your time is important for you, than you will always look to figure out the way to get out from these distractions. Now you have solution to these. This website_blocker program will block all the websites you are distracted to when you are doing your work. The best part of it is, it runs in the background. So you are left with no worry to look after it again and again.

How it works?

Website_blocker.py excutes the script every 5 sce or 5 minutes(as mentioned) and checks for the time on your host. Suppose you work from 8am to 4pm than in this duration the script runs in the backgroud and blocks the websites that are mentioned by you in the script. And the process stops as soon the time surpasses the entered time for the process to execute.

File manipulation is the key function to the program. For every host, we have a host file in it.
For Windows: C:\system32\drivers\etc\hosts
For Linux: /etc/hosts
What this program does is, it manipulates the host file and enters the redirected website and website name at the end of host file.
eg: 127.0.0.1 www.facebook.com [This will redirect the facebook to 127.0.0.1]
The website will be redirected in the time interval you are working. And these strings will be removed from the host file as soon as the time interval surpasses. This all task is automated by the python script and will totally excecute in background

To end the process open Task Mamager>Processes Find your program and End task.

Run this program with python_w.exe instead python.exe to execute it as background process. The program requires administrator privilege to run in background so make sure you run this as an administrator by right clicking >> Run as administrator.

1) To make this process automatic create a task in windows using Task Scheduler. Create a new task and name the task as Website Blocker(name-as you wish) make sure to check the box [Run with highest privileges] at the bottom this will make program run with every users and administrator.
2) At top, Create a new trigger and select [At system startup].
3) Create action and browse to the directory of your program and select it.
4) In conditions tab, uncheck [Start the task only if the computer is on AC power.]
Click Ok and run the task.

Now the program will run automatically in background as soon as your computer starts.
