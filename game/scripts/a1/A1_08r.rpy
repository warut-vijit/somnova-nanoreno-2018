#For replacing later:
#clubempty = "Default club indoor (before/after work)"
#club = "Default club indoor (during work)"
#alley = "Back alley"
#ARTech = whatever we decide to call the company Roman used to work for.
#knock.ogg - knocking on an interior door
#scene8rmusic = various music tracks, which aren't yet delivered. Followed by a general mood or tone.

label A1_08r: 

   show bg_black
   #play music scene8rmusic #(Relaxed, but tired, and not happy. Roman feels washed up. A husk, after the preceding events.)

   "If the last few weeks were a blur, the one that follows them is more like white noise."
   "Coming into work, waiting tables, and leaving passes by without notice, without any thought."
   "If I talk to Eris at all, it's never more than a grunt, and is forgotten within ten minutes."
   "After a few days, this mental quagmire starts to become unbearable."

   show bg_club_2_before_work with Dissolve (0.25)

   "I approach the door behind the bar, leading to Parker's office, and knock."
   #TODO play sound knock.ogg

   "After a few seconds, the door opens, and Parker emerges, closing the door behind him."

   show parker p1 e3 at center_left
   
   parker "Roman. Everything all right?"

   roman "Oh, yeah, everything's fine."

   "Not sure why I said that when it so clearly isn't. On the other hand, I don't know what exactly I wanted to say."

   roman "I was - eh - just wondering what happened to the whole employee of the month thing."

   parker p1 e2 "Oh, right. That."
   parker "Yeah, that didn't work out too well, did it?"
   parker "I was really hoping one of you would come up with something that worked."
   parker p1 e1 "I mean, not to be a dick about it, it would just be easier to pick a winner that way."
   parker p1 e2 "If you want to be employee of the month, Roman, then I'll print you off a certificate. I'm not doing the bonus, though."

   "This seems unusually harsh for Parker - but then, he does look unusually tired."

   roman "Nah, Don't bother. I know we didn't earn it. The club's exactly how it was before."

   parker p1 e1 "It's not that, Roman. I mean, sure, some new draw for this place would be nice."
   parker "I was hoping that it would just engage you a bit, is all. Get rid of all this despondence."
   parker "And it did for a bit. I saw that fire in you, felt the heat of it. But it didn't last... I was really hoping it would."

   "This throws me for a loop."

   roman "What are you talking about?"

   parker "I appreciate your passion for jazz, and the club's sensibilities in general. Not many people care about it any more."
   parker  "I thought we could really harness that, but it didn't work out. It's a shame."

   roman "This is all {i}very{/i} on the nose."

   "He shrugs."

   parker p1 e2 "Anyway, sorry for the employee of the month thing going down the crapper."
   parker "Maybe we'll try again next month, if you stick around."

   "But judging from his lack of enthusiasm, that seems unlikely."

   parker p1 e1 "Do you need anything else, then, Roman? I was in the middle of some paperwork."

   roman "No, I don't think so."

   parker "Good. See you around."

   hide parker with Dissolve(0.5)

   "He closes the door, and I turn to leave - but as I do, I see someone else approaching the bar."

   show eris p1 e1 at center_right

   eris "Were you just talking to Parker?"

   "She starts talking at me without any introduction."

   roman "Yeah. So?"

   eris "I wanted to ask him about the employee of the month thing."

   roman "Wow, we're so in sync."
   roman "I just asked. It's off."

   eris "Oh."
   eris "Right."

   roman "Did you think you might have won?"

   eris p2 e5 "No, actually. I was going to concede. I didn't deserve it."

   roman "Weird, that's exactly what Parker said."

   eris p2 e3 "...He said that?"

   roman "Yeah. It was kind of out of character, actually. He got very real with me."
   roman "Told me he felt really disappointed in you, and that you might as well resign. Also said he never liked you anyway and that you've got a huge- "

   eris p2 e5 "Hilarious, Roman. I've- "

   "But cutting her off, Parker appears once again from the office."

   show parker p1 e1 at center_left

   "He notices us."

   parker p1 e4 "Oh, is this bar where the cool kids hang out after work now? I had no idea."
   parker "I'm going out for a bit. Keep an eye on the place?"

   hide parker with Dissolve (0.5)

   "Parker strides towards the exit."

   eris p1 p1 e1 "Hold on! The competition, Roman won't give me a straight answer!"

   parker "It's off!"

   "He shouts over his shoulder, as the door closes behind him."

   eris p1 e1 "Charming."

   "After a few seconds, Eris walks back around to the other side of the bar, pulls out a stool, and perches herself upon it."

   eris p2 e5 "Kiwi mojito."

   roman "Ooo..kay. Your choice of rum?"

   "Eris gives me a withering look that very clearly says, 'Do I look like I give a shit?'"
   
   "After a few minutes, most of which was spent digging around in a cupboard under the bar for kiwi-flavoured syrup, I slide a luminous green drink in front of her. She takes a sip."

   eris p2 e3 "This is dreadful."

   roman "Just because I like jazz doesn't mean I know how to mix a drink. People take courses for that, you know? You can get certificates for it and everything."

   "She takes one more tentative sip, before moving it to one side."

   eris p3 e9 "It {i}is{/i} disappointing, though. I wish it could have gone better."

   roman "I know, Eris. We've been through it all so many times."

   "I pinch the bridge of my nose."

   roman "It's time to move on."

   eris p2 e3 "Harsh."
   eris p1 e1 "But you're right."

   "She pulls the drink back towards her and takes another sip, looking hopeful - but appearing to regret it immediately."

   eris p2 e3 "How much rum did you put in this thing?"

   roman "I dunno. About up to there?"

   "I place a finger half way up the glass."

   eris p2 e7 "For fuck's sake."

   "And she tips the drink down a drain behind the bar."

   eris p3 e9 "It was just like the good old days for a little bit, though, wasn't it?"
   eris "The late nights and the takeout and the tiffs."

   roman "You look so happy thinking about past arguments."
   roman "Oh, and we didn't actually get any takeout. You can owe me one, if you like."

   eris "You put such a damper on everything."

   roman "..."

   "A silence grows between the two of us that I’m compelled to break."

   roman "Yeah, I guess in a way, for just a little while, it was like the old days."

   "I'm very careful not to say the old days were {i}good{/i}."

   eris p1 e1 "But you really don't miss it at all, do you?"

   roman "I've never flip-flopped on that, Eris. You seemed to think that I would have some sudden realisation that I'd made a huge mistake in quitting."

   eris p3 e8 "You got me."
   eris p1 e1 "I was hopeful."

   roman "I still don't really understand why. I have my life, and you have yours. Why does what I do with mine matter to you?"

   eris "I don't really know, and frankly I don't want to talk about it again. This topic always seems to end with an argument."
   eris "I'm not going to ask you to come back to ARTech again. I promise."
   eris "I mean, it would be pointless, wouldn't it?"

   roman "Didn't you pretty much just ask me if I'd come back again in saying that, though?"

   eris p2 e5 "Please, just for once would you shut up?"
   eris "Could you just take this seriously for a moment?"

   roman "Okay. Sorry."

   eris p1 e1 "Maybe you should just do whatever you want."
   eris "There's no point trying to make you see... and I don't think there's any point in trying to change this place either."
   eris "Leave the city if you like. You're right - it's nothing to do with me."

   "She gets up to leave."

   roman "Is that... everything you wanted to say?"

   eris p2 e3 "What more did you expect?"

   roman "I don't know."

   "I think for a moment."

   roman "Closure?"

   eris p1 e1 "What is there to close?"

   hide eris with Dissolve(0.25)

   "Giving me a look that I can't place, Eris departs. As she leaves, I hear her greet Parker, who heads back in towards the bar."

   show parker p1 e1 at center_right with Dissolve (0.5)

   parker "Just left my wallet."

   "He gestures towards the office, shuffling past me."
   "As he comes back out, flapping his wallet, he look at me in the face, apparently for the first time since re-entering the bar."

   parker "You okay there, Roman? You don't look great."

   "I make a vague attempt to adjust my face into a more ok-looking configuration, and feel it failing."

   roman "Yeah."
   roman "Well, no. But yeah."

   parker "I know the feeling well. There's a lot on your mind, right?"

   roman "I guess so."

   parker p1 e2 "Mm."

   "Parker looks me in the face for a moment, his eyes darting between mine."

   parker "I've got stuff to be getting on with, but don't be a stranger, okay? You can talk to me."

   roman "Thanks, Parker."

   "I don't have anything more to say. After another moment's pause, Parker leaves, too."

   hide parker with Dissolve (0.5)

   "My thoughts are not pleasant company, and my hollow-feeling stomach is no better."
   "I reach for a bottle of whiskey, but halt, my hand halfway there, hovering in place."        
   "..."
   "....."
   "Fuck it."
   "I grab a pint glass, and pour a beer."