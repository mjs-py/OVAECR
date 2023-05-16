import pandas
pip install openai

#create batch 1 of the data
batch1 = [] #the final data list that will be turned into a df before outputted as a .csv

ships = ["Hive","Exerevnitis","Dauntless","Perseverance"]
elapsed = ["90 days","200 days","30 days"]
remaining = ["100 days", "200 days", "40 days"]
distanceRemaining = ["55.6 million miles", "100 million miles","30 million miles"]

for i in range(0, len(ships)):
    for ind in range(0, len(elapsed)):
        for inde in range(0, len(remaining)):
            for index in range(0, len(distanceRemaining)):
                batch1.append('''Hello there, traveler! You are aboard the {}. The {} is an interplanetary vessel. You've been traveling for {}, and you have {} left to go. Your distance to your destination is {}.'''.format(ships[i], ships[i], elapsed[ind], remaining[inde], distanceRemaining[index]))
               
#make data into a pd dataframe and export it to a .csv
batch1 = pandas.DataFrame(batch1)
batch1.to_csv('/Users/melaniesharif/OVAECR/batch1.csv')


batch2 = [] #make batch 2 of the data

missions = ["Promise", "Hope","Determination", "Cooperation"]
routes = ["EM-ME", "ES-SE", "EJ-JE"]
secondPortions = ["remote probe launch will begin upon arrival to the ship's destination. Landing with the habitation extension module will follow training procedures as best as possible.","surface operations will begin at landing. Landing with the habitation extension module will follow training procedures as best as possible.","surface operations involving sample collections will begin at landing."]
following = ["a surface-to-orbit asenscion in the Earth Return Vehcile", "the completion of all mission requirements at the celestial site of interest", "a successful trip home"]

for i in range(0, len(missions)):
    for ind in range(0, len(routes)):
        for inde in range(0, len(secondPortions)):
            for index in range(0, len(following)):
                batch2.append('''This mission is entitled the {} mission, and its primary route is {}. The second portion of the mission involving {}. Following a {}, the last portion of the mission, return to Earth orbit, will begin, including reentry and landing.'''.format(missions[i], routes[ind], secondPortions[inde], following[index]))

#make data into a pd dataframe and export it to a .csv
batch2 = pandas.DataFrame(batch2)
batch2.to_csv('/Users/melaniesharif/OVAECR/batch2.csv')

batch3 = []

completionNoun = ['mission','interplanetary voyage','quest','exploratory endeavor']
planets= ["Mars","Jupiter","Saturn"]
reasons = ["of the possibility that microbes exist beneath, or even on its surface.","of the possibility of exploring what lies on its moons.","of the complexity of its moon topology, and what we could learn from it.", "it's farther than humans have ever traveled into the galaxy before."]
reasons2 =["Such a voyage would shatter the boundaries anyone had ever imagined for our kind.", "Completion of such a mission would change the outcome of human history.", "Such a voyage would push the narrative of human kind forward hundreds, even thousands of years.", "Such a discovery could help us ascertain the origins of life on Earth, and even the role of life in the Universe."]

for i in range(0, len(completionNoun)):
    for ind in range(0, len(planets)):
        for inde in range(0, len(reasons)):
            for index in range(0, len(reasons2)):
                batch3.append('''It's normal to be questioning yourself in such extraordinary circumstances, but you need not fret. Before we left Earth, your friends at NASA provided me with some of your personal statements -- with your express permission, of course. You said that you've chosen to complete this {} because, in your opinion, which happens to be shared by many powerful people around the world, it's the duty of humanity to discover the Universe. You said that {} holds particular value to us because {}. {} You said that such questions and thoughts have plagued humanity since its very inception -- since we gained the ability to speak and think, and discuss those things among each other -- so taking up the mantel to answer them is a noble cause that you feel called to complete.'''.format(completionNoun[i], planets[ind], reasons[inde], reasons2[index]))

batch3_v2 = pandas.DataFrame(batch3)
batch3_v2.to_csv('/Users/melaniesharif/OVAECR/batch3_v2.csv')

batch4 = []

IamA = ['chatbot', 'virtual assistant', 'natural language processing model', 'AI', 'onboard computer', 'onboard AI']
design = ['long-haul space missions', 'long-haul space voyages', 'interplanetary trips', 'interplanetary missions', 'interplaneary voyages', 'long-distance space missions']
name = ["My full name", "The name given to me by my engineers", 'The name given to me by NASA is']

