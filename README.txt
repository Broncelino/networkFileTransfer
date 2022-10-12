# Overview

My name is Bryson Williams I have always loved computers and have been programming for a few years now.
I've already made other programs in various languages and have them 
posted to this github. As of now 9/17/22 I am aiming to become a Database admin or something else in that field.

#Description
I wrote a program that transfers a file from the client to the server. Simply running each program in the command line will execute the program
as long as the server program was ran first. If the client program gets run without the server listening for requests it will error and stop running.
The file that you want to tranfer needs to be in the same directory as the client code and after it gets transfered it will end up in the directory that has the server code.
The program supports every file type I have tried so far so I have no reason to suspect there is one that won't work.

#Purpose
Sharing files between computers can be a hastle. Going from my laptop to desktop there are a limited options. Emailing the file to myself but
there is a size limit to that of about 50Mb. Another is using a website like github but making a repository for every single file you
want to transfer will clutter your account if you don't get rid of them and you might just not want the file on there.
With this program there is no limit to the size of the files you can transfer and they will only exist in the original
location of the server program.


Demo vid https://youtu.be/k-_AMAaFDog

# Network Communication

I used a server-client system to tranfer files from the client machine to the server.
I'm using TCP to move the files because if any packets are lost the file may be corrupted
and unable to fulfil its purpose. The port is 5001 because it isn't used by the computer originally 
so it's an empty port.

# Development Environment
I used my laptop and desktop to develop the code using Visual Studio code as my software
and I run the program from the command console.
The code is written in python with the socket, tqm, and os libraries.
Socket is the main library that opens the server in one program and connects to it with the other sending the file.
Tqm is used to create a progress bar that shows how much of the file has been transfered.
Os is used to find the file specified in the client directory

# Useful Websites

Tech with Tim  https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1516s
realpython https://realpython.com/python-sockets/

# Future Work

* Make the client code work with absolute path names. Might already but in a different format than I tried
* Currently only works on local network. I could make it work publicly but that introduces security risks
* Changing the server code to deposit the recieved files into the directory of your choice.
