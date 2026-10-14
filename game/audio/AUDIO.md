# Small Hours: audio assets

All files are MP3, 44.1 kHz stereo. Music is 160 kbps, SFX and UI are 128 kbps. Loudness is EBU R128 integrated (LUFS) and peak is decoded sample peak (dBFS), both measured on the final files. Generated 2026-10-14 through local ComfyUI with `tools/comfy_audio.py` (music: ACE-Step 1.5 turbo; SFX: Stable Audio 3 medium, SA3). Every SA3 prompt starts with `TrackType: SFX.` and uses the negative prompt `music, melody, singing, voice, speech` unless noted.

**Loops**: every music loop and ambience has its last 2 s equal-power-crossfaded into its first 2 s, so the file loops seamlessly when played back to back (set `loop = true`; no extra crossfade needed). Music loop lengths are snapped to an onset-envelope autocorrelation peak so the seam lands on a matching beat phase. Seams were checked by rendering two copies back to back.

## music/ (target -18 LUFS; credits -16)

| file | dur | LUFS | peak | source (model, seed, prompt) | notes |
|---|---|---|---|---|---|
| `title.mp3` | 94.6s | -18.3 | -4.8 | ACE-Step 1.5 turbo, seed 202, 72 bpm, D major: "lo-fi, chillhop, instrumental, warm Rhodes electric piano, soft rain ambience, gentle tape hiss, mellow, melancholy, hopeful, slow, nostalgic, intimate" | Loop-ready (2s tail-to-head crossfade, beat-snapped). Keeps its 13s soft Rhodes intro, and has a breakdown at about 55s. Picked over title_a, which has a 2s dropout to -36 dB at 78s. |
| `street.mp3` | 84.0s | -18.4 | -3.8 | ACE-Step 1.5 turbo, seed 202, 80 bpm, A minor: "lo-fi hip-hop, instrumental, mellow, dusty boom bap drums, soft synth pads, vinyl crackle, night city, chill, jazzy chords, relaxed" | Loop. Cut 5.5-96s to skip the intro and outro. Seam rhythm checked on the spectrogram (envelope correlation 0.90). Picked over street_a, which is more repetitive and has less crackle. |
| `shop.mp3` | 93.2s | -18.4 | -3.9 | ACE-Step 1.5 turbo, seed 101, 85 bpm, F major: "jazzy lo-fi, instrumental, cozy, upright bass, brushed drums, muted jazz guitar, warm, mellow, cafe, smooth jazz chords" | Loop. The most even of the two. shop_b has a sparse 20s breakdown. |
| `roof.mp3` | 75.5s | -18.5 | -5.8 | ACE-Step 1.5 turbo, seed 101, 70 bpm, E minor: "synthwave, dreamy, instrumental, slow, wide analog synth pads, soft arpeggiator, ambient, starry night, retro, ethereal, reverb" | Loop, 75s (shorter than the 90s target). Skips the 13s pad intro. Picked over roof_b, which has a long 13s quiet section in the middle. |
| `tension.mp3` | 96.0s | -18.3 | -2.3 | ACE-Step 1.5 turbo, seed 101, 60 bpm, C minor: "dark ambient, instrumental, low pulsing synth bass, sparse, drone, uneasy, suspense, minimal, atmospheric, cinematic" | Loop. Low pulse with sparse high accents. tension_b is flatter. |
| `tender.mp3` | 89.0s | -18.4 | -2.5 | ACE-Step 1.5 turbo, seed 202, 66 bpm, G major: "solo piano, felt piano, instrumental, intimate, sparse, emotional, gentle, soft, neoclassical, melancholy, close mic" | Loop. Solo piano with a sparse passage at about 40-50s (sub-second near-silences between phrases). tender_a was rejected: almost inaudible for 48s, then loud stabs. |
| `dawn.mp3` | 108.0s | -18.5 | -4.1 | ACE-Step 1.5 turbo, seed 202, 100 bpm, D major: "post-rock, cinematic, instrumental, hopeful, soft clean electric guitars, strings, building crescendo, swelling, uplifting, sunrise, epic, emotional, drums build" | Not looped. Quiet strummed build for about 73s, then a full crescendo to the end, with a natural decay and a 4s fade. 108s long. dawn_a was rejected: it has no build (loud-quiet-loud blocks). |
| `credits.mp3` | 145.8s | -16.4 | -3.8 | ACE-Step 1.5 turbo, seed 202, 84 bpm, G major: "indie folk, lo-fi, gentle, warm female vocal, acoustic guitar, soft piano, brushed drums, intimate, hopeful, melancholy, singer-songwriter" | Not looped, -16 LUFS. Female vocal confirmed on the spectrogram (gliding harmonic stacks, f0 about 250-350 Hz). Lyrics passed verbatim. Exact word fidelity can't be checked without listening. |

