// SMALL HOURS — globals
// Line conventions (parsed by the engine):
//   @id:mood Text      spoken line with portrait (mood optional)
//   @you Text          the player speaks
//   @chorus / @radio / @phone / @sign   special voices
//   plain text         narration
// Tags: #go:scene #sfx:name #music:name #amb:name #fx:flicker|flash|dawn|dark #wait #end

VAR name = "Kit"
VAR time = 0            // minutes after 9:00 pm. 6:14 am = 554
VAR act = 0             // 0 prologue, 1..3 acts, 4 finale
VAR here = "shop"       // engine keeps this updated
VAR past = ""           // the player's backstory flavour

// orders: 0 none, 1 carrying, 2 delivered
VAR o_ozzie = 0
VAR o_teo = 0
VAR o_clinic = 0
VAR o_hotline = 0
VAR o_roof = 0
VAR o_tea = 0
VAR o_ludd = 0
VAR o_ice = 0

LIST noticed = cat_lu, cat_ozzie, cat_june, cat_teo, cat_mae, cat_nkechi, cat_hollis, cat_rafe, cat_imogen, cat_moth, k_gutter, k_tickets, k_lullaby, k_phonebill, k_lamp, k_seeds, k_awning, patent, clock, photo, lucky_cat, tv, rater_id, gerald, chapbook, imogen_voice, pia_stars, prayers, fortune, mural, kiosk, graffiti, records, iris_drive, cassette, june_photo, notes_wall, dev_lanyard, autopilot, kestrel_view, seed_names, dialect, drone_roost, sunrise_soda, pinboard, junction

LIST words = w_lu, w_teo, w_ozzie, w_june, w_mae, w_imogen, w_nkechi, w_hollis, w_rafe, w_moth, w_cat

// people
VAR teo_rated = false
VAR teo_told = false
VAR ozzie_heart = false
VAR ozzie_ride = false
VAR ozzie_clinic = false
VAR ozzie_lu = false
VAR june_case = 0       // 1 asked to look, 2 traced to Teo
VAR june_noodles = 0    // 1 invited, 2 done
VAR mae_met = false
VAR song_req = 0        // 1 heard request, 2 played
VAR mae_tape = 0        // 1 carrying, 2 given
VAR mae_choice = ""     // tape, clone, self
VAR imogen_met = false
VAR imogen_choice = ""  // lab, pia, roof
VAR dev_calm = false
VAR hollis_cover = false
VAR hollis_open = false
VAR rafe_met = false
VAR rafe_out = ""       // cut, stopped
VAR rafe_helped = false
VAR lu_patent = false
VAR recipe = false
VAR baby_name = ""
VAR mural_add = ""
VAR moth_go = 0
VAR moth_stay = 0
VAR moth_deep = 0
VAR moth_choice = ""    // go, stay
VAR reply_tone = ""
VAR msg_closing = ""
VAR cat_pets = 0

=== function notice(x)
{ noticed !? x:
    ~ noticed += x
}

=== function give_word(x)
{ words !? x:
    ~ words += x
}

=== function pass(m)
~ time = time + m
{ act < 4 && time > 505:
    ~ time = 505
}

=== function kindness()
~ return LIST_COUNT(noticed ^ (k_gutter, k_tickets, k_lullaby, k_phonebill, k_lamp, k_seeds, k_awning))

=== function cat_names()
~ return LIST_COUNT(noticed ^ (cat_lu, cat_ozzie, cat_june, cat_teo, cat_mae, cat_nkechi, cat_hollis, cat_rafe, cat_imogen, cat_moth))

=== function act1_done()
~ return o_ozzie == 2 && o_teo == 2 && o_clinic == 2 && o_hotline == 2

=== function act2_done()
~ return o_roof == 2 && o_tea == 2 && o_ludd == 2 && o_ice == 2

=== done ===
-> DONE
