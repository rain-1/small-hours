// ============ NIGHT CLINIC ============
=== enter_clinic ===
~ here = "clinic"
{ enter_clinic == 1:
    The night clinic smells like disinfectant and old coffee. From behind a door marked LABOUR &amp; DELIVERY, someone is swearing with tremendous creativity.
}
-> DONE

=== clinic_exit ===
#go:street
-> DONE

=== talk_nkechi ===
{ o_clinic == 1:
    -> nkechi_delivery
}
{ o_ice == 1:
    -> nkechi_ice
}
{ act >= 3 && not dev_calm:
    @nkechi Ah — good, you. I need you to do something with that man before he faints on my floor. Talk to him. Anything. You have a calming face. It's very boring. I mean that kindly.
    -> DONE
}
{ act >= 3 && dev_calm && words !? w_nkechi:
    -> nkechi_word
}
{ shuffle:
- @nkechi Hm? I'm fine. Babies come when babies come. Two thousand four hundred and twelve of them, and not one has ever checked the news first.
- @nkechi:smile You again. Are you lost or are you hungry? Both is allowed.
}
- (opts)
* [Ask about the cat.]
    @nkechi:smile Little Pastor? He sits in the waiting room with the frightened fathers. Very solemn. Very calming. Then he steals their sandwiches.
    @nkechi I call him Little Pastor because he visits everyone and he never brings anything.
    ~ notice(cat_nkechi)
    -> opts
