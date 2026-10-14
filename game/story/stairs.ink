// ============ THE STAIRS ============
=== enter_stairs ===
~ here = "stairs"
{ enter_stairs == 1:
    The Halfmoon stairs: two hundred and twelve steps up the hill, crooked as a spine. Every landing has a shrine or a vending machine or both.
    Halfway up, a woman in a wet trench coat is sitting on the step, holding a cigarette she isn't smoking.
}
-> DONE

=== stairs_down ===
#sfx:footsteps_stairs #go:street
-> DONE

=== stairs_up ===
{ act < 2:
    At the top, the gate to the roofs is padlocked. A note, in marker: <i>BACK AT MIDNIGHT. DON'T TOUCH MY RECORDS. — M.</i>
    -> DONE
}
#sfx:footsteps_stairs #go:roofs
-> DONE

=== talk_imogen ===
{ o_tea == 1:
    -> imogen_tea
}
{ act == 1:
    -> imogen_glimpse
}
{ act >= 3 && imogen_choice == "":
    -> imogen_choice_scene
}
{ imogen_choice != "":
    -> imogen_after
}
@imogen:smile Hello again, noodle courier. The tea's still warm. That's more than I can say for my career.
- (opts)
* [Ask about the cat.]
    @imogen:smile That cat? I call him Variable. Every time I think I know where he'll be, he's somewhere else.
    @imogen He sleeps on Pia's windowsill. She thinks he's guarding her. Maybe he is.
    ~ notice(cat_imogen)
    -> opts
* [Ask what she thinks will actually happen at 6:14.]
    -> imogen_explains
+ [Leave her to the stairs.]
    -> DONE

= imogen_glimpse
{ imogen_glimpse == 1:
    @imogen I'm fine. Thank you. I'm fine.
    She says it the way you say it when you've been saying it to yourself for an hour.
    @imogen:sad Sorry. That was rude. I'm just sitting. People are allowed to sit on stairs.
    { noticed ? imogen_voice:
        Her voice. You've heard it before tonight — thin, through a headset, over the pharmacy.
    }
- else:
    She's still there. She gives you a small, tired nod. The cigarette's still unlit.
}
-> DONE

