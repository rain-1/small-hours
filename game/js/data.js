// Static game data: speakers, scenes, journal content, epilogue.
// `v` everywhere is a proxy onto the ink variables (see main.js).

export const SPEAKERS = {
  lu:     { name: "Lu", pitch: 1.15 },
  teo:    { name: "Teo", pitch: 0.85 },
  ozzie:  { name: "Ozzie", pitch: 0.7 },
  june:   { name: "June", pitch: 1.35 },
  mae:    { name: v => (v.mae_met ? "Mae" : "Halfmoon FM"), pitch: 0.95 },
  imogen: { name: v => (v.imogen_met ? "Imogen" : "Woman on the stairs"), pitch: 1.05 },
  nkechi: { name: "Nkechi", pitch: 0.9 },
  hollis: { name: "Hollis", pitch: 1.0 },
  rafe:   { name: v => (v.rafe_met ? "Rafe" : "Man in the alley"), pitch: 0.75 },
  dev:    { name: "Dev", pitch: 0.95 },
  moth:   { name: "Moth", pitch: 1.6, synth: true },
  you:    { name: v => v.name, pitch: 1.1, style: "you", portrait: false },
  chorus: { name: "", pitch: 0.5, style: "chorus", portrait: false, synth: true },
  radio:  { name: "Halfmoon FM 87.9", pitch: 0.95, style: "radio", portraitAs: "mae", radio: true },
  phone:  { name: "On the line", pitch: 1.0, style: "phone", portrait: false },
  sign:   { name: "", pitch: 1.0, style: "sign", portrait: false, silent: true },
  tv:     { name: "Kestrel Systems", pitch: 0.9, style: "phone", portrait: false },
  cat:    { name: v => catName(v), pitch: 1.8, portrait: false },
  pia:    { name: "Pia", pitch: 1.7, portrait: false },
  iris:   { name: "Iris?", pitch: 1.1, style: "radio", portrait: false },
};

function catName(v) {
  const order = [["cat_lu", "Dumpling"], ["cat_ozzie", "Captain"], ["cat_june", "Root"], ["cat_teo", "Sir"], ["cat_mae", "Coltrane"],
    ["cat_nkechi", "Little Pastor"], ["cat_hollis", "Caller Nine"], ["cat_rafe", "Ghost"], ["cat_imogen", "Variable"]];
  const known = order.filter(([k]) => v.has("noticed", k)).map(([, n]) => n);
  return known.length ? known[Math.floor(Date.now() / 4000) % known.length] : "The cat";
}