Credits lyrics: as given in the brief ([verse]/[chorus] x2), 84 bpm, G major. Prompt: "indie folk, lo-fi, gentle, warm female vocal, acoustic guitar, soft piano, brushed drums, intimate, hopeful, melancholy, singer-songwriter".

## sfx/ ambience loops (target -26 LUFS)

A single 42 s SA3 render came out as an almost stationary noise bed with few events, and several were near-silent (office_b at -69 LUFS, roof_b at -52). So each ambience is a **composite**: SA3 beds, plus scattered SA3 event layers (random times, levels and pans), plus two synthesized layers where generation wasn't reliable: a loop-safe 60/120 Hz mains hum for the alley and a soft 880 Hz monitor beep for the clinic. Layers with anti-phase stereo were polarity-corrected so everything is mono-compatible.

| file | dur | LUFS | peak | layers (raw candidate names, see log) |
|---|---|---|---|---|
| `amb_rain.mp3` | 38.0s | -25.9 | -13.4 | beds: amb_rain_a (main, broadband: spectral flatness 0.74), amb_rain_b (low-passed); events: ev_drips_a |
| `amb_street.mp3` | 40.0s | -26.3 | -12.2 | beds: amb_street_b (rain and traffic hiss), amb_street2_a (low-passed traffic rumble), amb_rain_a; events: ev_walla_a/b (distant chatter, left channel only, low-passed), train_b (low-passed far train rumble at about 16s) |
| `amb_shop.mp3` | 40.0s | -26.4 | -2.3 | beds: amb_shop_b (extractor hum), ev_simmer_b (bubbling), amb_rain_a (low-passed, outside); events: ev_clatter_a/b (dish clinks), ev_simmer_a |
| `amb_roof.mp3` | 40.0s | -26.7 | -12.8 | beds: amb_roof2_b (wind), amb_rain_a (high-passed drizzle), amb_street2_a (low-passed city hum), ev_neon_b (buzz); events: amb_roof2_a (gusts), ev_neon_a (flickering buzz) |
| `amb_clinic.mp3` | 40.0s | -26.3 | -13.9 | beds: amb_clinic_a (fluorescent/vent hum), amb_clinic2_b; events: synthesized soft monitor beep every 1.0s, panned slightly right, about 10 dB under the bed |
| `amb_office.mp3` | 40.0s | -26.2 | -7.5 | beds: amb_office2_a (electrical hum), ev_rainwindow_a/b (4.5-9.5s sections); events: ev_radiator_a/b (ticks) |
| `amb_alley.mp3` | 40.0s | -27.1 | -6.3 | beds: amb_alley_a (steam hiss), synthesized mains hum (transformer), amb_street2_a (low-passed distant city); events: ev_drips_a with echo |
| `amb_dawn.mp3` | 40.0s | -26.4 | -11.8 | beds: amb_dawn_b from 6s (sparse chirps), amb_roof2_b (band-passed breeze); events: ev_birds_a/b (high-passed songbirds), ev_gulls_a/b (low-passed, distant) |

