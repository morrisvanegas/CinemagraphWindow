import time
from pymouse import PyMouse

# Simulates a mouse movement to keep screen on during Cinemagraph Window Display
# Super hack, but couldn't find how to change settings on pi to keep display from sleeping, so here we are
# Gets the screen size, moves the mouse to bottom right (you see the cursor less)
# Forever loop this. time.sleep should be less than monitor sleep time (about 10 minutes)
# Install PyMouse (sudo pip install PyUserInput) -> python manager for Python is pip. Dont use apt-get
# Open MorrisVanegas.com/Cinemagraphs on a browser.
# F11 to fullscreen
# ctrl+c to quit python script
# to run, type "python mouseclickloop.py" in terminal when in Desktop directory

m = PyMouse()
size = m.screen_size()
x = size[0]
y = size[1]

while True:
    m.position()
    m.move(x,y)
    m.click(x,y,1)
    time.sleep(3)
