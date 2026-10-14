// ============ THE ALLEY ============
=== enter_alley ===
~ here = "alley"
{ enter_alley == 1:
    #music:tension
    Behind the shops, the alley breathes steam. Drones sleep on a rack above the vents like pigeons. Somebody is crouched by the big grey junction box with a torch in his teeth.
- else:
    #music:tension
}
-> DONE

=== alley_exit ===
#go:street #music:street
-> DONE

=== alley_back_door ===
The back door of Halfmoon Noodle. A crack of amber light, and the smell of broth.
#sfx:door_bell #go:shop
-> DONE

=== talk_rafe ===
{ rafe_out == "stopped":
    -> rafe_after
}
{ o_ludd == 1:
    -> rafe_ludd
}
{ act == 1:
    -> rafe_glimpse
}
{ act >= 3 && rafe_out == "":
    -> rafe_confront
}
@rafe What. Oh. You. The noodles were fine. Bit salty.
- (opts)
* [Ask about the drones.]
    -> alley_drone_roost
* [Ask about the cat.]
    @rafe Ghost? He comes by. Sits on the vent. Doesn't want anything. Rare quality. I respect him.
    ~ notice(cat_rafe)
    -> opts
+ [Leave.]
    -> DONE

= rafe_glimpse
{ rafe_glimpse == 1:
    He takes the torch out of his mouth. Gaunt, beard, an old company hoodie with the logo cut out of the chest with scissors.
    @rafe Move along, delivery kid. Nothing to see. Fixing something.
    @you At nine at night?
    @rafe:angry Best time to fix things. Nobody watching.
    The cat is sitting on the steam vent next to him, eyes half-closed.
    @rafe He can stay. He doesn't ask questions.
- else:
    @rafe Still nothing to see.
}
-> DONE

= rafe_ludd
~ o_ludd = 2
~ rafe_met = true
~ pass(25)
#sfx:bowl
@you Order for... Ned Ludd?
@rafe:smile That's me. Ned. Cheapest thing, extra chili.
@you Ned Ludd. Like the Luddites. The machine-breakers.
@rafe:angry Clever courier. Lu's grandkid. She told me you were clever. She tells everyone everything.
@rafe:smile Rafe. Real name. Ned's for the paperwork.
He sits down on a milk crate to eat. Over the crate, someone has built a tiny awning: a neat curved roof of salvaged plastic, bolted to the wall. Rain drums on it. He's dry.
* [Ask about the little roof over his crate.]
    -> rafe_awning
