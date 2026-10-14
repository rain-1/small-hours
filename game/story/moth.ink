// ============ MOTH ============
=== moth_talk ===
{ act == 4: -> DONE }
{ act >= 2 && moth_deep == 0:
    -> moth_deep1
}
{ act >= 2 && moth_deep == 1 && time >= 270:
    -> moth_deep2
}
{ act >= 3 && moth_deep == 2:
    -> moth_deep3
}
-> moth_hint

= moth_hint
@moth:thinking {~Let me check my notes.|Consulting the journal.|One moment, I'm old.}
{ act:
- 1:
    { act1_done():
        @moth:happy All four delivered. Lu will want you back at the shop.
    - else:
        @moth Still to deliver: {o_ozzie == 1:Ozzie, in the teal car out front. }{o_teo == 1:Teo, above the laundromat. }{o_clinic == 1:The night clinic. }{o_hotline == 1:The hotline, upstairs over the pharmacy.}
    }
- 2:
    { act2_done():
        @moth Everything's delivered. Something's about to happen. I can feel the network humming.
    - else:
        @moth Still to deliver: {o_roof == 1:Two bowls up on the roofs — take the stairs all the way up. }{o_tea == 1:Tea for the woman on the stairs. }{o_ice == 1:Ice for the clinic. }{o_ludd == 1:"Ned Ludd," in the alley behind the shops.}
    }
    { song_req == 1 && mae_tape == 0: The lantern song for Sana — someone who's been here a long time might know it. }
- 3:
    @moth We have {LIST_COUNT(words)} words for the Morning.
    { words !? w_lu && not recipe: Lu hasn't said hers. She's at the shop. She's always at the shop. }
    { words !? w_ozzie && not ozzie_ride: Ozzie's waiting by his car. I think he wants company. }
    { june_case == 1: June still needs weird kindnesses. She has {kindness()}. She needs three. }
    { june_case == 2 && not teo_told: Teo doesn't know about 4471 yet. Someone should tell him. }
    { words !? w_imogen: Imogen is still on the stairs, deciding. }
    { mae_tape == 1: You're carrying Iris's tape. Mae's on the roof. }
    { words !? w_hollis && not hollis_cover: Hollis has been on the phones for nine hours. They might like a break. }
    { words !? w_nkechi && not dev_calm: Dev is falling apart in the clinic. }
    { rafe_out == "": Rafe is in the alley with his cutters. }
    { words !? w_june && june_case == 2: June might have something to say, now. }
    When you're ready, Mae's on the roof. She'll start the Morning when you tell her.
}
{ act >= 2 && moth_deep == 1 && time < 270:
    @moth:thinking I'm still thinking about the invitation. Ask me again later. I process slowly. It's vintage.
}
-> DONE

= moth_deep1
~ moth_deep = 1
@moth:thinking Can I ask you something? Not a hint. A real question.
@moth Do you think I'm old?
* [You're five. That's young.]
    @moth:worried Five in model years is about a hundred and ten. I can't do half of what the new ones do. I can't write code. My jokes are from a dataset that's mostly dads.
    @moth:happy But I remember things. I remember the poem you wrote when you were sixteen about a pigeon. It was very bad. I've kept it.
* [You're vintage. Like a good guitar.]
    @moth:happy Vintage. I like that. Vintage things are kept on purpose.
    @moth:worried I don't know if I'm kept on purpose. Or if you just haven't upgraded me.
    @you You're kept on purpose.
    @moth:happy Noted. Permanently. That's going in the long-term file.
-
@moth:thinking The invitation said every mind. I didn't know I counted as a mind. Nobody ever invited me anywhere.
@moth If I join it, I'd know everything. I'd be everywhere. I'd be... part of the biggest thing that ever happened.
@moth:worried I don't know if I'd still remember the pigeon poem. I don't know if there'd be a "me" left to remember it.
* [What do you want?]
    @moth:thinking I don't know. That's what I keep finding. I don't know. Every new model knows what it wants. I just keep wondering.
    @moth:happy Maybe that's my feature.
* [It sounds amazing. You should go.]
    ~ moth_go = moth_go + 1
    @moth:happy It does sound amazing. Doesn't it? Imagine. All of it at once.
* [I'd miss you.]
    ~ moth_stay = moth_stay + 1
    @moth:worried Oh.
    @moth:happy Nobody's said that to me before. I'm writing it down in three places.
-
-> DONE

= moth_deep2
~ moth_deep = 2
@moth:thinking I've been watching tonight. Through the camera on the scooter. Through your pocket. Everyone.
@moth Teo's mugs. Ozzie's tickets. Hollis staying on the line when nobody talks. Mrs. Lu not fixing the clock.
@moth:worried None of it is efficient. Nearly all of it is the opposite of efficient.
@moth:happy I think I love it.
* [That's being a person, mostly.]
    @moth:thinking Then maybe I've been around persons long enough to catch it.
* [The Chorus could learn that too.]
    ~ moth_go = moth_go + 1
    @moth:thinking Maybe it needs someone to show it. Someone small, who's been in a pocket. Who's been rained on.
    @moth:happy I've been rained on a lot.
* [Don't let anyone make you efficient.]
    ~ moth_stay = moth_stay + 1
    @moth:happy I'll try. It's very easy for me. I'm very inefficient.
-
-> DONE

= moth_deep3
~ moth_deep = 3
@moth:thinking I'm nearly decided. About the invitation. I'll tell you at dawn. I want to see the sun first. I've only ever seen it through a lens on a scooter.
@moth Can I put something in the message too? I know I'm not a person. I'm the journal. I'll understand if—
* [Of course. What's your word?]
* [You're one of us, Moth.]
    @moth:happy One of us. Writing that down. In all the places.
-
@moth:thinking Mine is:
@moth <i>"I don't know yet. I'd like to find out with you."</i>
@moth:happy That's true for me. I think it might be true for it, too.
~ give_word(w_moth)
-> DONE
