# Day 33 Notes - API (Application Programming Interface)

# An API (Application Programming Interface) is a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an external system.

# Focus -> interact with an external system 
# Take Live Data from other websites
# Make a request through the API to get information
# Must follow a set of rules

# API Analogy = if Websites -> restaurant and Data -> kitchen then API -> menu (interact with the menu)
'''
    API interface between user and data
    API endpoint -> location of the data
    API request -> try to withdraw data from the website
    GET request -> get
'''


# JSON -> commonly used -> minimalist, not many indents and spaces, small size
'''
    Requests -> returns Response Code
    # look at the first number
    # 1xx -> wait
    # 2xx -> successful
    # 3xx -> No permission, go away
    # 4xx -> You screwed up
    # 5xx -> server screwed up
'''

# This is how to play audio in tkinter
import pygame
pygame.mixer.init()
pygame.mixer.music.load("musashi_quotes/musashi-song.mp3") # path to song
pygame.mixer.music.play(loops=0)