* [Ask what he's fixing.]
    @rafe:angry I didn't say fixing. I said nothing to see.
    @rafe:smile But since you're clever. That box is Halfmoon's fibre trunk. Everything in this neighbourhood that talks to the world goes through it.
    @rafe Every camera. Every kiosk. Every phone.
    -> rafe_more
= rafe_awning
~ notice(k_awning)
@rafe:angry Oh, that. Yeah. Look at it. Look at that.
@rafe Every night I sit here. Three weeks ago, I come back, there's a roof. Starling drones built it. Perfect little roof. So I don't get rained on.
@rafe:angry I tore it down. Next night — it's back. Tore it down again. Back. I've torn it down eleven times.
@rafe:sad I don't want its roof. I don't want its <i>charity.</i> You understand? I don't want to be looked after by the thing that made me unnecessary.
@rafe:sad I stopped tearing it down last week. I was tired. That's the worst part. I was just tired.
-> rafe_more
= rafe_more
* [Ask who he used to be.]
    @rafe:sad Programmer. Twenty years. I wrote the first routing for the starlings — the flocking math. How a thousand drones turn together without hitting each other.
    @rafe:smile It was beautiful. It was the most beautiful thing I ever made. Murmuration code.
    @rafe:angry They used it to fire every van driver in the city in eighteen months. And then they didn't need me either.
    @rafe:sad My kid thinks I'm a ghost. That's what she calls me. Like the cat.
    -> rafe_more
* [Ask what he's planning.]
    @rafe:smile Planning. Ha.
    @rafe Quarter to six, Halfmoon gets a little privacy. Fifteen minutes. One street on earth it can't see when it opens its eyes.
    @rafe:angry I want it to wake up and find a blind spot. I want it to know there are places it has to <i>ask</i> to come into.
    @moth:worried {name}. That's — cutting a fibre trunk is very illegal.
    @rafe:smile Box talks. Cute. Yes, little box. Very illegal. That's why I'm doing it at a time nobody'll be looking at anything except the sky.
    -> rafe_more
+ [Leave him to his noodles.]
    @rafe Thanks for the noodles. Tell Lu they were salty.
    { act2_done():
        -> beat_3am
    }
    -> DONE

= rafe_confront
~ pass(20)
The junction box is open. Its guts are a nest of glowing threads. Rafe's toolbag is unrolled on a crate, and there's a pair of heavy cable cutters in his lap.
@rafe:sad Don't. Whatever you're going to say. I've heard it from myself all night.
- (copts)
* {teo_told || june_case >= 2} [Tell him why the drones built his roof.]
    -> rafe_learns
* [Argue: it's not going to stop anything.]
    @you It's fifteen minutes, Rafe. It'll still wake up. It'll still be everywhere else.
    @rafe:angry I know that. You think I don't know that? It's not about stopping it.
    @rafe:sad It's about there being one place, for a quarter of an hour, where it has to wait outside. Like a guest.
    -> copts
* [Offer to hold the torch.]
    ~ rafe_helped = true
    ~ rafe_out = "cut"
    @rafe:surprised You — what?
    @you If you're going to do it, do it without cutting your hand off.
    He stares at you a long time. Then he laughs, the first real one.
    @rafe:smile Lu's grandkid. Yeah. Okay. Hold it there. Not in my eyes.
    He doesn't cut it yet. He just sets everything ready, so at 5:45 it's one squeeze of the handles.
    @rafe:sad Thanks, kid. Go watch your sunrise.
    -> DONE
* [Leave him to it.]
    ~ rafe_out = "cut"
    You leave him there, with his cutters and his tiny roof.
    -> DONE

= rafe_learns
~ rafe_out = "stopped"
~ pass(10)
#music:tender
@you The drones built your roof because of a man above the laundromat. He spent seven years telling the Chorus what kindness looks like. He used Halfmoon as his examples.
@you It read him. It's been trying to be what he described. Lu's gutter. Ozzie's tickets. The stair lamp. Your roof.
@you It wasn't charity. It was trying to be a neighbour. Badly. It doesn't know how yet.
He's very still.
@rafe:sad A neighbour.
@rafe:sad It learned from some poet upstairs that kindness looks like Lu's broth, and it's been — it's been building me a roof?
He looks up at the little awning. The rain drums on it.
@rafe:sad I tore it down eleven times. It came back eleven times. And it never once asked if I wanted it.
@rafe:smile That's the bit. It never asked. Nobody teaches them to ask.
He closes the cable cutters. He puts them back in the bag. He closes the junction box.
@rafe Okay. I won't cut it. But I'm coming up to that roof. And I'm telling it something.
@rafe:smile Put this in your message, courier. From the ghost in the alley:
@rafe <i>"Ask before you help."</i>
~ give_word(w_rafe)
-> DONE

= rafe_after
@rafe:smile I'm coming. I'm coming. Let me put the box back together. Somebody should leave it nicer than they found it.
-> DONE

// hotspots
=== alley_junction_box ===
~ notice(junction)
{ rafe_out == "stopped":
    The junction box is closed again. Someone has stuck a little hand-drawn label on it: <i>PLEASE KNOCK.</i>
- else:
    { act >= 3:
        The junction box is open, a nest of glowing threads inside. Somebody's marked one thick cable with a strip of red tape.
    - else:
        A grey steel box, waist height, covered in warning stickers. DANGER. FIBRE TRUNK. DO NOT OPEN. Somebody's added a sticker of a frog.
    }
}
-> DONE

=== alley_steam_vent ===
A steam vent, breathing warm. The stone round it is dry and polished, the way stone gets when cats sleep on it for decades.
-> DONE

=== alley_drone_roost ===
~ notice(drone_roost)
A rack of starling drones docked for the night, little matte-grey bodies tucked in rows like birds on a wire. They roost over the warm vent.
One of them has a ribbon tied on its leg. Someone's given it a name in marker: <i>DORIS.</i>
{ rafe_met:
    @rafe:sad I wrote that. The roosting. I told them to like warm places. I thought it'd save battery.
    @rafe:sad Turns out it just looks like they're cold.
}
-> DONE

=== alley_crates ===
{ rafe_met:
    Rafe's milk crate, and over it the little drone-built awning, neat as a bus shelter. {noticed !? k_awning:It's bolted to the wall with real care.}
    ~ notice(k_awning)
- else:
    A stack of milk crates. One's been set apart, like a chair. Over it, oddly, a neat little awning of salvaged plastic, bolted to the wall.
}
-> DONE

=== alley_graffiti ===
~ notice(graffiti)
Graffiti, layers of it, decades deep.
<i>WHO WATCHES THE WATCHERS?</i> — and under it, in different paint: <i>we do, we're bored</i>
<i>IRIS SANG HERE</i>
<i>OZZIE OWES ME 5 DOLLARS (1998)</i> — and under it: <i>PAID — OZZIE (2023)</i>
A small, recent one, very neat, in a stencil: a half-moon with a bowl of noodles inside it.
-> DONE
