WEBSITE_BLOCKER

Have you ever been distracted from the social media websites or some other websites from web while executing your work. You need to figure out the way to overcome these distractions. If your time is important for you, than you always look to figure out the way to get out from these distractions. Now you have solution to this. This website_blocker program will block all the websites you are distracted to when you are doing your work. The best part of it is, runs in the background. So you are left with no worry to look after it again and again.

How it works?

Website_blocker.py excutes the script every 5 sce or 5 minutes(as mentioned) and checks for the time on your host. Suppose you work from 8am to 4pm than in this duration the script runs in the backgroud and blocks the websites that are mentioned by you in the script. And the process stops as soon the time surpasses the entered time for the process to execute.

File manipulation is the key function to the program. For every host, we have a host file in it.
For Windows: C:\system32\drivers\etc\hosts
For Linux: /etc/hosts
What this program does is, it manipulates the host file and enters the redirected website and website name at the end of host file.
eg: 127.0.0.1 www.facebook.com [This will redirect the facebook to 127.0.0.1]
The website will be redirected in the time interval you are working. And these strings will be removed from the host file as soon as the time interval surpasses. This all task is automated by the python script and will totally excecute in background

To end the process open Task Mamager>Processes Find your program and End task.
