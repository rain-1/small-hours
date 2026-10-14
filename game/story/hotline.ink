// ============ HUMANS ONLY HOTLINE ============
=== enter_hotline ===
~ here = "hotline"
{ enter_hotline == 1:
    Up a steep staircase over the pharmacy. A door with a hand-painted sign: <i>HUMANS ONLY HOTLINE — come in, we're probably on the phone.</i>
    Three desks, warm lamps, every phone blinking.
    #sfx:phone_ring
}
-> DONE

=== hotline_exit ===
#sfx:footsteps_stairs #go:street
-> DONE

=== talk_hollis ===
{ o_hotline == 1:
    -> hollis_delivery
}
{ hollis_cover && not hollis_open:
    -> hollis_opens
}
{ shuffle:
- @hollis:smile Hey, noodle angel. Lines are wild. Everybody wants to know if a human's still here. I keep saying: yep. Still here.
- @hollis Shh — sorry — line six is crying. Give me a sec.
}
- (opts)
* [Ask about the cat.]
    @hollis:smile Caller Nine? He comes in through the window and sits on desk nine. We don't have a desk nine. We have three desks. He sits on the space where desk nine would be.
    @hollis I've decided he's a caller. He just never says anything. Some of them don't.
    ~ notice(cat_hollis)
    -> opts
* [Ask how the hotline works.]
    @hollis You pay a coin. Literally, a coin, or a few cents online. Then you get a human. Verified. Me, or Priya, or Old Sam on weekends.
    @hollis:smile We don't fix anything. We're not therapists. We just pick up. You'd be amazed how many people only need someone to pick up.
    -> opts
* {not hollis_cover && act >= 2} [Offer to watch the phones so they can eat.]
    -> hollis_cover_scene
+ [Leave them to it.]
    -> DONE

= hollis_delivery
~ o_hotline = 2
~ pass(25)
A person in an enormous wool sweater, headset on, teal buzz-cut growing out, waves you in without looking up. They mouth: <i>one sec.</i>
@hollis Yeah. Yeah, I'm here. I'm a person. Take your time.
#sfx:bowl
You put the bowl on the desk. They're listening so hard to the phone they don't notice. A thin voice leaks from the headset.
@phone "...I'm sitting on some stairs. I'm supposed to be at work. I help make the thing everyone's counting down to."
@phone "My daughter's asleep upstairs. I came home to tuck her in and I can't — I can't go back. I don't know which is braver."
@hollis What would you tell your daughter to do?
@phone "...That's not fair."
@hollis:smile I know. Sorry. I've got a lot of practice being unfair at four in the morning.
@phone "...It's ten at night."
@hollis Then I'm early.
A small laugh on the line. Then a click.
~ notice(imogen_voice)
@hollis:sad That one was good. She'll be okay. Maybe.
They finally look at the bowl. Their whole face changes.
@hollis:smile Lu. Oh, she's the best. I forgot to eat at, like, two in the afternoon. Thank you, noodle angel.
-> DONE

= hollis_cover_scene
~ hollis_cover = true
~ pass(30)
@hollis:surprised You'd — really? I haven't eaten sitting down in... okay. Okay! Rules: you're a human. You don't fix. You don't promise anything. You stay.
@hollis If they don't talk, you stay anyway. That's the whole job.
They hand you the headset. It's warm. #sfx:phone_ring
@you Humans Only Hotline. I'm, um. I'm a human.
@phone "...are you a real one?"
It's a kid. Eight, maybe nine.
@phone "My mum said I could call because I can't sleep. Is it going to hurt? The Morning?"
* [Tell her the truth: nobody knows.]
    @you I don't know. Nobody really knows. But I don't think so. The people who made it tried really hard for it not to hurt anyone.
    @phone "Okay. That's what my mum said too. I wanted to check with a different grown-up."