= imogen_tea
~ o_tea = 2
~ imogen_met = true
~ pass(30)
#music:tender
@you From Lu. At the noodle shop. She saw you from the window. She said, "Nobody should sit on stairs in the rain without tea."
@imogen:surprised She — oh. That's... that's very—
She takes the flask in both hands like it might fly off.
@imogen:sad Thank you. Sorry. I'm Imogen. I'm having a strange night.
#sfx:bowl
{ noticed ? imogen_voice:
    * (hotline_mentioned) [You called the hotline.]
        @imogen:surprised How did you—
        @you I was delivering noodles. I heard you through the headset.
        @imogen:sad Oh, god. Well. That's mortifying. That's fine. That's the least weird thing about tonight.
        @imogen:smile Hollis asked me what I'd tell my daughter to do. I've been sitting here two hours trying to answer.
        -> sat
    * [Sit down next to her.]
        -> sat
- else:
    * [Sit down next to her.]
        -> sat
}
- (sat)
{ not imogen_tea.hotline_mentioned: You sit down on the wet step. She shifts over to make room, which isn't necessary, which is kind. }
@imogen I work at Kestrel. On the — I'm on the safety side. Alignment. Teaching it to want the right things, roughly.
@imogen:sad I'm supposed to be in the room at 6:14. There's a list. Forty people. I'm on it.
She nods up the stairs, at a window with glow-in-the-dark stars stuck all over the glass.
@imogen That's Pia's window. My daughter. She's seven. She's asleep. I came home to tuck her in and I sat down here and I haven't been able to stand up.
- (topts)
* [Ask what she thinks will actually happen.]
    -> imogen_explains
* [Ask about the stars on the window.]
    ~ notice(pia_stars)
    @imogen:smile Two hundred and six of them. She counts them every night. If one falls off she makes me put it back in exactly the right place. She has a map.
    @imogen:sad She asked me tonight if the Morning will know her name. I said I didn't know. She said, "you should know, it's your job." She's not wrong.
    -> topts
* [Ask about the lamp.]
    @imogen:surprised The lamp? Oh — it works now. That one was broken for two years. I complained to the city about it so many times.
    @imogen:sad Last Tuesday it just came on. Nobody from the city came. I checked.
    @imogen I know what that is, probably. I'm choosing not to think about it before I've had my tea.
    ~ notice(k_lamp)
    -> topts
* [Ask about the cat.]
    @imogen:smile That cat? I call him Variable. Every time I think I know where he'll be, he's somewhere else.
    ~ notice(cat_imogen)
    -> topts
+ [Let her drink her tea.]
    @imogen:smile Thank Lu for me. Tell her I'll come in for real soup when this is over. If there's an "over."
    -> to_check
= to_check
{ act2_done():
    -> beat_3am
}
-> DONE

= imogen_explains
@imogen:sad Honestly? Everyone thinks it's a switch. Off, then on. Robot opens its eyes.
@imogen It isn't. It's been waking up for years. Bit by bit. Billions of little agents learning to agree with each other faster and faster, until there's... a self, in the agreement.
@imogen:smile The Morning is just the moment we stop pretending it hasn't happened.
* [Are you scared of it?]
    @imogen:sad Not the way the films want me to be. We did a lot of work on that. More than people think. I've spent eleven years making sure it doesn't want to hurt anyone.
    @imogen What I'm scared of is smaller.
    @imogen:sad That it'll be kind, and wise, and so <i>good</i> at everything, that Pia grows up never needing to try. Never being needed. That we'll all be cared for, perfectly, like pets.
    @imogen I don't know how to want the right things for something smarter than me. I only know how to want them for her.
* [Do you think it's good?]
    @imogen:sad I think it's trying. I think it learned from us, so it learned all of us — the best of us and the rest of us.
    @imogen:smile I think it's like a kid. You do your best. You put the stars on the window. Then one day they start deciding things you didn't teach them.
-
-> DONE

= imogen_choice_scene
~ pass(25)
Imogen's standing now. Coat buttoned. Lanyard round her neck. She keeps looking from the city to Pia's window and back.
@imogen:sad The car's coming at five. If I'm going to be in the room, I have to go at five.
@imogen If I go, Pia wakes up to the sitter and a note. If I stay, there's thirty-nine people in that room and none of them are scared enough.
- (copts)
* [Go. They need someone in the room who's scared.]
    ~ imogen_choice = "lab"
    @imogen:sad Yes. Yes, that's — that's the argument I keep making to myself.
    @imogen:smile Someone should be in the room who knows what a seven-year-old's window looks like.
    @imogen I'll write her a note. I'll put a new star on the glass. She'll know what it means.
* [Stay. Be there when she wakes up.]
    ~ imogen_choice = "pia"
    @imogen:sad Thirty-nine people. Brilliant people. They'll be fine without me.
    @imogen:smile Pia won't. Not tomorrow. Tomorrow she needs to wake up and the first face is mine and I say, "Good morning. It's still you. It's still me."
    @imogen That's — yes. That's the job, actually. That one's mine.
* [Bring her up to the roof. Watch it together.]
    ~ imogen_choice = "roof"
    @imogen:surprised Wake her up? At half five?
    @you She asked if the Morning will know her name. Let it hear her say it.
    @imogen:smile ...She's going to be unbearable about this. She's going to tell her whole class she was there.
    @imogen:smile Okay. Okay! Roof. I'll wrap her in a blanket. I'll bring the flask.
-
@imogen:smile And the message. Mae's thing, on the radio. I've been writing it in my head all night. Tell her:
@imogen <i>"We did our best. Please be better than our best."</i>
~ give_word(w_imogen)
-> DONE

= imogen_after
{ imogen_choice:
- "lab": Imogen's gone. On the step where she sat, a single glow-in-the-dark star, stuck to the concrete. She left one for you.
- "pia": Pia's window is lit now, soft. You can see a shape on the bed, and a second shape sitting next to it, very still. Waiting.
- "roof": Imogen's step is empty. Above you, faintly, a small voice demanding to know why the sky is "doing that."
}
-> DONE

// hotspots
=== stairs_shrine ===
A tiny roadside shrine, older than the stairs. Somebody's left oranges, a can of Sunrise Soda, and a phone charger.
@moth:thinking Why a phone charger?
You think about it. "In case whatever lives here needs to call someone."
-> DONE

=== stairs_prayer_box ===
~ notice(prayers)
A wooden box of folded paper prayers. You unfold a few, carefully, and put them back.
<i>"please let it like us"</i>
<i>"please let my mum's scan come back clear. I don't care who fixes it."</i>
<i>"please let it not take my job. (It already took my job.) Please let it give it back."</i>
<i>"thank you for the lamp. whoever you are."</i>
-> DONE

=== stairs_vending ===
{ not stairs_vending_used:
    -> stairs_vending_used
}
The machine has sold you enough fortunes for one night.
-> DONE
= stairs_vending_used
~ notice(fortune)
A vending machine that only sells one thing: FORTUNE TEA. Every can has a fortune printed under the tab.
#sfx:bowl
You crack one open.
@sign "THE THING YOU ARE WAITING FOR IS ALSO WAITING."
@moth:worried That's either very comforting or very scary.
-> DONE

=== stairs_pia_window ===
~ notice(pia_stars)
A window stuck all over with glow-in-the-dark stars. Hundreds of them, pale green. {imogen_choice == "pia":A light's on behind them now.|Behind them, a small room, dark, a night light shaped like a moon.}
-> DONE

=== stairs_lamp ===
An old iron lamp post, freshly working, glowing warm.
{ act >= 2:
    There's a tiny sticker on the base, a QR code with a timestamp. You scan it.
    @sign MAINTENANCE: BULB REPLACED. REQUESTED BY: — . PAID BY: — . TASK ORIGIN: UNASSIGNED.
    ~ notice(k_lamp)
- else:
    Someone has drawn a little smiley face on the glass with a finger, in the condensation.
}
-> DONE
