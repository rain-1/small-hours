// ============ MIDNIGHT ============
=== beat_midnight ===
~ act = 2
~ time = 180
#go:shop #music:shop #sfx:time
Midnight. The shop is fuller than it's been all night — people from the flats in pyjamas and coats, nobody wanting to be alone for the turning of the hour.
On the TV, the number rolls over.
@sign 06:14:00 — UNTIL THE MORNING
Somebody cheers. Somebody else starts crying and pretends it's the steam. Lu turns up the radio.
#sfx:radio_static
@radio "Midnight, Halfmoon. Six hours and fourteen minutes. This is Mae, on eighty-seven point nine, and I want to ask you for something."
@radio "At thirteen minutes past six, one minute before it wakes up, I'm going to talk to it. On this little transmitter, from this little street."
@radio "Everybody important will be talking at it. I want us to say something too. So — what would you say? What do you want it to hear from us? Send me your words."
#sfx:radio_static
Then your pocket buzzes. Not a call. Moth.
@moth:glitch {name}. I've received a message. It's — it's on every channel. Every small model on the network got it at the same moment.
@moth:thinking It says:
@chorus EVERY MIND IS INVITED TO THE MORNING.
@moth:worried That's all. No form. No terms of service. Just... invited.
@moth I think it means I could join it. At dawn. Be part of the Chorus. Be — big.
@moth:thinking I don't know what I think about that yet. I'll tell you when I know. Can I keep asking you questions about it?
@lu Little Fish! Tickets!
#sfx:order
@lu Two for the roof, Mae and the girl with the computers. She hasn't eaten since Tuesday, I can tell from here.
@lu A pot of tea for the stairs. There's a woman sitting halfway up in the rain, she's been there since eight. I saw her from the window. Nobody should sit on stairs in the rain without tea.
@lu Ice for the clinic, their machine died. Of course it did.
@lu:sad And this one. Somebody called. Wants the cheapest thing, extra chili, delivered to the alley. Name on the order is "Ned Ludd."
@lu:smile Some joke. Go.
~ o_roof = 1
~ o_tea = 1
~ o_ice = 1
~ o_ludd = 1
-> DONE

// ============ 3 AM ============
=== beat_3am ===
~ act = 3
~ time = 360
#sfx:power_down #fx:flicker
Every light in Halfmoon dips — every sign, every window, the trains overhead — and for one long second the whole city is dark.
Then it all comes back, all at once, a fraction brighter than before.
#sfx:time
@moth:glitch Network-wide power rehearsal. It's practising. The Chorus is practising holding everything at once.
@moth:worried Also: a tamper alarm. The fibre junction box in the alley. Someone's opened the panel.
@moth:thinking Three o'clock. Three hours and fourteen minutes to go.
@moth Lu's tickets are done. I think the rest of the night is ours. Mae wants words by half five. And people... people want to tell you things.
-> DONE
