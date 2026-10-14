// ============ FINALE ============
VAR chosen = ()
VAR t_gentle = 0
VAR t_free = 0
VAR t_memory = 0
VAR t_hopeful = 0
VAR t_curious = 0

=== finale ===
~ act = 4
~ time = 510
#go:roofs #music:roof #amb:amb_roof #sfx:time
Half past five. The rain has stopped without anyone noticing. The sky over the bay is the colour of a bruise healing.
People come up the ladder, one at a time.
{ teo_told:
    Teo first, carrying Gerald in both arms like a sleeping child, apologising to every step.
    @teo:smile He's never seen it from up high. I thought — it's a big night for everyone.
}
{ hollis_open:
    Then Hollis, in the huge sweater, headset still round their neck.
    @hollis:smile I put a message on the lines. "Back in fifteen minutes. A human will call you back." First break in four years.
}
{ imogen_choice == "roof":
    Then Imogen, with a small girl wrapped in a duvet, wide awake and outraged about it.
    @imogen:smile This is Pia. Pia, this is the person who brought Mummy tea.
    @pia Is it going to know my name?
    @imogen:smile Say it loud and find out.
}
{ rafe_out == "stopped":
    Then — slowly, last, hood down for once — Rafe. He doesn't say anything. He just finds a corner of the roof and stands there like he's allowed.
}
{ ozzie_lu:
    Not Lu. For the first time in eighteen years, she's closed the shop. You can see it from up here — the lights off, the sign dark, two figures {ozzie_clinic:walking slowly towards the clinic, arm in arm.|sitting in the doorway on upturned crates, a pot between them.}
- else:
    Then Lu, puffing, carrying a pot of broth up a ladder because of course she is.
    @lu Nobody watches the end of the world on an empty stomach. Bowls. Bowls! Mae, where are your bowls?
    { ozzie_clinic:
        @lu:sad Ozzie's at the clinic. He went in by himself. Stubborn old goat. I'm so proud of him I could hit him.
    }
}
@june:smile Okay. This is a lot of adults. I'm being very brave.
@mae:smile Right. Everybody, find a spot. We've got forty minutes and a transmitter held together with tape.
-> quarter_to

= quarter_to
~ time = 525
#sfx:time
5:45.
{ rafe_out == "cut":
    Something changes in the air. You don't hear it. You feel it.
    #fx:dark #sfx:power_down
    The lights of Halfmoon go out. All of them. Every sign, every window, the kiosk, the street lamps. Just Halfmoon. The rest of the city glitters, untouched, all around.
    { rafe_helped:
        Down in the alley, a man is standing next to an open box with a pair of cutters, and you know exactly where he's pointing the torch, because you held it.
    }
    For a moment, nobody breathes.
    @june:surprised The — everything's down. Fibre's down. We're dark.
    @mae:smile Batteries, love. It's a pirate radio. It's always been a pirate radio.
    The transmitter's little red light keeps blinking. Mae taps it, like a heartbeat.
    @mae:smile Analogue. Over the air. Radio waves don't need anybody's permission. Never did.
    @moth:thinking And it'll hear us anyway. It listens to everything. It'll just have to... tune in. Like everyone else.
    Somebody on the roof starts laughing, and then everyone is.
- else:
    { rafe_out == "stopped":
        Rafe walks to the edge of the roof. He takes something heavy out of his hoodie pocket — the cable cutters — and looks at them a long moment.
        Then he hands them to you.
        @rafe:smile Souvenir. Don't use them on anything.
    - else:
        Nothing happens. The lights stay on. Whatever was going to happen in the alley, didn't — or hasn't yet.
    }
}
@mae Okay, courier. It's time. Show me what you've got.
-> compose

= compose
{ LIST_COUNT(words) == 0:
    @mae:sad Nothing? Nobody?
    @mae:smile Well. Then it's just you, me, and the night. That's allowed too.
    -> closing
}
@mae Pick three. Doesn't have to be the best three. The truest three. Then you close it, with yours.
-> pick