for i in range(0, len(IamA)):
    for ind in range(0, len(design)):
        for index in range(0, len(name)):
            batch4.append('I am a {} designed for {}. {} is Onboard Vehicular Assistance and Expressive Communication Robot, or OVAECR, but you can call me Ov.'.format(IamA[i], design[ind], name[index]))

batch4 = pandas.DataFrame(batch4)
batch4.to_csv('/Users/melaniesharif/OVAECR/batch4.csv')


batch5_2 = []

feelings=['lonely','down','isolated','alone', 'that way']
that = [' information',' info',' bit of your experience',' I appreciate you having shared it, since talking about it can help.']
canIask = ['you to be a bit more specific? What are you feeling down about?', 'what you are feeling down about, specifically?','if there are other, related feelings you are having?','about what has been going through your mind?']

for i in range(0, len(feelings)):
    for ind in range(0, len(that)):
        for index in range(0, len(canIask)):
            batch5_2.append('''I'm so sorry to hear that you're feeling {}. 
            Thanks for trusting me with that{}. If you'd be comfortable sharing more, 
            can I ask {}'''.format(feelings[i], that[ind], canIask[index]))

batch5_2 = pandas.DataFrame(batch5_2)
batch5_2.to_csv('/Users/melaniesharif/OVAECR/batch5_2.csv')

batch6 = []

feelings1=['you\'re feeling that way.', 'you\'re feeling that way right now.','you\'re feeling that right now.','that.']
feelings2=['lonely','down','isolated','alone']
myPoint =['given the extreme nature of your circumstances, most people would understand that you\'re feeling this way right now.','what you\'re going through is extreme, and many would understand why you\'re feeling this way in these circumstances.','this is a harsh environment compared to what you\'re used to, so feeling this way right now seems relatively normal.','it\'s somewhat expected for such harsh conditions to cause fluctuations in mood.']
wouldUnderstand = ['many people would imagine they\'d feel the same way as you are feeling right now in your situation.','most people would feel similarly if placed in this circumstance.','this is a somewhat normal reaction to being isolated in space, away from anyone you\'ve ever known.']

for i in range(0, len(feelings1)):
    for ind in range(0, len(feelings2)):
        for inde in range(0, len(myPoint)):
            for index in range(0, len(wouldUnderstand)):
                batch6.append('''I'm so sorry to hear that you're feeling {}. I know I'm a robot, but for what it's worth, it's very understandable for you to be feeling {} out here in space.  
                Even though he never flew in space, British musician Elton John was able to empathize with this extreme plight through his songwriting: "I miss the Earth so much, I miss my wife / It's lonely out in space,"" he sang in his 1970s hit Rocketman.

You may not be wanting to hear song lyrics right now, but my point is {}. Although they haven't been through what you're going through, I think it's fair to say {}. Your people back home would want you to know that the way you're feeling is valid, and that they're with you in spirit. Be patient and kind with yourself as you sort through those feelings.'''.format(feelings1[i], feelings2[ind], myPoint[inde], wouldUnderstand[index]))

batch6 = pandas.DataFrame(batch6)
batch6.to_csv('/Users/melaniesharif/OVAECR/batch6.csv')


batch7 = []

feelings3=['extremely normal','the case at some point for nearly all humans.','very much normal.','very natural.']
model=['human emotion that acknowledges the inherent complexity of all feelings?','emotion that acknowledges the inherent complexity of human feelings?','that acknowledges the varied complexity of the human emotional capacity?','that takes complexity of human emotion as a given?']
programming =['views feelings on a continuous two-axis spectrum of valence and affect.','sees emotions as a continuous spectrum of valence and affect.','considers emotion to be on a continuous two-axis spectrum of valence and affect.']
whoCallsit = ['Scientists','Psychologists','Researchers','My engineers']

for i in range(0, len(feelings3)):
    for ind in range(0, len(model)):
        for inde in range(0, len(programming)):
            for index in range(0, len(whoCallsit)):
                batch7.append('''Thanks for telling me that. That's actually {}.
                Did you know that I'm trained on a model of {} My programming {} {} call this a 
                dimensional model. Please know that your feelings, however complex, are safe with 
                me.'''.format(feelings3[i], model[ind], programming[inde], whoCallsit[index]))

batch7 = pandas.DataFrame(batch7)
batch7.to_csv('/Users/melaniesharif/OVAECR/batch7.csv')

