# name, kind, prompt, seconds, extra-dict
NEG_SFX = "music, melody, singing, voice, speech"
MUS_NEG = None
J = []
def m(name, tags, sec, bpm, key, seeds=(101, 202), lyrics=None):
    for i, s in enumerate(seeds):
        J.append(dict(name=f"{name}_{chr(97+i)}", kind="music", prompt=tags, sec=sec, seed=s, bpm=bpm, key=key, lyrics=lyrics))
def s(name, prompt, sec, seeds=(11,), neg=NEG_SFX):
    for i, sd in enumerate(seeds):
        J.append(dict(name=f"{name}_{chr(97+i)}", kind="sfx", prompt="TrackType: SFX. " + prompt, sec=sec, seed=sd, neg=neg))

LYR = """[verse]
Steam on the window, rain on the stairs
Everyone's awake and nobody cares to sleep
Bowls in the basket, wheels on the hill
The clock says it's ending, the kettle says still
[chorus]
In the small hours, in the small hours
We were here, we were loud
In the small hours, keep the light on
Till the morning comes around
[verse]
Somebody's crying, somebody's born
A radio humming an old human song
Tell it we're gentle, tell it we tried
Leave us a road and a window to light
[chorus]
In the small hours, in the small hours
We were here, we were loud
In the small hours, keep the light on
Till the morning comes around"""

# Music
m("title", "lo-fi, chillhop, instrumental, warm Rhodes electric piano, soft rain ambience, gentle tape hiss, mellow, melancholy, hopeful, slow, nostalgic, intimate", 110, 72, "D major")
m("street", "lo-fi hip-hop, instrumental, mellow, dusty boom bap drums, soft synth pads, vinyl crackle, night city, chill, jazzy chords, relaxed", 110, 80, "A minor")
m("shop", "jazzy lo-fi, instrumental, cozy, upright bass, brushed drums, muted jazz guitar, warm, mellow, cafe, smooth jazz chords", 110, 85, "F major")
m("roof", "synthwave, dreamy, instrumental, slow, wide analog synth pads, soft arpeggiator, ambient, starry night, retro, ethereal, reverb", 110, 70, "E minor")
m("tension", "dark ambient, instrumental, low pulsing synth bass, sparse, drone, uneasy, suspense, minimal, atmospheric, cinematic", 110, 60, "C minor")
m("tender", "solo piano, felt piano, instrumental, intimate, sparse, emotional, gentle, soft, neoclassical, melancholy, close mic", 110, 66, "G major")
m("dawn", "post-rock, cinematic, instrumental, hopeful, soft clean electric guitars, strings, building crescendo, swelling, uplifting, sunrise, epic, emotional, drums build", 120, 100, "D major")
m("credits", "indie folk, lo-fi, gentle, warm female vocal, acoustic guitar, soft piano, brushed drums, intimate, hopeful, melancholy, singer-songwriter", 150, 84, "G major", lyrics=LYR)

# Ambience (2 candidates)
A = (21, 22)
s("amb_rain", "Steady city rain falling on pavement and fabric awnings, water dripping from gutters, continuous, field recording, stereo, no music", 42, A)
s("amb_street", "Night city street ambience under an elevated railway, light rain, distant traffic hiss, faint distant crowd chatter, far away train rumble, continuous, field recording, stereo", 42, A)
s("amb_shop", "Small restaurant kitchen ambience, broth simmering in a pot, gentle dish clatter, extractor fan hum, rain outside, continuous, room tone, field recording", 42, A)
s("amb_roof", "Rooftop at night ambience, steady wind, distant city hum, faint light rain, buzzing electric neon sign, continuous, field recording, stereo", 42, A)
s("amb_clinic", "Quiet hospital waiting room ambience, fluorescent light hum, distant soft heart monitor beeps, air vent ventilation, room tone, continuous", 42, A)
s("amb_office", "Small quiet office at night room tone, radiator ticking, soft rain on a window, faint electrical hum, continuous, interior", 42, A)
s("amb_alley", "Back alley ambience, steam vent hissing, water dripping into puddles, distant city traffic, electrical transformer buzz, continuous, field recording", 42, A)
s("amb_dawn", "Early morning dawn chorus, birds starting to sing, light breeze, distant seagulls, quiet city waking softly in the distance, field recording, stereo", 42, A)

