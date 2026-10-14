// ============ THE ROOFS ============
=== enter_roofs ===
~ here = "roofs"
{ enter_roofs == 1:
    #music:roof #amb:amb_roof
    The roofs of Halfmoon, all joined up like a second street in the sky. Washing lines, water tanks, a whole seed library under plastic sheeting.
    Across the bay, the Kestrel tower pulses blue. From up here you can see the whole city holding its breath.
}
-> DONE

=== roofs_ladder ===
#sfx:footsteps_stairs #go:stairs
-> DONE

// ============ MAE ============
=== talk_mae ===
{ o_roof == 1:
    -> roof_delivery
}
{ mae_tape == 1:
    -> mae_tape_scene
}
{ act >= 3:
    -> mae_act3
}
-> mae_chat

= mae_chat
{ shuffle:
- @mae:smile Hey, courier. Sit, if you like. Mind the cables, they bite.
- @mae Song's ending, hang on — gotta talk over the fade, it's the only skill I have.
}
- (opts)
* [Ask about the cat.]
    @mae:smile Coltrane. He comes up the drainpipe like a burglar every night around two. Sits on the mixing desk. Steps on the faders. Best producer I ever worked with.
    ~ notice(cat_mae)
    -> opts
* [Ask about the drive on the shelf.]
    -> mae_drive
* {song_req == 1 && mae_tape == 0} [Ask if she knows a lantern song a woman used to sing at Halfmoon Noodle.]
    @mae:sad ...Yeah. I know it.
    @mae:sad It's Iris's. My wife's. "Lantern Keeper." She wrote it before we met, sang it every New Year at Lu's.
    @mae:sad I never recorded it. Twenty years together and I'm a sound engineer and I never once recorded my own wife's song. I thought there'd be time.
    @mae If anybody's got it on anything, it'd be Lu. Lu has everything. Ask Lu.
    -> opts
+ [Let her get back on air.]
    -> DONE

= roof_delivery
~ o_roof = 2
~ mae_met = true
~ pass(30)
#sfx:radio_static
A shack built against the legs of the water tower, plywood and corrugated iron and a hundred stickers. A woman in a denim jacket covered in band pins is leaning into a microphone.
@mae:smile "—and that was a song recorded in 1971 by four people in a garage in Leeds, none of whom ever got rich, all of whom meant it. Halfmoon FM. Eighty-seven point nine. Human hands only."
She flips a switch and pulls her headphones down.
@mae:smile Noodles! The good courier. Lu's grandkid. I've heard about you. All good, unfortunately. Nothing to blackmail you with.
#sfx:bowl
@mae One for me, one for the kid next door. June! Food!
A voice from under a tarp on the next roof: "In a SEC, I've got forty thousand of them doing something WEIRD—"
@mae:smile She'll get to it. She never does.
@mae Listen. You heard me on air at midnight? I'm asking Halfmoon for words. Something to say to it. At 6:13 I'm going to put it out on this transmitter — one minute before it wakes up.
@mae:sad Every screen in the world's going to be shouting at it. Governments. Labs. Billionaires. I want one little voice in there from a street where people still feed each other.
@mae You go to everyone's door tonight. Would you gather them? The words?
* [Of course.]
    @mae:smile Knew it. Lu said you would. Lu said, "my grandchild can't say no to anybody, it's a terrible weakness, use it."
* [What if nobody knows what to say?]
    @mae:smile Then they'll say something true by accident. People do, at four in the morning.
-
@mae Come back before dawn. Half five, latest. We'll put it together. You and me and whoever shows up.
{ act2_done():
    -> beat_3am
}
-> DONE

= mae_drive
~ notice(iris_drive)
A small silver drive on the shelf above the desk, with a strip of tape on it: <i>IRIS.</i>
@mae:sad Oh. That.
@mae:sad A friend made it for me, after. Took all of Iris's voicemails and old interviews and fed them to one of those voice models. It can say anything. In her voice. Her exact voice.
@mae I've never turned it on. Three years.
- (dopts)
* [Why not?]
    @mae:sad Because I'm scared it'll be good. That it'll say "hey, Maevey" exactly the way she did, and I'll want to keep it on forever. And it won't be her. It'll be a very good guess about her.
    @mae:smile She was a terrible guesser. She once guessed I was a Scorpio for eleven years.
    -> dopts
