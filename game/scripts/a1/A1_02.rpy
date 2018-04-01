label A1_02:
    scene bg_alley with Dissolve(1.5)
    play audio navcomp
    navcomp "You have arrived."
    roman "I know I've arrived. The building's right in front of me."
    "I don't know what drives me to have the same conversation with my car every day. It just keeps happening."
    play audio navcomp
    navcomp "Sorry about that. Your feedback is important to us. If you'd like to- "
    # TODO: play audio car_off
    "Before it can finish, I turn the car off."
    "I don't get out immediately, though. The events of yesterday are still playing on my mind."
    "What are the chances that Eris, of all people, would have started working at the Arcady just a few weeks after me?"
    "I sit for a while, mulling this thought over and getting nothing more out of it."
    "Eventually, I give it up, and head inside."
    # TODO: Chill scene 2 music
    # $ queue_music(music_chill)
    scene bg_club_2_before_work with Dissolve(0.5)
    show parker p1 e1 at centered
    parker "Morning, Roman."
    roman "Good morning, Parker."
    # TODO: play audio mop_bucket
    "I make my way hastily to the cupboard behind the bar and grab a bucket and mop from underneath it to begin the day's work."
    parker "Did you sleep all right?"
    roman "Uh..."
    "I was hoping my attempts at looking busy might reduce the risk of smalltalk. No such luck."
    roman "Yeah, fine thanks."
    parker p1 e5 "Oh, good. I thought you might have had a lot on your mind."
    "Is he talking about what I think he's talking about?"
    # TODO: play audio mop_splash
    "Emerging from behind the bar, I slap the soaked mop down on the floor a little harder than necessary, spattering my pants with soapy water."
    "It takes significant effort not to scowl when I look back up at Parker, and I'm not sure I totally pull it off."
    roman "What makes you say that?"
    parker p1 e1 "Well, you know."
    "He looks at me suggestively. Yeah, he's totally talking about what I think he's talking about. I'm not giving him the benefit, though."
    roman "Haven't the foggiest."
    parker "All that business with you and Eris yesterday."
    roman "Ha!"
    "The bitter, bark-like laugh I emit belies the air of levity I meant to construct."
    roman "It was nothing."
    "But, of course, Parker isn't going to accept that."
    parker p1 e4 "Come on, Roman. I'm not stupid. There's something going on there."
    parker "The moment you recognized her, you went all tense. You could cut the air with a knife."
    roman "I'm not sure where you're getting that from, Parker. There's nothing going on between me and Eris."
    roman "And besides, even if there were, is it really anything to do with you?"
    "That was the wrong thing to say. His next works are heavy with sarcasm."
    parker "Oh, my apologies, please do forgive me for prying into your personal life."
    parker "But, unfortunately, it is my business. I've had staff with history before. It's a pain in the ass."
    parker "They either waste half the day fornicating in the store cupboard, or they can't work within 50 feet of each other without frightening the customers."
    # TODO: Tense scene 2 music
    # $ queue_music(music_tense)
    parker "So, what's it gonna be with you?"
    roman "We just worked together in the past. That's all it is."
    parker p1 e4 "Come off it, Roman. Don't hold out on me."
    menu:
        "Parker's pushing me hard. I need to get him off my case."
        "Seriously. That's all it was. Just coworkers.":
            $ cooperation += 1
            call just_coworkers
        
        "Fine. She made my time at my old place a living hell.":
            $ rivalry += 1
            call living_hell
    
    # TODO: play audio mop_bucket
    "I do as he says, taking up the mop I'd left leaning against the side of the bucket. As Parker disappears into the back office, I'm left pondering the honesty of my own words."
    "Yeah, so me and Eris have a rough history, but do I really need to bother myself with that? Maybe now it's time to let bygones be bygones. This is supposed to be the start of a new chapter...or something like that. God, that sounds pretentious."
    "I don't know. It's hard to forget a... rivalry like that, if a rivalry is what we had. Shit like this is hard to define in the real world."
    "Eris never did anything that I could really call offensive to me, but we were just so different in the way we work that any kind of cooperation with her seemed impossible."
    "For the sake of this job, is it time to put some actual effort in? I'm done with ARTech, so having a coworker with different views doesn't mean they're out to destroy my work...right?"
    # TODO: Timeskip animation
    # TODO: Potential second interior background?
    "After a few hours I hear Eris make her way into work, but thankfully manage to avoid conversation by making sure I'm working on the opposite side of the room."
    "As I'm replacing the last burned-out tealight, my phone vibrates."
    # TODO: Show phone?
    "A message from Parker."
    phone "Meeting in 10. See me at the bar. - Delivered by ARTech"
    "You'd think messages delivered straight from his brain would have more personality."
    # TODO: Hide phone?
    "I spend another few minutes straightening the already-straightened tables before feeling like I might be pushing it, and head to the bar."
    "As I approach, I see no sign of Parker - but Eris is there already. I steel myself and walk right into the waiting jaws of the abyss."
    show eris p1 e1 at center_right
    eris "Roman."
    roman "Eris."
    "I see what Parker meant about the atmosphere between us now. I really can't avoid how {i}tense{/i} this is."
    "A few seconds of silence are all the excuse I need. I head behind the bar and grab a lowball glass and a bottle."
    # TODO: play audio mop_bucket
    "As I pour myself more than a dram of a pleasant looking Islay twelve-year, Eris clucks her tongue. Like an angry chicken."
    eris p2 e7 "Isn't it a little early for that?"
    roman "Sun's over the yardarm."
    eris p3 e3 "...What does that mean?"
    roman "What, you don't know what a yardarm is?"
    "And before having to reveal that I don't know either, I move on."
    roman "You have any idea what Parker wants to talk to us about?"
    eris p1 e1 "Nope."
    "I raise my glass and take a nose, then a sip. It's not bad. Rich, and quite smoky."
    eris "Careful now, you don't want to break Parker's second rule here."
    "She's picking a fight, but..."
    "I don't really have anything to say to Eris. My thoughts return, as they have throughout the whole afternoon, to what Parker said to me earlier - but the thoughts are mostly cyclical and meaningless."
    # TODO: p2 e1 doesn't exist.
    eris p1 e1 "Is this going to be a problem for you? Me, working here?"
    # eris p2 e1 "Is this going to be a problem for you? Me, working here?"
    "I look up from my glass in shock, but before I can reply, Parker emerges from the back office."
    show eris p1 e1 at center_right
    show parker p1 e1 at center_left
    "He glances at the whiskey in my hand next to me and gives me a slightly disapproving look, but says nothing."
    parker "Ho-kay. Monthly meeting. Let's see..."
    "He pulls out a small ring-bound pad and a stubby pencil."
    parker p1 e5 "So, in these meetings I just like to take stock of things, how you are doing as a team, and listen to any concerns you have."
    parker p1 e1 "Usually I'd involve the whole staff, but I'm going to talk to the rest of them later. There's something I wanted to pick your brains about, specific like."
    parker "With your mutual backgrounds in AR tech - thank you for sharing that with me, by the way, whether or not it was deliberate - well, I could use your advice."
    eris p2 e7 "Wow, look at that, {i}Roman{/i}. Only a few days working here and I'm already being asked how to run the business."
    "Her arrogance spikes my irritation. This is clearly not shared by Parker, who merely looks politely amused."
    show eris p1 e1 at center_right
    roman "What do you need our advice on, Parker?"
    "He lets out a sigh, though one that sounds far too exaggerated to be real."
    parker p1 e2 "It's, eh - well, I'll be honest with you two; I think the club could do to perform a bit better."
    parker p1 e1 "Don't get me wrong, we're not at risk of going under or anything like that. I just think we have the capacity to see more people come through our doors."
    parker "I'm not really sure why, and figuring out why that might be, and how we can make it better - I think you might be able to help with that."
    "There's a pause, as Parker looks expectantly at us."
    parker "So, uh... any ideas?"
    show eris p1 e1 at center_right
    "I'm not sure what to say. Eris looks curious though, and pipes in."
    eris "...What does this have to do with our 'mutual backgrounds in AR tech'?"
    parker "Oh, nothing, really. I just figure you must both be pretty smart."
    roman "{i}One{/i} of us definitely is."
    show eris p2 e5 at center_right
    "I get a punch in the shoulder for my trouble, to which Parker turns a blind eye."
    eris p1 e1 "Do you have {i}any{/i} idea the numbers that you'd like to see?"
    parker "Not really. I just feel like the club isn't really keeping up with the times, so maybe a new change could do some good with the establishment. It's not a coincidence that I've recently hired on a new AR performer such as yourself Eris. I just like to do what I can to provide a great service for my customers."
    "My mind is still racing over the idea that Eris is performing as a singer, but this entire conversation is beginning to bug the hell out."
    roman "Who cares about whether or not we're keeping up with the times?"
    roman "We play jazz and serve decent booze. What needs to change?"
    "Parker opens his mouth to speak, but doesn't get a chance to before Eris cuts in."
    eris p2 e4 "You can't expect people to keep coming back for the same old stuff every day. People like different things, and something {i}new{/i} and exciting might be exactly what this place needs!"
    "Of course, like always, she would direct attention to herself."
    roman "Well, they're definitely not going to keep coming back if this place, a jazz club, stops playing jazz!"
    show eris p2 e5
    parker p1 e2 "Before you two keep going on, I really just need a definitive and solid idea to work from."
    parker p1 e1 "Is that something you could potentially work together on?"
    eris p2 e4 "Not necessarily. All I need to do is simply up my performance quality."
    roman "How?"
    eris "From my last performance I didn't - uh - engage the audience enough. It could definitely stand to have some more excitement to it."
    roman "People don't come here to be shouted at from the stage. They want to sit back and enjoy some jazz and a drink."
    eris p1 e1 "I'm not going to shout at them! I just want them to know I know they exist."
    roman "Well I think they just need to be able to appreciate the atmosphere a little more and enjoy the place itself. We should put something on."
    eris "Like what? Music?"
    roman "No. I don't know, uh -"
    "I look around for inspiration. I don't know what this place needs, exactly, but it's lacking... something."
    "It needs a bit of... a bit of..."
    "My wandering eyes land on the glass in my hand. I turn to Parker, who's now eyeing the same glass in my hand with suspicion."
    roman "Okay! I know what we need to do. I think I have a plan to make this place exactly what a jazz club should be."
    eris "Oh yeah? And what would that be?"
    roman "I don't have the details just yet. But trust me. It's just what this place needs."
    eris p2 e3 "Do you really expect us to go along with this plan of yours when you don't even know what the plan is?"
    roman "I do know what the plan is! Or, I know what it involves. I think."
    roman "Look, Parker, I can sort it all out. Tomorrow night I might just need a hand bringing a few things in. What do you say?"
    parker "I don't know what I'm saying yes or no to, Roman. That doesn't exactly fill me with confidence."
    # TODO: p1 e5 doesn't exist.
    eris p2 e5 "Wait a minute, is my idea just completely off the table for this imaginary idea then?"
    # eris p1 e5 "Wait a minute, is my idea just completely off the table for this imaginary idea then?"
    parker "Of course not, Roman just- "
    "Interrupting him, I let a string of words fly out of my mouth without processing exactly what they mean - but Eris is once again a threat that I need to dispatch."
    roman "We'll have a competition!"
    "There's a moment's silence...immediately broken by Eris laughing harshly."
    eris "A competition? Are you serious?"
    roman "Yes. I'm serious."
    "I come close to saying 'Are you scared you'll lose?' before realising I'm not twelve."
    eris p2 e7 "Oh. I legitimately thought that was a joke."
    "Ignoring her, I turn again to Parker."
    roman "What do you think?"
    show eris p1 e1 at center_right
    "He looks thoughtful for a moment."
    parker p1 e3 "Funnily enough, that's pretty close to what I wanted to talk about next."
    parker p1 e5 "I was thinking of starting an 'Employee of the Month' sort of thing. You know, give you all a bit of motivation. Perhaps this competition of yours could play into that?"
    "Eris' expression says, quite clearly, 'You've got to be kidding me.'"
    "This mirrors my thoughts on the subject, but I instead decided to look politely interested."
    parker p1 e2 "...There'll be a small cash bonus."
    roman "Yes! Yeah! That sounds like a great idea."
    show eris p3 e9 at center_right
    show parker p1 e1 at center_left
    "Eris nods...half-heartedly."
    eris "I could... get on board with that."
    eris p1 e1 "So, how's it going to work? How's it judged?"
    parker "Don't worry yourself about that. I'll take a survey from the patrons or something."
    parker "I just want you two, tomorrow night, to do... whatever it is you have planned. You, Eris, with your audience engagement, and you, Roman, with your... eh... what-a-jazz-club-should-be thing. Whatever it is."
    eris "Tomorrow night?!"
    parker "Well, no, not both of you at once. Perhaps Roman should give his idea a go first?"
    roman "No problem."
    eris p2 e5 "Oh my God, Roman..."
    "Annoyed with my cockiness, she crosses her arms, looking at me with murder in her eyes."
    eris p1 e1 "Mm. Fine. Okay, Parker - I'll go for it the day after."
    parker p1 e5 "Excellent. Glad to hear it."
    "He looks between us both, smiling - but clearly sensing the tension in the air."
    parker p1 e3 "Ahem, well, that's killed two birds with one stone. I'll leave you to it."
    parker "We open in a bit, so make sure the place is ship shape, yeah?"
    "As Eris and I stare daggers at one another Parker once again tries to intervene."
    parker p1 e4 "Is...this going to be another problem between you two? I really can't have this become a big thing."
    parker "Because God help me if I've made it worse..."
    parker "..."
    parker p1 e2 "Actually, you know what, maybe pitting you two against one another wasn't the best idea. Why don't I just- "
    show parker p1 e1
    # These two lines are shown simultaneously.
    eris p1 e1 "No, it's fine." (multiple = 2)
    roman "There's not going to be a problem." (multiple = 2)
    "..."
    "Another awkward pause."
    eris "Maybe this is exactly what we need."
    "Parker looks skeptical, his eyes darting once again between Eris and I - but eventually he sighs."
    parker p1 e2 "Fine. I have a feeling I'm going to regret this, but fine. You two go ahead."
    show parker at transform_hide
    hide parker
    "He heads back into the office, and I hear the door closing behind him"
    "Neither of us watch him go. We're stuck, staring at one another like a two cats unsure of who's going to pounce first."
    "Unexpectedly Eris lets out a laugh."
    eris p1 e1 "This is kind of silly, isn't it?"
    roman "Wha...what do you mean?"
    eris "All this, because of some old rivalry?"
    roman "What!? It's nothing to do with that!"
    "Yes it does."
    eris p2 e2 "Yes it does! You wouldn't get off my case!"
    roman "{i}You{/i} wouldn't get off {i}mine{/i}!"
    eris p2 e5 "Christ, Roman."
    "Now agitated, Eris slips a hand inside her pocket and pulls out a sleek, black e-cigarette."
    roman "You know you can't do that indoors."
    eris p1 e1 "And you're not allowed to drink. At least I'm not breaking one of Parker's rules."
    "Eris inhales the smoke and I frustratingly gulp down whiskey that's become warmer from the heat of a tense grip."
    "After her long inhale she produces a thick, white cloud from her nose and mouth. Oddly it doesn't smell sickly sweet like e-cigarette vapour usually does.."
    roman "Is that tobacco flavored? Do they really still make those for E-cigs?"
    eris p2 e7 "You aren't the only one who can appreciate the past."
    eris p1 e1 "But there is such a thing as taking it too far."
    "She takes another puff."
    eris "What exactly are you planning for tomorrow? Really?"
    roman "I have it worked out."
    "I'm trying to convince myself as much as her."
    roman "What about you?"
    eris "I don't know."
    eris "This was my very first night with performing, but already the crowd is getting to me."
    roman "What do you mean? They're a pretty chill bunch. Totally harmless."
    eris "Well, yeah, that's the problem. They were floating in here, barely taking any of it in. They sat in their chairs and looked vaguely in the direction of the stage, eyes glazed over, poisoned themselves for a few hours, and then...left."
    eris "I just wanted some of them to give a shit about what I was doing up there."
    eris p2 e5 "Because {i}I{/i} give a shit!"
    eris "You know what it's like to put your heart and soul into a performance, only to have it met with passive interest? What about when you hear the loudest applause coming from the staff - the people paid to be here?"
    roman "I've certainly never had anyone applaud me before."
    eris "That's right, you wouldn't. You didn't even catch the performance did you?"
    eris p3 e9 "Experiencing that kind of feeling...it's horrible."
    eris p1 e1 "And I don't know if it's something I'm doing wrong or what, but I've gotta find a way to change it."
    roman "Heh."
    eris p2 e3 "What?"
    "I'm not sure that was the best moment to laugh - not that it was exactly by choice."
    roman "So is that really all we are? Two people just out for others to give a shit?"
    "Eris gives me a hard look..."
    eris p1 e1 "No Roman, we aren't even close to being the same."
    "...and takes another long drag."
    eris "I don't know why I'm doing this, but listen."
    eris "Fuck Parker's employee of the month thing. Who cares? Let's make this wager more exciting for the two of us."
    roman "Hmm. What are the stakes?"
    eris "Okay... you know how you're constantly going on about wanting to get out of the city and start fresh, all that jazz?"
    roman "I can't deny that."
    eris "If you win - if Parker gives you employee of the month instead of me - I'll help pay for you to get out. We'll go halves on it. Whatever you need."
    roman "Oookay. That's... incredible generous."
    roman "I assume there's a catch? You wouldn't just give me that kind of money."
    eris "Naturally."
    eris "If {i}I{/i} win -"
    "She puffs her e-cig, the thick mist floating ominously between us."
    eris p2 e7 " - You have to go back to ARTech. You have to re-apply. I know they'd take you back."
    "..."
    "Why..."
    roman "Why the hell would I do that!?"
    eris p1 e1 "Because you're wasted in this place. I just want you to go back to doing what you were good at doing."
    # TODO: p2 e1 doesn't exist.
    eris p1 e1 "I mean, you were brilliant."
    # eris p2 e1 "I mean, you were brilliant."
    eris "Why did you decide to work at this dump, anyway?"
    "She gives me a good few seconds to produce an answer - but one is not forthcoming."
    roman "It's -"
    "My mind is racing in all kinds of directions."
    roman "Is this why you applied -"
    eris "Give it up."
    eris "I don't know what's going on with you, but when you can't justify it to yourself, you have a problem."
    eris p2 e5 "You know how much we achieved at that place? Greenway was a huge step for our team! We have done so much already! Why would you want to let go of that?"
    roman "Greenway? You want to bring up Greenway? Now?"
    eris p2 e2 "Yeah, so what?"
    "Does she not feel about it the way I do?"
    roman "I just... I can't even fathom how I could look back on it like that."
    eris p1 e1 "Well, sure, you don't need to 'look back' on it. Just... there's no need to completely throw it away, either."
    eris "Do you even care about what we did for ARTech? I mean, your work on neural sound encoding, you can't just forget that part of your life."
    "I look at her, lost for words."
    "After a while, she takes one more long drag, exhaling not quite in my direction but close enough that I still feel her faceful of vapour."
    eris "Enjoy your drink, Roman."
    show eris at transform_hide
    hide eris
    show bg_black with Dissolve(1.5)
    return
            
