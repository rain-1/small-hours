// ============ STREET ============
=== enter_street ===
~ here = "street"
{ enter_street == 1:
    Halfmoon Street. Rain coming down through the light of a hundred signs, the train rail humming overhead.
    @moth Starling flock passing over. Thirty-one drones. They're avoiding the stairs again. They hate the stairs.
    #sfx:starlings
}
-> DONE

=== street_shop_door ===
#sfx:door_bell #go:shop
-> DONE

=== street_laundromat_door ===
{ o_teo == 0:
    SUDS &amp; STARS. Inside, a single dryer turns, slow as a planet. The door to the flats upstairs is locked.
    A buzzer with a handwritten label: <i>NOVAK-BANERJEE (please knock gently, I'm working)</i>
    -> DONE
}
#sfx:footsteps_stairs #go:teo_room
You climb the narrow stairs. Somebody upstairs is listening to whale sounds.
-> DONE

=== street_alley ===
#go:alley
-> DONE

=== street_hotline_door ===
#sfx:footsteps_stairs #go:hotline
-> DONE

=== street_clinic_door ===
#go:clinic
-> DONE

=== street_stairs_up ===
#sfx:footsteps_stairs #go:stairs
-> DONE

=== street_water_tower ===
Up on the hill, the old water tower. A tiny red light blinks on its antenna: 87.9.
{ act == 1: Someone lives up there, sort of. Mae. The radio's always on in Halfmoon because of her. | You can just see a silhouette up there, waving her arms at something. Mae, dancing. }
-> DONE

=== street_vending ===
{ not got_soda:
    -> got_soda
}
{ shuffle:
- The machine hums at you. It's lonely. All the other vending machines in the city talk now.
- You press the coin return out of habit. Nothing. You press it again, out of hope. Nothing.
}
-> DONE
= got_soda
A coin-op vending machine. Coins! Real ones. You find one in your jacket.
#sfx:bowl
@sign SUNRISE SODA — LIMITED EDITION — FLAVOUR: "TOMORROW"
It tastes like orange and pennies and nerves.
@moth:thinking The manufacturer's website says they will stop making it after tonight. Or start making a lot more. They haven't decided.
~ notice(sunrise_soda)
-> DONE

=== street_cat ===
#sfx:cat_meow
~ cat_pets = cat_pets + 1
{ noticed !? cat_moth:
    A fat grey tom on a crate, one white sock, a notch out of one ear. He looks at you like you owe him money.
    @moth:thinking Scanning. Classification: cat. Confidence: ninety-nine percent. Name: unknown.
    @moth:happy I'll call him Unidentified Warm Object. That's what my sensor log says when he sleeps on the scooter.
    ~ notice(cat_moth)
    -> DONE
}
{ act >= 3 && cat_names() >= 6 && words !? w_cat:
    The cat headbutts your hand, hard, then sits up very straight and looks at you.
    @cat Mrrp.
    @moth:thinking I think he wants to contribute to the message.
    @moth:happy I'm adding it. I'm the journal. I make the rules.
    ~ give_word(w_cat)
    -> DONE
}
#sfx:cat_purr
{ shuffle:
- You scratch behind the notched ear. He leans in so hard he nearly falls off the crate.
- He accepts one stroke, then bites you very gently, as a receipt.
- He purrs like a small engine nobody needs to maintain.
- He sniffs your basket with great professional interest.
}
{ cat_names() > 1 && cat_names() < 10: {cat_names()} names so far, and he answers to none of them. }
{ cat_names() >= 10: Ten names. He answers to all of them, and none, and dinner. }
-> DONE

=== street_kiosk ===
~ notice(kiosk)
A swarm kiosk — a slim pillar where you can post an errand and let the agents bid on it.
{ act:
- 1:
    @sign OPEN TASKS: 4,113 — AVG BID: 0.04 — "Walk my dog at 4am (it is anxious about the Morning)" — "Find my mother's handwriting in old scans" — "Explain the Morning to my grandad using only football"
- else:
    @sign OPEN TASKS: 12,880 — AVG BID: 0.01 — NEW CATEGORY: UNASSIGNED
    Under UNASSIGNED there's a list of jobs nobody posted, all marked done:
    @sign HALFMOON STAIRS LAMP #3 — replace bulb — bid 0.00 — DONE
    { june_case >= 1:
        @moth That's one of June's orphan tasks. Nobody asked. Nobody paid.
        ~ notice(k_lamp)
    - else:
        @moth:thinking Bid zero. That's not how bidding works.
    }
}
-> DONE

=== street_mural ===
{ act < 3:
    Someone's painting a mural on the pharmacy shutter: a huge sun coming up over the bay. It's half done. Paint cans underneath, a sign taped to one:
    @sign ADD SOMETHING. — the kids from Cable Lane
    { act >= 2: Since you last looked, somebody has added a tiny crooked lighthouse. }
    ~ notice(mural)
    -> DONE
}
{ mural_add != "":
    The mural's nearly finished. Your {mural_add} is there, in the corner of the sunrise, slightly wobbly. It's perfect.
    -> DONE
}
The sun's almost finished now. Somebody added a lighthouse, a frog, a fish. There's a brush in a can of yellow, still wet.
* [Paint a bowl of noodles.]
    ~ mural_add = "bowl of noodles"
* [Paint a fat grey cat with one white sock.]
    ~ mural_add = "fat grey cat"
* [Paint a tiny scooter with a glowing screen.]
    ~ mural_add = "tiny scooter"
    @moth:happy Is that me? That's me. I've never been in art before.
* [Leave it for someone else.]
    You put the brush back. Somebody else will need it.
    -> DONE
-
~ notice(mural)
You paint your {mural_add} into the corner of the sunrise. It's wobbly. It's yours.
-> DONE

// ============ OZZIE (car) ============
=== street_car ===
{ act >= 3 && not ozzie_ride:
    -> talk_ozzie.ozzie_ride_invite
}
{ act == 2:
    Dolores is parked and ticking as she cools. Ozzie's inside the shop, at his stool, being fed.
    -> DONE
}
{ ozzie_ride:
    Dolores sits by the kerb, engine off, rain beading on her windscreen. {ozzie_clinic:A note on the dash: "AT THE CLINIC. DON'T TOUCH THE RADIO."|Ozzie's left a window cracked for the cat.}
    -> DONE
}
-> talk_ozzie

=== talk_ozzie ===
{ o_ozzie == 1:
    -> ozzie_delivery
}
{ shuffle:
- @ozzie Kiddo. Get in, get out, you're letting the rain in.
- @ozzie:smile I'm not parked. I'm thinking with the engine on.
}
- (opts)
* [Ask about the cat.]
    @ozzie:smile The Captain? Fat bastard. Sorry. Fat gentleman. He rides with me sometimes. Sits on the dash like a hood ornament.
    @ozzie Best co-pilot I ever had. Never once told me to turn left.
    ~ notice(cat_ozzie)
    -> opts
* [Ask about the box on the dashboard.]
    -> ozzie_autopilot
* [Ask why he drives around all night.]
    @ozzie They told me I can't drive a cab no more. Fine. Cars drive themselves, better than me, I watched the numbers, fine.
    @ozzie:sad But Dolores, she's old. If I stop driving her, her legs seize up. Same as me.
    @ozzie:smile So every night we go round Halfmoon, round the bay, back. Keep the legs moving.
    -> opts
* {ozzie_heart} [Ask how he's feeling. Really.]
    @ozzie:angry Who told you? Lu told you. Or Nkechi. It's a conspiracy of nice women.
    @ozzie:sad I'm fine, kiddo. The heart's tired. It drove a lot of miles.
    @ozzie They say maybe after tonight there's new medicine. "After the Morning." Everybody says "after the Morning" like it's a bus that's coming.
    @ozzie I been waiting on buses my whole life. I don't get excited for buses.
    -> opts
+ [Let him get back to thinking.]
    -> DONE

= ozzie_delivery
~ o_ozzie = 2
~ pass(25)
#sfx:car_engine
You knock on the window of a teal hatchback older than you are. It rolls down with a sound like a tired accordion.
@ozzie:smile The noodle courier! Finally. I was about to starve to death in a vehicle, they'd find me in a week, the cat would've eaten my face.
#sfx:bowl
@ozzie How much do I owe her?
* [Lu says it's on the house.]
    @ozzie:angry On the house! Eleven years, it's always on the house! I'm a proud man! I have savings!
    He takes the bowl. He holds it in both hands like it's warm in a way that has nothing to do with soup.
    @ozzie:sad Tell her thank you. No. Don't tell her. She'll get a big head.
* [Tell him he owes her twelve dollars.]
    @ozzie:surprised Twelve! She charges me? Since when?
    He's already counting out coins. Then he stops, squints at you.
    @ozzie:smile She told you to say it's free and you're messing with me. Look at that face. Your grandmother's face. Liar's face.
    He gives you the coins anyway. "For you. Buy a soda from that sad machine."
-
@ozzie Hey, you want to hear something crazy? Look at this.
He waves a fistful of paper. Parking tickets, dozens of them, all stamped PAID.
@ozzie Three hundred forty dollars. Two years of tickets. I don't pay them, it's a principle, the city took my licence so the city can wait.
@ozzie:angry Then this morning — all paid. All of them. Nobody tells me who. The city says "settled by an anonymous agent." An AGENT.
@ozzie:sad Some robot paid my tickets. I'm insulted. I'm so insulted I could cry, kiddo.
~ notice(k_tickets)
@moth:thinking "Anonymous agent" is a swarm category. It means nobody posted the task. Strange.
@ozzie The box talks? Since when does the box talk?
@moth:happy Since always. Hello, Mr. Ferreira.
@ozzie:smile Polite box. Better than mine. Mine I never even switched on.
-> opts_after
= opts_after
* [Ask about his box.]
    -> ozzie_autopilot
+ [Leave him with his soup.]
    @ozzie:smile Go on. Tell Lu it was too salty. She loves that.
    -> DONE

= ozzie_autopilot
~ notice(autopilot)
A grey box screwed under the dash, a sticker on it: AUTODRIVE RETROFIT KIT — ACTIVATE IN SETTINGS.
@ozzie The city sent everybody one. Free. "Upgrade your legacy vehicle." Dolores could drive herself tomorrow if I pressed the button.
@ozzie:sad I never pressed it. Five years. Don't ask me why.
@ozzie:smile I'll tell you why. If she drives herself, what am I? A passenger. In my own Dolores.
@ozzie Some things you keep doing yourself so you remember you're there.
-> DONE

= ozzie_ride_invite
@ozzie Kiddo. C'mere.
Ozzie's out of the car, leaning on her roof, cap pushed back. The rain's thinner now. He looks older in the blue hour.
@ozzie I'm going up to the hill road. The overlook. Gonna see if the sun still knows the way.
@ozzie:sad Was gonna go by myself. Thought I'd ask. You don't have to.
* [Get in.]
    -> ozzie_drive
* [Not yet — I still have things to do.]
    @ozzie:smile Sure, sure. I'll be here till five. After that, me and Dolores have a date.
    -> DONE

=== ozzie_drive ===
~ ozzie_ride = true
~ pass(40)
#sfx:car_engine
#music:tender #amb:none
You get in. The passenger seat has a dent in exactly your shape, from a thousand other passengers.
@ozzie Seatbelt. I'm old-fashioned.
He drives with two fingers on the wheel and talks to the car under his breath. "Easy, easy, girl, that's it." She takes the hill like it's a favour.
#go:hill_road
The overlook. The whole of Lantern Bay underneath you, lit up like someone spilled a jewellery box. Across the water the Kestrel tower pulses, slow and blue.
@ozzie:smile Thirty-eight years I drove this city. I know every street by smell. Fish market, bakery on Fourth, the sewer by the stadium.
@ozzie I used to bring fares up here at night when they were sad. Never charged them for the detour.
He's quiet a while. The engine ticks.
@ozzie:sad Nkechi wants me in the clinic. She says the new treatments, the ones the machines made, they might come soon. Months, maybe.
@ozzie:sad Months, I don't know if I have. Weeks, maybe, she says, if I'm stubborn.
@ozzie And I'm stubborn, kiddo.
- (opts)
* [Ask what he's afraid of.]
    @ozzie:sad Afraid? I'm afraid I hope, and then it doesn't come, and I spent my last weeks in a waiting room instead of here.
    @ozzie I'm afraid it does come, and I'm in a world where nobody needs a man who knows streets by smell.
    @ozzie:smile Mostly I'm afraid of hospital food. Lu ruined me. Eleven years. I can't eat bad soup.
    -> opts
* [Tell him to go to the clinic. Tonight.]
    ~ ozzie_clinic = true
    @you Go to Nkechi. Tonight. Not because the Morning's coming. Because you're here now, and we'd like you here later.
    @ozzie:surprised "We."
    @you Lu. Me. Dolores. The Captain. The lucky cat you glued wrong.
    @ozzie:smile I glued it perfect.
    He doesn't say yes. He doesn't say no. But he puts the car in gear like a man who's made a decision.
    -> opts
* [Tell him to tell Lu. Whatever it is he never says.]
    ~ ozzie_lu = true
    @you Eleven years of soup, Ozzie.
    @ozzie:sad I know.
    @you She's never once charged you.
    @ozzie:angry I KNOW. You think I don't know? You think I'm stupid? Eleven years I've been coming every night to eat soup I don't need from a woman who—
    He stops. He laughs, wet.
    @ozzie:smile Who. Yeah. Okay. Yeah, kiddo.
    -> opts
* {opts > 1} [Just watch the city with him.]
    -> ozzie_ride_end
= ozzie_ride_end
The city breathes below you. A starling flock lifts off the docks, turns once like a thought, and settles.
@ozzie Hey. Mae's thing. The message. You're collecting.
@ozzie:smile Tell it this, from me. Tell it—
@ozzie <i>"Leave us a few roads to get lost on."</i>
~ give_word(w_ozzie)
@ozzie:smile Okay. Okay, Dolores. Home.
#go:street #music:street #amb:amb_street
He drops you back on Halfmoon Street. {ozzie_clinic:He parks outside the clinic, not his usual spot. He sits there a moment, then gets out.|He parks in his usual spot and turns the engine off. First time all night.}
-> DONE