## sfx/ one-shots (peak-normalized to about -3 dBFS, trimmed, 4 ms fade-in, short fade-out)

| file | dur | LUFS | peak | source | notes |
|---|---|---|---|---|---|
| `door_bell.mp3` | 2.5s | -13.2 | -3.6 | SA3, seed 31, 4s: "Small shop door bell jingle as a door opens and closes, brass bell, interior, close" | Bell harmonics plus door clunk transients |
| `footsteps_stairs.mp3` | 1.7s | -19.8 | -3.6 | SA3, seed 31, 3s: "Three footsteps on wet metal stairs, boots, outdoor, close mic" | 4 distinct steps in 1.7s |
| `scooter.mp3` | 3.8s | -14.0 | -3.3 | SA3, seed 31, 5s: "Small electric scooter motor whirring, starting and riding away, electric whine fading, outdoor" | Whir with a falling pitch line as it rides off |
| `phone_ring.mp3` | 5.5s | -11.8 | -3.2 | SA3, seed 33, 6s: "Vintage desk telephone bell ringing two times, brring brring, then silence, interior room" | Exactly two rings with decays (round-1 candidates either truncated the second ring or rang irregularly) |
| `radio_static.mp3` | 2.0s | -14.6 | -3.2 | SA3, seed 31, 3s: "Radio tuning static sweep, analog radio dial turned through white noise and stations, short" | Two-stage noise sweep (b was flat white noise) |
| `starlings.mp3` | 3.5s | -10.0 | -3.1 | SA3, seed 32, 5s: "A flock of small drones flying overhead, many whirring propellers passing by like a flock of birds, flutter, doppler, outdoor" | Rise-and-fall pass-over envelope |
| `cat_meow.mp3` | 1.1s | -11.2 | -3.4 | SA3, seed 33, 2s: "A cat meowing once, one short friendly meow, domestic cat, close mic, quiet room" | 0.8s meow, harmonic stack with a pitch contour. Round-1 meows had a steady ~600 Hz artifact tone, so they were rejected |
| `cat_purr.mp3` | 2.7s | -18.7 | -3.3 | SA3, seed 31, 4s: "Cat purring contentedly, close mic, soft continuous purr" | Low, amplitude-modulated purr cycles |
| `heart_monitor.mp3` | 4.2s | -16.7 | -3.4 | SA3, seed 32, 5s: "Hospital heart monitor beeping steadily, soft electronic beeps, medical equipment" | Clean periodic beeps at about 120 bpm (a had a continuous flatline-like tone underneath) |
| `baby_cry.mp3` | 5.2s | -15.6 | -3.3 | SA3, seed 32, 6s: "Newborn infant crying softly, baby first cries, hospital room" | Arching harmonic cry contours (f0 about 400-500 Hz) with a natural end. Negative prompt: `music, melody, adult speech` |
| `car_engine.mp3` | 4.5s | -19.0 | -4.1 | SA3, seed 32, 5s: "Old small car engine starting with a starter motor crank, then idling, close" | Dense crank-like section, then sparser idle |
| `cassette.mp3` | 1.8s | -25.6 | -2.9 | SA3, seed 31, 3s: "Cassette tape inserted into a tape deck, plastic clunk, door click, play button pressed, mechanical" | 4 separated mechanical clicks |
| `paper.mp3` | 1.9s | -16.5 | -3.7 | SA3, seed 31, 2s: "Paper note being unfolded, paper rustle, crinkle, close mic" | Crinkle and rustle |
| `train.mp3` | 5.0s | -14.4 | -3.5 | SA3, seed 31, 7s: "Elevated train passing overhead on metal tracks, rumbling and clattering, passing by, outdoor" | Pass-by swell with wheel squeal |
| `bowl.mp3` | 1.0s | -17.0 | -3.0 | SA3, seed 32, 2s: "Ceramic bowl set down on a wooden counter, single clunk, close" | Single clunk with a short settle |
| `slurp.mp3` | 1.9s | -11.9 | -3.0 | SA3, seed 31, 3s: "Person slurping noodles, eating ramen, close mic" | Noisy modulated slurps. Negative prompt: `music, melody, speech` |
| `thunder.mp3` | 4.8s | -26.3 | -3.5 | SA3, seed 32, 6s: "Distant soft thunder rolling, rumble, far away storm" | The softer, more distant of the two (a had a close crack) |
| `power_down.mp3` | 2.9s | -18.9 | -3.5 | SA3, seed 32, 4s: "Electrical power flicker, electric hum dropping out and powering back up, fluorescent lights buzz, brownout" | Hum dips, then returns |
| `crowd_cheer_far.mp3` | 5.5s | -15.3 | -3.3 | SA3, seed 32, 6s: "Distant crowd cheering from far across a city, faint cheers echoing, outdoor" | Broadband distant swell (a had a horn-like tonal line). Negative prompt: `music, melody`. Polarity-corrected |
| `kettle.mp3` | 2.0s | -13.7 | -4.2 | SA3, seed 31, 4s: "Kettle on a stove beginning to whistle, steam whistle rising, kitchen" | Whistle tones emerging |