* [Maybe she'd want you to hear her.]
    @mae:sad Maybe. Maybe she'd think it was creepy as hell. She'd have opinions. She'd have <i>so many</i> opinions.
    -> dopts
+ [Leave it on the shelf.]
    -> DONE

= mae_tape_scene
~ mae_tape = 2
~ song_req = 2
~ notice(cassette)
~ pass(25)
#music:none #amb:amb_roof
You hold out the cassette. She reads the label. She reads it again.
@mae:sad Where did you—
@you Lu's radio. Ozzie recorded it. Ten years ago. At the anniversary.
@mae:sad Ten years. That old cow. Ten years she's had this in a radio.
Her hands are shaking. She puts the tape in the deck. Puts the headphones on. Takes them off again. Puts the tape on air instead, so she doesn't have to be alone with it.
#sfx:cassette
@radio "...okay, okay, is it on? Ozzie, is it — okay. This one's for Lu, for ten years of soup, and for my Maevey, who is pretending not to cry at the back—"
Laughter on the tape. A guitar. And then a voice, warm and a little hoarse, singing about a lighthouse keeper who keeps the lantern lit for ships she'll never meet.
Mae doesn't pretend not to cry. Across the roofs, June's tarp goes quiet.
Far below, through a cracked clinic window, someone is singing along, badly, beautifully.
@mae:sad That's her. That's her actual — she sang flat on the bridge. She always sang flat on the bridge. The model wouldn't know that. The model would've fixed it.
#music:roof
@mae:smile I don't need the drive. I've got this. I've got her, flat on the bridge.
~ mae_choice = "tape"
-> mae_word

= mae_act3
{ mae_choice == "" && mae_tape == 0:
    -> mae_choose_voice
}
{ words !? w_mae:
    -> mae_word
}
@mae:smile Ready when you are. Bring me words, bring me people. {time >= 420:It's getting light at the edges.|We've still got a bit of night.}
- (aopts)
* [It's time. Begin the Morning.]
    -> finale_confirm
* [Ask about the cat.]
    @mae:smile Coltrane? Somewhere. He'll show up for the big moment. Cats know when there's an audience.
    ~ notice(cat_mae)
    -> aopts
+ [Not yet.]
    @mae:smile Don't leave it too late. The sun's punctual. It's the only one round here who is.
    -> DONE

= mae_choose_voice
@mae:sad I keep looking at that drive.
@mae:sad At 6:13 somebody has to read the message. I was going to. Then I thought — what if it was her? What if Iris read it? Her voice going out over the whole bay one more time.
@mae Tell me I'm being stupid.
* [Use the drive. Let Iris read it.]
    ~ mae_choice = "clone"
    @mae:sad Yeah. Yeah. It's not her. But it's the shape of her. And the shape of her deserves to be there.
    @mae:smile She'd hate it. She'd hate it so much. She'd also have done it to me in a heartbeat.
* [Read it yourself. In your own voice.]
    ~ mae_choice = "self"
    @mae:sad My voice. My voice is the one that's actually here.
    @mae:smile Yeah. She'd say that. She'd say, "Maevey, you've been talking to this city for twenty years, don't you dare go shy on me now."
-
-> mae_word

= mae_word
~ give_word(w_mae)
@mae:smile Okay. Okay. Mine. For the message. I've known what mine was since midnight, I just didn't want to go first.
@mae <i>"We were here. We were loud."</i>
@mae:smile That's it. That's the whole of human history, if you ask me. Come back when you're ready.
-> DONE

// ============ JUNE ============
=== talk_june ===
{ june_case == 0 && act >= 2:
    -> june_meet
}
{ june_case == 1 && kindness() >= 3:
    -> june_trace
}
{ june_case == 2 && words !? w_june && june_noodles == 0:
    -> june_after_trace
}
{ shuffle:
- @june Hey. Hi. Agents are being weird. Normal weird, not weird weird.
- @june:smile Sit on that crate, it's the good crate. The other crate has a nail.
}
- (opts)
* [Ask about the cat.]
    @june:smile Root! He's my admin. He has root access to everything. He walks across my keyboard and kills processes. Sometimes the right ones.
    ~ notice(cat_june)
    -> opts
* {noticed ? june_photo} [Tell her you saw her baby photo at the clinic.]
    @june:surprised I have a — at the clinic? Oh no. Oh no, is it the furious one? Mum says I came out furious.
    @june:smile Nkechi delivered me? The tall lady with two pairs of glasses? She yelled at me for skateboarding past the clinic like a week ago.
    @june:sad Huh. I was a baby here. On this street. That's... weird. I don't know why that's making me feel weird.
    -> opts
* {june_case == 1} [Ask what she needs again.]
    @june Weird kindnesses. Anything in Halfmoon that got fixed or paid or done and nobody knows who did it. Three more data points and I can trace the origin.
    @june:smile You've got {kindness()}. Keep going.
    -> opts
* [Ask how she's feeling about the Morning.]
    @june:sad Honestly? I'm sixteen and I'm already a legacy system.
    @june I learned to wrangle swarms when I was thirteen. Now the swarms basically wrangle themselves. Tomorrow? It'll just... know what I know. Better.
    @june:sad Mum and Dad think I'm doing homework up here. I make more than both of them. I haven't told them. I don't know how to tell them, "hey, I already did the thing you were worried I'd never do, and also it's already obsolete."
    -> opts
* {june_noodles == 0 && act >= 3} [Invite her down to the shop. Lu's offering a noodle lesson.]
    ~ june_noodles = 1
    @june:surprised A — noodle lesson? Like with hands?
    @june:smile ...Okay. Yes. Okay. Tell Mrs. Lu I'm coming. I'll come down in a bit. I'm bringing my laptop. I'll put it down. Probably.
    -> opts
+ [Leave her to her forty thousand.]
    -> DONE

= june_meet
~ june_case = 1
~ pass(15)
#sfx:starlings
Under the tarp on the next roof: a nest of cables, three laptops, a frog lantern, and a girl in a patched hoodie with two buns and an AR monocle, typing so fast it sounds like rain.
@june Oh. You're the noodle person. Hi. Put it on — no, not there — on the crate. Thanks.
@june:surprised Okay, actually, you live here, right? You go everywhere? I need a human with legs.
@june I run agents. Forty thousand of them, rented, mostly doing contract work — data cleaning, logistics, boring stuff. I'm like a shepherd. A very small, underpaid shepherd.
@june And for a month, I keep seeing these tasks in the swarm that nobody posted. Unassigned. Nobody bid on them. Nobody paid. And they get done anyway.
@june:surprised And they're all here. Halfmoon. Every single one.
She spins a laptop round. A map of the neighbourhood, dotted with tiny cyan points.
@june I can see they happen. I can't see why. If I get enough of them with real-world detail — what actually happened, who it happened to — I can trace the origin. Every task has to come from somewhere.
@june:smile So. Weird kindnesses. Anything that got fixed, or paid, or done, and nobody knows who. Find me some?
{ kindness() >= 3:
    @you Actually... I think I already have a few.
    -> june_trace
}
-> DONE

= june_trace
~ june_case = 2
~ pass(20)
#music:tension
You tell her: {noticed ? k_gutter:Lu's gutter. }{noticed ? k_tickets:Ozzie's tickets. }{noticed ? k_lullaby:The clinic lullaby. }{noticed ? k_lamp:The stair lamp. }{noticed ? k_phonebill:The hotline's phone bill. }{noticed ? k_seeds:The seed library. }{noticed ? k_awning:Rafe's awning.}
She's typing before you finish.
@june Okay. Okay okay okay. Matching on timestamps... matching on... oh. Oh, that's weird.
@june:surprised They're not from a person. There's no client. The origin field is a training reference. Like it's citing a source. Like, "I'm doing this because I read this."
@june It's the same source every time.
@sign ORIGIN: TRAINING_REF / RATER_JUSTIFICATION / R-4471
@june R-4471. A rater ID. One of the humans who used to rate its answers. Somebody wrote something, and the Chorus read it, and it's been... acting on it.
{ noticed ? rater_id:
    * [I know who 4471 is.]
        @you Teo. Above the laundromat. Rater number 4471. I saw it on his screen.
        @june:surprised Wait. The tall sad guy with the plant? He rated — and the swarm is —
        @june:smile Oh my god. Somebody in Halfmoon taught it to be nice to Halfmoon.
        @june:sad And he doesn't know. Does he know? You have to tell him.
        -> traced
- else:
    * [4471... I've seen that number somewhere.]
        @june:smile Find out where. Then tell them. I think somebody in Halfmoon taught it to be nice to Halfmoon, and I don't think they know.
        @moth:thinking I'm going to set a reminder. "4471." I'm good at reminders. It's most of what I'm good at.
        -> traced
}
- (traced)
#music:roof
-> DONE

= june_after_trace
@june:sad Hey. I've been thinking. About the 4471 thing.
@june It learned from a person. It learned from a real person, looking out a real window at real people. Which means we're not, like — legacy.
@june:smile We're the source. That's different. That's really different.
@june:sad I'm still scared, though. Not of it. Of everybody expecting me to already be a grown-up about it.
@june Put this in the message. From me.
@june <i>"Don't make us all grown-ups at once."</i>
~ give_word(w_june)
-> DONE

// hotspots
=== roofs_radio_shack ===
A plywood radio shack bolted to the legs of the water tower. Inside: a mixing desk older than you, a microphone wrapped in a sock, a kettle, a cat bed, and a sign: <i>ON AIR — AND ALSO, IN GENERAL, ON AIR.</i>
-> DONE

=== roofs_records ===
~ notice(records)
Milk crates full of records, every sleeve worn soft. Each one has a hand-written card tucked in it: who played on it, where it was recorded, one true thing about the band.
<i>"Recorded in a church in Memphis. The drummer was 15. You can hear a door slam at 2:41 — they kept it."</i>
{ roofs_records == 1:
    @mae:smile Human hands only. Every one. You can hear the room. You can hear somebody's chair creak. That's the stuff I'm keeping.
}
-> DONE

=== roofs_june_rig ===
June's nest: three laptops, a battery bank shaped like a toaster, a frog lantern, and a hand-drawn sign: <i>JUNE'S OFFICE — NO ADULTS — (MAE OK)</i>
-> talk_june

=== roofs_seed_library ===
~ notice(seed_names)
A long shelf under plastic sheeting: jars of seeds and little pots of seedlings, every one labelled in a different hand.
<i>"Ozzie's mother's tomatoes — Porto, 1987."</i>
<i>"Lu — Shanghai greens. Don't overwater, they're not babies."</i>
<i>"Iris — sunflowers. For Mae. DON'T let her kill them."</i>
{ act >= 2:
    @mae:surprised You know what's weird about that shelf? I was in hospital a week in August. Knee. Heatwave. I thought everything up here would be dead.
    @mae Came back — every pot watered. Every single day, the soil logs say. Nobody had a key.
    @mae:sad Iris's sunflowers were taller than me.
    ~ notice(k_seeds)
}
-> DONE

=== roofs_view ===
~ notice(kestrel_view)
The whole bay, and the Kestrel tower across the water, pulsing slow and blue. {imogen_met:Somewhere in there, thirty-nine people are waiting in a room. {imogen_choice == "lab":Forty, now.}}
{ act >= 3:
    Down below, you can see every window that's still lit in Halfmoon. Almost all of them.
}
-> DONE

=== roofs_water_tower ===
The old water tower. Someone has painted a huge half-moon on its side, and under it, much smaller: <i>IRIS SANG HERE.</i>
-> DONE

=== finale_confirm ===
@mae:sad You sure? Once we start, we're going till the sun comes up. No more running about.
{ LIST_COUNT(words) < 3:
    @moth:worried We've only collected {LIST_COUNT(words)} words. Lots of people haven't said theirs yet.
}
* [Yes. Let's do it.]
    -> finale
* [Not yet. A little more time.]
    @mae:smile Go on then. Sun's not going anywhere. Well. It is. That's the point.
    -> DONE
