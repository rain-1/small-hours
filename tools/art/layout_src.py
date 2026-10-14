"""Source of truth for game/data/layout.json (interaction regions + figure spots).

  python3 tools/art/layout_src.py   # writes game/data/layout.json

Hotspots are [x, y, w, h]; figures are [x_center, y_feet] for a ~110px figure.
"occluders" (optional) are rects the engine may redraw over figures (e.g. the
shop counter in front of Lu).
"""
import json, os

L = {
    "street": {
        "hotspots": {
            "shop_door": [274, 206, 52, 62],
            "laundromat_door": [8, 204, 108, 64],
            "alley": [122, 128, 30, 104],
            "hotline_door": [352, 144, 104, 52],
            "clinic_door": [486, 204, 64, 64],
            "stairs_up": [570, 140, 70, 128],
            "car": [18, 266, 136, 68],
            "vending": [340, 222, 28, 48],
            "cat": [127, 233, 28, 22],
            "kiosk": [458, 210, 14, 60],
            "mural": [368, 210, 88, 58],
            "water_tower": [578, 6, 58, 86],
        },
        "figures": {},
    },
    "shop": {
        "hotspots": {
            "ticket_rail": [196, 146, 130, 26],
            "tv": [138, 50, 70, 68],
            "clock": [244, 34, 36, 44],
            "lucky_cat": [189, 235, 28, 38],
            "photo": [297, 101, 32, 40],
            "radio": [336, 110, 50, 34],
            "back_door": [528, 104, 64, 168],
            "pot": [384, 180, 72, 56],
            "front_door": [22, 106, 86, 220],
            "stools": [186, 306, 394, 42],
        },
        "figures": {"lu": [300, 318], "guest": [470, 346]},
        "occluders": {"counter": [136, 272, 478, 54]},
    },
    "teo_room": {
        "hotspots": {
            "monitors": [168, 150, 224, 72],
            "plant": [424, 138, 62, 98],
            "mugs": [160, 222, 250, 15],
            "bookshelf": [98, 40, 60, 260],
            "pinboard": [166, 36, 104, 80],
            "window": [486, 44, 92, 150],
            "door": [14, 152, 78, 148],
        },
        "figures": {"teo": [262, 338]},
    },
    "stairs": {
        "hotspots": {
            "shrine": [220, 156, 66, 82],
            "prayer_box": [237, 239, 32, 23],
            "vending": [357, 148, 48, 114],
            "pia_window": [446, 56, 72, 72],
            "lamp": [325, 112, 30, 150],
            "up": [570, 92, 70, 72],
            "down": [0, 284, 110, 76],
        },
        "figures": {"imogen": [442, 262], "cat": [292, 262]},
    },
    "roofs": {
        "hotspots": {
            "radio_shack": [120, 130, 140, 172],
            "records": [258, 272, 66, 34],
            "june_rig": [480, 190, 156, 112],
            "seed_library": [326, 174, 108, 98],
            "view": [300, 14, 160, 158],
            "water_tower": [42, 0, 136, 128],
            "ladder": [10, 284, 60, 76],
        },
        "figures": {
            "mae": [224, 322], "june": [514, 300],
            "gathering1": [300, 338], "gathering2": [362, 346],
            "gathering3": [424, 336], "gathering4": [140, 344],
        },
    },
    "clinic": {
        "hotspots": {
            "desk": [4, 212, 176, 98],
            "coffee": [182, 172, 40, 128],
            "baby_photos": [232, 30, 176, 158],
            "labour_door": [438, 88, 106, 212],
            "chairs": [234, 236, 168, 64],
            "posters": [548, 64, 40, 144],
            "exit": [596, 72, 44, 228],
        },
        "figures": {"nkechi": [420, 336], "dev": [300, 334]},
    },
    "hotline": {
        "hotspots": {
            "phones": [178, 226, 300, 26],
            "switchboard": [210, 48, 244, 104],
            "notes_wall": [476, 34, 112, 182],
            "kettle": [494, 218, 90, 32],
            "window": [16, 52, 124, 142],
            "sofa": [0, 226, 156, 78],
            "exit": [590, 92, 46, 208],
        },
        "figures": {"hollis": [392, 340]},
    },
    "alley": {
        "hotspots": {
            "junction_box": [32, 166, 110, 130],
            "steam_vent": [476, 200, 48, 80],
            "drone_roost": [418, 88, 170, 74],
            "crates": [410, 236, 58, 60],
            "graffiti": [178, 128, 140, 162],
            "back_door": [347, 152, 56, 144],
            "exit": [566, 40, 74, 256],
        },
        "figures": {"rafe": [180, 332]},
    },
    "hill_road": {
        "hotspots": {
            "car": [32, 192, 270, 148],
            "view": [310, 30, 330, 226],
            "guardrail": [302, 258, 338, 42],
        },
        "figures": {"ozzie": [420, 336]},
    },
    "map": {
        "hotspots": {
            "shop": [246, 150, 50, 46],
            "laundromat": [104, 182, 46, 40],
            "clinic": [412, 160, 44, 40],
            "hotline": [318, 146, 46, 48],
            "alley": [278, 124, 24, 42],
            "stairs": [496, 120, 80, 92],
            "roofs": [420, 34, 110, 86],
        },
        "figures": {},
    },
}
L["roofs_dawn"] = json.loads(json.dumps(L["roofs"]))

out = os.path.join(os.path.dirname(__file__), "..", "..", "game", "data", "layout.json")
with open(out, "w") as f:
    f.write("{\n" + ",\n".join(f'  "{k}": ' + json.dumps(v, separators=(", ", ": ")) for k, v in L.items()) + "\n}\n")
print("wrote", os.path.normpath(out))
