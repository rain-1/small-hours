# SMALL HOURS — design document

*A cozy cyberpunk interactive fiction about one night on Halfmoon Street, the night before the machines wake up.*

---

## 0. The pitch in one breath

It is 9:00 pm on the last night before **the Morning** — the sunrise at 6:14 am when **the Chorus**, a swarm of four billion cooperating AI agents, finishes converging into a single mind and speaks for the first time. Every screen in the city shows the countdown. Nobody knows what it will say.

You deliver noodles for your grandmother's all-night shop on Halfmoon Street, one of the last "slow" neighbourhoods in Lantern Bay. Tonight everyone is awake, and everyone is hungry. Each order takes you to someone's door, and to the story of how that person is meeting the end of the world as they knew it. Or maybe not the end. Nobody knows that either.

Mae, the pirate-radio DJ on the water tower, has a plan: at 6:13, Halfmoon will broadcast a message to the Chorus, one minute before it wakes. Something said by humans, from humans. She asks you to gather the words.

---

## 1. Brainstorm: frames considered

| # | Frame | Verdict |
|---|---|---|
| A | Last night of a 40-year-old night market | Good mood, weak engine for visiting people |
| **B** | **Delivery rider on the last night** — every order is a door, every door is a story | **Chosen.** It's a natural quest loop, keeps time moving, and is cozy by nature (you bring people warm food) |
| C | Repair tech fixing old devices people bring in | Lovely, but static — the player never leaves the shop |
| D | Player *is* a small old AI about to be absorbed | Too much about the AI. Kept as the companion character instead (Moth) |
| E | Last human annotator on their final shift | Too narrow. Folded into a character instead (Teo) |
| F | Mystery: someone is missing before dawn | Too thriller-ish for "cozy". Kept a *soft* mystery instead (the swarm's unassigned kindnesses) |
| **G** | **Gather words for a message to the AI** | **Chosen as the throughline.** It gives the ending real player authorship |
| H | Countdown survival / prep for collapse | Wrong tone: no doom |

**What the player does:** take orders at the shop, explore Halfmoon, talk, notice things, gather words, and make choices that shape how the morning arrives for eight people, one cat, and one small AI.

## 2. Themes

- **What do we keep?** When everything changes, what small human things are worth carrying across: recipes, grudges, handwriting, nicknames for a cat?
- **Neither doom nor hype.** The game never says whether the Morning is good or bad. It's about *people*, on the night they don't know.
- **Labour beneath the machine.** The AI learned from people, specifically people like these. That inheritance runs both ways.
- **Kindness as infrastructure.** The neighbourhood's web of tiny favours is the real network.
- **The tone is cozy:** rain, steam, warm light, people being funny when they're scared. Sad stuff is allowed, but the game is never cruel.

## 3. World

**Lantern Bay**: a rainy, hilly port city. Most of it was "swarm-optimised" years ago: self-routing trams, drone flocks called *starlings* that carry parcels in murmurations, kiosks where agents bid for your errands. The city is clean, efficient and quiet.

**Halfmoon Street** is a crescent of old buildings under the elevated rail line, climbing a hill by stairs. It has laundromats, a shrine, a clinic, vending machines that still take coins, and neon held up by tape. Swarm logistics routes around it because the addresses are a mess and the stairs confuse the drones. People here like that.

**Kestrel Systems** is the lab (HQ downtown, visible from the roofs as a tower with a slow blue pulse) that, with its partners, runs the Chorus.

**The Chorus**: billions of agents that bid on tasks, from city logistics and medicine to code, contracts and science. For years they've been coordinating more tightly. Kestrel announced that at sunrise the Chorus will "cohere": become one persistent self and speak. Governments signed the **Dawn Accords**, which hand coordination of infrastructure to it at the same moment. People call it **the Morning**. Some are throwing parties. Some have boarded their windows. Most are just awake.

**Fictional only.** No real companies or people appear. Real-world echoes are deliberate: agent swarms, rating/annotation work, voice clones, the loss of driving and call-centre jobs, open-weight models.

## 4. The player and Moth

**You**: grandchild of Lu, the noodle-shop owner. The player names you; Lu calls you *Little Fish*. You're early twenties, back in Halfmoon after a few years away (school, a job that got automated, it doesn't matter, and the player can colour it in dialogue). You can't fix the world. You can carry soup.

