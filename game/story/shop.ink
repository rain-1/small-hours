// ============ PROLOGUE ============
=== start ===
~ act = 0
#music:shop #amb:amb_shop
9:00 pm. Halfmoon Noodle. The windows are fogged so thick the street outside is just colours.
The TV on the shelf has been showing the same thing all day: a number, getting smaller.
@sign 09:14:00 — UNTIL THE MORNING
@lu Little Fish! You're late.
@you I'm early. You said nine.
@lu:smile Nine is late. Eight-thirty is on time. Eight is when good grandchildren come.
She doesn't look up from the pot. Steam rolls off it like weather.
@lu Apron. Hands. Then sit, eat. Nobody carries my soup on an empty stomach.
A bowl appears in front of you. It always does.
#sfx:bowl
* [Eat.]
    You eat. It tastes exactly like being nine years old and safe.
* [Ask why she's staying open all night.]
    @lu Why? Because tonight nobody is sleeping, and nobody should be hungry and alone at the same time. One of those I can fix.
    You eat. It tastes exactly like being nine years old and safe.
-
@lu Good. Now. You have been back in Halfmoon two weeks and you still haven't told me properly what happened in the city.
* [I worked on buildings. The swarm draws better buildings.]
    ~ past = "architect"
    @you I was a junior architect. Then the firm got a swarm licence. It drew in a night what we drew in a year. Better, too. I checked.
    @lu:sad Hm. Better is not the only thing a building has to be.
* [I drove deliveries. The app stopped needing drivers.]
    ~ past = "driver"
    @you I drove for a delivery app. Then the app didn't need drivers anymore. They sent a very nice email.
    @lu Hm. Well. Now you deliver for me. I don't send emails.
* [I was studying. I'm not sure what for, anymore.]
    ~ past = "student"
    @you I was studying. I just... couldn't tell anymore what I was studying for.
    @lu:smile Nobody can tell that at your age. That is not the Morning's fault. That is being twenty-two.
-
@lu Anyway. You're here. Tonight I need legs.
She slaps four paper tickets onto the rail. #sfx:order
@lu Ozzie, out front in his car. Number twelve, beef broth. <i>On the house</i> — don't tell him. He'll argue.
@lu Teo, above the laundromat. Cold noodles, extra cucumber, he's a sad boy, give him the good chopsticks.
@lu The clinic. Two congee. Nkechi and whoever's poor husband is in the waiting room tonight.
@lu And the hotline, upstairs over the pharmacy. One for Hollis. They forget to eat when the phones are busy, and tonight the phones are busy.
~ o_ozzie = 1
~ o_teo = 1
~ o_clinic = 1
~ o_hotline = 1
~ act = 1
@lu Go on. Your scooter is plugged in out back. Moth was asking about you.
Your pocket buzzes. The little dash unit, unclipped from the scooter, blinks awake in your hand.
@moth:happy Good evening, {name}. Battery sixty-four percent. Roads: wet. Orders: four.
@moth:thinking Also, there are nine hours and fourteen minutes until the Morning. Every channel keeps telling me. I don't know what to do with the information, so I'm passing it to you.
@lu:smile That machine talks more than Ozzie.
@moth:worried That is statistically untrue.
@moth I'll keep your journal, as usual. Press the button with my name if you want me. I'm not busy. I'm never busy. It's one of my features.
-> DONE

// ============ SHOP: enter ============
=== enter_shop ===
~ here = "shop"
{ act == 1 && act1_done():
    -> beat_midnight
}
{ act == 2 && song_req == 1 && mae_tape == 0 && not shop_radio.tape_found:
    The radio is playing something with a lot of saxophone in it. Lu is humming along, badly, on purpose.
}
-> DONE

// ============ LU ============
=== talk_lu ===
{ act:
- 1: -> lu_act1
- 2: -> lu_act2
- 3: -> lu_act3
- else: -> DONE
}

= lu_act1
{ act1_done():
    -> beat_midnight
}
{ shuffle:
- @lu Why are you standing here? Soup is getting cold in your basket. Cold soup is a crime with only one victim and it's me.
- @lu:smile Go, go. The tickets don't deliver themselves. Yet.
- @lu You're doing the face. Your mother did the face. Go do something with your hands, the face goes away.
}
- (opts)
* [Ask what she thinks about the Morning.]
    @lu Every few years somebody says the world is ending. When I was your age it was the year 2000 — all the computers were going to forget what year it was.
    @lu Then it was the bird flu. Then the oceans. Now this.
    @lu:smile Every time, the next day, people needed noodles.
    @you And if this time it's different?
    @lu:sad Then they'll need them even more, Little Fish.
    -> opts
* [Ask about the cat outside.]
    @lu:smile Dumpling? He's not my cat. He's nobody's cat. He's everybody's cat. He eats here, then he eats at the clinic, then he eats at the hotline, then he comes back here and tells me nobody fed him.
    @lu Liar. Fat liar. I love him.
    ~ notice(cat_lu)
    -> opts
* {noticed !? k_gutter} [Ask about the new gutter.]
    @lu Ha! You saw? Three years, that gutter dripped right on the door. Right on the customers' heads. I called the landlord forty times.
    @lu:surprised Then last week, morning, I come down — fixed. New bracket. Even painted. Landlord says it wasn't him.
    @lu So, a ghost. A ghost with a ladder. I left him a bowl of noodles on the step. Gone in the morning.
    @moth:thinking Ghosts don't eat noodles. I've checked a lot of databases.
    @lu Dumpling does.
    ~ notice(k_gutter)
    -> opts
+ [Back to work.]
    -> DONE

= lu_act2
{ shuffle:
- @lu Roof, stairs, alley, ice. You have a lot of legs tonight.
- @lu:smile Midnight already. When I was young midnight was the start of things.
- @lu If you see Dumpling, tell him the clinic is lying about feeding him.
}
- (opts)
* {song_req == 1 && mae_tape == 0} [Ask about a lantern song a woman used to sing here at New Year.]
    -> lu_tape
* {noticed ? patent && not lu_patent} [Ask about the patent in the back room.]
    -> lu_patent_talk
* {noticed !? k_phonebill && hollis_open} [Ask if she's been paying the hotline's phone bill.]
    @lu:surprised Me? Pay a phone bill? For someone else? I would never.
    @lu I would bring soup. Soup is better than a phone bill. You can't eat a phone bill.
    @lu:smile Ask somebody richer.
    ~ notice(k_phonebill)
    -> opts
* [Ask about her and Ozzie.]
    @lu:sad There's no "her and Ozzie." There's Ozzie, who eats here, and me, who feeds him. Eleven years.
    @lu He has a car he talks to and a heart that doesn't work right, and I have a pot.
    @you His heart?
    @lu:sad Nkechi talks too much. Don't tell him I told you. He thinks if nobody says it out loud it isn't true.
    ~ ozzie_heart = true
    -> opts
+ [Back to work.]
    -> DONE

= lu_act3
{ not recipe:
    -> lu_recipe
}
{ shuffle:
- @lu Go say your things to people. I'll be here. I'm always here, that's the whole point of me.
- @lu:smile You have broth on your sleeve. Good. Now you smell like a professional.
}
- (opts)
* {song_req == 1 && mae_tape == 0} [Ask about the lantern song.]
    -> lu_tape
* {noticed ? patent && not lu_patent} [Ask about the patent.]
    -> lu_patent_talk
* {june_noodles == 1} [Tell her June wants to learn to pull noodles.]
    -> june_noodle_lesson
+ [Back to work.]
    -> DONE

= lu_tape
@lu:surprised The lantern song. Who's asking about the lantern song?
@you A woman in labour at the clinic. Her mother used to bring her here at New Year. Someone sang.
@lu:sad Iris. That was Iris. Mae's Iris.
@lu Every New Year, she sat right there, on that stool, and sang that song and everybody cried into my soup and said it was the steam.
She goes very still.
@lu There's a tape. Ten years ago she sang it at our anniversary and Ozzie recorded it on that old radio. I never took it out. It's still in there.
@lu:sad Three years I didn't have the heart to play it and I didn't have the heart to take it out.
@lu Take it to Mae. She should have it. She should have had it a long time ago. I was a coward about it.
@you You weren't a coward.
@lu:smile I was a little coward. Old women are allowed. Go.
~ notice(cassette)
~ mae_tape = 1
#sfx:cassette
You eject the tape from the radio. The label, in someone's loopy handwriting: <i>LANTERN KEEPER — live at Halfmoon Noodle — for Lu, for ten years of soup.</i>
-> DONE

= lu_patent_talk
~ lu_patent = true
@you Grandma. The frame in the back room. "Lattice memory arrangement. Inventor: Lu Meifang."
She stops stirring. That almost never happens.
@lu:sad You were in my back room.
@lu Hm. Well. You were always in my back room. You used to sleep on the rice sacks.
@lu Twenty-two years I drew little squares. Very small. Smaller than you can think. How to put memory next to arithmetic so they don't have to walk so far to talk.
@lu:smile The Lu lattice. They still use it. It's in every one of those machines. Billions of my little squares.
@lu:sad Everything that thing thinks tonight, it thinks on my squares.
* [Are you proud of it?]
    @lu:sad I quit the year your mother died. Everyone thought it was grief. It was grief. It was also that I looked at what my squares were for, and I didn't know.
    @lu Proud? I don't know. I made something beautiful and I didn't get to decide what it was for.
    @lu:smile So I made soup. Soup, I decide what it's for.
* [Is that why you turned the frame face down?]
    @lu:sad I turned it down because it was looking at me.
    @lu:smile Old women are allowed to be dramatic, also.
-
@lu Maybe tomorrow I turn it back over. We'll see what it says, when it wakes up. If it says something stupid I'm leaving it face down.
-> DONE

= lu_recipe
~ recipe = true
~ pass(30)
#music:tender
@lu Come here. Wash your hands. No, properly. Like a surgeon.
@lu Tonight I teach you the broth.
@you Now? It's three in the morning.
@lu:smile Three in the morning is when the broth tells the truth. Everybody is tired and nobody is pretending.
She hands you the ladle. It is heavier than it looks. It's been her ladle for eighteen years.
@lu Bones first. Roast them till they smell like a bonfire somebody's happy at. Then cold water — cold, not warm, warm makes it cloudy and cloudy is lazy.
@lu Star anise. Two. Not three. Three is for showing off.
@lu Then you wait. Six hours. Don't touch it. The waiting is the recipe. Everybody wants to skip the waiting.
* [Write it down.]
    You take out your phone to write it down. She puts her hand over it.
    @lu No. Write it here.
    She taps your chest.
* [Ask if the Chorus could make this.]
    @lu:smile Probably. Maybe better. Maybe tomorrow there's a machine in every kitchen that makes my broth exactly.
    @lu:sad But it won't have waited for you. You understand? It's not the soup. It's that somebody stood here six hours.
-
She takes a small notebook from her apron. It's soft as cloth from handling.
@lu Everything's in there. Your great-grandmother's dialect in the margins. Nobody alive reads it except me. Now you can learn.
~ notice(dialect)
@lu:sad I'm sixty-eight. When the machine wakes up, maybe it fixes my knees and I live to a hundred and fifty. Maybe not. Either way. Someone should have the book.
@lu If Mae asks you what I'd tell the Morning — tell her this.
@lu:smile <i>"Eat something first. Then decide."</i>
~ give_word(w_lu)
#music:shop
-> DONE

= june_noodle_lesson
~ june_noodles = 2
~ pass(20)
#sfx:door_bell
June arrives five minutes later with her hood up and her laptop clutched against her chest like a shield.
@june:surprised Hi. Hello. Mrs. Lu. I don't— I've never cooked anything. I microwave. I've microwaved some things professionally.
@lu:smile Laptop down. Not on the counter. Laptop on the stool. Good.
@lu Flour. Water. Salt. Hands. That's the whole technology.
For twenty minutes, June Takahashi-Reyes, who directs forty thousand artificial minds, gets flour on her eyebrows.
The first noodle snaps. The second snaps. The fifth one stretches, and stretches, and doesn't break.
@june:surprised Oh. OH. Look. Look at it. I made a noodle. Nothing helped me.
@lu:smile Badly. You made a bad noodle. It's a perfect bad noodle. Eat it.
@june:smile That's the first thing in like three years I made without anything helping me.
She eats the noodle. She laughs with her mouth full. She looks sixteen.
{ words !? w_june:
    @june:smile Hey. For Mae's message. Put this:
    @june <i>"Don't make us all grown-ups at once."</i>
    ~ give_word(w_june)
}
-> DONE

// ============ SHOP: hotspots ============
=== shop_ticket_rail ===
{ act:
- 1: { act1_done(): All four tickets are spiked on the rail, done. Lu will want to see you. | The tickets flutter in the steam. {o_ozzie == 1:Ozzie, out front. }{o_teo == 1:Teo, above the laundromat. }{o_clinic == 1:The clinic. }{o_hotline == 1:The hotline, over the pharmacy.} }
- 2: { act2_done(): Done. All of them. | New tickets. {o_roof == 1:Two bowls for the roof — Mae and "the kid". }{o_tea == 1:A pot of tea for the stairs. }{o_ludd == 1:"NED LUDD — the alley — cheapest thing, extra chili." }{o_ice == 1:A bag of ice for the clinic.} }
- else: The rail is empty. Lu says there won't be any more tickets tonight. "Tonight, you deliver yourself."
}
-> DONE

=== shop_tv ===
~ notice(tv)
{ act:
- 0: -> DONE
- 1:
    @sign KESTREL SYSTEMS — LIVE
    A spokesperson in a soft grey sweater is smiling very carefully.
    @tv "—not a switch being flipped. Think of it as the Chorus finishing a sentence it has been saying for years. At 6:14, local time, it will be able to say 'I'."
    @tv "We want to stress there is nothing you need to do. Go to sleep, if you can."
    The ticker underneath: <i>MARKETS CLOSED — 41 NATIONS SIGN DAWN ACCORDS — "LAST NIGHT" PARTIES IN 300 CITIES — MAN IN OSLO ATTEMPTS TO SEND THE WORLD'S LAST FAX</i>
- 2:
    A panel of experts is arguing. One of them says "consciousness" and the other three groan.
    @tv "—what I want to know is who gets to talk to it first. Is it the lab? The governments? Is it just whoever's loudest?"
    @lu From the kitchen: Turn that off, they've been saying the same thing since lunch.
    You don't turn it off. Neither does she.
- 3:
    The TV has given up on talking. It's just the countdown now, and a slow aerial shot of the bay, and the Kestrel tower pulsing blue like a heartbeat.
    Somewhere in the city, someone has set off fireworks early. They look small and brave on the screen.
}
-> DONE

=== shop_clock ===
The clock on the wall says thirteen minutes to five. Its glass is cracked. It has said thirteen minutes to five for eighteen years.
{ not lu_clock_asked:
    -> lu_clock_asked
}
-> DONE
= lu_clock_asked
~ notice(clock)
@lu:sad Don't fix it. People keep offering.
@lu It stopped the night your mother died. Four forty-seven in the morning. I got home from the hospital and it was stopped and I thought: good. You too.
@lu:smile Twice a day it's right. That's more than most of us.
-> DONE

=== shop_lucky_cat ===
A white lucky cat, waving one paw. The paw has a crack across it, glued back with something gold.
{ not shop_lucky_cat_seen:
    -> shop_lucky_cat_seen
}
It keeps waving. Somebody has to.
-> DONE
= shop_lucky_cat_seen
~ notice(lucky_cat)
@lu Ozzie knocked it over in 2015, waving his arms about a parking warden. He glued it himself. With gold, like the Japanese do.
@lu:smile He's very proud. It's crooked. Don't tell him.
-> DONE

=== shop_photo ===
~ notice(photo)
A photo, sun-faded: a young woman on a scooter, laughing at whoever is holding the camera. Same chin as you. Same terrible helmet.
{ shop_photo == 1:
    @moth:thinking Is that—
    @you My mum. Lin. She was twenty.
    @moth That's the scooter. Our scooter. The frame, anyway. I'm newer.
    @moth:happy I like knowing that. That something carried her before it carried you.
}
-> DONE

=== shop_radio ===
{ act:
- 1:
    #sfx:radio_static
    @radio "...this is Halfmoon FM, eighty-seven point nine, the last slow station in Lantern Bay. All night tonight, human records only, played by a human, badly."
    @radio "Next up, something from 1974 by people who are all dead now and would be thrilled you're listening. Stay up with me."
- 2:
    { song_req == 1 && mae_tape == 0:
        -> tape_found
    - else:
        #sfx:radio_static
        @radio "...dedications are open. Somebody on Cable Lane wants to tell their brother they're sorry about the car. Darren, he's sorry about the car."
    }
- 3:
    #sfx:radio_static
    @radio "{time >= 420:Not long now, Halfmoon. Put the kettle on. Find your people.|Still here. Still human. Still taking words for the Morning.}"
}
-> DONE
= tape_found
The radio's cassette door is cracked open a little. There's a tape inside, label faded.
@lu:sad Don't—
@lu Hm. No. Ask me first. Ask me properly.
-> DONE

=== shop_back_door ===
{ act >= 2 && noticed !? patent:
    Lu is busy with a customer. You slip through the curtain into the back room.
    Rice sacks. A camp bed. Twenty years of calendars from the fish market.
    On the shelf, a frame turned face-down. You turn it over.
    @sign UNITED PATENT OFFICE — LATTICE MEMORY ARRANGEMENT FOR HIGH-DENSITY TENSOR COMPUTE — INVENTOR: LU MEIFANG
    There's a photo tucked in the corner: Lu at forty, in a cleanroom suit, giving the camera the finger.
    You put it back face-down. Then, after a moment, face-up.
    ~ notice(patent)
- else:
    { act >= 2: The back room. The patent frame on the shelf {lu_patent:is face-up now.|is where you left it.} | The curtain to the back room. Rice sacks, a camp bed, Lu's private things. {act < 2:Lu would notice. She notices everything.} }
}
-> DONE

=== shop_pot ===
{ recipe:
    You know what's in it now. Bones, cold water, two star anise. Six hours. Somebody standing here.
- else:
    The broth pot is the size of a bathtub for a small dog. It has been going since five this afternoon.
    { shuffle:
    - It smells like a bonfire somebody's happy at.
    - Lu catches you leaning over it. "Don't breathe in my soup."
    - The steam fogs your glasses, if you had glasses. It fogs your whole face.
    }
}
-> DONE

=== shop_stools ===
{ act == 2 && here == "shop":
    -> talk_ozzie_shop
}
You sit on a stool for a second. Your legs tell you how many stairs there are in Halfmoon.
{ shuffle:
- Rain on the window. The pot ticking. Lu humming. For a second, there is no Morning at all.
- On the stool next to yours someone has carved, long ago: <i>I.A. + M.A.</i> inside a crooked heart.
- The TV counts down. You find you've been holding your breath. You let it out.
}
-> DONE

=== shop_front_door ===
#sfx:door_bell #go:street
-> DONE

=== talk_ozzie_shop ===
Ozzie has come in out of the rain and claimed his stool. He's halfway through a second bowl he's pretending is his first.
{ talk_ozzie_shop == 1:
    @ozzie:smile Kiddo! Sit, sit. Your grandmother's trying to poison me with kindness again.
    @lu It's leftover.
    @ozzie It's never leftover. Eleven years, it's never once been leftover.
    @lu:smile Then eat faster and it will be.
}
- (opts)
* [Ask how they met.]
    @ozzie:smile Ha! I drove her. 2015, no, 2014. Rain like this. She gets in the back of my cab with a pot. A whole pot of soup, on her lap, lid taped down.
    @ozzie I say lady, if that spills, you're paying to clean it. She says if it spills, you'll be begging to lick the seats.
    @lu I never said lick.
    @ozzie:smile You implied lick. I've been eating here ever since.
    -> opts
* {ozzie_heart} [Watch them, and say nothing about his heart.]
    Lu refills his bowl without asking. He thanks her without looking up. Eleven years, and they still do this little dance where neither of them says anything true.
    It looks like a kind of love that's scared of its own size.
    -> opts
+ [Leave them to it.]
    -> DONE
