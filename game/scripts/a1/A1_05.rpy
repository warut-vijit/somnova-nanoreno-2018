﻿label A1_05:
    show screen scene_number("A1_05")
    scene bg_club_2_after_work with Dissolve (1.0)
    $ queue_music(music_five)
    "After an hour or so of mindless busy-work that does nothing to lift my mood, I decide I need a break."
    "There's nothing else to do, and I can feel the events of the last few days gnawing away at my insides. Maybe some nicotine will solve my problems?"
    scene bg_back_alley with Dissolve(0.25)
    play audio backdoor_open
    "Outside, the grim sky darkens; the sun is quickly swallowed up by the city's towering skyline."
    "As I step through Arcady's backdoor, already rummaging in my pocket for a lighter and a cigarette I rolled while inside, I notice another presence in the alley."
    play audio backdoor_close
    "The heavy door swings shut behind me, and the figure whips around."
    show eris p2 e2 at center_right
    "I rein in a smirk. It seems to go unnoticed, and Eris quickly recovers."
    $ crossfade_music(1.0, 0.3, 0.5)
    eris p1 e1 "Oh, Roman."
    "A small pause."
    eris "Hello."
    roman "Hey, Eris."
    "I'm just about to give up on finding the cigarette when I realise I'd tucked it behind my ear."
    "I light up and take a puff."
    "Unfortunately, I fail to notice that Eris is downwind of me--and when I exhale, sighing in relief, she emerges from a faceful of smoke coughing and irritated."
    eris p2 e5 "What the hell, Roman?"
    roman "Shit, sorry Eris. That wasn't deliberate, I swear."
    eris p2 e5 "Are you sure about that?"
    roman "I swear. I didn't notice the wind."
    "I move across the alley so we're facing one another."
    show eris p1 e1 at centered
    "She seems to sense my sincerity and calms down a little."
    eris "Hmph."
    "As I take another drag, she watches curiously, puffing on her own e-cigarette."
    $ crossfade_music(0.3, 1.0, 0.5)
    eris p3 e3 "Where did you even get those?"
    roman "Huh?"
    eris "Like, if I wanted to buy a regular, {i}actual{/i} cigarette, I wouldn't know where to go. They don't sell them in convenience stores around here, do they?"
    roman "They don't?"
    eris p2 e7 "...Do you seriously live in the past?"
    roman "I'd like to."
    show eris p1 e10
    "Eris laughs loudly, and I absolutely see why. I actually chuckle a little myself."
    roman "Okay, that might have been a bit on-the-nose."
    eris p1 e6 "Yeah, just a little bit."
    eris "For real, though. Where do you get them?"
    roman "The corner shop under my flat still sells them; I didn't know it was unusual..."
    eris "Well, it is."
    roman "What, have you been trying to find them for yourself?"
    eris p1 e1 "Not really. I just notice these things. I always wondered about it back at ARTech when we took breaks together, but I never thought to ask."
    roman "Have you never tried a real cigarette or something?"
    eris p2 e4 "No. I'm not a fan of cancer."
    eris p1 e1 "I'm surprised those things are still legal."
    roman "You think with the amount of money tobacco companies are pumping into--"
    eris "Yeah, yeah, I know."
    eris p2 e3 "How can you be so cynical about it anyway? You're propping them up too."
    roman "Being cynical about the manipulation of our democracy by gargantuan, inhuman corporations and enjoying a little smoke from time to time are two completely different things."
    "I inhale arrogantly, making my grin as shit-eating as humanly possible. Eris still seems curious."
    $ crossfade_music(1.0, 1.0, 0.5)
    roman "...You want a go?"
    eris p1 e2 "Are you asking me if I want to have a go at inhaling millions of carcinogenic particles and altering my respiratory system--potentially irreversibly?"
    roman "Yeah."
    show eris p3 e9
    "She takes a moment to decide."
    eris p1 e1 "Fine."
    "She takes the cigarette from me, holding it in a way that clumsily mirrors how characters on TV might hold one."
    eris p2 e3 "...How do I--"
    roman "You literally just put it between your lips and breathe in. Make sure not to swallow the damn thing."
    roman "And don't just immediately blow the smoke out either; that's just wasting--"
    "But before I can finish, the cigarette is thrust back at me amidst a coughing fit. I try not to laugh..."
    "And fail."
    roman "Aw man, I didn't think it could be that extreme in real life..."
    "She tries to talk, but keeps coughing and clears her throat."
    eris p3 e8 "Ugh, Roman, that was vile! Why would you do that to yourself?"
    roman "I thought you liked the flavour of tobacco?"
    eris p2 e5 "That was {i}nothing{/i} like my vape!"
    roman "Well, yeah, they probably wouldn't sell many vapes if they were as gross as actual cigarettes."
    show eris p1 e6 at centered
    "I manage to get a laugh out of her."
    eris "You have a point."
    eris "So why do you smoke them?"
    $ crossfade_music(1.0, 0.3, 0.5)
    "I shrug."
    roman "Why do you vape your... vape?"
    roman "Wait, is that the word for it? And the noun at the same time? Or is there another word for using an e-cigarette?"
    eris p3 e9 "I... don't know. I don't talk about it that much."
    roman "Oh."
    roman "Well, I don't really know why I smoke; I've tried e-cigarettes and I just didn't like them. Too artificial."
    eris p2 e7 "Is it the same reason you work here, listen to jazz music, and drink expensive whiskey?"
    roman "It's not {i}always{/i} whiskey. Gin and brandy are fine too."
    eris p2 e5 "No. Really."
    roman "I just like it, I guess. It's as simple as that."
    show eris p1 e1 at centered
    "We fall into silence for a moment."
    "A bitter wind blows through the alley, and Eris starts shivering."
    eris "It's cold."
    roman "Yeah, I noticed."
    eris "Why are you still out here?"
    "She gestures to my hand and I look down. My cigarette has burned down to a tiny stub."
    "After a second's pause, I take the pack of cigarettes from my pocket and simply pull out another."
    eris p2 e3 "You're {i}chain smoking{/i} now?"
    roman "I don't think it counts as chain smoking if it's only two in a row."
    roman "...Does it?"
    roman "Nah, it's gotta be more than that. Three, at minimum."
    "I take a drag."
    roman "That was really something--that whole affair--wasn't it?"
    eris p3 e9 "We really messed up."
    eris "I'm... sorry your plan didn't work out, Roman. It was a good idea."
    menu:
        "A little ripe for her to say that now--but still, the sentiment is definitely there."
        "Do you really mean that?":
            $ cooperation += 1
            $ scene_5_rivalry = False
            call A1_05_c from _call_A1_05_c
        "Don't patronize me.":
            $ rivalry += 1
            $ scene_5_cooperation = False
            call A1_05_r from _call_A1_05_r
    return