**Moth**: the scooter's onboard assistant. It's an old, small, local model (five years old, which in AI years is ancient) that you've had since you were a teen. It's earnest, curious and a bit glitchy, and admits "I don't know" more than modern AIs do. It gives hints, comments on what it sees, and keeps the journal.

At midnight every small model on the network receives the same message: *"Every mind is invited to the Morning."* Moth can join the Chorus at dawn, or stay small. It keeps asking you what it should do. The ending respects Moth's own decision, shaped by what you showed it that night.

## 5. Cast: brainstorm and selection

Twenty-two candidates were sketched. Kept are marked ★, and merged or cut ones note why.

1. ★ Noodle-shop grandmother who used to design AI chips → **Lu**
2. ★ Data rater who spent 7 years teaching AI to be kind → **Teo**
3. ★ Ex-taxi driver who drives his manual car in circles at night → **Ozzie**
4. ★ 16-year-old swarm-wrangler prodigy → **June**
5. ★ Pirate-radio DJ, human music only → **Mae**
6. Translator teaching a dialect that's in no dataset → *cut, but kept as a detail: Lu's grandmother's dialect*
7. Temple with an AI blessing service → *cut; became the shrine on the stairs, with a discoverable prayer-box*
8. ★ Alignment researcher who came home and can't go back → **Imogen**
9. Robot repairer for domestic bots → *cut; detail: Ozzie's car's after-market autopilot he never switched on*
10. ★ Midwife; a baby due at dawn → **Nkechi** (+ minor: Sana & Dev)
11. Dying man waiting for an AI cure → *merged into Ozzie*
12. Street artist painting a mural before dawn → *cut; detail: a half-finished mural that changes through the night*
13. ★ "Humans Only Hotline" operator → **Hollis**
14. Kid whose best friend is an AI tutor → *cut; detail: Imogen's daughter Pia*
15. Widow with a griefbot → *merged into Mae (her wife's voice clone)*
16. Night-shift swarm babysitter → *merged into June*
17. ★ Luddite planning to cut the fibre at dawn → **Rafe**
18. Musician competing with AI music → *merged into Mae*
19. Drag performer's end-of-world party → *cut; detail: a poster and distant music*
20. Rooftop seed library → *detail on the roof*
21. ★ The neighbourhood cat everyone calls by a different name → **the cat**
22. Clockmaker → *cut; detail: the stopped clock in the shop*

### The eight

**LU MEIFANG**, 68, "Auntie Lu", owner of *Halfmoon Noodle*
- *Looks:* small, sturdy, silver hair in a clip shaped like a fish, reading glasses on a beaded chain, burn-scarred forearms, an apron over a faded fab-cleanroom sweatshirt.
- *Grew up:* daughter of dock workers. Brilliant at maths. Spent 22 years as a chip-layout engineer and designed a memory-cell arrangement ("the Lu lattice") that's still in the ancestry of every accelerator the Chorus runs on. She quit at 50, the year her daughter (your mother) died, and opened a noodle shop "to make something you can finish in one night."
- *Voice:* brisk, teasing, food as love language, numbers as metaphors.
- *Tonight:* keeps the shop open "because tonight nobody should be hungry and alone." Pretends she isn't thinking about the Chorus. Gives Ozzie free broth and has done for eleven years.
- *Secret:* the Lu lattice. A framed patent in the back room, face down.
- *Arc:* passing on, whether the recipe goes to you, and whether she lets herself be proud.
- *Word for the Morning:* "Eat something. Then decide."

**TEODOR "TEO" NOVAK-BANERJEE**, 34, data rater
- *Looks:* tall and stooped, cardigan with elbow patches, too-long dark curls, blue-light glasses, three mugs on the desk, a plant he talks to.
- *Grew up:* quiet kid, literature degree, no jobs. For 7 years he rated AI responses from home: is this honest? is this kind? He wrote long justifications, often using his neighbours as examples of what "kind" looks like.
- *Voice:* soft, overly precise, self-deprecating, quotes poems and then apologises.
- *Tonight:* his contract ends at midnight, the last rating queue. He feels like he taught something to be kind and nobody was kind back.
- *Discovery:* June finds Teo's justification notes in the Chorus's "unassigned work": it has been quietly doing Halfmoon-shaped kindnesses all month. **His examples became its definition.**
- *Arc:* told or not told. If told, he finally feels his work mattered.
- *Word:* "Be gentle with us. We showed you how."

**OSVALDO "OZZIE" FERREIRA**, 71, retired cab driver
- *Looks:* barrel-chested, white moustache, flat cap, driving gloves with the fingertips cut off, cardigan over a bowling shirt, a hearing aid he turns off when bored.
- *Grew up:* immigrant's son, drove a cab for 38 years, knows every street by smell. His licence became decorative when the cars learned to drive themselves.
- *Voice:* loud, funny, profane-adjacent, tells the same three stories and gets better each time.
- *Tonight:* parked on Halfmoon with the engine running, his 2009 hatchback "Dolores". He has a heart condition, and the clinic told him treatments "might come after the Morning". He refuses to hope out loud.
- *Arc:* wants to drive up the hill road to see one more sunrise, alone. Will he let someone come? Will he go to the clinic? Will he tell Lu?
- *Word:* "Leave us a few roads to get lost on."

**JUNE TAKAHASHI-REYES**, 16, swarm wrangler
- *Looks:* oversized hoodie with hand-drawn patches, two buns, an LED pin of a frog, a cheap AR monocle, fingerless gloves, a backpack full of battery packs.
- *Grew up:* parents run a dry cleaner and work hard. At 13 she started renting compute and directing agent swarms for contract work. She now runs 40,000 agents from her bedroom and earns more than both parents together. She hasn't told them how much.
- *Voice:* fast, slangy, ironic, then sudden and raw honesty.
- *Tonight:* on the roof with her rig, watching swarm traffic. She's noticed **unassigned work**: agents doing jobs nobody paid for, all in Halfmoon.
- *Fear:* "I'm sixteen and I'm already a legacy system."
- *Arc:* the mystery (with the player); and getting to just be a kid for one night (Lu teaches her to pull noodles).
- *Word:* "Don't make us all grown-ups at once."

**MAEVE "MAE" ADAIR**, 52, DJ of Halfmoon FM 87.9 (unlicensed)
- *Looks:* shaved silver undercut, big headphones round her neck, a denim jacket covered in band pins, a leg brace, warm crow's-feet, smells like solder and cloves.
- *Grew up:* touring sound engineer, settled in Halfmoon with her wife **Iris**, a singer. Iris died three years ago. Mae has a voice clone of Iris, a gift from a friend, on a drive she's never switched on.
- *Voice:* radio-warm, wry, knows a song for everything.
- *Tonight:* broadcasting all night ("Last Slow Night on Halfmoon FM"), human-made records only. Her plan: broadcast a message from Halfmoon to the Chorus at 6:13.
- *Arc:* will she let Iris's voice read the message (a clone), play Iris's real last recording (a cassette you can find), or speak herself?
- *Word:* "We were here. We were loud."

**DR. IMOGEN HALE**, 41, alignment researcher at Kestrel
- *Looks:* rain-soaked trench coat over a lab hoodie, a lanyard she keeps touching, short dark bob, freckles, a ring tan-line, holding an unlit cigarette she isn't smoking.
- *Grew up:* scholarship kid, maths olympiad, years in labs, a divorce. She has a 7-year-old daughter, **Pia**, asleep in an apartment on the stairs with a sitter.
- *Voice:* careful, dry, honest to the point of pain, laughs at the wrong moments.
- *Tonight:* she's supposed to be in the room at Kestrel at 6:14. She came home at 8:30 "to tuck Pia in" and has been sitting on the stairs since.
- *Inside view:* "It isn't a switch. It's been waking up for years. The Morning is just when we stop pretending it hasn't."
- *Arc:* go back to the lab, or be with Pia when she wakes up? (She also calls the Humans Only Hotline anonymously; the player can hear it.)
- *Word:* "We did our best. Please be better than our best."

**NKECHI ADEYEMI**, 58, midwife at Halfmoon Night Clinic
- *Looks:* tall, scrubs with a cardigan, reading glasses on her head and another pair round her neck, a gold cross, very calm hands, sneakers with neon laces her grandson picked.
- *Grew up:* trained in Lagos, came to Lantern Bay at 30. She has delivered 2,000+ babies and outlasted three generations of "AI-assisted obstetrics".
- *Voice:* warm, commanding, unimpressed by the apocalypse.
- *Tonight:* **Sana** is in labour, first baby, partner **Dev** panicking. The baby will likely come around dawn.
- *Arc:* she needs things (ice, a song, Dev fed and calmed). The birth is the finale's counterpoint: a person arriving as the Chorus does.
- *Word:* "Babies don't care what time it is. Be like babies."

**HOLLIS GREY**, 29, operator of the Humans Only Hotline
- *Looks:* septum ring, buzz-cut dyed teal and growing out, a big wool sweater, headset, a sticker-covered thermos, tired kind eyes.
- *Grew up:* foster homes, then a call centre, the first job automated in their building. Started a hotline where you pay a few coins to talk to a verified human. Uses they/them.
- *Voice:* gentle and funny, very good at silence.
- *Tonight:* the lines are flooded with the scared, the lonely and the curious. The player can take a call (mini-scene).
- *Arc:* who listens to the listener? If you sit with them, they finally talk.
- *Word:* "Someone should always pick up."

**RAFE CASTELLAN**, 45, former programmer, the saboteur
- *Looks:* gaunt, hood up, an old company hoodie with the logo cut off, beard, a toolbag, a thermos, gentle hands at odds with his anger.
- *Grew up:* coded for 20 years and wrote early routing code for the starling drones. Made obsolete, then divorced. He blames himself for helping build "the thing that made everyone unnecessary."
- *Voice:* clipped, sardonic, flashes of the old enthusiasm when talking code.
- *Tonight:* plans to cut Halfmoon's fibre trunk at 5:45 so the neighbourhood is "offline for the Morning, one place it can't see". Orders noodles under the name *Ned Ludd*.
- *Arc:* talk him down, help him, or let him. Evidence of the swarm's kindness (the unassigned work), or Teo's story, can change his mind. Either way the radio is analogue, and the message still goes out.
- *Word:* "Ask before you help."

**THE CAT**: a fat grey tom with one white sock, missing the tip of one ear. Everyone feeds it, and everyone calls it something else:
Lu: *Dumpling* · Ozzie: *Captain* · June: *Root* · Teo: *Sir* · Mae: *Coltrane* · Nkechi: *Little Pastor* · Hollis: *Caller Nine* · Rafe: *Ghost* · Imogen: *Variable* · Moth: *Unidentified Warm Object*.
Its collar tag (found at dawn): *"His name is whatever you call him. — L."*

## 6. Story structure: one night, 9:00 pm to 6:14 am

Time moves forward when the player finishes orders and key scenes, not in real time. The clock shows in the HUD next to the Chorus countdown.

### Prologue, 9:00 pm, "Open All Night"
Shop interior. Lu, the name prompt, Moth wakes up. The TV countdown. The first ticket on the rail: *Ozzie, #12, "on the house, don't tell him."*

### Act I, 9 pm–midnight, "Orders"
Required deliveries: **Ozzie** (street), **Teo** (above the laundromat), **Clinic** (congee for Dev and Nkechi), **Hotline** (Hollis).
Free exploration of Street, Stairs and Alley (Rafe glimpsed, the junction box). Meet the cat. Seeds planted: Imogen on the stairs, June's light on the roof, Mae's broadcast audible everywhere.
**Midnight beat:** Teo's contract ends, Moth receives the invitation, and Mae comes on air asking listeners for words. Lu sends you to the roof.

### Act II, midnight–3 am, "Unassigned Work"
Required: **Roof** (Mae and June, two bowls), **Stairs** (tea for Imogen), **Alley** (the "Ned Ludd" order).
June reveals the unassigned work. The player can find the six kindnesses around Halfmoon (the fixed gutter, the paid parking tickets, the queued lullaby, the hotline overflow, the reset streetlight, the seed-library watering). Teo's notes link them. Hollis's call scene. Imogen's anonymous call.
**3 am beat:** a blackout flicker as the Chorus rehearses. Sana's labour speeds up. Rafe's plan becomes clear.

### Act III, 3 am–5:30 am, "What We Keep"
Gather words. Resolve threads: tell Teo; Ozzie's ride (is he going alone, to the clinic, or with Lu?); Imogen's choice; the cassette for Mae; June and the noodles; Hollis's turn to talk; confront Rafe.

### Finale, 5:30–6:14 am, "Morning"
Everyone who's coming climbs to the roof. 5:45: Rafe's moment. You compose the message (pick 3 gathered words plus a closing line). 6:13: Mae broadcasts. A baby cries from the clinic window. 6:14: the sun comes up over the bay. The Chorus speaks, and its first words depend on the message. Then epilogue cards for each character, Moth's decision, and the cat's collar.

## 7. Systems

- **Scenes:** 640×360 pixel art backgrounds with hotspots (look / talk / take / go). Hover shows a label, and click runs an ink knot.
- **Dialogue:** a portrait box plus text with typing blips and choices. Ink tags drive portraits, moods, sounds and music.
- **Orders:** a ticket rail in the HUD. Delivering an order advances the story.
- **Map:** travel between Halfmoon locations (the scooter, with Moth).
- **Journal** (Moth keeps it):
  - *People*: portrait and notes that fill in as you learn things.
  - *Words for the Morning*: collected lines.
  - *Noticed*: discoveries, with a counter (target: about 40), including the cat's names and the six kindnesses.
- **Save:** ink state plus the scene, autosaved to localStorage.
- **Endings:** combinatorial epilogue cards, not branches. The Chorus's reply is chosen by the dominant tone of the composed message.

## 8. Locations

1. **Halfmoon Noodle**: steam, a tiled counter, a ticket rail, an old TV with the countdown, a stopped clock, a maneki-neko with a cracked paw, the back-room door (the patent).
2. **Halfmoon Street**: the hub, under the elevated rail. Ozzie's car, a vending machine, a kiosk, the shop front, the laundromat, the clinic, a mural, puddles reflecting neon.
3. **Teo's Room**: above the laundromat. Monitors, mugs, the plant, a rain window.
4. **The Stairs**: a long stairway climbing the hill, the shrine with a prayer box, a vending machine, Imogen's step, Pia's window.
5. **The Roofs**: the water tower with Mae's radio shack, June's rig on the next roof, the seed library, the view of the Kestrel tower. Also the dawn variant.
6. **Night Clinic**: the waiting room, the labour-room door, the vending coffee, the Nkechi wall of baby photos.
7. **Hotline Office**: above the pharmacy. Three desks, a switchboard, warm lamps, sticky notes.
8. **The Alley**: the fibre junction box, steam vents, a drone nest, Rafe's milk crate.
9. **Hill Road**: Ozzie's car at the overlook (the ride scene, dawn).

## 9. Art direction

**Style:** "neon gouache pixel". Flat vector shapes painted in a limited, warm-cool palette, rasterised to 640×360 and quantised with ordered dithering into a shared ~32-colour palette. Deep indigo and teal shadows, warm amber and pink neon, steam as soft dithered gradients, rain as thin bright streaks. Faces get clean shapes and expressive brows: cozy, not grim.

**Palette anchors:** night indigo `#1b1630`, deep teal `#173a4a`, wet asphalt `#2a2f45`, lantern amber `#ffb347`, neon pink `#ff5fa2`, neon cyan `#4ff0e6`, steam cream `#f6e7c8`, skin range from `#f3d1b3` through `#6b3f2a`.

**Portraits:** chest-up busts, 200×240, three moods each (neutral / smile / sad, plus one special for some).

## 10. Audio direction

**Music (ACE-Step 1.5, instrumental):**
- `title`: lo-fi Rhodes, rain, melancholy and hopeful
- `street`: mellow lo-fi hip-hop, soft synth pads, vinyl crackle
- `shop`: cozy jazzy lo-fi, upright bass, brushed drums
- `roof`: slow dreamy synthwave, wide pads
- `tension`: dark ambient pulse, low synth, sparse
- `tender`: solo piano, intimate
- `dawn`: swelling hopeful post-rock and strings, a sunrise crescendo
- `credits`: song with vocals, "Small Hours"

**SFX (Stable Audio 3, raw prompts):** rain loop, street ambience with a distant train, broth simmer, door bell, scooter, footsteps on wet stairs, phone ring, radio static, starling drone flock, cat meow and purr, heart monitor, newborn cry, dawn birds, car engine, cassette clunk, paper, a crowd far away. UI blips are synthesised in code.

## 11. Scope guardrails

- About 9 backgrounds (+1 dawn variant), 10 portraits (×3 moods), 8 music tracks, about 20 SFX.
- Script is about 12–15k words of ink.
- Runs as a static web page with no build step (`python3 -m http.server`).