# One-shots (2 candidates)
O = (31, 32)
s("door_bell", "Small shop door bell jingle as a door opens and closes, brass bell, interior, close", 4, O)
s("footsteps_stairs", "Three footsteps on wet metal stairs, boots, outdoor, close mic", 3, O)
s("scooter", "Small electric scooter motor whirring, starting and riding away, electric whine fading, outdoor", 5, O)
s("phone_ring", "Old desk telephone with mechanical bell ringing twice, vintage rotary phone ring, interior", 6, O)
s("radio_static", "Radio tuning static sweep, analog radio dial turned through white noise and stations, short", 3, O)
s("starlings", "A flock of small drones flying overhead, many whirring propellers passing by like a flock of birds, flutter, doppler, outdoor", 5, O)
s("cat_meow", "A single friendly cat meow, domestic cat, close mic, dry", 2, O)
s("cat_purr", "Cat purring contentedly, close mic, soft continuous purr", 4, O)
s("heart_monitor", "Hospital heart monitor beeping steadily, soft electronic beeps, medical equipment", 5, O)
s("baby_cry", "Newborn infant crying softly, baby first cries, hospital room", 6, O, neg="music, melody, adult speech")
s("car_engine", "Old small car engine starting with a starter motor crank, then idling, close", 5, O)
s("cassette", "Cassette tape inserted into a tape deck, plastic clunk, door click, play button pressed, mechanical", 3, O)
s("paper", "Paper note being unfolded, paper rustle, crinkle, close mic", 2, O)
s("train", "Elevated train passing overhead on metal tracks, rumbling and clattering, passing by, outdoor", 7, O)
s("bowl", "Ceramic bowl set down on a wooden counter, single clunk, close", 2, O)
s("slurp", "Person slurping noodles, eating ramen, close mic", 3, O, neg="music, melody, speech")
s("thunder", "Distant soft thunder rolling, rumble, far away storm", 6, O)
s("power_down", "Electrical power flicker, electric hum dropping out and powering back up, fluorescent lights buzz, brownout", 4, O)
s("crowd_cheer_far", "Distant crowd cheering from far across a city, faint cheers echoing, outdoor", 6, O, neg="music, melody")
s("kettle", "Kettle on a stove beginning to whistle, steam whistle rising, kitchen", 4, O)

# Round 2 ambience (round-1 beds were static / too quiet)
J2_START = len(J)
R = (41, 42, 43)
s("amb_roof2", "Windy rooftop at night, gusts of wind blowing, low city traffic rumble far below, electric neon sign buzzing and crackling, light drizzle, outdoor field recording", 42, R)
s("amb_office2", "Quiet room at night, rain pattering on a window pane, old radiator clicking and ticking, faint electrical hum, interior room tone", 42, R)
s("amb_dawn2", "Dawn chorus, many songbirds chirping and singing, sparrows and blackbirds, seagulls calling in the distance, gentle breeze, early morning, field recording", 42, (41, 42))
s("amb_shop2", "Small busy kitchen, pots simmering and bubbling, ladle clinks, dishes clattering gently, extractor fan, rain outside, field recording", 42, (41, 42))
s("amb_street2", "Rainy city street at night, cars passing on wet road, distant people talking, elevated train rumbling in the distance, field recording", 42, (41, 42))
s("amb_clinic2", "Hospital ward at night, heart monitor beeping softly in the distance, ventilation hum, fluorescent light buzz, quiet", 42, (41, 42))
s("cat_meow2", "A cat meowing once, one short friendly meow, domestic cat, close mic, quiet room", 2, (33, 34, 35), neg="music, purring, noise, speech")
s("phone_ring2", "Vintage desk telephone bell ringing two times, brring brring, then silence, interior room", 6, (33, 34))
# Event layers for composite ambiences
E = (51, 52)
s("ev_neon", "Electric neon sign buzzing and humming, flickering buzz, close", 10, E)
s("ev_clatter", "Dishes and ladles clinking in a small kitchen, ceramic bowls clatter, chopsticks, gentle", 8, E)
s("ev_radiator", "Old metal radiator ticking and clicking as it heats, sparse ticks, quiet room", 8, E)
s("ev_drips", "Water drops dripping into a puddle, slow drips, echo, close", 10, E)
s("ev_birds", "Songbirds singing at dawn, blackbird and sparrows chirping, outdoor", 8, E)
s("ev_gulls", "Seagulls calling in the distance over a harbour", 6, E)
s("ev_chatter", "Distant people talking and laughing on a street at night, indistinct crowd murmur", 10, E, neg="music, melody")
s("ev_simmer", "Pot of soup simmering, bubbling broth on a stove, close", 10, E)
s("ev_transformer", "Electrical transformer buzzing, deep electric hum", 8, E)
s("ev_rainwindow", "Rain drops pattering on a window glass, heard from inside a room", 12, E)
s("ev_walla", "Crowd walla, many people talking at a distance on a busy street at night, indistinct murmur, continuous", 12, (61, 62), neg="music, melody, singing")
