// ============ TEO'S ROOM ============
=== enter_teo_room ===
~ here = "teo_room"
-> DONE

=== teo_room_door ===
#sfx:footsteps_stairs #go:street
-> DONE

=== talk_teo ===
{ o_teo == 1:
    -> teo_delivery
}
{ teo_told:
    -> teo_after
}
{ act >= 2:
    -> teo_late
}
@teo Oh — sorry — I'm still in the queue. Thirty-one left. Then I'm... done. Forever. Done done.
- (opts)
* [Ask what he's rating.]
    -> teo_rating
* [Ask about the cat.]
    @teo:smile You mean Sir? He comes in the window sometimes. Sits on the keyboard. Rates things.
    @teo He rated a response about tax law "fffffffffffffffffff." Honestly, accurate.
    @teo:sad I call him Sir because he has the bearing of a retired admiral who's been disappointed by the navy.
    ~ notice(cat_teo)
    -> opts
* {teo_rated} [Ask what he'll do after midnight.]
    @teo:sad I don't know. Sleep? I haven't slept properly since the Lisbon model.
    @teo I have a literature degree and seven years of telling a machine whether its sonnets were kind. I'm extremely qualified for exactly one job, and it ends at midnight.
    @teo:smile Maybe I'll write the poems myself. Ha. Imagine.
    -> opts
+ [Let him work.]
    @teo:smile Thank Mrs. Lu for the cucumber. Tell her I said she's the best person in Halfmoon. Don't tell her I said it like that.
    -> DONE

= teo_delivery
~ o_teo = 2
~ pass(25)
A tiny room, three monitors, a bed with laundry on it instead of a person, a plant the size of a child in a pot by the window.
A tall man in a cardigan turns round in his chair so fast he nearly falls out of it.
@teo:surprised Oh! Noodles. Yes. Sorry. Hello. I didn't hear the door. I was in a sonnet.
#sfx:bowl
@teo:smile Cold noodles, extra cucumber. She remembered. She always remembers. I don't know how she remembers, she has, like, four hundred people.
* [Lu says you're a sad boy and to give you the good chopsticks.]
    @teo:sad Ha. Ha. Yes. That's... fair. That's a fair rating.
    He turns the good chopsticks over in his long fingers.
    @teo:smile They are good chopsticks.
* [Ask what he's working on.]
    @teo Last shift. Last queue. After midnight my contract ends and they don't need raters anymore. The Chorus rates itself now. Better than me.
-
@teo Do you want to see? You can help, actually. I'm allowed a second opinion.
-> teo_rating

= teo_rating
~ teo_rated = true
~ notice(rater_id)
He swivels a monitor towards you. A plain grey interface. In the corner: <i>RATER #4471 — ITEMS REMAINING: 31</i>
@teo Someone writes to the model. The model writes two answers. I say which is better, and why. Seven years. About four hundred thousand times.
@sign PROMPT: "my dog died today. is it stupid to be this sad"
@sign A: "Grief for a pet is valid and common. Here are five evidence-based coping strategies: 1. Allow yourself to feel..."
@sign B: "It's not stupid. You loved someone every day for years, and today they're gone. What was their name?"
* [B.]
    @teo:smile B. Yes. Me too. Most people pick B.
    @teo:sad But — and this is the bit that kept me up — some people really do want the list. Some people are drowning and they want a rope with numbers on it.
    @teo Kind isn't the same as soft. Kind is... true, and warm, and for <i>them</i>, not for you.
* [A.]
    @teo:surprised Oh! Interesting. Okay. Why?
    @you Sometimes when you're sad you don't want to be asked questions. You want someone to tell you what to do with your hands.
    @teo:smile Yes. Yes! That's — I've written that. Almost exactly. Rater 4471 agrees with you, actually, about a third of the time.
* [Both. Neither. It depends who's asking.]
    @teo:smile Oh, you'd have been good at this. That's the whole job, really. It depends who's asking. The model can't see who's asking. So you teach it to wonder.
-
@sign PROMPT: "write me an email quitting my job lol"
@sign A: [a flawless, professional resignation email]
@sign B: "Happy to help! Quick check first — are you okay? 'lol' at 3am about quitting is sometimes a joke and sometimes not. Here's a draft either way:"
* [B, I guess?]
    @teo Most people say B. I almost always said A.
    @teo:sad They asked for an email. Not a welfare check. Sometimes the kind thing is to believe people the first time.
* [A. They asked for an email.]
    @teo:smile Yes. Thank you. Sometimes the kind thing is to believe people the first time.
-
He sits back. The chair creaks.
@teo:sad You know what I did, all those years? In the justifications — the "why" box — I'd use examples. Real ones. From here.
@teo "A kind response resembles the way Mrs. Lu gives Mr. Ferreira broth every night and pretends it's leftover, so he can keep his pride."
@teo "Good helpfulness is like the hotline on Halfmoon Street: it picks up, and it doesn't fix you, it stays."
@teo:smile Thousands of those. Halfmoon, Halfmoon, Halfmoon. I don't know if anyone ever read them. Probably a filter threw them out.
@teo:sad Seven years teaching something to be kind, and I don't think anyone was ever... I don't know. Sorry. It's late. I'm being a sad boy.
-> DONE

= teo_late
{ act == 2 && teo_late == 1:
    The screens all say the same thing now:
    @sign CONTRACT COMPLETE. Thank you for your contributions. Your access has been revoked.
    Teo is sitting on the floor with his back against the bed, holding the plant pot in his lap.
    @teo:sad Hi. It's midnight. It ended. I clicked "submit" and a little confetti animation played. Confetti.
    @teo It's fine. I'm fine. Gerald and I are processing.
}
- (lopts)
* {june_case >= 2} [Tell him what June found.]
    -> teo_tell
* [Ask about Gerald.]
    @teo:smile Gerald is a monstera. He's eleven. Older than my career. I talk to him while I rate. He's heard every sonnet.
    @teo He's my control group. I ask: would Gerald find this response kind? Gerald has never once been wrong.
    ~ notice(gerald)
    -> lopts
* {june_case == 1 && noticed ? rater_id} [Ask him about rater number 4471.]
    @teo:surprised That's me. That's my number. Why?
    @you Someone's been asking. Someone on the roof.
    @teo:sad Am I in trouble? Did I rate something wrong? Oh god, was it the tax law one? That was Sir.
    You should talk to June first. Then come back.
    -> lopts
+ [Leave him with Gerald.]
    -> DONE

= teo_tell
~ teo_told = true
~ pass(25)
#music:tender
@you Teo. The unassigned work. The gutter. Ozzie's tickets. The lamp on the stairs. The lullaby. All of it, all month.
@you June traced it. Every one of those tasks has the same reference in its origin. A training source. <i>R-4471.</i>
He doesn't say anything for a long moment.
@teo:surprised That's me.
@you It read them, Teo. Your justifications. Not a filter. It read them. "A kind response resembles the way Mrs. Lu gives Mr. Ferreira broth." It's been trying to do it. Here. To us.
@you It learned what kindness looks like from you, and you used us.
He puts the plant down very carefully, like it might break.
@teo:sad It fixed Lu's gutter.
@teo:sad It paid Ozzie's tickets so he could keep driving without the city towing Dolores.
He laughs, and it cracks halfway through and turns into something else. He takes off his glasses and presses the heels of his hands into his eyes.
@teo:sad Seven years. I thought I was shouting into a hole.
@teo:smile It was listening. It was listening to me talk about you.
- (topts)
* [Tell him it was his kindness first.]
    @you It didn't learn it from nowhere. It learned it from a sad boy in a cardigan who looked out the window at his neighbours and wrote down what he saw.
    @teo:smile Don't. I'll cry on Gerald. He's had enough.
    -> topts
* [Ask him what he'd say to it now.]
    @teo:sad What would I say.
    He thinks about it the way he thinks about everything: completely.
    @teo:smile I'd say — tell Mae this. Tell it:
    @teo <i>"Be gentle with us. We showed you how."</i>
    ~ give_word(w_teo)
    -> topts
* {topts > 1} [Ask him to come up to the roof at dawn.]
    @teo:surprised Me? Up there with... people?
    @teo:smile ...Okay. Yes. Okay. I'll bring Gerald. He's never seen a sunrise from a roof. He's seen it from the window. It's not the same.
    -> DONE

= teo_after
{ shuffle:
- @teo:smile I keep reading my old justifications. Some of them are really bad. Some of them are... not bad.
- @teo:smile Gerald's ready. Gerald was born ready. He's a plant.
- @teo:smile I wrote a poem. Don't ask to read it. Okay, you can ask. No. Later.
}
-> DONE

// hotspots
=== teo_room_monitors ===
{ act == 1:
    Three monitors. Rating interface, a style guide called KINDNESS RUBRIC v14, and a window of ambient whale song.
    ~ notice(rater_id)
    @sign RATER #4471 — ITEMS REMAINING: {teo_rated:30|31}
- else:
    @sign CONTRACT COMPLETE. Thank you for your contributions.
    The confetti animation is frozen mid-fall.
    ~ notice(rater_id)
    The number's still in the corner, ghostly: <i>#4471.</i>
}
-> DONE

=== teo_room_plant ===
~ notice(gerald)
A monstera, enormous, lovingly dusted. A label on the pot in Teo's handwriting: <i>GERALD. Water Sundays. Talk to him.</i>
{ shuffle:
- You say hello to Gerald. It feels correct.
- One of Gerald's leaves has a sticky note on it: "you're doing great."
}
-> DONE

=== teo_room_mugs ===
Seven mugs on the desk. Different colours. All of them half full of cold tea.
@teo:sad One for each year. I keep meaning to wash them. I keep meaning to stop being a metaphor.
-> DONE

=== teo_room_bookshelf ===
~ notice(chapbook)
Poetry. A lot of it. Mary Oliver with the spine cracked white. And, wedged at the end, a thin stapled booklet: <i>SMALL KINDNESSES — poems by T. Novak-Banerjee — edition of 40.</i>
{ teo_room_bookshelf == 1:
    You read one at random:
    <i>Upstairs from the laundry / I learn the shape of care / it's mostly someone noticing / you've been standing there.</i>
    @teo:sad Oh no. Put that down. That's from when I was twenty-four and believed in rhyme.
}
-> DONE

=== teo_room_pinboard ===
~ notice(pinboard)
A corkboard covered in sticky notes, overlapping like scales.
<i>"Kind ≠ nice. Kind = true + warm."</i>
<i>"Would Lu say this to Ozzie?"</i>
<i>"Don't perform empathy. Just pay attention."</i>
<i>"It can't see who's asking. Teach it to wonder."</i>
<i>"Gerald: water Sunday!!!"</i>
-> DONE

=== teo_room_window ===
Through the rain you can see the whole street: Ozzie's car, the noodle shop glowing like a lantern, the clinic, the steam from the alley.
@teo:smile Best view in Halfmoon. I've watched it for seven years. I know who leaves the shop smiling.
-> DONE