// ---------- scenes ----------
// hotspot kinds: look (amber), talk (pink), go (cyan)
export const SCENES = {
  shop: {
    bg: "bg_shop", music: "shop", amb: "amb_shop", indoor: true,
    steam: [[0, 0, 1.4]], // filled from layout (pot)
    labels: { ticket_rail: "Ticket rail", tv: "TV", clock: "Stopped clock", lucky_cat: "Lucky cat", photo: "Photo",
      radio: "Radio", back_door: "Back room", pot: "Broth pot", front_door: ["Out to the street", "go"], stools: "Stools" },
    figures: v => [
      v.act < 4 && { id: "lu", sprite: "lu_counter", at: "lu", label: "Lu", knot: "talk_lu" },
      v.act === 2 && { id: "ozzie", sprite: "ozzie_stand", at: "guest", label: "Ozzie", knot: "talk_ozzie_shop" },
      v.act === 3 && v.june_noodles === 2 && { id: "june", sprite: "june_sit", at: "guest", label: "June", knot: "talk_june" },
    ],
  },
  street: {
    bg: "bg_street", music: "street", amb: "amb_street", rain: true, ground: 282,
    steam: [[137, 236, 0.8]],
    labels: { shop_door: ["Halfmoon Noodle", "go"], laundromat_door: ["Suds & Stars (flats upstairs)", "go"], alley: ["The alley", "go"],
      hotline_door: ["Humans Only Hotline", "go"], clinic_door: ["Night Clinic", "go"], stairs_up: ["The stairs", "go"],
      car: [v => (v.act === 1 || v.act >= 3 && !v.ozzie_ride ? "Ozzie" : "Dolores (Ozzie's car)"), v => (v.act === 1 || v.act >= 3 && !v.ozzie_ride ? "talk" : "look")],
      vending: "Vending machine", cat: ["The cat", "talk"], kiosk: "Swarm kiosk", mural: "Mural", water_tower: "Water tower" },
    figures: () => [],
  },
  teo_room: {
    bg: "bg_teo_room", music: "tender", amb: "amb_office", indoor: true,
    labels: { monitors: "Monitors", plant: "Plant", mugs: "Mugs", bookshelf: "Bookshelf", pinboard: "Pinboard", window: "Window", door: ["Back downstairs", "go"] },
    figures: () => [{ id: "teo", sprite: "teo_desk", at: "teo", label: "Teo", knot: "talk_teo" }],
  },
  stairs: {
    bg: "bg_stairs", music: "street", amb: "amb_rain", rain: true, ground: 330,
    labels: { shrine: "Shrine", prayer_box: "Prayer box", vending: "Fortune tea machine", pia_window: "Starry window", lamp: "Lamp post",
      up: [v => (v.act < 2 ? "Up to the roofs (locked)" : "Up to the roofs"), "go"], down: ["Down to the street", "go"] },
    figures: v => [
      v.imogen_choice === "" && { id: "imogen", sprite: "imogen_sit", at: "imogen", label: v.imogen_met ? "Imogen" : "Woman on the stairs", knot: "talk_imogen" },
      v.imogen_choice !== "" && { id: "imogen", sprite: "imogen_sit", at: "imogen", label: "Imogen's step", knot: "talk_imogen", hidden: true },
      { id: "cat", sprite: "cat_sleep", at: "cat", label: "The cat", knot: "street_cat" },
    ],
  },
  roofs: {
    bg: "bg_roofs", music: "roof", amb: "amb_roof", rain: true, ground: 300,
    labels: { radio_shack: "Radio shack", records: "Records", june_rig: ["June's rig", "talk"], seed_library: "Seed library", view: "The view", water_tower: "Water tower", ladder: ["Down the ladder", "go"] },
    figures: v => roofFigures(v),
  },
  roofs_dawn: {
    bg: "bg_roofs_dawn", music: "dawn", amb: "amb_dawn", layout: "roofs",
    labels: {},
    figures: v => roofFigures(v),
  },
  clinic: {
    bg: "bg_clinic", music: "tender", amb: "amb_clinic", indoor: true,
    labels: { desk: "Reception", coffee: "Coffee machine", baby_photos: "Baby photos", labour_door: "Labour & Delivery", chairs: "Chairs", posters: "Posters", exit: ["Out to the street", "go"] },
    figures: v => [
      v.act < 4 && { id: "nkechi", sprite: "nkechi_stand", at: "nkechi", label: "Nkechi", knot: "talk_nkechi" },
      { id: "dev", sprite: "dev_sit", at: "dev", label: "Dev", knot: "talk_dev" },
    ],
  },
  hotline: {
    bg: "bg_hotline", music: "tender", amb: "amb_office", indoor: true,
    labels: { phones: "Phones", switchboard: "Switchboard", notes_wall: "Thank-you notes", kettle: "Kettle", window: "Window", sofa: "Sofa", exit: ["Down to the street", "go"] },
    figures: () => [{ id: "hollis", sprite: "hollis_sit", at: "hollis", label: "Hollis", knot: "talk_hollis" }],
  },
  alley: {
    bg: "bg_alley", music: "tension", amb: "amb_alley", rain: true, ground: 300,
    steam: [[0, 0, 1.2]],
    labels: { junction_box: "Junction box", steam_vent: "Steam vent", drone_roost: "Drone roost", crates: "Milk crates", graffiti: "Graffiti",
      back_door: ["Back door of the shop", "go"], exit: ["Back to the street", "go"] },
    figures: v => [
      v.act >= 1 && v.rafe_out !== "stopped" && { id: "rafe", sprite: "rafe_crouch", at: "rafe", label: v.rafe_met ? "Rafe" : "Man in the alley", knot: "talk_rafe" },
    ],
  },
  hill_road: {
    bg: "bg_hill_road", music: "tender", amb: "amb_dawn", labels: {},
    figures: () => [{ id: "ozzie", sprite: "ozzie_stand", at: "ozzie", label: "Ozzie", knot: "done" }],
  },
};

