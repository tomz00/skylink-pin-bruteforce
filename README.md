# Skylink Live TV PIN code bruteforce
A simple Python script to bruteforce 4 digits parental PIN code on Skylink Live TV.

## Script
The script is working with PINs from 0000 to 1000 by default. You can simply change the numbers in the Python script. After that, you can also run it multiple times at once with different PINs.

## Setup
First, you have to retrieve Bearer token, which is used as Authorization. To do that, open DevTools and switch to Network tab (or Ctrl+Shift+I). With DevTools opened, navigate to https://livetv.skylink.sk/. Filter for queue.solocoo.tv and you should see a GET request with the token in the URL. Finally, update the token in the Python script. It is very likely that the token will expire, or will not work after some time. You will get error and the Python script will exit. After this, you can just repeat the process with new token.
