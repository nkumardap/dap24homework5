"""
INSTRUCTIONS

Available: June 24th at 11:59AM

Due: July 4th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework5.py file
(b) Must commit homework5.py and games.csv to your clone of the 
GitHub homework repo
(c) Must NOT repeatedly use a hard-coded path for the working directory

Failure to do any of these will result in the loss of points
"""

"""
BoardGameGeek.com is a website devoted to - as the name suggests - board games.
Among other things, it allows users to rate games. BoardGameGeek.com then uses 
these ratings to  create a list of the top board games of all time. You can 
see the first page of that list at this link:

https://boardgamegeek.com/browse/boardgame/page/1

You will be using this  (and the next page) to create a dataset of 
games, using the URL of game to gather further information. Read all three Parts 
of this assignment before you start working on it since you may want to plan things 
before you let your code run to complete the scraping.

(Note that clicking on the name of a game will take you to a webpage that contains
further details of the game. For example, the top
game is Brass: Birmingham and clicking on its title will take you to 
https://boardgamegeek.com/boardgame/224517/brass-birmingham. This will be 
important later.)


PART 1

Extract data from the table to construct a dataset containing the following: rank
title, year, description, geek rating, avg rating, num voters, and game's webpage 
URL. Repeat this for page 2 of the list of top board games of all time. 
Use a function to automate retrieval from a page.

Restriction: Insert a 5 second pause between requests for pages containing the 
tables

Hint: Note that the title, year, description, and game's webpage URL are all 
contained in the third cell of each row. We haven't covered the .split() 
method  that strings have  in class, so you may want to look it up. The 
game URL is embedded with the title.


PART 2

Using the game URL that is embedded in the title, visit each page in the top 
200 and extract the "weight" of the game. The "weight" of a game is a measure 
of how complex it is. For each game, open the game's webpage, extract the 
measure, and add that measure to the dataset. 

Restriction: Use a function to automate retrieval from a particular game URL. 

Hint: Content on these pages is "dynamically loaded" which means that *after* 
the webpage opens, boardgamegeek.com will pull content out of its servers and
populate sections of the page. This means you can no longer use the requests 
package to download all the content. Instead you will have to install 
the selenium package and use the webdriver module.

Research how the webdriver module works and use it to download content from the 
webpages of the individual games. 

Related hints: 
    
    a You'll have to use sleep() to wait for the page to open completely;
it took just 1 second on my system but might take more time on yours.

    b Using driver.quit() to close the window after you are done should
help automate the process and avoid unnecessary clicking.

    c Note that what works for one page might not work for another. Note
that Brass: Birmingham is a medium weight game, Castles of Burgundy is a light
game, and On Mars is considered a heavy game. Look at how the code of actual
numbers changes around these.
    
    d As with all things, make sure that this works for one page before
adding more. 

    e. Once you are confident in your code's ability to do a dozen pages
do Part 3 before you run this code for all 200.


PART 3

Games are often "reimplemented" with the basic game rules tweaked
to create a new game. For example, the top game is "Brass: Birmingham" which
reimplements "Brass: Lancashire." But both of these games are in the top 100!
That seems wasteful; let's fix that. 

You can see whether a game reimplements another game because, on its webpage,
just above the title, is a note that says "Reimplements:" and the name of the
game.

Use the function you created in Part 2 to extract the name of the game that 
is being reimplemented and add that to the dataset.

When that is done, create a list of all the games that are being reimplemented.
Remove the lower-ranking of these games from the top 200 list that you've created.

Save the resulting dataset as games.csv

Hint: Be careful that you're actually using "Reimplements" - a 
"Reimplemented by" note is sometimes in that position instead!
"""