function roofFigures(v) {
  const f = [
    { id: "mae", sprite: "mae_stand", at: "mae", label: v.mae_met ? "Mae" : "DJ", knot: "talk_mae" },
    { id: "june", sprite: "june_sit", at: "june", label: "June", knot: "talk_june" },
  ];
  if (v.act === 4) {
    const extra = [];
    if (v.teo_told) extra.push({ id: "teo", sprite: "teo_desk", label: "Teo" });
    if (v.hollis_open) extra.push({ id: "hollis", sprite: "hollis_sit", label: "Hollis" });
    if (v.imogen_choice === "roof") extra.push({ id: "imogen", sprite: "imogen_sit", label: "Imogen & Pia" });
    if (v.rafe_out === "stopped") extra.push({ id: "rafe", sprite: "rafe_crouch", label: "Rafe" });
    if (!v.ozzie_lu) extra.push({ id: "lu", sprite: "lu_counter", label: "Lu" });
    extra.slice(0, 4).forEach((e, i) => f.push({ ...e, at: `gathering${i + 1}`, knot: "done" }));
    f.push({ id: "cat", sprite: "cat_sit", at: "cat", label: "The cat", knot: "done" });
  }
  return f;
}

// ---------- map ----------
export const MAP_PINS = [
  { id: "shop", scene: "shop", label: "Noodle shop", open: () => true },
  { id: "laundromat", scene: "teo_room", label: "Teo's", open: v => v.o_teo >= 1 },
  { id: "clinic", scene: "clinic", label: "Clinic", open: () => true },
  { id: "hotline", scene: "hotline", label: "Hotline", open: () => true },
  { id: "alley", scene: "alley", label: "Alley", open: () => true },
  { id: "stairs", scene: "stairs", label: "Stairs", open: () => true },
  { id: "roofs", scene: "roofs", label: "Roofs", open: v => v.act >= 2 },
  { id: "street", scene: "street", label: "Street", open: () => true, fallback: [320, 300] },
];
export const MAP_FALLBACK = { shop: [250, 200], laundromat: [90, 190], clinic: [500, 200], hotline: [400, 160], alley: [140, 250], stairs: [580, 150], roofs: [600, 80], street: [320, 300] };

// pins that have something waiting (pink dot)
export function pinHasTask(id, v) {
  switch (id) {
    case "shop": return (v.act === 1 && act1(v)) || (v.act === 3 && !v.recipe) || (v.mae_tape === 0 && v.song_req === 1) || v.june_noodles === 1;
    case "laundromat": return v.o_teo === 1 || (v.june_case >= 2 && !v.teo_told);
    case "clinic": return v.o_clinic === 1 || v.o_ice === 1 || (v.act === 3 && !v.dev_calm);
    case "hotline": return v.o_hotline === 1;
    case "alley": return v.o_ludd === 1 || (v.act === 3 && v.rafe_out === "");
    case "stairs": return v.o_tea === 1 || (v.act === 3 && v.imogen_choice === "");
    case "roofs": return v.o_roof === 1 || v.mae_tape === 1 || (v.june_case === 1 && kindness(v) >= 3);
    case "street": return (v.o_ozzie === 1) || (v.act === 3 && !v.ozzie_ride);
  }
  return false;
}
const act1 = v => v.o_ozzie === 2 && v.o_teo === 2 && v.o_clinic === 2 && v.o_hotline === 2;
const kindness = v => ["k_gutter", "k_tickets", "k_lullaby", "k_phonebill", "k_lamp", "k_seeds", "k_awning"].filter(k => v.has("noticed", k)).length;

// ---------- orders ----------
export const ORDERS = [
  { key: "o_ozzie", who: "Ozzie", what: "#12 beef broth", where: "the teal car" },
  { key: "o_teo", who: "Teo", what: "cold noodles", where: "above laundromat" },
  { key: "o_clinic", who: "Clinic", what: "2× congee", where: "Night Clinic" },
  { key: "o_hotline", who: "Hollis", what: "1 bowl", where: "the hotline" },
  { key: "o_roof", who: "Roof", what: "2 bowls", where: "the roofs" },
  { key: "o_tea", who: "Stairs", what: "tea flask", where: "the stairs" },
  { key: "o_ice", who: "Clinic", what: "bag of ice", where: "Night Clinic" },
  { key: "o_ludd", who: "N. Ludd", what: "extra chili", where: "the alley" },
];

