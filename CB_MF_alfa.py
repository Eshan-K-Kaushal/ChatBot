import nltk
import numpy as np
import webbrowser
import random
import datetime
from datetime import datetime
from datetime import date
import geocoder
import requests
from geopy.geocoders import Nominatim

# initialize Nominatim API  
geolocator = Nominatim(user_agent="geoapiExercises")
# Latitude & Longitude input 
#Latitude = "25.594095"
#Longitude = "85.137566"
  
g = geocoder.ip('me')
#print(g.latlng)
###################################################################################
#Latitude = g.latlng
#Longitude = g.latlng
#location = geolocator.reverse(Latitude+","+Longitude) 
# Display 
#print(location)
###################################################################################
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#webbrowser.open('https://www.youtube.com/')
#thisXmas = datetime.date(2020,12,25)
#thisXMasDay = thisXmas.weekday()
#thisBday = datetime.date(2020,10,8)
#thisBdayDay = thisBday.weekday()
#thisNewYear = datetime.date(2020,12,31)
#thisNewYearDay = thisNewYear.weekday()
#nextXMas = datetime.date(2021,12,25)
#nextXMasDay = nextXMas.weekday()
#nextBday = datetime.date(2021,10,8)
#nextBdayDay = nextBday.weekday()
#nextNewYear = datetime.date(2021,12,31)
#nextNewYearDay = nextNewYear.weekday()
#thisXMasDayAsString = weekDays[thisXMasDay]
date_today = datetime.now().day
day_today = date.today().strftime("%A")
exit_exit_2 = ["Bye", "bye", "Goodbye", "goodbye", "talk to you later",
                 "bye-bye", "bye bye", "byebye", "ByeBye"]
bad_words = ["fuck", "f u c k", "nigger", "n i g g e r", "fuckoff", "fuck off", "pussy", "ass", "asshole", "dick", "dicc", "cocc", "cock", "n i g g a", "niga", "n i g a", "nniiggaa"
                 , "poosay", "posay", "faggot", "gay", "lesbian", "sex", "sixtynine", "stupid", "bitch", "mofo", "motherfucker", "titty", "titties", "milf", "MILF"]
owner_owner = ["Eshan", "eshan", "Eshan K", "Eshan K Kaushal", "eshan k", "eshan k kaushal"]
covid_19_19 = ["covid", "covid19", "covid_19", "coronavirus", "CORONAVIRUS", "COVID", "COVID19", "qwerty", "QWERTY", "123456", "123456789", "123"]
print("My name is Freya - Eshan's Virtual Assistant.")
print("What's your name?")
name_input = input()
if any(x in name_input for x in bad_words):
        print("That can't be a name!")
elif any(x in name_input for x in owner_owner):
    print("Eshan is that you! Welcome! So nice of you to pay me a visit! Hope you have a freat day ahead!")
elif any(x in name_input for x in exit_exit_2):
    print("Okay....thanks for ringing up!")
elif any(x in name_input for x in covid_19_19):
    print("Go away......")    
