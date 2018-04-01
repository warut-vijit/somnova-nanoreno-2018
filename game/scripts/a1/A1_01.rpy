label A1_01:
    stop music
    $ queue_music(music_one)
    $ crossfade_music(0.0, 1.0, 0.0)
    play audio ambient_city
    show bg_black
    "There's something that I hate about this city."
    "Maybe it's the staleness of the air, or the lack of available parking."
    "But if I had to choose one thing though, it's the people."
    "They all look the same, with everyone swiping the air through their AR rigs."
    "Most of the time they rudely bump into you, barely acknowledging you as they keep going."
    "Society really likes the shiny stuff, and those AR rigs are no exception."
    "Admittedly, the tech is pretty interesting, but it's just a pain in the ass to move around everyone while they're clearly focused on something else."
    "No one 'takes a walk' anymore, now you have to be on your rig for a game or a phone call."
    "It's really stifling to me. I want to talk to people, but no one's ever without a device these days."
    "I'd give anything to get out of this city at this point. Maybe head out of state, get a new job, that sort of thing."
    "A fresh start."
    $ crossfade_music(1.0, 0.0, 2.5)
    scene bg_club_2_before_work with Dissolve(2.5)
    "A place that hasn't caught the AR plague."
    "I guess you could call me a hipster, but I wouldn't be offended if you did."
    "I like the way people did things back in the 90s and the Aughts--without bunch of bombardment by shiny tech that commands your attention 24/7."
    "And that's what this place--the Arcady Jazz Club--is all about."
    "I got a job as a waiter here mainly because I wanted to soak in this atmosphere; a breath of fresh air away from the stagnant city outside."
    "Parker, my boss, manages this club exactly the way I like it. He's cultivated a unique atmosphere."
    show parker p1 e1 at centered
    parker "Good afternoon, Roman. Good to see you. Ready for another night shift?"
    roman "As ready as I'll ever be. How were the crowds today?"
    parker p1 e5 "Same as usual."
    parker p1 e1 "Oh, I have a new waitress who I need you to help train on some of the stuff in the back. She's coming in soon."
    parker p1 e5 "Turns out she's an AR performer too, so I hope to have her bring in a crowd every once in a while."
    "I grimace."
    parker p1 e3 "What's with that look?"
    roman "AR performers, Parker? Really? I thought this was a more traditional jazz club."
    parker "Well, I never said that. I got a friend in the industry, so I decided to buy an older model from him cheap a few months ago."
    parker p1 e1 "I just never got around to using it."
    parker "But I have a business to run, so I have to try to cater to what's popular out there."
    parker "Relax, Roman. It'll draw a crowd. You know what that means."
    roman "More tips?"
    parker p1 e5 "That's the spirit, Roman! Now, she's going to come in about a half hour. If you can set up that AR stage for her when she gets in, that would be a huge help."
    roman "...Sure. Where's the console?"
    parker p1 e1 "In the back. Just hit switches three and seven to get the lights when it asks you."
    show parker at transform_hide
    hide parker
    "Well, I guess it's better paid work than my last job..."
    show bg_black with Dissolve(0.75)
    hide bg_black with Dissolve(0.75)
    "Soon, the evening crowd moves in, ordering drinks and dinner."
    "My ears eventually pick up a fragment of conversation."
    customer_a "I wonder if she's performing here tonight..."
    customer_b "She said in her last vlog that she's working on getting a second gig ready by this week."
    customer_a "Yeah? Sweet, it'd be nice to meet her."
    "I wonder if they're talking about that new waitress-slash-vocalist. Who is she, I wonder?"
    "Even without AR rigs, I barely follow much of the way of pop artists. Maybe she's famous?"
    "Though why would she want to work here anyway?"
    "..."
    "Whatever. If Parker says it'll bring a crowd, I guess I'll play along."
    show parker p1 e1 at centered
    parker "Oh, Roman, forgot to mention. You remember that we have a monthly meeting tomorrow, right?"
    roman "Yeah, I remember. This'll be my first one, anything I can expect?"
    parker p1 e5 "Nah, nothing that won't surprise you."
    parker p1 e1 "Hopefully."
    parker p1 e5 "Just checking. By the way, the girl just walked in. I'll have her meet you once she's done clocking in."
    show parker at transform_hide
    hide parker
    play audio lightfootsteps
    "True to his word, in a few moments I catch the sound of footsteps approach me from behind."
    "I turn around and catch sight of just who it is that I'll be working with."
    # TODO: CG1
    show eris p1 e6 at centered
    "She's wearing our uniform, but the sleeves are made of a trendy semi-transparent fabric."
    waitress_girl "Hey there! Parker said to talk to you."
    "I've heard that voice before..."
    roman "Ah, nice to meet you..."
    "Wait. I know that face."
    eris p1 e2 "Oh. My. God. Roman?"
    "She enunciates that phrase exactly like how I remember. It never left me, no matter how much I tried."
    "My body tenses in apprehension."
    show eris p2 e5 at centered
    roman "Fancy meeting you here, Eris."
    eris "Likewise."
    roman "..."
    eris p2 e3 "..."
    eris "You grew a beard. Looks... {i}nice.{/i}"
    "It's clear she doesn't like it."
    roman "Did it myself. Made a project out of it."
    "I got lazy and decided I could save money by not shaving."
    "And she knows it."
    # TODO: p3 e1 doesn't exist.
    eris "So, want to show me around or...?"
    # eris p3 e1 "So, want to show me around or...?"
    "What the fuck are you doing here?"
    "A million questions are racing through my head, but..."
    "Knowing Parker, and especially knowing Eris, I do my best to push away the ensuing conflict."
    "The topic will come up eventually down the line."
    roman "Just gimme a sec with this."
    eris p2 e3 "What is it?"
    roman "An AR platform parker bought a few months ago. Says it's for you."
    # TODO: p2 e10 doesn't exist.
    eris "What, that old thing? That's at least two years out of date."
    # eris p2 e10 "So, want to show me around or...?"
    # TODO: p2 e1 doesn't exist.
    # show eris p2 e1 at centered
    roman "Should still work, right? For your... {i}performances{/i}?"
    eris p3 e3 "Geez, since when did you become such an old fogey? You used to eat and breathe this stuff back at ARTech with me."
    eris p3 e9 "We had a lot of fun with that Greenway project, remember?"
    roman "Wow, and here I thought you hated it."
    eris p2 e5 "What?"
    roman "I mean, you'd go on and on about how Ted couldn't get his shit together, or that I wasn't taking this project seriously enough."
    roman "Am I wrong?"
    eris p2 e5 "..."
    eris p2 e3 "Do I get this tour or not?"
    roman "Yeah, sure. Sorry."
    show eris at center_right
    # TODO: End CG1
    "Eris follows me to the kitchen."
    roman "Have you taken orders yet?"
    eris p1 e1 "Not really, my first shift was just serving tables."
    roman "Perfect, lemme show you how it's done."
    roman "When you get an order, just pin it up on the rack and the cooks will take care of it."
    roman "Unfortunately there's no cool lingo."
    eris p1 e1 "Cool lingo?"
    roman "You know, like the lingo short-order cooks use. `A cup of mud` being a mug of coffee, for example."
    eris p3 e3 "What are you talking about, dude?"
    "I was hoping I could have some fun with her, but same cold exterior as always."
    roman "Just make sure you get the order right. Cooks here hate it when you screw up."
    eris p1 e1 "Like not asking for a 'cup of mud'?"
    "My mistake, she's not going to let me live that down."
    roman "Okay, forget that, next is the the employee console."
    "I proudly show her the small touchpad with the current time and a few buttons."
    roman "Just find your name on the employee list, hit the login button, and your time will be recorded for your shift."
    roman "Parker really wants everyone to punch in as soon as they can, so keep on top of that."
    roman "He gets pissed if you mess up your time, says the labor paperwork isn't worth it."
    roman "Aside from that, though, Parker's pretty relaxed about how things are run here, but there's a few ground rules he's said to basically everyone;"
    roman "Don't start fights."
    roman "Don't get drunk."
    roman "Let him handle the people who won't leave you alone."
    roman "If you follow those rules you're good to go."
    show eris at centered
    roman "Okay, that's basically the tour. Any questions?"
    eris p1 e6 "Seems short. I give it a two out of five."
    roman "{i}Any questions?{/i}"
    eris p1 e1 "I'm fine. It won't be hard to figure out the rest from here."
    "She gives me a hard look, almost as if she's ruminating on what to say."
    eris "Thanks."
    show eris at transform_hide
    hide eris
    "Shit. I thought I was done dealing with people like her."
    show parker p1 e1 at centered
    parker "So finished already?"
    parker "You didn't put her through her paces too much, I hope."
    roman "..."
    parker p1 e3 "Roman? You okay?"

    menu:
        "How should I answer him?"

        "It's nothing.":
            $ cooperation += 1
            $ scene_5_cooperation = False
            roman "Hm? It's nothing."
            parker "..."
            "He doesn't seem convinced."

        "That waitress was... irritating.":
            $ rivalry += 1
            $ scene_5_rivalry = False
            roman "That waitress was..."
            parker p1 e2 "A little grating? Yeah, she does have that impression doesn't she?"
            parker "She did seem pretty desperate for the job though."
            parker p1 e1 "I'll have a chat with her."
            "He eyes me carefully."
        
    parker p1 e4 "Take a quick break for me, okay? Don't want you scaring away our clientele with that look on your face."
    roman "...Sure thing."
    show parker p1 e1 at centered
    show parker at transform_hide
    hide parker
    stop dynamic_1 fadeout 5.0
    stop dynamic_2 fadeout 5.0
    "Man, this sucks. How'd she even find this place, anyway?"
    "Memories of the past come flooding back to me."
    "Arguments over deadlines, panic over downed servers, angry PMs breathing fire down our backs..."
    roman "Geez, and she wonders why I quit."
    roman "..."
    "I could really use a smoke right about now."
    "Grabbing my coat from the break room, I leave my tarnished sanctuary for the world outside."
    "Perhaps tomorrow will give me something to keep my mind off of Eris."
    "Knowing her, that's probably not going to happen."
    show bg_black with Dissolve(1.5)

    return