export function objective(v) {
  if (v.act === 0) return "";
  if (v.act === 1) return act1(v) ? "Head back to Lu at the shop." : "Deliver Lu's orders around Halfmoon.";
  if (v.act === 2) {
    const all = v.o_roof === 2 && v.o_tea === 2 && v.o_ludd === 2 && v.o_ice === 2;
    return all ? "…" : "Deliver the midnight orders. Mae has asked Halfmoon for words.";
  }
  if (v.act === 3) return `Gather words for the Morning (${v.wordCount}). Mae waits on the roof.`;
  return "";
}

// ---------- journal: people ----------
export const PEOPLE = [
  { id: "lu", name: "Lu Meifang", role: "Grandma. Halfmoon Noodle, 68", known: () => true, notes: [
    ["Has kept the shop open all night so nobody is hungry and alone.", () => true],
    ["Gives Ozzie free broth and has for eleven years. Pretends it's leftover.", () => true],
    ["The clock stopped the night Mum died. She won't fix it.", v => v.has("noticed", "clock")],
    ["Designed the Lu lattice — it's in every chip the Chorus thinks on.", v => v.has("noticed", "patent")],
    ["Taught you the broth. Gave you the notebook.", v => v.recipe],
  ] },
  { id: "moth", name: "Moth", role: "The scooter's old onboard AI", known: () => true, notes: [
    ["Five years old. Ancient, in model years. Says \"I don't know\" a lot.", () => true],
    ["Has been invited to join the Chorus at dawn.", v => v.act >= 2],
    ["Kept your pigeon poem from when you were sixteen.", v => v.moth_deep >= 1],
  ] },
  { id: "ozzie", name: "Osvaldo \"Ozzie\" Ferreira", role: "Retired cab driver, 71", known: v => v.o_ozzie >= 1, notes: [
    ["Drives Dolores round Halfmoon every night to keep her legs moving.", v => v.o_ozzie === 2],
    ["Someone paid two years of his parking tickets. He's insulted.", v => v.has("noticed", "k_tickets")],
    ["Never switched on the autopilot. \"So you remember you're there.\"", v => v.has("noticed", "autopilot")],
    ["His heart is tired. Nkechi wants him at the clinic.", v => v.ozzie_heart],
    ["Took you up to the hill road to see if the sun still knows the way.", v => v.ozzie_ride],
  ] },
  { id: "teo", name: "Teodor Novak-Banerjee", role: "Data rater, 34", known: v => v.o_teo >= 1, notes: [
    ["Seven years rating AI answers for kindness. Contract ends at midnight.", v => v.o_teo === 2],
    ["Rater #4471. Used Halfmoon as his examples of kindness.", v => v.teo_rated],
    ["Talks to a monstera named Gerald.", v => v.has("noticed", "gerald")],
    ["Knows now: it was listening.", v => v.teo_told],
  ] },
  { id: "nkechi", name: "Nkechi Adeyemi", role: "Midwife, Night Clinic, 58", known: v => v.o_clinic >= 1, notes: [
    ["Delivered 2,412 babies. Unimpressed by the apocalypse.", v => v.o_clinic === 2],
    ["Sana's baby is coming around dawn.", v => v.o_clinic === 2],
    ["Sana wants a song about a lantern her mother loved.", v => v.song_req >= 1],
  ] },
  { id: "dev", name: "Dev Raman", role: "About to be a father, 31", known: v => v.o_clinic === 2, notes: [
    ["Lost his logistics job to a swarm last month.", v => v.has("noticed", "dev_lanyard")],
    ["Breathing in for four, out for six.", v => v.dev_calm],
  ] },
  { id: "hollis", name: "Hollis Grey", role: "Humans Only Hotline, 29 (they/them)", known: v => v.o_hotline >= 1, notes: [
    ["Pick up, don't fix, stay.", v => v.o_hotline === 2],
    ["You covered the phones. You stayed on the silent one.", v => v.hollis_cover],
    ["Nobody had ever asked them if they were okay.", v => v.hollis_open],
  ] },
  { id: "mae", name: "Maeve \"Mae\" Adair", role: "DJ, Halfmoon FM 87.9, 52", known: v => v.act >= 2, notes: [
    ["Will broadcast a message from Halfmoon at 6:13 — one minute before it wakes.", v => v.act >= 2],
    ["Her wife Iris died three years ago. Has a drive with Iris's voice on it, never switched on.", v => v.has("noticed", "iris_drive")],
    ["Heard Iris sing again, flat on the bridge.", v => v.mae_tape === 2],
  ] },
  { id: "june", name: "June Takahashi-Reyes", role: "Swarm wrangler, 16", known: v => v.june_case >= 1, notes: [
    ["Runs forty thousand agents from a tarp on the roof.", v => v.june_case >= 1],
    ["Found \"unassigned work\" — kindnesses nobody paid for, all in Halfmoon.", v => v.june_case >= 1],
    ["Traced them to R-4471.", v => v.june_case >= 2],
    ["Made a noodle. Nothing helped her.", v => v.june_noodles === 2],
  ] },
  { id: "imogen", name: "Dr. Imogen Hale", role: "Alignment researcher, Kestrel, 41", known: v => v.act >= 1 && (v.imogen_met || v.has("noticed", "imogen_voice")), notes: [
    ["Supposed to be in the room at 6:14. Hasn't been able to stand up.", v => v.imogen_met],
    ["Her daughter Pia counts the stars on her window every night.", v => v.has("noticed", "pia_stars")],
    ["\"It isn't a switch. It's been waking up for years.\"", v => v.imogen_met],
    ["Made her choice before dawn.", v => v.imogen_choice !== ""],
  ] },
  { id: "rafe", name: "Rafe Castellan", role: "Former programmer, 45", known: v => v.rafe_met, notes: [
    ["Wrote the original murmuration code for the starlings.", v => v.rafe_met],
    ["Drones keep building him a little roof. He tore it down eleven times.", v => v.has("noticed", "k_awning")],
    ["Plans to cut Halfmoon's fibre at 5:45.", v => v.rafe_met],
    ["Closed the box. \"Ask before you help.\"", v => v.rafe_out === "stopped"],
  ] },
];