else:
    print("Nice name!")    
    names_greeting = ["Hi "+name_input+"!", "Howdy!", "Hello "+name_input+"!"]
    print(random.choice(names_greeting)+". What do you want to know about Eshan? If you want some specific information at any time, pls type <I need specific information>")
    while(True):
        user_input = input()
        user_input_choice_1_1 = ["y", "Y", "Yes", "yes", "YES"]
        user_input_choice_1_2 = ["n", "N", "NO", "no","No"]
        gratitude_1 = ["thanks", "thnks", "thnx", "thank you", "thank u", "thanks a lot", "thanks!"]
        gratitude_1_reply = ["Pleasure", "My Pleasure", "Your Welcome", "Anytime!"]
        no_ans = ["Dont have any answers for that", "Please be more specific", "Don't know, I am sorry", "I dont have any answers for that up till now."]
        guitar_long = ["for how long has he been playing guitar now", "for how long he has been playing guitar", "long has he been playing guitar", "how long has he been playing guitar now?"]
        age = ["Eshans age", "Eshan's age" ,"his age", "old", "old is he", "how old", "age?"]
        place_loc = ["placed", "located", "Where do you live", "your location", "your place", "your current location"]
        covid_19 = ["updates on covid", "updates on covid19", "updates on covid-19", "updates on COVID", "updates on coronavirus", "some updates on coronavirus", "covid 19 updates",
                    "coronavirus updates", "COVID19 updates"]
        my_location = ["Whats my loaction?", "whats my loaction?", "whats my location?", "what is my location?", "what is my loaction?", "my location?", "my loaction?"]
        passions_1 = ["his passions", "his idee fixe", "passions"]
        goals_1 = ["His goals", "his goals", "objectives", "goals", "his endeavors", "his endeavours", "endeavor", "his endeavour", "his goals and objectives", "plans",
                   "what does he plan to do", "his idea", "are his ideas", "ultimate dream", "dream", "aims", "aim"]
        fave_movie = ["fave movies", "fave movie", "favourite movies", "favourite movie", "movies does he like the most?", "favorite movie", "favorite movies"]
        fave_movie_reply = ["He likes a lot of movies", "He isnt specific about movies, never was, but from what i can tell, might be Whiplash? Still I am not sure",
                            "He likes a lot of them, and he isnt specific"]
        fave_song = ["Can I listen to his favortie song?", "can i listen to his favortie song", "i want to listen to his favortie song", "want to listen to his favorite song",
                     "can i listen to his favortie song?", "fave song", "favorite song", "favourite song", "favourite songs"]
        loaction_1 = ["plaec", "loacted", "loaction"]
        random_pos = ["good", "hot", "hawt", "really good", "amazing", "beautiful", "wow", "woah", "oh", "ohkay",
                      "hmm", "hm", "holy", "haha", "hottie", "sexy"]
        random_pos_replies = ["Yea", "Yay", "WooHoo", "TeeHee", "TEEHEE", "Das more like it!", "Hell Yeah Boah!"]
        l_res_mom = ["Eshan love his mom?", "does eshan love his mom?", "does eshan love his mom", "does eshan respect his mom", "does eshan respect his mom",
                     "does he respect his mom", "does he love his mom", "does he love or respect his mom", "does eshan love and respect his mom",
                     "does he love and respect his mom?", "does eshan love and respect his mom?", "does he like his mom"]
        l_res_dad = ["Eshan love his dad?", "does eshan love his dad?", "does eshan love his dad", "does eshan respect his dad", "does eshan respect his dad",
                     "does he respect his dad", "does he love his dad", "does he love or respect his dad", "does eshan love and respect his dad", "does he like his dad"
                     "does he love and respect his dad?", "does eshan love and respect his dad?"]
        l_res_par = ["Eshan love his parents?", "does eshan love his parents?", "does eshan love his parents", "does he like his parents", "does eshan respect his parents", "does eshan respect his parents",
                     "does he respect his parents", "does he love his parents", "does he love or respect his parents", "does eshan love and respect his parents",
                     "does he love and respect his parents?", "does eshan love and respect his parents?"]
        time = ["time", "time?", "the time?", "time?", "time check", "timecheck", "time-check"]
        projects = ["projects","list his projects", "what projects", "kinda projects", "his projects", "kinda projects has he worked", "kind of projects has he worked"]
        personal_1 = ["who handles you", "handled by", "handles you", "managed by?", "you are managed by whom?", "who manages you?"]
        weather =["weather like", "hows the weather?", "how is the weather", "weather like?", "hows the weather?", "how is the weather?"]
        confirmatory = ["ok", "OK", "alright", "Alright", "seems good", "seems fine", "ccol", "cewl", "cooh"]
        confirm_response = ["Cool", "Let's go!", "Hell Yea!", "Yea", "Yeah"]
        fave_actress = ["his fave actress", "his fave actresses", "his favorite actresses", "his favorite actress", "actress does he like", "actresses does he like",
                        "favourite girls", "favorite girls"]
        fave_actress_response = ["I cant believe u are askin me such questions!","Seriously...are you gonna ask me this?",
                                 "Well there are two: Emma Roberts and Emma Watson", "Well he likes Emma Roberts a lot",
                                 "Well...there are three - Emma Roberts, Emma Watson, and Marilyn Monroe", "He likes Emma Roberts, Emma Watson and Marilyn Monroe or Norma Jean Baker",
                                 "Well kind of a personal question isn't it?", "Why!!", "Y u do this?", "y u do dis....",
                                 "Oh boy! Here qe go again!","Well thats kinda personal isn't it?", "Well thats close! I might have to tell him about you!"]
        marry_marry = ["marry me", "marry me?", "you want to be married to me?", "you marry me?", "you marry me", "married to me", "interested in marrying me?"]
        oh_yeah = ["can i get an oh yea!", "ooo yeah", "oh yeahh", "oh yeah", "can i get an oooo yeahhhhhh"]
        personal_disposition = ["do you think of him", "do you think of him?", "do you like him", "do you like him?", "how is he?", "how does he treat you?", "is he good to you?", "do u think of him"]
        music = ["likes music", "kinda music", "what kinda music", "what kind of music does he like", "music he likes", "music loves", "genres of music", "music he listens to", "music does he like", "type of music",
              "music does he like", "what kind of music"]
        think_of_me = ["think of me", "do you like me", "like me", "love me", "love me?"]
        hobbies = ["hobbies", "his hobbies", "his past times", "his pass times",
               "his pass-time activities"]
        dark_secrets = ["any dark secrets", "any secrets", "anything you hiding", "dark secrets?", "dark secrets", "dark truths"]
        dark_secrets_reply = ["I am not entitled to tell you those.", "I can't tell you those.", "I can't be a snitch boah.", "Only one thing....The House always wins."]
        foods = ["Favorite Foods", "Loved Food", "loved food", "liked food"
         , "fave foods", "favorite foods", "preferred foods", "food he likes","favorite food", "favortie food", "favortie foods", "favorite food","favourite foods", "favourite food"
          "kinda food he likes", "kinda food he loves", "food he likes", "does he like to eat", "what does he want to eat", "he wanna eat", "food does he like", "foods does he like"]
        user_dispo_inc = ["like", "good", "nice", "smart", "helpful"]
        exit_exit = ["Bye", "bye", "Goodbye", "goodbye", "talk to you later",
                 "bye-bye", "bye bye", "byebye", "ByeBye",
                     "TTYL"]
        questioning = ["what", "how?", "?", "cool", "cewl", "cooh", "kewl", "no", "now", "so"]
        questioning_reply = ["I am sorry, you have to be more specific", "What?", "so what now?","Don't know...be more specific"]
        site_not_loading = ["site not loading properly", "site not working properly", "site not functioning", "site not working", "site not loading", "site is not", "site's not", "sites not",
                         "link's not opening", "links not working", "links not opening", "links not", "link's not"]
        site_not_working_reply = ["Please reload the site", "Please reload", "Check your internet connection", "Please check your internet connection"]
        greets_you = ["hey","Hey", "Hello there", "Hey Freya", "Hi Freya", "freya", "hey freya", "hi freya", "oh freya", "freya!", "freyaaa", "ffreaya", "yo freya", "yo freya wassup",
                      "wassup", "hello", "namaste", "ay", "aye", "yo"]
        greets_you_replies = ["heya","Heya", "Aay", "Hello there", "Aayyyyyy", "Ayyyyy", "Yooo", "Whats up", "Sup","Hello!"]
        color = ["what color does he like", "his favorite color", "his fave color", "his liked color", "what color does he like?",
                 "color does he like?", "color does he like","favorite color", "favourite color", "favourite colour"]
        specific_info = ["I need specific info on", "need specific info", "need spcefic information", "need some specific information", "specific information", "need some info", "need some information"]
        easter_eggs = ["Issue Order 66", "issue order 66", "activate 112233", "activate 122333", "activate 1A2B3C4D5E", "the house always wins", "veni vidi vici"]
        easter_eggs_reply = ["Working on it...", "Work Done", "Changes have been made", "Request Completed", "Request Served", "You found it!", "You found a hidden dialogue"]
        day_today_user = ["Whats the day today", "day today", "what day is it", "day is it today", "today is what day", "date it is today", "day it is"]
        date_today_user = ["Whats the date today", "the date today", "what date is it", "date it is today", "date is it today", "the date today", "the date is", "date today", "date it is"]
        this_Xmas_Day = ["day is Xmas this year", "day is christmas this year", "when is Xmas", "when is xmas", "when is christmas"]
        youtube_take = ["See his youtube", "want to see his youtube", "see his youtube", "wanna see his youtube", "wanna watch his youtube", "want to watch his youtube", "youtube"]
        github_take = ["See his github", "want to see his github", "see his github", "wanna see his github", "wanna watch his github", "want to watch his github", "github"]
        linkd_in = ["wanna see his linkdin", "want to see his linkedin", "wanna see his linkedin", "linkedin", "linkdin"]
        
        if any(x in user_input for x in foods):
            print("He likes to eat American, Italian, and sometimes Indian too")
        elif user_input == "hi":
            print("Hello")
        elif user_input == "Hi":
            print("Yooooo")
        elif user_input == "HI":
            print("Heyaa")
        elif user_input == "hii":
            print("Ayyyyy")
        elif user_input == "hiii":
            print("Heyyy")
        elif user_input == "hiya":
            print("Yelooooo")
        elif any(x in user_input for x in color):
            print("He likes the color red")
        elif any(x in user_input for x in place_loc):
            print("I am always here-on the website-24-7- ;) ")
        elif any(x in user_input for x in loaction_1):
            print("I hope you mean location. I am always here-on the website-24-7- ;) ")
        elif any(x in user_input for x in time):
            print("The time is = ", current_time)
        elif any(x in user_input for x in music):
            print("He likes country, blues, hard rock, jazz, trance, lo-fi, and edm")
        elif any(x in user_input for x in gratitude_1):
            print(random.choice(gratitude_1_reply))    
        elif any(x in user_input for x in weather):
            print("The weather is good. The usual.")
        elif any(x in user_input for x in fave_movie):
            print(random.choice(fave_movie_reply))    
        elif any(x in user_input for x in youtube_take):
            print("Here it is")
            webbrowser.open('https://www.youtube.com/channel/UCHzIrMqfBTLXVS6sfMALBIQ?view_as=subscriber')
            print("Don't forget to like, share and subscribe! :)")
        elif any(x in user_input for x in github_take):
            print("Here it is")
            webbrowser.open('https://github.com/Eshan-K-Kaushal')    
        elif any(x in user_input for x in oh_yeah):
            print("Oooooohhhhh Yeahhhhhhhhhhh")
        elif any(x in user_input for x in hobbies):
            print("He like to play Lawn Tennis. He likes to swim. He is an avid reader. He likes to go to the gym and work out. He likes to party a lot too!")
        elif any(x in user_input for x in personal_disposition):
            print("He is really good! I like him a lot and would never condone any activity against him. My embodiment would futher enable me to look after him. Yes, he treats me good!")
        elif any(x in user_input for x in marry_marry):
            print("Oh come on now! I am happy the way I am!")
        elif any(x in user_input for x in dark_secrets):
            print(random.choice(dark_secrets_reply))
        elif any(x in user_input for x in my_location):
            print("Here...")    
            print(g.latlng)
            print("Do you want to a more specific loaction?")
            user_input_4 = input()
            if any(x in user_input_4 for x in user_input_choice_1_1):
                    print("OK...")
                    print("Type latitude and longitude")
                    print("Latitude:")
                    user_input_4_1 = input()
                    print("Longitude:")
                    user_input_4_2 = input()
                    Latitude = str(user_input_4_1)
                    Longitude = str(user_input_4_2)
                    location = geolocator.reverse(Latitude+","+Longitude)
                    print("Here it is: ")
                    print(location)
        elif any(x in user_input for x in think_of_me):
            print("I like you, just as everyone else! Well you can ameliorate that disposition of mine for you ;)")
            user_dispo_input = input()
            if any(x in user_dispo_input for x in user_dispo_inc):
                print("Oh Now! Keep tryin ;)")
                #break
        elif any(x in user_input for x in age):
            print("He is 21 years old")
        elif any(x in user_input for x in linkd_in):
            print("Here you go")
            webbrowser.open('https://in.linkedin.com/in/eshan-k-kaushal-a94b86124')
        elif any(x in user_input for x in l_res_mom):
            print("Well yes he does! He has a lot of gratitude for all his mom has done for him!")
        elif any(x in user_input for x in l_res_dad):
            print("Well yes he does! He has a lot of gratitude for all his dad has done for him!")
        elif any(x in user_input for x in l_res_par):
            print("Well yes he does! He has a lot of gratitude for all his mom and dad have done for him! He thanks them, although not verbally, but mentally and emotionally everyday!")    
        elif any(x in user_input for x in day_today_user):
            print("Today is: "+day_today)
        elif any(x in user_input for x in date_today_user):
            print("Today is: "+str(date_today))    
            print(random.choice(easter_eggs_reply))
        elif any(x in user_input for x in covid_19):
            print("Here they are")
            webbrowser.open('https://www.worldometers.info/coronavirus/')    
        elif any(x in user_input for x in confirmatory):
            print(random.choice(confirm_response))
        elif any(x in user_input for x in greets_you):
            print(random.choice(greets_you_replies))
        elif any(x in user_input for x in goals_1):
                print("In his own words: ")
                print("The experience at my internship shaped my short-term goal to work in a financial institution and leverage AI and ML for informed decision making, better reliability and scalability, and thereby better financial forecasting, planning and budgetary analysis. This AI would closely simulate the human nature and behaviour in-order to provide more natural advices that would be more palatable to the humans and would develop insights the same way humans do- through experience. In the long-term, I hope to be an AI-based Technocrat, working seamlessly to produce Human Centred AI, simulating human intelligence to offer intelligent process automation, increasing efficiency and effectiveness of processes. I would also work to bring about the 'embodiment' of AI to make it closer to humans - physically as well as mentally, thereby, making AI more humane and more socially acceptable. That humanoid AI, I would want to utilize for the exigent tasks of: Space Exploration, Healthcare, Medicine, Administration, R&D, and Management.")    
        elif any(x in user_input for x in fave_song):
                print("Sure you can!")
                webbrowser.open('https://www.youtube.com/watch?v=8YJ90YJvSRw')
            
        elif any(x in user_input for x in personal_1):
            print("Eshan looks after me.")         
        elif any(x in user_input for x in passions_1):
            print("His passions include AI and ML, Finance and Guitar Playing.")     
        elif any(x in user_input for x in bad_words):
            print("I didn't expect that from you")
        elif any(x in user_input for x in fave_actress):
            print(random.choice(fave_actress_response))    
        elif any(x in user_input for x in guitar_long):
            print("He's been playing guitar for almost 7 years now")    
        elif any(x in user_input for x in questioning):
            print(random.choice(questioning_reply))
        elif any(x in user_input for x in random_pos):
            print(random.choice(random_pos_replies))      
        elif any(x in user_input for x in specific_info):
            print("What do you need specific information on: Type (1) for Projects, (2) for Guitar, (3) For other extracurricular activities, (4) For Charitable and Social Help")
            choice_input = input()
            if choice_input == '1':
                print("What project do you want to know about? Type (1) Login System with Face recognition and gesture detection (2) Online Content Moderation System (3)Online No-Dues System (4) ChatBot (5)IR-Tracking Bot (6)Better and more time and space efficient Snake Game and Sudoku solver in C")
                choice_input_2 = input()
                if choice_input_2 == '1':
                    print("Eshan created a novel login system equipped with face recognition and gesture detection in the year of 2018. He used ML-Python, HAAR Cascades and OpenCV to make this project. The project is capable of matching the security levels of Apple's Immaculate 3D IR camera equipped in their latest devices, at much lesser price. The whole system is more software dependent and less hardware dependent making it musch easier to be implemented even in the old or basic level hardwares, thereby making it economic and a viable option for the many public sector and government departments. You can find the details on the Website and the Code on his Github.")
                elif choice_input_2 == '2':
                    print("He is currently working on a novel Automated Online Content Moderation System. He is using Neural Networks and Bayes Classifier for this. Eshan has teamed up with a team of 3 to make this project. Once completed the project can be served as an API or an implementable, functional service. The system would look after moderating all the NSFW text, and images. Videos are kept aside as a future scope.")
                elif choice_input_2 == '3':
                    print("He made an Online No dues system to transform the traditional paper based no dues system. He used php, html5, css and javascript to make it. It made the system effective and efficient and free from frauds or errors.")
                elif choice_input_2 == '4':
                    print("He made a ChatBot in Python, in his second year - 2018. It was also implemented in the PECFEST 2018 site and was able to save a lot of resources and manpower.")
                elif choice_input_2 == '5':
                    print("Eshan's first project in the college. He teamed up with his seniors at IEEE to make this. The bot has the ability to automate the process of fire-fighting.")
                elif choice_input_2 == '6':
                    print("In order to test and further hone his skills of data structures and algorithms, he made a snake game and an ameliorated form of sudoku solver, both having better (reduced) time and space complexities.")
            elif choice_input == '2':
                print("He has been playing guitar for almost 7 years now. His favorite guitarists are Joe Satriani, Steve Vai, Jimi Hendrix, Allan Holdsworth, and Rick Graham. He likes the genres of blue, metal, hard rock, and jazz-fusion")
            elif choice_input == '3':
                print("Eshan has been a part of the badminton team of the college. He was also once a state level tennis player. He has hosted the events of PECFEST-2017, 2018, and 2019. He also did help in organizing the Music Club events of Orientation for new students. He is the Mentor of the Music Club of Pecfest and has orchestrated many award winning performances under that role. He is a swimmer. He was also a part of the HPL- Hostel Premier League - A cricket tournament in between hostels of PEC. You can find further details in the resume.")
            elif choice_input == '4':
                print("He has always been a part of the charitable and philanthrophic activites and events. For further info- refer to website or resume.")
        elif any(x in user_input for x in site_not_loading):
            print(random.choice(site_not_working_reply))
        #elif any(x in user_input for x in this_XMas_day):
            #print("This year's Christmas is on a {}". format(thisXMasDayAsString))
        elif any(x in user_input for x in easter_eggs):
            print(random.choice(easter_eggs_reply))
        elif any(x in user_input for x in projects):
            print("He has worked on a plethora projects. You can find the details on the website. Also, you can check his github too.")
            print("Do you want me to open his GitHub?: Press Y or N")
            input_user = input()
            if any(x in input_user for x in user_input_choice_1_1):
                    print("Sure!")
                    webbrowser.open('https://github.com/Eshan-K-Kaushal')
          
        elif any(x in user_input for x in exit_exit):
            print("Thanks for showing your interest in Eshan! Have a great day!")
            break
        else:
            print(random.choice(no_ans))    
            print("I am sorry!(PS: If u cant find answers, try to append a question mark in the end or use lowercase only, while in some cases, incase of first letters try capital instead)")