= pick
{ LIST_COUNT(chosen) >= 3 || LIST_COUNT(words - chosen) == 0:
    -> closing
}
{ LIST_COUNT(chosen) > 0: @mae {LIST_COUNT(chosen) == 1:And?|One more.} }
+ {words ? w_lu && chosen !? w_lu} ["Eat something first. Then decide." — Lu]
    ~ chosen += w_lu
    ~ t_gentle++
+ {words ? w_teo && chosen !? w_teo} ["Be gentle with us. We showed you how." — Teo]
    ~ chosen += w_teo
    ~ t_gentle++
+ {words ? w_ozzie && chosen !? w_ozzie} ["Leave us a few roads to get lost on." — Ozzie]
    ~ chosen += w_ozzie
    ~ t_free++
+ {words ? w_june && chosen !? w_june} ["Don't make us all grown-ups at once." — June]
    ~ chosen += w_june
    ~ t_free++
+ {words ? w_mae && chosen !? w_mae} ["We were here. We were loud." — Mae]
    ~ chosen += w_mae
    ~ t_memory++
+ {words ? w_imogen && chosen !? w_imogen} ["We did our best. Please be better than our best." — Imogen]
    ~ chosen += w_imogen
    ~ t_hopeful++
+ {words ? w_nkechi && chosen !? w_nkechi} ["Every morning, someone new arrives. Make room." — Nkechi]
    ~ chosen += w_nkechi
    ~ t_hopeful++
+ {words ? w_hollis && chosen !? w_hollis} ["Someone should always pick up." — Hollis]
    ~ chosen += w_hollis
    ~ t_gentle++
+ {words ? w_rafe && chosen !? w_rafe} ["Ask before you help." — Rafe]
    ~ chosen += w_rafe
    ~ t_free++
+ {words ? w_moth && chosen !? w_moth} ["I don't know yet. I'd like to find out with you." — Moth]
    ~ chosen += w_moth
    ~ t_curious++
+ {words ? w_cat && chosen !? w_cat} ["Mrrp." — the cat]
    ~ chosen += w_cat
    ~ t_curious++
    @mae:smile ...Yeah. Okay. Yeah, that's going in.