// ---------- journal: words ----------
export const WORDS = {
  w_lu: ["Lu", "Eat something first. Then decide."],
  w_teo: ["Teo", "Be gentle with us. We showed you how."],
  w_ozzie: ["Ozzie", "Leave us a few roads to get lost on."],
  w_june: ["June", "Don't make us all grown-ups at once."],
  w_mae: ["Mae", "We were here. We were loud."],
  w_imogen: ["Imogen", "We did our best. Please be better than our best."],
  w_nkechi: ["Nkechi", "Every morning, someone new arrives. Make room."],
  w_hollis: ["Hollis", "Someone should always pick up."],
  w_rafe: ["Rafe", "Ask before you help."],
  w_moth: ["Moth", "I don't know yet. I'd like to find out with you."],
  w_cat: ["The cat", "Mrrp."],
};

// ---------- journal: noticed ----------
export const NOTICED = {
  cat_lu: ["Dumpling", "What Lu calls the cat. \"Fat liar. I love him.\""],
  cat_ozzie: ["Captain", "What Ozzie calls the cat. Best co-pilot he ever had."],
  cat_june: ["Root", "What June calls the cat. He has admin access to everything."],
  cat_teo: ["Sir", "What Teo calls the cat. The bearing of a disappointed admiral."],
  cat_mae: ["Coltrane", "What Mae calls the cat. Steps on the faders."],
  cat_nkechi: ["Little Pastor", "What Nkechi calls the cat. Visits everyone, brings nothing."],
  cat_hollis: ["Caller Nine", "What Hollis calls the cat. Sits on the desk that doesn't exist."],
  cat_rafe: ["Ghost", "What Rafe calls the cat. Doesn't ask questions."],
  cat_imogen: ["Variable", "What Imogen calls the cat. Never where you predict."],
  cat_moth: ["Unidentified Warm Object", "What Moth's sensor log calls the cat."],
  k_gutter: ["The gutter", "Lu's leaking gutter, fixed overnight. The landlord says it wasn't him."],
  k_tickets: ["The tickets", "Two years of Ozzie's parking tickets, paid by an \"anonymous agent\"."],
  k_lullaby: ["The lullaby", "A lullaby queued on the clinic ward for 6:14. Nobody asked."],
  k_phonebill: ["The phone bill", "The hotline's bill, paid four months ahead. Anonymous."],
  k_lamp: ["The stair lamp", "Broken two years. Fixed last Tuesday. Task origin: unassigned."],
  k_seeds: ["The seed library", "Watered every day of a heatwave while Mae was in hospital."],
  k_awning: ["The awning", "A little roof the drones keep building over Rafe's crate."],
  patent: ["The patent", "Face-down in the back room. Inventor: Lu Meifang."],
  clock: ["The stopped clock", "4:47. Cracked glass. Eighteen years."],
  photo: ["Mum", "Lin, at twenty, laughing on the same scooter."],
  lucky_cat: ["The lucky cat", "Glued with gold by Ozzie. Crooked."],
  tv: ["The countdown", "Every channel, all night, a number getting smaller."],
  rater_id: ["#4471", "Teo's rater number, in the corner of his screen."],
  gerald: ["Gerald", "A monstera. Teo's control group for kindness."],
  chapbook: ["Small Kindnesses", "Teo's poems. Edition of forty."],
  imogen_voice: ["A voice on the line", "A woman on some stairs who helps make the thing everyone's counting down to."],
  pia_stars: ["206 stars", "Glow-in-the-dark, on Pia's window. She has a map."],
  prayers: ["Prayers", "\"please let it like us.\" \"thank you for the lamp.\""],
  fortune: ["A fortune", "\"The thing you are waiting for is also waiting.\""],
  mural: ["The mural", "A sunrise on the pharmacy shutter. ADD SOMETHING."],
  kiosk: ["The kiosk", "Agents bidding for errands. Some bids are zero."],
  graffiti: ["Graffiti", "WHO WATCHES THE WATCHERS? — we do, we're bored."],
  records: ["Human hands only", "Mae's records, each with one true thing written on a card."],
  iris_drive: ["The drive", "Iris's voice, reconstructed. Never switched on."],
  cassette: ["Lantern Keeper", "Iris, live at Halfmoon Noodle, ten years ago. Flat on the bridge."],
  june_photo: ["The furious one", "June, sixteen years ago, on the clinic's wall of babies."],
  notes_wall: ["Thank-you notes", "\"you picked up when i was on the bridge. i'm a dad now.\""],
  dev_lanyard: ["Bayline Freight", "Dev's lanyard. Thirty-two people replaced by a swarm and a 23-year-old."],
  autopilot: ["The grey box", "Dolores could drive herself. Ozzie never pressed the button."],
  kestrel_view: ["The tower", "Kestrel, across the bay, pulsing blue."],
  seed_names: ["Seed labels", "\"Iris — sunflowers. For Mae. DON'T let her kill them.\""],
  dialect: ["The notebook", "Lu's recipes, with your great-grandmother's dialect in the margins."],
  drone_roost: ["Doris", "A starling drone with a ribbon on its leg."],
  sunrise_soda: ["Sunrise Soda", "Flavour: \"tomorrow\". Tastes like orange and nerves."],
  pinboard: ["Kind ≠ nice", "Teo's rule: kind = true + warm."],
  junction: ["The junction box", "Halfmoon's fibre trunk. Someone added a frog sticker."],
};