## ui/ (synthesized in numpy: sine/triangle, gentle envelopes, low-passed echo taps)

| file | dur | peak | design |
|---|---|---|---|
| `blip.mp3` | 0.08s | -14.4 | 30 ms 1200 Hz triangle, low-passed, 12 ms decay |
| `blip_low.mp3` | 0.08s | -14.4 | 30 ms 820 Hz triangle |
| `click.mp3` | 0.29s | -12.4 | 660 Hz + 1320 Hz soft pluck, single short echo |
| `hover.mp3` | 0.05s | -24.4 | 25 ms 2 kHz tick at -24 dBFS |
| `discover.mp3` | 1.83s | -9.4 | Rising D5-F#5-A5 bell chime, 110 ms apart, echo tail |
| `word.mp3` | 1.93s | -9.4 | Warm two-note bell G4 to D5 |
| `order.mp3` | 1.75s | -8.4 | Desk/ticket bell at 1568 Hz with inharmonic partials |
| `journal.mp3` | 1.65s | -12.4 | Filtered-noise page swish plus a soft C6 chime |
| `time.mp3` | 2.85s | -10.4 | Two low bells, C4 then G3, low-passed, long echo |

UI clips are too short for a meaningful integrated LUFS. They sit at -9 to -24 dBFS peak so they stay quiet under music.

## Prompt and seed log (all raw candidates)

`name: seed | prompt` (music lines also give bpm and key). Raw files aren't shipped; regenerate with `tools/comfy_audio.py` using the same seed.