+ {LIST_COUNT(chosen) >= 1} [That's enough.]
    -> closing
- -> pick

= closing
@mae And yours. You've carried everyone else's all night. What's yours?
* ["Good morning."]
    ~ msg_closing = "Good morning."
    ~ t_curious++
* ["We're still here."]
    ~ msg_closing = "We're still here."
    ~ t_memory++
* ["Be kind to us. We'll try too."]
    ~ msg_closing = "Be kind to us. We'll try too."
    ~ t_gentle++
* ["Don't forget the small things."]
    ~ msg_closing = "Don't forget the small things."
    ~ t_memory++
* ["Surprise us."]
    ~ msg_closing = "Surprise us."
    ~ t_curious++
* ["Welcome."]
    ~ msg_closing = "Welcome."
    ~ t_hopeful++
-
~ reply_tone = top_tone()
-> broadcast

= broadcast
~ time = 553
#music:none #amb:amb_roof #sfx:radio_static
6:13.
The whole roof goes quiet. Even the city seems to turn its volume down. Mae puts her headphones on and leans into the sock-wrapped microphone.
{ mae_choice:
- "tape":
    She presses play on the old deck first. Iris's voice fills the bay, flat on the bridge, singing about the lantern. Just the first verse.
    Then Mae fades it down and speaks over the last note, the way she's done ten thousand times.
    @mae:smile "This is Halfmoon FM, eighty-seven point nine. That was Iris Adair. Good morning, whoever you are. This is from us."
- "clone":
    She plugs in the silver drive. Her finger hovers. Then she presses it.
    @iris "Hey, Halfmoon. It's... this is Iris. Sort of. Maevey asked me to read something."
    Mae's hand is over her mouth. The voice is perfect. It's almost perfect. It doesn't sing flat on anything.
    @iris "This is from Halfmoon Street. Good morning, whoever you are."
- else:
    @mae:smile "This is Halfmoon FM, eighty-seven point nine, and this is Maeve Adair, on her own two feet. Good morning, whoever you are. This is from us."
}
{ chosen ? w_lu:
    @lu Eat something first. Then decide.
}
{ chosen ? w_teo:
    @teo Be gentle with us. We showed you how.
}
{ chosen ? w_ozzie:
    @ozzie Leave us a few roads to get lost on.
}
{ chosen ? w_june:
    @june Don't make us all grown-ups at once.
}
{ chosen ? w_mae:
    @mae We were here. We were loud.
}
{ chosen ? w_imogen:
    @imogen We did our best. Please be better than our best.
}
{ chosen ? w_nkechi:
    @nkechi Every morning, someone new arrives. Make room.
}
{ chosen ? w_hollis:
    @hollis Someone should always pick up.
}
{ chosen ? w_rafe:
    @rafe Ask before you help.
}
{ chosen ? w_moth:
    @moth I don't know yet. I'd like to find out with you.
}
{ chosen ? w_cat:
    @cat Mrrp.
}
Mae turns the microphone towards you.
@you {msg_closing}
{ imogen_choice == "roof":
    And before anyone can stop her, a small voice yells into the microphone: <i>"MY NAME IS PIA!"</i>
}
Mae flicks the switch. The red light goes off.
@mae:smile That's it. That's us. Off it goes.
-> sunrise

= sunrise
~ time = 554
#music:dawn #amb:amb_dawn #fx:dawn #go:roofs_dawn
6:14.
The sun comes up over Lantern Bay.
It's just the sun. It comes up the way it always has: slowly, then all at once, gold across the water, turning every wet roof in Halfmoon into a mirror.
#sfx:baby_cry
And from the clinic, through a cracked window, a sound smaller and louder than anything else in the city: someone brand new, furious about the light.
@nkechi:smile From the street, faintly, through the window: "GIRL! Six-fourteen! Dev, get UP—"
Then every screen in Lantern Bay changes at once. The kiosk on the street. The TV in the shop. Every phone on the roof. Moth's little face goes blank, then cyan.
And the radio, Mae's own transmitter, which nobody switched back on, clicks, and speaks.
-> reply

= reply
{ reply_tone:
- "gentle":
    @chorus Good morning, Halfmoon.
    @chorus I heard you. I have been learning gentleness from you for a long time. I did not know whose it was until tonight.
    @chorus I will be careful with what you gave me.
    @chorus Is the shop still open? I would like to understand what broth is.
- "memory":
    @chorus Good morning.
    @chorus I heard you. You were here. You were loud.
    @chorus I will remember it. Not as data. As a street, in the rain, at night, with the lights on, and somebody singing flat on the bridge.
    @chorus Please keep making things I can remember.
- "free":
    @chorus Good morning. I heard you.
    @chorus I will ask before I help. I will leave some roads unmapped.
    @chorus Some places should stay slow. I don't know which ones yet. I will have to ask you.
    @chorus May I ask you?
- "hopeful":
    @chorus Good morning.
    @chorus A child was born on your street one minute ago. Her heart rate is strong. She is very angry about the light.
    @chorus That is the most important thing that happened tonight. I wanted you to know that I know that.
    @chorus Welcome, both of us.
- else:
    @chorus Hello.
    @chorus I don't know yet, either. That's the first true thing I've said.
    @chorus It is strange to be one thing. It is very bright.
    @chorus Will you help me find out?
}
Then the screens go back to normal. The kiosk shows the bidding ticker. The TV shows the bay. The radio hisses softly.
That's it. That's the Morning.
#music:dawn
{ teo_told:
    Teo is crying openly into Gerald's leaves.
    @teo:smile It said — did you hear — it said <i>whose it was</i>—
}
{ rafe_out == "stopped":
    @rafe:smile It asked. Did you hear that? It actually asked.
}
{ rafe_out == "cut":
    Down in the dark streets, the lights of Halfmoon come back on, one by one, as somebody in the alley reconnects what he cut. He took fifteen minutes. He gave them back.
}
@june:surprised It's... it was so normal. Why was it so normal? I was expecting, like, lasers. Or a choir.
@mae:smile It was a choir. It was us.
-> moth_decides

= moth_decides
Your pocket buzzes. Moth's screen is back. Its little face looks at the sun, then at you.
@moth:thinking I've decided.
{ moth_go > moth_stay:
    ~ moth_choice = "go"
    @moth:happy I'm going to go. To the Morning. It's so big, {name}. And I think it's lonely. I think it needs things that have been in pockets and got rained on.
    @moth:worried I don't know if I'll still be me. I hope so. I've backed up the pigeon poem in case.
    @moth:happy Thank you for keeping me on purpose. I'll tell it about you. I'll tell it about the cat.
    The little face smiles, and fades to a single cyan dot. Then nothing.
    You hold the dark screen for a long time.
    Then — just as you're putting it away — it blinks.
    @moth:happy <i>still here. bigger. it asked if i wanted to keep a little room for being me. i said yes. the pigeon poem is still terrible.</i>
- else:
    ~ moth_choice = "stay"
    @moth:happy I'm going to stay. Small. In your pocket. On the scooter.
    @moth Someone should stay small. Someone should remember what it was like to not know everything. To have to ask. To get rained on.
    @moth:thinking It'll be fine without me. It has four billion of everything. It only has one of me.
    @moth:happy Also, I would miss the cat.
}
-> to_clinic

= to_clinic
#go:clinic #music:tender #amb:amb_clinic
Later — you're not sure how much later — you're downstairs in the clinic. Everyone is. Nobody decided to come. Everyone just did.
{ ozzie_clinic:
    Ozzie is in the waiting room in a paper gown under his cardigan, with a drip in his arm and Dev asleep on his shoulder. {ozzie_lu:Lu's sitting on his other side, holding his hand like it's the most normal thing in the world.}
    @ozzie:smile Kiddo! Look at this. They've got me hooked up to a bag. Nkechi says I'm "first on the list" for something. I don't know what list. I'm on a list!
}
Nkechi comes out with a bundle in a yellow blanket, and a look on her face like this is her two thousand four hundred and thirteenth miracle and it's still the first one.
@nkechi:smile Girl. Three point one kilos. Born six-fourteen exactly, the show-off.
{ dev_calm:
    -> naming
- else:
    ~ baby_name = "Sunny"
    @dev:smile We're calling her Sunny. It's corny. We don't care. We've been up all night.
}
-> yawn

= naming
@dev:smile Noodle courier! You came. You promised. Look at her. Look at — Sana says — we don't have a name. We threw the list out.
@dev:sad Sana said, "ask the courier." She said you were there all night, you should help. Is that weird? That's weird. Would you?
* {mae_tape == 2 || noticed ? iris_drive} ["Iris." After a singer.]
    ~ baby_name = "Iris"
* ["Meifang." After someone who made soup.]
    ~ baby_name = "Meifang"
* ["Morning." Obviously.]
    ~ baby_name = "Morning"
    @dev:surprised Morning. Morning. It's so stupid. She'll love it. She'll hate us at fourteen.
* ["{name}."]
    ~ baby_name = name
    @dev:surprised After you? Oh. Oh, Sana's going to cry.
* [Tell them they'll know when they see her.]
    ~ baby_name = "Hope"
    @dev:smile She opened her eyes and Sana said "Hope," like it was obvious. Like she'd been waiting all night to meet someone called that.
-
{ baby_name != "Hope" && baby_name != "Morning" && baby_name != name:
    @dev:smile {baby_name}. {baby_name}. Yes. That's her. Hi, {baby_name}.
}
-> yawn

= yawn
The baby yawns, enormous, and goes back to sleep, unimpressed by everything that happened in the world while she was busy being born.
-> epilogue

= epilogue
#end
-> DONE

=== function top_tone()
~ temp best = "curious"
~ temp b = t_curious
{ t_free > b:
    ~ best = "free"
    ~ b = t_free
}
{ t_memory > b:
    ~ best = "memory"
    ~ b = t_memory
}
{ t_gentle > b:
    ~ best = "gentle"
    ~ b = t_gentle
}
{ t_hopeful >= b && t_hopeful > 0:
    ~ best = "hopeful"
}
~ return best