* [Tell her it's going to be fine.]
    @you It's going to be fine.
    @phone "How do you know?"
    You remember Hollis: <i>you don't promise anything.</i>
    @you I don't, actually. I'm sorry. I just really hope so. Is that okay?
    @phone "...Yeah. That's more honest."
* [Ask her what she's scared of.]
    @you What's the scariest part?
    @phone "That I'll wake up and everything will be different and I won't know where anything is."
    @you Is your mum going to be there when you wake up?
    @phone "Yeah."
    @you Then you'll know where the most important thing is.
-
@phone "Okay. I'm going to try sleeping now. Bye, human."
Click. #sfx:phone_ring
The next one. An old man, very polite.
@phone "Hello. I don't need anything. I just wanted to tell a person about my tomatoes. Is that all right?"
* [Of course. Tell me about your tomatoes.]
* [I have... a few minutes.]
-
He tells you about his tomatoes. They are called Brandywine. His late wife grew them from seeds her father brought over on a ship. This year they split in the rain but tasted better than ever.
@phone "That's all. Thank you. Everyone I talk to now is very clever. I wanted someone who'd just say 'oh, lovely.'"
@you Oh, lovely.
@phone "Yes. Exactly like that. Goodnight."
#sfx:phone_ring
The third call. You pick up. Nobody speaks. You can hear breathing, and rain, and a TV somewhere counting down.
* [Stay.]
- (silence)
The line stays open. Ten seconds. Twenty.
* [Stay.]
    -> silence
* [Say: "I'm still here."]
-
@you I'm still here.
A long breath out on the other end.
@phone "...thanks."
Click.
Hollis is standing in the doorway with their bowl. They've been there a while.
@hollis:smile You stayed. Most people can't stand the silent ones. You stayed.
-> DONE

= hollis_opens
~ hollis_open = true
~ pass(15)
Hollis is sitting on the sofa, bowl empty, knees up, headset round their neck. The lines are quiet for one rare minute.
@hollis:sad Can I tell you something weird?
@hollis Nobody's ever picked up for me. On this line. I mean — obviously. It's my line. But four years, thousands of calls, I've never once been the caller.
- (hopts)
* [Ask: "Are you okay?"]
    @you Are you okay?
    They stare at you. Then laugh, startled.
    @hollis:sad Wow. Okay. Nobody's asked me that in... huh.
    @hollis:sad I grew up in a lot of houses. Seven, eight. You learn to listen for which voice in the house is safe. I got really good at hearing voices.
    @hollis So I made a place where the voice is always safe. Where someone always picks up. Because nobody did, for a while, for me.
    @hollis:smile I'm okay. Tonight I'm really okay. Thanks for asking. Seriously.
    -> hopts
* [Ask about the notes on the wall.]
    -> hotline_notes_wall
* [Ask what they'd tell the Morning.]
    @hollis:smile Oh, easy. I've been thinking about it all night, honestly.
    @hollis <i>"Someone should always pick up."</i>
    @hollis Whatever it is. However clever. Somebody calls at four in the morning — pick up. Don't fix them. Stay.
    ~ give_word(w_hollis)
    -> hopts
+ [Let them rest.]
    -> DONE

// hotspots
=== hotline_phones ===
{ hollis_cover: Three phones, every line blinking. You know how heavy that headset is now. | Three old desk phones and three headsets. Every line is lit. Every light is somebody. }
-> DONE

=== hotline_switchboard ===
A hand-built light panel, labelled in tape: LINE 1, LINE 2... LINE 8. There's a ninth light, unlabelled, which never comes on.
{ noticed ? cat_hollis: Desk nine. Caller Nine's line. }
-> DONE

=== hotline_notes_wall ===
~ notice(notes_wall)
A wall of thank-you notes, hundreds, every colour.
<i>"you picked up when i was on the bridge. i'm a dad now."</i>
<i>"thank you for not trying to sell me anything"</i>
<i>"I just needed to hear a person breathe. Thank you, Sam."</i>
{ hollis_open || act >= 2:
    In the corner, a printed bill, stamped: <i>PAID — ANONYMOUS — 4 MONTHS IN ADVANCE.</i> Under it, Hollis has written: <i>WHO ARE YOU?? (thank you)</i>
    ~ notice(k_phonebill)
}
-> DONE

=== hotline_kettle ===
{ not made_tea:
    -> made_tea
}
The kettle ticks as it cools.
-> DONE
= made_tea
#sfx:kettle
You put the kettle on without asking. When it boils, you make two mugs and put one next to Hollis's elbow.
They look at the mug like nobody's done that in a long time. They mouth: <i>thank you.</i>
-> DONE

=== hotline_window ===
Pink neon from the HOTLINE sign leaks in through the rain. Down on the street, you can see your scooter, and Ozzie's car, and the cat on his crate like a loaf of bread with opinions.
-> DONE

=== hotline_sofa ===
A sagging green sofa with a crocheted blanket and a pillow that says <i>YOU ARE NOT A BURDEN.</i> It has clearly been slept on many times.
-> DONE
