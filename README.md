# Quiddler
Quiddler Card Game (both solitaire and multiplayer) Project

HOW?

Written in Python using tkinter.  Pyenchant is used to check spelling in the Solo version.

WHY?

This project is one of my first.  I am a self taught amateur and I do not have permission from the makers of Quiddler the physcial card game.
This project is for my own eductional purposes only and should not be distributed or sold.  

WHAT?

Quiddler is a spelling card game - an ideal project to tackle for a someone like myslef.  I wanted to try something that hadn't (to my knowledge) been attempted
before, instead of another poker or blackjack game tutorial.

The RULES of Quiddler can be found here:

https://www.setgame.com/sites/default/files/instructions/QUIDDLER%20INSTRUCTIONS%20-%20ENGLISH.pdf

The results are unfinished.  The single player version is pretty functional and can be played through to the end but is very unpolished (needs to be refactored for sure; mostly spaghetti, GUI looks like total shit.)

The multiplayer version was intended for my wife and I to play on seprate computers over our local network; I literally learned to code becasue she was beating me at Quiddler too much and I was tired of shuffling lmao (true story).  The multiplayer version works through to completion on my computer (two instances: one server & one client) but I have never sucessfuly gotten it to work on seperate computers becasue of my lack of skill in regards to networking / server client architecture etc. 

The images folder in this repository has all the card / board image assests (again I own nothing and have no permission).  High quality images are definately needed.

IMPORTANT 

You'll definately need to alter the code to enter your own local IP info into both the Server & Client Py files if you want the multiplayer version to work of course.  

Naturally, I have not learned to write an installer or the like so these games can only be played by running the .py files.  If you're trying to run the multiplayer version, you have to start the Server first and then have the client connect (obviously); server listens for client to connect to server socket.


Maybe someone else who loves this game will help finish it to something that resembles a "real" program.
