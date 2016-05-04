Smart Closet - Classify your clothes and get recommendations
------

# The event

![C.A.R.S Hackathon Logo](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/cars_logo.jpg)

This project was developed during [C.A.R.S Hackathon](https://www.facebook.com/events/487695348105055), held in Madrid, Spain between April 29th and 30th 2016.

The event was sponsored by [Nikitas Language Abroad Schools](http://www.nik-las.com/) and [IE Business School](http://www.ie.edu/).

# The idea

![Idea draft](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/blackboard.jpg)

The hackathon kicked off with the delivery of a folder to every participant with the details of the problems to solve, followed by background presentations by everyone involved.

The problem we chose to tackle was **Problem IV: Clothing dressing App**. The idea was to build a closet that *"... categorizes clothing in your closet and those purchased through your favourite stores, and the incorporate it with outfit suggestions to users"*.

After a coaching and networking session by [Reka Nikoletta Gazda](http://www.rekanikoletta.com/) using [Points of You](http://www.points-of-you.com) methodology, we were asked to describe in three words how we were going to approach the event. Our team members came up with the following terms:

- Mockup
- Prototype
- Presentation
- Prize
- Technology
- People
- Victory
- Present

It is clear that we were focused on delivering a practical and functional winning solution, rather than relying on more abstract concepts.

It had to be flexible and inexpensive, making use of as many technologies present on the fashion market as possible.

The name of the project, "Smart Closet" reflects the fact that the closet becomes an active device, rather than a passive furniture intended for mere storage.

# The team

![Smart Closet team members](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/team.jpg)

Meet the team:

- Fernando Álvarez-Uría, Software Engineer (right). <fauria@gmail.com>. [View LinkedIn profile](https://www.linkedin.com/in/fauria)
- Javier Yuste - International Management (left). <javier.yuste@alumni.ie.edu>. [View LinkedIn profile](https://www.linkedin.com/in/javieryustegarcia)
- Jesús San Román García, International Management (middle). <jesussanromangarcia@student.ie.edu>. [View LinkedIn profile](https://www.linkedin.com/in/jesussanromangarcia)

We all knew before the hackathon. Some of us worked together on [previous](https://github.com/fauria/smart-closet) [hackathons](https://github.com/fauria/white-eyes), and some were fellow students.

# Tools

![Mockup flow](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/mockup.gif)

For this project, we relied on the following tools:

- [Raspberry Pi](https://www.raspberrypi.org/) model B, interfacing with a laptop via ethernet.
- MIFARE clone [RC522 RFID](https://www.mifare.net/wp-content/uploads/2015/03/NXP-Z-card.pdf) reader.
- Two 13.56Mhz cards and two tags.
- [Canva](https://www.canva.com) mockup design tool.
- [POP](https://popapp.in) prototyping tool.
- [Apple Keynote](http://www.apple.com/mac/keynote/) presentation.

**[Try the Smart Closet App Mockup](https://popapp.in/w/projects/572486fbbb163c267576b35b/preview)**

# Prototype

![Fully functional prototype](https://github.com/fauria/smart-closet/raw/master/assets/smart-closet_prototype.gif)

The prototype simulates the entrance of clothes in the smart closet.

The initial setup starts with an empty closet, and the user sequentially adds a polo shirt, a jacket, a pair of trousers and a pair of shoes.

Using RFID tags, we simulate how the system detects and incorporates the incoming clothes, making them available to the system to gather information, perform analysis and present results.

The RFID reader was attached to the RaspberryPi throug the GPIO pins.

A Python script interfacing with the [MFRC522](https://github.com/mxgxw/MFRC522-python) reader via [SPI](https://github.com/lthiery/SPI-Py) performed a GET request to an [Express](http://expressjs.com/) server running on top of Node.js. Thanks to [socket.io](http://socket.io/) library, the user inteface was updated every time a request was made.

## Future improvements

![RFID Connection Diagram](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/Smart_Closet_Setup_bb.jpg)

Implementing an smart advisor using efficient machine learning classifiers that provide best recommendations is key to success.

There are [many approaches](http://eia.udg.edu/~blopez/publicacions/montaner-aireview03.pdf) to this, so finding one that performs great wold present both a difficult and rewarding challenge. 

Integrating other sources of data, such as weather forecasts or planned events from a calendar will tailor the recommendations even further, rising the *smart* aspects of the application to higher levels.

A big data infrastructure will need to be architectured to both collect and analyse data generated by the closets. 

That will provide textile companies with insights on aspects of the clothing lifecycle currently unreachable, such as how many times a piece of clothes is weared, how much does it last, or how often it is combined with other clothing.

Finally, an smart cross selling module will anticipate the customer needs, offering advise on both new purchases and replacement of end of life garments.

# The presentation

![Smart Closet team in front of the jury](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/presentation.jpg)
 
The jury was formed by **Jorge Arévalo**, Software Developer from [Reclamador](https://www.reclamador.es/), **Adolfo Sanz De Diego**, CEO and founder of [Hackathon Lovers](http://hackathonlovers.com/) and **Reka Nikoletta**, founder of coaching agency [Reka Nikoletta Gazda](http://www.rekanikoletta.com/).

The pitch started with an introduction by Jesús San Román, continued with a technical description by Fernando Álvarez-Uría and finished with business details by Javier Yuste.

Once we concluded our pitch, the jury asked some questions related to both economic and technical aspects of the project, and gave recommendations on how to improve the presentation itself as well.

**[Download the presentation](https://raw.githubusercontent.com/fauria/smart-closet/master/Smart-Closet-Presentation.pptx)**

# Awards

Our project was awarded the first prize, along with the following items:

## IE Powerbank
![IW Poerbank](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/powerbank.jpg)

## Coaching Session
![Coaching Session Voucher](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/coaching_voucher.jpg)

## Week session
![Language Week Voucher](https://raw.githubusercontent.com/fauria/smart-closet/master/assets/language_voucher.jpg)

We were really satisfied with our achived performance and the quality of the products delivered, given such a short period of time.

# Coverage

> Hackevents

### Announcment: [C.A.R.S. Hackathon](http://www.hackathonspain.com/calendario/c-r-s-hackathon/)

> Hackathon Spain

### Announcment: [CARS: Hack-A-Thon](http://hackevents.co/hackathon/spain/madrid/1490-cars-hack-a-thon)
