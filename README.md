# Alphabot_webServer
## General description of the project

This is our second project with the alphabot.  
It is a web-app written in python using Flask and a database (SQLite) where we save some data (for example who did a move).

## HTML pages
There are two HTML pages: the first used for the login and then the page with all the commands to make the Alphabot move.  
- The first page contains a form where you have to put a username and a password to be consequently directed to the second page (the username and password are saved on a database).  
- The second page contains some buttons with the elementals moves (forward, backward, left and right) and a space where you can enter a complex command that will be executed by the alphabot (this is also saved on the database).

## Cookies
To save in a history the username, time and move made (on our database) we decided to use cookies.

By Masia Matteo & Fenoglio Cristian