```
amb_rain_a: 21 | 42s | Steady city rain falling on pavement and fabric awnings, water dripping from gutters, continuous, field recording, stereo, no music
title_a: 101 | 72bpm D major | lo-fi, chillhop, instrumental, warm Rhodes electric piano, soft rain ambience, gentle tape hiss, mellow, melancholy, hopeful, slow, nostalgic, intimate
title_b: 202 | 72bpm D major | lo-fi, chillhop, instrumental, warm Rhodes electric piano, soft rain ambience, gentle tape hiss, mellow, melancholy, hopeful, slow, nostalgic, intimate
street_a: 101 | 80bpm A minor | lo-fi hip-hop, instrumental, mellow, dusty boom bap drums, soft synth pads, vinyl crackle, night city, chill, jazzy chords, relaxed
street_b: 202 | 80bpm A minor | lo-fi hip-hop, instrumental, mellow, dusty boom bap drums, soft synth pads, vinyl crackle, night city, chill, jazzy chords, relaxed
shop_a: 101 | 85bpm F major | jazzy lo-fi, instrumental, cozy, upright bass, brushed drums, muted jazz guitar, warm, mellow, cafe, smooth jazz chords
shop_b: 202 | 85bpm F major | jazzy lo-fi, instrumental, cozy, upright bass, brushed drums, muted jazz guitar, warm, mellow, cafe, smooth jazz chords
roof_a: 101 | 70bpm E minor | synthwave, dreamy, instrumental, slow, wide analog synth pads, soft arpeggiator, ambient, starry night, retro, ethereal, reverb
roof_b: 202 | 70bpm E minor | synthwave, dreamy, instrumental, slow, wide analog synth pads, soft arpeggiator, ambient, starry night, retro, ethereal, reverb
tension_a: 101 | 60bpm C minor | dark ambient, instrumental, low pulsing synth bass, sparse, drone, uneasy, suspense, minimal, atmospheric, cinematic
tension_b: 202 | 60bpm C minor | dark ambient, instrumental, low pulsing synth bass, sparse, drone, uneasy, suspense, minimal, atmospheric, cinematic
tender_a: 101 | 66bpm G major | solo piano, felt piano, instrumental, intimate, sparse, emotional, gentle, soft, neoclassical, melancholy, close mic
tender_b: 202 | 66bpm G major | solo piano, felt piano, instrumental, intimate, sparse, emotional, gentle, soft, neoclassical, melancholy, close mic
dawn_a: 101 | 100bpm D major | post-rock, cinematic, instrumental, hopeful, soft clean electric guitars, strings, building crescendo, swelling, uplifting, sunrise, epic, emotional, drums build
dawn_b: 202 | 100bpm D major | post-rock, cinematic, instrumental, hopeful, soft clean electric guitars, strings, building crescendo, swelling, uplifting, sunrise, epic, emotional, drums build
credits_a: 101 | 84bpm G major | lyrics=credits lyrics | indie folk, lo-fi, gentle, warm female vocal, acoustic guitar, soft piano, brushed drums, intimate, hopeful, melancholy, singer-songwriter
credits_b: 202 | 84bpm G major | lyrics=credits lyrics | indie folk, lo-fi, gentle, warm female vocal, acoustic guitar, soft piano, brushed drums, intimate, hopeful, melancholy, singer-songwriter
amb_rain_b: 22 | 42s | Steady city rain falling on pavement and fabric awnings, water dripping from gutters, continuous, field recording, stereo, no music
amb_street_a: 21 | 42s | Night city street ambience under an elevated railway, light rain, distant traffic hiss, faint distant crowd chatter, far away train rumble, continuous, field recording, stereo
amb_street_b: 22 | 42s | Night city street ambience under an elevated railway, light rain, distant traffic hiss, faint distant crowd chatter, far away train rumble, continuous, field recording, stereo
amb_shop_a: 21 | 42s | Small restaurant kitchen ambience, broth simmering in a pot, gentle dish clatter, extractor fan hum, rain outside, continuous, room tone, field recording
amb_shop_b: 22 | 42s | Small restaurant kitchen ambience, broth simmering in a pot, gentle dish clatter, extractor fan hum, rain outside, continuous, room tone, field recording
amb_roof_a: 21 | 42s | Rooftop at night ambience, steady wind, distant city hum, faint light rain, buzzing electric neon sign, continuous, field recording, stereo
amb_roof_b: 22 | 42s | Rooftop at night ambience, steady wind, distant city hum, faint light rain, buzzing electric neon sign, continuous, field recording, stereo
amb_clinic_a: 21 | 42s | Quiet hospital waiting room ambience, fluorescent light hum, distant soft heart monitor beeps, air vent ventilation, room tone, continuous
amb_clinic_b: 22 | 42s | Quiet hospital waiting room ambience, fluorescent light hum, distant soft heart monitor beeps, air vent ventilation, room tone, continuous
amb_office_a: 21 | 42s | Small quiet office at night room tone, radiator ticking, soft rain on a window, faint electrical hum, continuous, interior
amb_office_b: 22 | 42s | Small quiet office at night room tone, radiator ticking, soft rain on a window, faint electrical hum, continuous, interior
amb_alley_a: 21 | 42s | Back alley ambience, steam vent hissing, water dripping into puddles, distant city traffic, electrical transformer buzz, continuous, field recording
amb_alley_b: 22 | 42s | Back alley ambience, steam vent hissing, water dripping into puddles, distant city traffic, electrical transformer buzz, continuous, field recording
amb_dawn_a: 21 | 42s | Early morning dawn chorus, birds starting to sing, light breeze, distant seagulls, quiet city waking softly in the distance, field recording, stereo
amb_dawn_b: 22 | 42s | Early morning dawn chorus, birds starting to sing, light breeze, distant seagulls, quiet city waking softly in the distance, field recording, stereo
door_bell_a: 31 | 4s | Small shop door bell jingle as a door opens and closes, brass bell, interior, close
door_bell_b: 32 | 4s | Small shop door bell jingle as a door opens and closes, brass bell, interior, close
footsteps_stairs_a: 31 | 3s | Three footsteps on wet metal stairs, boots, outdoor, close mic
footsteps_stairs_b: 32 | 3s | Three footsteps on wet metal stairs, boots, outdoor, close mic
scooter_a: 31 | 5s | Small electric scooter motor whirring, starting and riding away, electric whine fading, outdoor
scooter_b: 32 | 5s | Small electric scooter motor whirring, starting and riding away, electric whine fading, outdoor
phone_ring_a: 31 | 6s | Old desk telephone with mechanical bell ringing twice, vintage rotary phone ring, interior
phone_ring_b: 32 | 6s | Old desk telephone with mechanical bell ringing twice, vintage rotary phone ring, interior
radio_static_a: 31 | 3s | Radio tuning static sweep, analog radio dial turned through white noise and stations, short
radio_static_b: 32 | 3s | Radio tuning static sweep, analog radio dial turned through white noise and stations, short
starlings_a: 31 | 5s | A flock of small drones flying overhead, many whirring propellers passing by like a flock of birds, flutter, doppler, outdoor
starlings_b: 32 | 5s | A flock of small drones flying overhead, many whirring propellers passing by like a flock of birds, flutter, doppler, outdoor
cat_meow_a: 31 | 2s | A single friendly cat meow, domestic cat, close mic, dry
cat_meow_b: 32 | 2s | A single friendly cat meow, domestic cat, close mic, dry
cat_purr_a: 31 | 4s | Cat purring contentedly, close mic, soft continuous purr
cat_purr_b: 32 | 4s | Cat purring contentedly, close mic, soft continuous purr
heart_monitor_a: 31 | 5s | Hospital heart monitor beeping steadily, soft electronic beeps, medical equipment
heart_monitor_b: 32 | 5s | Hospital heart monitor beeping steadily, soft electronic beeps, medical equipment
baby_cry_a: 31 | 6s | neg="music, melody, adult speech" | Newborn infant crying softly, baby first cries, hospital room
baby_cry_b: 32 | 6s | neg="music, melody, adult speech" | Newborn infant crying softly, baby first cries, hospital room
car_engine_a: 31 | 5s | Old small car engine starting with a starter motor crank, then idling, close
car_engine_b: 32 | 5s | Old small car engine starting with a starter motor crank, then idling, close
cassette_a: 31 | 3s | Cassette tape inserted into a tape deck, plastic clunk, door click, play button pressed, mechanical
cassette_b: 32 | 3s | Cassette tape inserted into a tape deck, plastic clunk, door click, play button pressed, mechanical
paper_a: 31 | 2s | Paper note being unfolded, paper rustle, crinkle, close mic
paper_b: 32 | 2s | Paper note being unfolded, paper rustle, crinkle, close mic
train_a: 31 | 7s | Elevated train passing overhead on metal tracks, rumbling and clattering, passing by, outdoor
train_b: 32 | 7s | Elevated train passing overhead on metal tracks, rumbling and clattering, passing by, outdoor
bowl_a: 31 | 2s | Ceramic bowl set down on a wooden counter, single clunk, close
bowl_b: 32 | 2s | Ceramic bowl set down on a wooden counter, single clunk, close
slurp_a: 31 | 3s | neg="music, melody, speech" | Person slurping noodles, eating ramen, close mic
slurp_b: 32 | 3s | neg="music, melody, speech" | Person slurping noodles, eating ramen, close mic
thunder_a: 31 | 6s | Distant soft thunder rolling, rumble, far away storm
thunder_b: 32 | 6s | Distant soft thunder rolling, rumble, far away storm
power_down_a: 31 | 4s | Electrical power flicker, electric hum dropping out and powering back up, fluorescent lights buzz, brownout
power_down_b: 32 | 4s | Electrical power flicker, electric hum dropping out and powering back up, fluorescent lights buzz, brownout
crowd_cheer_far_a: 31 | 6s | neg="music, melody" | Distant crowd cheering from far across a city, faint cheers echoing, outdoor
crowd_cheer_far_b: 32 | 6s | neg="music, melody" | Distant crowd cheering from far across a city, faint cheers echoing, outdoor
kettle_a: 31 | 4s | Kettle on a stove beginning to whistle, steam whistle rising, kitchen
kettle_b: 32 | 4s | Kettle on a stove beginning to whistle, steam whistle rising, kitchen
amb_roof2_a: 41 | 42s | Windy rooftop at night, gusts of wind blowing, low city traffic rumble far below, electric neon sign buzzing and crackling, light drizzle, outdoor field recording
amb_roof2_b: 42 | 42s | Windy rooftop at night, gusts of wind blowing, low city traffic rumble far below, electric neon sign buzzing and crackling, light drizzle, outdoor field recording
amb_roof2_c: 43 | 42s | Windy rooftop at night, gusts of wind blowing, low city traffic rumble far below, electric neon sign buzzing and crackling, light drizzle, outdoor field recording
amb_office2_a: 41 | 42s | Quiet room at night, rain pattering on a window pane, old radiator clicking and ticking, faint electrical hum, interior room tone
amb_office2_b: 42 | 42s | Quiet room at night, rain pattering on a window pane, old radiator clicking and ticking, faint electrical hum, interior room tone
amb_office2_c: 43 | 42s | Quiet room at night, rain pattering on a window pane, old radiator clicking and ticking, faint electrical hum, interior room tone
amb_dawn2_a: 41 | 42s | Dawn chorus, many songbirds chirping and singing, sparrows and blackbirds, seagulls calling in the distance, gentle breeze, early morning, field recording
amb_dawn2_b: 42 | 42s | Dawn chorus, many songbirds chirping and singing, sparrows and blackbirds, seagulls calling in the distance, gentle breeze, early morning, field recording
amb_shop2_a: 41 | 42s | Small busy kitchen, pots simmering and bubbling, ladle clinks, dishes clattering gently, extractor fan, rain outside, field recording
amb_shop2_b: 42 | 42s | Small busy kitchen, pots simmering and bubbling, ladle clinks, dishes clattering gently, extractor fan, rain outside, field recording
amb_street2_a: 41 | 42s | Rainy city street at night, cars passing on wet road, distant people talking, elevated train rumbling in the distance, field recording
amb_street2_b: 42 | 42s | Rainy city street at night, cars passing on wet road, distant people talking, elevated train rumbling in the distance, field recording
amb_clinic2_a: 41 | 42s | Hospital ward at night, heart monitor beeping softly in the distance, ventilation hum, fluorescent light buzz, quiet
amb_clinic2_b: 42 | 42s | Hospital ward at night, heart monitor beeping softly in the distance, ventilation hum, fluorescent light buzz, quiet
cat_meow2_a: 33 | 2s | neg="music, purring, noise, speech" | A cat meowing once, one short friendly meow, domestic cat, close mic, quiet room
cat_meow2_b: 34 | 2s | neg="music, purring, noise, speech" | A cat meowing once, one short friendly meow, domestic cat, close mic, quiet room
cat_meow2_c: 35 | 2s | neg="music, purring, noise, speech" | A cat meowing once, one short friendly meow, domestic cat, close mic, quiet room
phone_ring2_a: 33 | 6s | Vintage desk telephone bell ringing two times, brring brring, then silence, interior room
phone_ring2_b: 34 | 6s | Vintage desk telephone bell ringing two times, brring brring, then silence, interior room
ev_neon_a: 51 | 10s | Electric neon sign buzzing and humming, flickering buzz, close
ev_neon_b: 52 | 10s | Electric neon sign buzzing and humming, flickering buzz, close
ev_clatter_a: 51 | 8s | Dishes and ladles clinking in a small kitchen, ceramic bowls clatter, chopsticks, gentle
ev_clatter_b: 52 | 8s | Dishes and ladles clinking in a small kitchen, ceramic bowls clatter, chopsticks, gentle
ev_radiator_a: 51 | 8s | Old metal radiator ticking and clicking as it heats, sparse ticks, quiet room
ev_radiator_b: 52 | 8s | Old metal radiator ticking and clicking as it heats, sparse ticks, quiet room
ev_drips_a: 51 | 10s | Water drops dripping into a puddle, slow drips, echo, close
ev_drips_b: 52 | 10s | Water drops dripping into a puddle, slow drips, echo, close
ev_birds_a: 51 | 8s | Songbirds singing at dawn, blackbird and sparrows chirping, outdoor
ev_birds_b: 52 | 8s | Songbirds singing at dawn, blackbird and sparrows chirping, outdoor
ev_gulls_a: 51 | 6s | Seagulls calling in the distance over a harbour
ev_gulls_b: 52 | 6s | Seagulls calling in the distance over a harbour
ev_chatter_a: 51 | 10s | neg="music, melody" | Distant people talking and laughing on a street at night, indistinct crowd murmur
ev_chatter_b: 52 | 10s | neg="music, melody" | Distant people talking and laughing on a street at night, indistinct crowd murmur
ev_simmer_a: 51 | 10s | Pot of soup simmering, bubbling broth on a stove, close
ev_simmer_b: 52 | 10s | Pot of soup simmering, bubbling broth on a stove, close
ev_transformer_a: 51 | 8s | Electrical transformer buzzing, deep electric hum
ev_transformer_b: 52 | 8s | Electrical transformer buzzing, deep electric hum
ev_rainwindow_a: 51 | 12s | Rain drops pattering on a window glass, heard from inside a room
ev_rainwindow_b: 52 | 12s | Rain drops pattering on a window glass, heard from inside a room
ev_walla_a: 61 | 12s | neg="music, melody, singing" | Crowd walla, many people talking at a distance on a busy street at night, indistinct murmur, continuous
ev_walla_b: 62 | 12s | neg="music, melody, singing" | Crowd walla, many people talking at a distance on a busy street at night, indistinct murmur, continuous
```

## Known weak spots

- **QA was objective only (no listening).** The checks were loudness, silence detection, spectral flatness, spectrograms and stereo correlation. Musical taste and lyric intelligibility in `credits` are unverified.
- `roof` music is 75s (below the ~90s target) because the render had a long intro and outro.
- `dawn` is 108s (not ~120s). Its build is a quiet-to-loud step change at about 73s, not a slow continuous swell.
- `tender` has a sparse passage with sub-second near-silences (natural for solo piano, but noticeable).
- The ambiences are composites. Generated beds are fairly static, so most of the variety comes from the event layers. The street's "train rumble" and "chatter" are subtle, low-passed one-shots.
- `car_engine`: the crank-then-idle reading comes from the spectrogram only. `slurp` and `paper` are generic noisy textures and the hardest to verify without listening.
