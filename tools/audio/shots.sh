# name source maxdur fadeout gate
P="$HOME/Code/Eidoverse/comfy-env/bin/python /tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/scripts/proc.py shot"
R=/tmp/claude-1000/-home-riv-Code-claude-game/079066a0-8d3e-4e7b-9d93-b973c06998eb/scratchpad/audio_raw; S=/home/riv/Code/claude-game/game/audio/sfx
while read n src md fo g; do $P $R/$src.mp3 $S/$n.mp3 --br 128k --maxdur $md --fadeout $fo --gate $g; done <<'EOT'
door_bell door_bell_a 3 0.4 -55
footsteps_stairs footsteps_stairs_a 2.2 0.1 -40
scooter scooter_a 4 0.5 -40
phone_ring phone_ring2_a 5.6 0.4 -50
radio_static radio_static_a 2.2 0.2 -40
starlings starlings_b 4.5 0.6 -40
cat_meow cat_meow2_a 1.5 0.08 -45
cat_purr cat_purr_a 3.2 0.4 -40
heart_monitor heart_monitor_b 4.2 0.2 -40
baby_cry baby_cry_b 5.5 0.5 -40
car_engine car_engine_b 4.5 0.5 -40
cassette cassette_a 2.5 0.1 -40
paper paper_a 2 0.15 -40
train train_a 6.5 0.6 -40
bowl bowl_b 1.2 0.2 -40
slurp slurp_a 2.5 0.2 -40
thunder thunder_b 5.5 1.2 -60
power_down power_down_b 3.2 0.3 -40
crowd_cheer_far crowd_cheer_far_b 5.5 0.8 -40
kettle kettle_a 3.5 0.4 -55
EOT