label just_coworkers:
    roman "Seriously. That's all it was. Just coworkers."
    parker "Just coworkers?"
    roman "Yeah. I mean, sure, we had our disagreements, but who doesn't? It was nothing more than that."
    "Parker gives me the most skeptical look I've ever seen."
    roman "What's that look for? Seriously, there was nothing more to it."
    roman "We worked together on a project called Greenway, this experimental unfinished AR tech, and maybe we didn't see eye-to-eye now and then. It's as simple as that."
    "As I'm finishing my explanation, Parker lets out a long drawn out sigh."
    parker p1 e2 "All right, Roman. If you say so."
    show parker p1 e1
    "For a moment, he fixes me with a searching look, his eyes piercing."
    parker "This isn't going to get in the way of your work here, is it?"
    roman "No, Parker, I promise you, it won't."
    "That searching stare is unwavering."
    roman "It was some... dumb tiff at our old job, and it was nothing personal. I won't let it get in the way of my work here. You have my word."
    "Seeming still unsatisfied, but appearing to sense he's going to get nothing more out of me, Parker nods."
    parker p1 e2 "Mm. Well, I can't ask much more than that. Back to it, then. The crowd will be here soon enough."
    show parker p1 e2 at transform_hide
    hide parker
    return
    
label living_hell:
    roman "Fine. She made my time at my old place a living hell."
    roman "From the start, she was {i}constantly{/i} second-guessing me. I couldn't get a goddamn word in the entire time!"
    roman "The minute I made a suggestion it was all 'That's ridiculous, it can't possibly work!' or 'Did you even think that through? It's stupid.' And I swear she never had time to actually think about... whatever the fuck I had said!"
    "I don't remember what it was that we exactly disagreed over, but I've already built up too much of a momentum to stop."
    show parker p1 e3
    roman "I don't know what she went through to have the impression that she could constantly shut me down like that, but it was just so... ugh! She's impossible!"
    roman "Don't get me wrong, I tried to cooperate with her, I really did, but do you know what it's like to work with someone who'll never give you any quarter? When it seems like they'd never even consider, not once, that what you have to say might have value?"
    "Brandishing a finger, I realise how loud my voice has gotten, and do nothing to lower it."
    roman "She had no right to be my superior! We were hired at the same time, at the same level!"
    roman "And don't get me started on -!"
    stop music fadeout 1
    parker p1 e4 "Roman, calm down."
    "His voice is forceful, and as my voice bounces of the walls of the empty bar, lingering in the air and ringing in my ears, I feel my cheeks burn."
    roman "I- I wasn't- "
    "Parker's expression isn't one of shock, but a combination of understanding and disappointment."
    parker "You know you've just confirmed exactly what I was worried about, don't you, Roman?"
    parker "If working with Eris is going to be this hard for you, then we have a problem."
    roman "Parker, no, it's not like that!"
    show parker p1 e4 at centered
    "He raises his eyebrows."
    roman "That shit, it's all in the past. I want to move past it. I do."
    "Do I?"
    roman "Yeah!"
    "Amidst Parker's confusion I answer myself out loud."
    show parker p1 e1 at centered
    "Parker looks as though he wants to hear more, so I keep talking. I can already hear the lack of conviction in my voice. Could he?"
    roman "There's no sense in holding onto stuff from the past like this, and getting angry for something that happened long ago isn't going to do anyone any good."    
    parker "..."
    "He looks...satisfied enough."
    # TODO: Chill scene 2 music
    # $ queue_music(music_chill)
    parker p1 e5 "Wise words. Mind you live by them."
    "He fixes me with a knowing stare for a beat, before continuing."
    parker p1 e1 "I am surprised to hear you and Eris have such a turbulent history, to be honest. I didn't really expect anything like this to happen when I was bringing her on board, even when I mentioned you during our interview."
    parker p1 e3 "Though I probably shouldn't talk about that with you."
    "He hastens to fix his slip-up - but I'm not about to let that go."
    roman "You mentioned me to Eris before she started? What did she say?"
    parker p1 e1 "I just said, I can't talk about that with you. It's private."
    roman "I don't think it's against any employment law, right? Considering the circumstances - and if you spoke about me, surely I have the right to know what it was about?"
    "I hardly have an in-depth knowledge of employment law - though I'm hoping Parker has very little understanding as well."
    "That or a kind heart."
    parker p1 e4 "Well..."
    parker p1 e1 "All right, all right. I just mentioned your name, in passing - you know, when mentioning some of the staff during her hiring interview - and when I came to your name, she sort of... fixated on it."
    roman "And?"
    parker "We didn't really linger on the subject. She said that she worked with you before, and that you were a, eh... what was it, now..."
    parker "Actually, she just sort of trailed off."
    "Coming to his senses, some sharpness returns to his voice."
    parker p1 e4 "Not that {i}this{/i} is any of {i}your{/i} business."
    "But I've heard all I need to know."
    "I don't know what I expected."
    "Should I be offended about her choice of words describing me? Is it that she hardly cares, or was what she had to say too rude for Parker to repeat?"
    parker p1 e1 "I don't expect any trouble to come of this, Roman. Eris is now as valued here as you are."
    "He says this firmly, but not unkindly. Not exactly kindly, either."
    parker "Let's get back to it, then. The crowd will be arriving soon."
    show parker p1 e1 at transform_hide
    hide parker
    return
