# web-scraping-challenge
Mission to Mars

This challenge was very difficult in that it brought together many aspects of our learning over the last month (and beyond) and brought them together in a single exercise. 

The challenge of getting the "Featured Mars Image" to work when the JPL web site had made a change we didn't know about added to the overall frustration level. 

I've found the webscraping process to be challenge as it appears not all tabs we attempt to connect on work. Its not easy to tell if its a coding issue on our side or a software limitation. 

Webscraping also appears to be a bit of an art form in the sense that, with practice, it should get easier (fingers crossed)

Compling the data sources and building the scraping dictionary was methodical but tedious and slow going task. 

I had completed the "Featured Mars Image" task before being told we didn't need to do it, so I left it in place. I used splinter enter the JPL.nasa.gov sight and had it click through two menu levels to reach the imgages folder filterd on "Mars only" images. Beautifulsoup was then able to draw out the most recent Mars image. 

To connect to chrome, I found a module that allowed me to connect without having to reference my local chrome driver. 

"from webdriver_manager.chrome import ChromeDriverManager"

With this import in place the executable path is =
executable_path = ChromeDriverManager().install()}

Once the scraping.py file was completed, the Mongo DB and Flask Application process went fairly smoothly except for the challenge of how to make an html table display (use |safe) and how to get the hemispheres dictionary to unpack and present (use a "for" loop. 

All in all, the hardest assignment yet, for me.

Save space travels:
![alt text](https://i.pinimg.com/originals/ee/f4/ee/eef4ee90952d20809e28ccd1c4e05616.jpg =400x)
