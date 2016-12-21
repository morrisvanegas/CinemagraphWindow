# CinemagraphWindow

This cinegraph window displays a cinemagraph in a web browser that is descriptive of the weather at the location based on the IP address of the browser. Although not necessary, I created a wooden window to mount the monitor on. Throw a steaming pie on the window sill to cool and you have an immersive environment!

Example here:
http://morrisvanegas.com/cinemagraphs/ (will open a cinemagraph based on your current location's weather)

More details here:
http://morrisvanegas.com/forus/cinemagraphs.html

## SETUP
* Create an account from OpenWeatherMap.org to generate your Key.
* Add this key to the index.html file
* Add the index to your site (along with the rest of the files)
* Save the world.
* See a cinemagraph of the weather outside by opening index in your browser. 
* If you want, feel fry to find/create other cinemagraphs and replace the folders.


## FILES
index.html - what should get loaded

getweatherforlocation.php - Requests location based on IP address. Also requests weather as specific location once location has been found. 

mouseclickloop.py - For some reason, I couldn't get my computer monitor to not fall asleep. I tried multiple solutions I found online, but my monitor kept shutting off. Finally, I decided to create a simple script that moves the mouse every few minutes so the monitor is always active. This is an extremem hack, but I'll fix this later. 

/gifs - cinemagraphs organized by temperature ranges. 

## USES
Upon loading, you will see a cinemagraph fill your browser. Temperature, along with a description of the weather will be displayed in the top left. 
The footer houses a toggle switch, a link to my portfolio to read details of the cinemagraph, and a link to @fourtonfish's website, who created a tutorial that this cinemagraph is highly based off of. 
Clicking the temperature switches from F to C.
Clicking toggle button removes the temperature and description and displays only the cinemagraph. 
The window automatically reloads every 5 minutes, so beware that the weather portrayed may be delayed. 


## THANKS
This was adapted code from FourtonFish. Thanks for all the help, and actually replying to cold emails. 