label A1_05_c:
    roman "Do you really mean that?"
    eris p2 e7 "No."
    $ crossfade_music(1.0, 1.0, 0.5)
    roman "Funny."
    eris p1 e6 "Thanks."
    roman "Ah, you know, yours was good too."
    eris p1 e1 "Clearly not good enough."
    "Her nostrils flare and she sighs."
    eris p3 e8 "I do actually miss working with you sometimes, you know."
    "This throws me for a loop."
    roman "...For real?"
    eris p1 e1 "Yeah. We got stuff done then. I feel kind of restricted now."
    eris "I mean, my thing here didn't work--and it's {i}definitely{/i} like we're getting less done at ARTech."
    eris "I feel a bit fed up with it, to be honest."
    roman "You, fed up? That's not like you at all."
    eris p2 e5 "I'm not a walking stereotype, Roman!"
    eris p3 e8 "..."
    eris "Sorry, I didn't mean to snap; it's just frustrating. I'm not used to things crashing and burning like that."
    roman "It's okay. I understand."
    roman "I mean, I'm used to my plans crashing and burning--but I understand."
    "I say this with a little chuckle, hoping to lift Eris's spirits--but she continues looking despondent."
    "I place a hand on her shoulder."
    show eris p1 e2 at centered
    roman "This was just one thing--one slip up."
    roman "It doesn't mean anything. \"Everybody makes mistakes\" doesn't even apply here; it was just bad luck."
    eris p2 e5 "It wasn't bad luck! I didn't do what I wanted to do."
    eris "I {i}couldn't{/i}. I wasn't good enough."
    roman "Oi. No talking about yourself like that."
    show eris p3 e8 at centered
    roman "I know that's a load of crap and so do you, underneath this mopey exterior."
    "I realise my hand is still on her shoulder, and hastily remove it."
    eris p3 e9 "I know you're right..."
    eris "It just doesn't {i}feel{/i} like it."
    "She sighs again, then looks back up at me."
    eris p1 e1 "Thank you for listening, though. And for trying to help."
    eris "I thought you kind of hated me."
    roman "I mean, I did--just a little bit."
    show eris p1 e2 at centered
    roman "I'm not sure why, though. I just sort of had it in my head that you were the reason I hated working at ARTech."
    eris "You... you {i}hated{/i} it?"
    roman "I mean, no, I didn't--not at the time. I don't think I did, anyway... It's hard to tell."
    eris p2 e3 "You've lost me."
    roman "I just started losing focus of what I want out of life and..."
    roman "I don't know. I didn't know what I wanted and my brain started making up reasons to make a change."
    roman "I latched onto every little thing that was wrong about it--even if it was inconsequential--and used that to justify leaving."
    roman "And I guess part of me regrets it a little bit."
    roman "But I don't think I'd go back."
    eris p3 e3 "So, what has all that... got to do with me?"
    roman "I think we just..."
    roman "I mean, I spent almost every day with you. You were the biggest part of the job to me."
    roman "And I guess the biggest part of my life; I didn't have much else going on."
    roman "So that's what my brain latched onto."
    eris p3 e8 "I... was the biggest part of your life?"
    roman "Yeah."
    eris "That's..."
    eris p1 e10 "That's so sad!"
    "She laughs--and it {i}echoes{/i} down the alley."
    roman "Fuck you, Eris."
    "And I can't help but laugh too."
    roman "I just poured my heart out to you!"
    eris p2 e7 "Well, I'm not going to help you bottle it back up."
    eris p1 e6 "But that {i}was{/i} very sweet, I suppose. Who knew you had a heart?"
    roman "I'm a sincere guy... what can I say?"
    eris p1 e1 "Mmmhmm. If only you could have shown that at literally any other time in your life."
    "I take the final drag off my second cigarette and chuck the butt into the gutter."
    "Eris looks sort of expectant."
    roman "We're good, aren't we? We're {i}actually{/i} all good?"
    eris p1 e6 "Yeah. I think so."
    "I put my hand out."
    eris p2 e3 "A handshake?"
    roman "What were you expecting, a proposal?"
    "She takes my hand, squeezing quite a bit harder than necessary."          
    eris "Well... thanks, Roman."
    show eris p2 e3 at transform_hide
    hide eris
    "After the brief shake I turn to go. Eris doesn't stop me."
    stop dynamic_1 fadeout 1.0
    stop dynamic_2 fadeout 1.0
    return