* {ozzie_heart == false && act >= 1} [Ask if there's anything else she needs.]
    @nkechi Tell that stubborn old man in the teal car to come and see me. He'll know which one he is.
    @nkechi:sad He knows what it's about. He's pretending he doesn't. Tell him I said pretending doesn't work on hearts.
    ~ ozzie_heart = true
    -> opts
* [Ask what she thinks about the Morning.]
    @nkechi When I started, they said the machines would deliver the babies. Then they said the machines would tell me how to deliver the babies.
    @nkechi:smile Now the machine on my desk tells me Sana's numbers and I tell the machine to hush, and then I hold Sana's hand.
    @nkechi Whatever wakes up tonight, it will not be holding Sana's hand. I will be. That's my job. Somebody's job will always be the hand.
    -> opts
* {noticed ? june_photo} [Tell her June is on the roof.]
    @nkechi:surprised June Takahashi-Reyes? Two point nine kilos, came out looking furious at everybody?
    @nkechi:smile Oh, tell her I said hello. Tell her she still owes me for the blanket she was sick on.
    -> opts
+ [Let her work.]
    -> DONE

= nkechi_delivery
~ o_clinic = 2
~ pass(25)
A tall woman in scrubs and a cardigan comes out of the delivery room, reading glasses on her head and another pair on a chain round her neck.
@nkechi:smile Congee! Lu is a saint. Lu is the only saint. Give.
#sfx:bowl
She takes one, and hands the other to a man in the waiting room chairs who is rocking slightly.
@nkechi Dev. Eat. You're no good to her fainted.
@dev:sad I can't. I can't eat. Is she okay? Is it normal that she said that thing about my mother?
@nkechi:smile It is extremely normal. She'll say worse by four o'clock.
She turns back to you, lowers her voice.
@nkechi First baby. Long labour. She'll come round dawn, I think. Sunrise baby.
@nkechi:sad They put a lullaby on the ward speakers, you know. Queued for 6:14 exactly. Nobody here asked for it. The system says "anonymous agent."
@nkechi I'm not taking it off. It's a nice lullaby.
~ notice(k_lullaby)
-> opts_after
= opts_after
* [Ask about the man in the chair.]
    @nkechi:smile That's Dev. He is having a very hard night, by which I mean his wife is.
    @nkechi Lost his job last month — logistics, the swarm took the whole department. Now this. Be nice to him.
    -> DONE
+ [Go.]
    -> DONE

= nkechi_ice
~ o_ice = 2
~ song_req = 1
~ pass(20)
#sfx:bowl
@nkechi:smile Ice! Oh, Lu, you darling. Our machine died at eleven. Of course it did. Tonight of all nights.
@nkechi Now. I need one more thing and you're going to think I'm mad.
@nkechi Sana wants a song. When she was little her mother took her to Halfmoon Noodle at New Year and a woman sang. Something about a lantern. A lighthouse keeper.
@nkechi:sad Her mother's gone now. She wants to push this baby out to that song. She can't remember the words. Can't find it anywhere online.
@nkechi:smile You go everywhere tonight. Ask around. Mae on the radio knows every song ever sung.
{ act2_done():
    -> beat_3am
}
-> DONE

= nkechi_word
~ give_word(w_nkechi)
{ song_req == 2:
    @nkechi:smile Listen. The song. That woman's voice came through the speaker and Sana stopped swearing and started singing along. Badly. Beautifully.
- else:
    @nkechi:smile Sana's stopped swearing. She's humming instead. Something about a lantern, she only knows half of it.
}
@nkechi Eight centimetres. Won't be long now.
@nkechi And Dev's still upright. You did that.
@nkechi:smile For your message. Tell the thing this, from the night shift:
@nkechi <i>"Every morning, someone new arrives. Make room."</i>
-> DONE

// ============ DEV ============
=== talk_dev ===
{ act >= 3 && not dev_calm:
    -> dev_calm_scene
}
{ dev_calm:
    @dev:smile I'm okay. I'm okay! I'm breathing in for four. Out for six. I'm a breathing expert now.
    -> DONE
}
{ shuffle:
- @dev:sad Sorry. Hi. Sorry. Do you know if it's normal to feel like you're going to throw up for nine hours?
- @dev:sad She told me to get out and then she told me to come back and then she told me I was "a rumour." What does that mean?
}
- (opts)
* [Ask about his lanyard.]
    ~ notice(dev_lanyard)
    A lanyard from a logistics company, BAYLINE FREIGHT. The photo on it is him, looking much less tired.
    @dev:sad I don't know why I'm wearing it. Habit. Thirty-two people in my department and now it's a swarm and one supervisor who's twenty-three.
    @dev:smile The severance was okay. I'll be home for the first six months. Sana says that's the universe being weird but generous.
    -> opts
* [Ask if they've picked a name.]
    @dev:sad We had a list. Then we threw the list out. Then she said, "we'll know when we see her." What if I don't know? What if I'm the only one who doesn't know?
    -> opts
+ [Leave him to his breathing.]
    -> DONE

=== dev_calm_scene ===
~ dev_calm = true
~ pass(20)
Dev is standing, sitting, standing again. He has torn a paper cup into a perfect spiral.
@dev:sad She's — they said eight centimetres — I don't know what that means but it sounds like a lot of centimetres —
* [Sit with him and breathe.]
    You sit next to him. You don't say anything. You breathe in, slow. Out, slower. After a while, he does too.
* [Make him laugh.]
    @you Nkechi's delivered two thousand four hundred babies. Statistically, she's going to be fine. You might faint, though.
    @dev:surprised I might faint?
    @you You've torn a cup into a spiral, Dev.
    He looks at the spiral. He laughs, too loud, then can't stop.
* [Tell him he's going to be good at this.]
    @you You're going to be good at this.
    @dev:sad You don't know that.
    @you You've been terrified for nine hours for somebody who doesn't exist yet. That's the whole job, isn't it?
-
@dev:smile Okay. Okay. Thank you. Who are you, by the way? You just keep turning up with food.
@you I'm the noodle courier.
@dev:smile The noodle courier. When she's here — when she's out — come and meet her. Okay? Promise.
-> DONE

// hotspots
=== clinic_desk ===
A reception desk with a sleeping terminal and a sign in marker pen: <i>BACK IN 5 MINS — NKECHI.</i> Under it, in different pen: <i>(she means 5 hours)</i>
-> DONE

=== clinic_coffee ===
{ not had_coffee:
    -> had_coffee
}
You decide you've suffered enough.
-> DONE
= had_coffee
The coffee machine is older than the clinic. It dispenses something brown into a paper cup with the confidence of a liar.
It tastes like a hot penny that's given up.
@moth:worried I'm detecting stress in your posture.
-> DONE

=== clinic_baby_photos ===
~ notice(june_photo)
A whole wall of baby photos, hundreds of them, curling at the corners. Every one labelled in the same neat hand: a name, a weight, a date.
In the middle of the third row: a scowling newborn in a yellow blanket. <i>JUNE T-R — 2.9kg — the furious one.</i>
{ clinic_baby_photos == 1:
    @moth:happy Sixteen years ago. That's June. From the roof.
}
-> DONE

=== clinic_labour_door ===
You don't go in. Through the little window you see a woman gripping the bed rail, and Nkechi's hand on her back, steady as a wall.
{ song_req == 2:
    Faintly, from a speaker inside, a woman's voice singing about a lantern. Sana is singing along, out of tune, crying.
- else:
    @phone "—DEV, IF YOU COME IN HERE WITH THAT FACE AGAIN—"
}
-> DONE

=== clinic_chairs ===
-> talk_dev

=== clinic_posters ===
{ shuffle:
- @sign AI-ASSISTED BIRTH? ASK YOUR MIDWIFE. (Someone has added in pen: "she'll laugh")
- @sign BREATHE IN FOR FOUR. OUT FOR SIX. YOU'RE DOING GREAT. (Someone has added: "Dev, this means you")
}
-> DONE