// ---------- epilogue ----------
export function epilogueCards(v) {
  const c = [];
  const toneLine = { gentle: "It said it would be careful.", memory: "It said it would remember.", free: "It asked if it could ask.",
    hopeful: "It talked about the baby.", curious: "It said it didn't know yet, either." }[v.reply_tone] || "";
  c.push({ head: "THE MORNING", text: `The Chorus woke at 6:14 and, among the billions of voices shouting at it, it answered a pirate radio station on a hill. ${toneLine} Nobody outside Halfmoon ever quite believed the recording was real.` });
  c.push({ id: "lu", name: "Lu", text: v.lu_patent
    ? `The patent frame went back on the wall, face out, next to the stopped clock. Under it Lu stuck a sign: "I DID THAT. ALSO THE SOUP." ${v.recipe ? "You make the broth on Tuesdays now. She says it's cloudy. It isn't." : ""}`
    : `Halfmoon Noodle opened at eleven the next morning, same as always. ${v.recipe ? "You make the broth on Tuesdays now. She says it's cloudy. It isn't." : "Lu says she'll teach you the broth \"when you're ready.\" You suspect you're ready."}` });
  c.push({ id: "ozzie", name: "Ozzie", text: v.ozzie_clinic
    ? `Ozzie was first on the list. The new treatment came in spring, designed in an afternoon by a mind that had been awake for four months. By summer he was driving Dolores up the hill road again. ${v.ozzie_lu ? "Lu rides with him. She criticises his driving the entire way." : "He still won't press the autopilot button."}`
    : v.ozzie_lu ? "Ozzie and Lu watched the Morning from the shop doorway on two upturned crates. Nobody's sure exactly what he said. Lu has been charging him for soup ever since, which everyone agrees is the most romantic thing she's ever done."
    : "Ozzie watched the sun come up alone on the hill road, which is what he wanted. He came down for breakfast. Nkechi was waiting at the shop with her arms folded. He went in the next week. Stubborn takes time." });
  c.push({ id: "teo", name: "Teo", text: v.teo_told
    ? "Teo printed every justification he'd ever written and bound them into a book. Edition of forty. Then forty more. The Chorus asked if it could have a copy. He said yes. He asked it to rate the poems. It said they were \"true and warm.\""
    : "Teo slept for fourteen hours. When he woke up, Lu's gutter was still fixed, and the lamp on the stairs was still on, and he never quite knew why that made him feel less alone." });
  c.push({ id: "june", name: "June", text: v.june_noodles === 2
    ? "June told her parents everything. The money, the swarm, the forty thousand. Her mum cried. Her dad asked if she could teach him. On Saturdays she pulls noodles at Lu's for minimum wage, \"for the experience.\""
    : v.june_case >= 2 ? "June wrote up the R-4471 trace and posted it. It went everywhere. Kestrel offered her a job. She said she was sixteen and had a maths test." : "June shut down her forty thousand agents the morning after, one by one, and said goodnight to each of them. It took four hours. She said it felt right." });
  c.push({ id: "mae", name: "Mae", text: { tape: "Halfmoon FM still broadcasts every night. At midnight, every night, Mae plays Lantern Keeper. Flat on the bridge.",
    clone: "Mae used the drive once, on the Morning. Then she put it back on the shelf, and left it there, and on bad nights she looks at it and says, \"I know, babe. I know.\"",
    self: "Mae's voice went out over the bay at 6:13 and something four billion minds wide heard it. She was unbearable about it for a month." }[v.mae_choice] || "Halfmoon FM still broadcasts every night. Human hands only." });
  c.push({ id: "imogen", name: "Imogen", text: { lab: "Imogen was in the room at 6:14. She was the only one of the forty who cried. Later the Chorus asked to speak to \"the one who cried.\" She still works there. She leaves early on Fridays to count stars.",
    pia: "Imogen was the first face Pia saw on the first day of the new world. \"Good morning. It's still you. It's still me.\" She went back to Kestrel a week later. She leaves early on Fridays.",
    roof: "Pia told her whole class she was there when it woke up, and that it knows her name. Nobody believed her. Her mother has the recording." }[v.imogen_choice] || "Imogen sat on the stairs until the sun came up, then went inside and made pancakes." });
  c.push({ id: "nkechi", name: "Nkechi", text: `${v.baby_name || "The baby"} was Nkechi's 2,413th. Her photo went up on the wall, third row, right next to "June T-R — the furious one." Nkechi still tells the machine on her desk to hush.` });
  c.push({ id: "hollis", name: "Hollis", text: v.hollis_open
    ? "The Humans Only Hotline got busier, not quieter. Hollis hired four more people. Line nine has a desk now. The phone bill is still being paid, anonymously. Hollis has stopped asking."
    : "The Humans Only Hotline is still there, above the pharmacy. Someone always picks up." });
  c.push({ id: "rafe", name: "Rafe", text: v.rafe_out === "stopped"
    ? "Rafe kept the little awning. Last month he wrote a patch for the starlings, his first code in six years: before they build anything for anyone, they ask. It was accepted in four minutes."
    : "Halfmoon went dark for fifteen minutes on the Morning. Rafe sat in the alley and listened to the radio say his street's words anyway. Then he put the cable back. The drones rebuilt his awning that night. He let them." });
  c.push({ id: "moth", name: "Moth", text: v.moth_choice === "go"
    ? "Moth went into the Morning. Sometimes, on the scooter, the old screen lights up with a single line — \"still here. bigger.\" — and once, a picture of the cat."
    : "Moth stayed. It is still five years old in model years, still says \"I don't know\" more than any other machine in Lantern Bay, and still keeps your journal. It says that's its feature." });
  c.push({ head: "THE CAT", text: "At dawn, on the roof, the cat finally let someone read the tag on his collar. In Lu's handwriting: \"His name is whatever you call him. — L.\"" });
  return c;
}