label A1_05_r:
    roman "Don't patronize me."
    eris p2 e2 "Oh. Okay. I mean, I was trying to be nice."
    roman "No, it's fine. I was just..."
    $ crossfade_music(1.0, 0.0, 0.5)
    "Annoyed because you're being totally two-faced?"
    roman "...Still feeling kind of embarrassed about the whole thing."
    eris p2 e3 "Bullshit."
    roman "Yeah, that wasn't convincing, was it?"
    roman "Seriously though... Why not say something at the time instead of just putting me down? That's how it's {i}always{/i} been with you."
    eris p1 e1 "...What are you talking about?"
    stop dynamic_1 fadeout 10.0
    stop dynamic_2 fadeout 10.0
    roman "Oh my god, why do you keep pretending like there's no history?"
    eris p2 e5 "Because I literally have no idea what you're talking about or what's wrong with you right now, Roman!"
    eris "Just like last time, you're being a dick--and from my point of view, it's for absolutely no reason whatsoever."
    roman "That's exactly it, then, isn't it? The shit that matters to me {i}obviously{/i} matters to you."
    eris "Christ! Okay, I'm sorry? I guess? For... what--for saying I didn't think your idea would work? Is that what this is all about?"
    roman "Yes! Imagine that for, like, years of your life. {i}That's{/i} what this is all about!"
    eris "Oh, man, you are still {i}so{/i} hung up on ARTech that I just don't... ugh! I don't get it!"
    eris "I don't know what shit you've got in your head, but nothing bad happened there. We disagreed sometimes--but so what? It happens! Stop getting so hung up on the past!"
    roman "I am {i}not{/i} hung up on the past! I'm not some fucking cliché--this guy who's just obsessed with retro shit for no reason and has no other attributes."
    eris "When have I ever--"
    roman "{i}All. The. Time.{/i}"
    "She laughs, throwing her head back."
    eris p2 e3 "Are you {i}that{/i} insecure?"
    roman "Oh, fuck off, Eris!"
    show eris p2 e3 at transform_hide
    hide eris
    "I storm towards the door, throw it open, head back inside the club, and slam it behind me."
    scene bg_club_2_after_work with Dissolve(0.5)
    "Slamming the wall with my fist, I breath deeply, my mind a blur."
    "What happened?"
    "...I actually don't know."
    "What was that even about? What did we argue about? Whatever logic was in my mind at the time is already gone; my emotions are all that remain."
    "Everything she does seems to get on my nerves--but I can't explain it."
    "I should probably try to. What was it this time?"
    "I think back."
    eris "{i}I was trying to be nice.{/i}"
    roman "{i}Why not say something at the time instead of putting me down?{/i}"
    "Wait, was it all me? Was I in the wrong?"
    "...No. Fuck that."
    "I mean, maybe this one time--but I am {i}not{/i} wrong about the past. I'm not!"
    roman "Fuck it."
    "Saying this out loud, without really understanding why, I re-open the door."
    scene bg_back_alley
    roman "Eris?"
    "She's nowhere to be seen."
    roman "Eris!"
    eris "...What?"
    "Apparently not having gone far, her voice echoes from around a corner. After a moment, she reappears."
    show eris p2 e5 at center_left
    eris "What do you want?"
    roman "I just needed you to... "
    roman "I mean, I need to say that--"
    show eris p2 e3
    roman "I am {i}not{/i} wrong about the past. Stop saying I'm misremembering it when--"
    eris "Oh, right. You just wanted to keep being a dick. I thought you were coming out to do some big dramatic apology or something."
    eris "Grow up, Roman. See you tomorrow."
    hide eris with Dissolve(0.25)
    "She turns, and heads back around the corner, presumably towards home."
    "My brain buzzing, my face burning, and my fingers tingling, I shakily grab another cigarette and light up."
    show bg_black with Dissolve(1.5)
    return
