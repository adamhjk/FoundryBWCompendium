#!/usr/bin/env python3
"""
Generate Burning Wheel armor compendium entries for Foundry VTT
"""

import json
import random
import string

def generate_id(length=16):
    """Generate a unique 16-character alphanumeric ID"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Armor type definitions
ARMOR_TYPES = [
    {
        "name": "Gambeson",
        "dice": 1,
        "base_cost": 3,
        "description": "Gambesons are cloth, padded armor and thin, boiled leather. This armor was cheap, easy to make and effective when enough was worn.",
        "untrained": "none",
        "penalties": {
            "agilityPenalty": 0,
            "speedObPenalty": 0,
            "speedDiePenalty": 0,
            "climbingPenalty": 0,
            "healthFortePenalty": 0,
            "throwingShootingPenalty": 0,
            "stealthyPenalty": 0,
            "swimmingPenalty": 0,
            "perceptionObservationPenalty": 0
        },
        "img": "icons/equipment/chest/breastplate-layered-leather-brown.webp"
    },
    {
        "name": "Reinforced Leather",
        "dice": 2,
        "base_cost": 6,
        "description": "Reinforced leather was boiled and reinforced with metal rings, small plates or lamellar. This was probably the most popular armor for foot soldiers worldwide. It was fairly cheap and very effective; it can stop all but the most powerful blows.",
        "untrained": "none",
        "penalties": {
            "agilityPenalty": 1,
            "speedObPenalty": 0,
            "speedDiePenalty": 0,
            "climbingPenalty": 0,
            "healthFortePenalty": 1,
            "throwingShootingPenalty": 0,
            "stealthyPenalty": 0,
            "swimmingPenalty": 1,
            "perceptionObservationPenalty": 0
        },
        "img": "icons/equipment/chest/breastplate-leather-studded-brown.webp"
    },
    {
        "name": "Light Mail",
        "dice": 3,
        "base_cost": 10,
        "description": "Light mail is either a light chain shirt or a heavy gambeson with a coat of metal plates sewn into the cloth. It's light, flexible and concealable.",
        "untrained": "light",
        "penalties": {
            "agilityPenalty": 1,
            "speedObPenalty": 1,
            "speedDiePenalty": 1,
            "climbingPenalty": 0,
            "healthFortePenalty": 1,
            "throwingShootingPenalty": 1,
            "stealthyPenalty": 1,
            "swimmingPenalty": 1,
            "perceptionObservationPenalty": 0
        },
        "img": "icons/equipment/chest/breastplate-scale-grey.webp"
    },
    {
        "name": "Heavy Mail",
        "dice": 4,
        "base_cost": 15,
        "description": "Interlocking rings form a shirt, hood, sleeves, skirt and leggings all worn over leather or cloth padding—which provides protection from impact (and from the armor itself). More often than not, the chain is covered by a decorative outer layer of cloth as well. Heavy mail is versatile, effective, heavy and expensive.",
        "untrained": "heavy",
        "penalties": {
            "agilityPenalty": 2,
            "speedObPenalty": 1,
            "speedDiePenalty": 1,
            "climbingPenalty": 1,
            "healthFortePenalty": 1,
            "throwingShootingPenalty": 2,
            "stealthyPenalty": 1,
            "swimmingPenalty": 2,
            "perceptionObservationPenalty": 0
        },
        "img": "icons/equipment/chest/breastplate-chainmail-iron.webp"
    },
    {
        "name": "Plated Mail",
        "dice": 5,
        "base_cost": 20,
        "description": "Using the same basic kit as heavy mail, certain areas are reinforced with hard metal plates; usually a breast and back plate, as well as arm and leg greaves. This armor is extraordinarily expensive and very effective.",
        "untrained": "plate",
        "penalties": {
            "agilityPenalty": 2,
            "speedObPenalty": 1,
            "speedDiePenalty": 1,
            "climbingPenalty": 1,
            "healthFortePenalty": 2,
            "throwingShootingPenalty": 2,
            "stealthyPenalty": 2,
            "swimmingPenalty": 2,
            "perceptionObservationPenalty": 0
        },
        "img": "icons/equipment/chest/breastplate-helmet-steel.webp"
    },
    {
        "name": "Full Plate",
        "dice": 6,
        "base_cost": 50,
        "description": "This is the Cadillac and armored tank of the Middle Ages rolled into one. It is the most frequently depicted armor in cinematic recreations of the Middle Ages—though its historical lifespan was actually rather short. This is the stuff of the knights in shining armor. It is rare, heavy, powerful and hideously expensive to maintain.",
        "untrained": "plate",
        "penalties": {
            "agilityPenalty": 1,
            "speedObPenalty": 1,
            "speedDiePenalty": 1,
            "climbingPenalty": 1,
            "healthFortePenalty": 2,
            "throwingShootingPenalty": 1,
            "stealthyPenalty": 1,
            "swimmingPenalty": 3,
            "perceptionObservationPenalty": 0
        },
        "img": "icons/equipment/chest/breastplate-collared-steel-grey.webp"
    }
]

# Helmet definitions
HELMETS = [
    {
        "name": "Leather Hood",
        "dice": 1,
        "base_cost": 2,
        "description": "A simple leather hood or skull cap that provides minimal protection.",
        "perceptionPenalty": 0,
        "img": "icons/equipment/head/hood-leather-brown.webp"
    },
    {
        "name": "Light Helmet",
        "dice": 2,
        "base_cost": 3,
        "description": "A light helmet or pot helm that covers the head.",
        "perceptionPenalty": 1,
        "img": "icons/equipment/head/helm-barbute-scaled-grey.webp"
    },
    {
        "name": "Spangenhelm",
        "dice": 3,
        "base_cost": 5,
        "description": "A segmented helmet with an open face design.",
        "perceptionPenalty": 1,
        "img": "icons/equipment/head/helm-barbute-studded-steel.webp"
    },
    {
        "name": "Open-faced Bascinet",
        "dice": 4,
        "base_cost": 8,
        "description": "A well-crafted helmet with an open face or barbute design.",
        "perceptionPenalty": 2,
        "img": "icons/equipment/head/helm-masked-steel-grey.webp"
    },
    {
        "name": "Closed Bascinet",
        "dice": 5,
        "base_cost": 13,
        "description": "A closed-face helmet such as a sallet or closed bascinet.",
        "perceptionPenalty": 2,
        "img": "icons/equipment/head/helm-full-steel.webp"
    },
    {
        "name": "Great Helm",
        "dice": 6,
        "base_cost": 25,
        "description": "A massive great helm that fully encloses the head.",
        "perceptionPenalty": 3,
        "img": "icons/equipment/head/helm-great-steel-grey.webp"
    }
]

# Shield definitions
SHIELDS = [
    {
        "name": "Buckler",
        "dice": 1,
        "base_cost": 2,
        "description": "A small buckler shield used for parrying.",
        "img": "icons/equipment/shield/buckler-wooden-boss-brown.webp"
    },
    {
        "name": "Target Shield",
        "dice": 2,
        "base_cost": 4,
        "description": "A medium-sized round target shield.",
        "img": "icons/equipment/shield/round-wooden-boss-steel.webp"
    },
    {
        "name": "Heater Shield",
        "dice": 3,
        "base_cost": 6,
        "description": "A large heater-style shield providing substantial protection.",
        "img": "icons/equipment/shield/heater-steel-worn-blue.webp"
    },
    {
        "name": "Great Shield",
        "dice": 4,
        "base_cost": 8,
        "description": "A massive shield that provides excellent protection at the cost of mobility.",
        "img": "icons/equipment/shield/kite-steel-grey.webp"
    }
]

# Quality modifiers
QUALITIES = {
    "poor": {
        "prefix": "Poor",
        "quality": "poor",
        "cost_mult": 0.5,
        "desc_suffix": " This is poor quality and will fall apart quickly—all 1s rolled count for losing armor dice."
    },
    "run of the mill": {
        "prefix": "",
        "quality": "run of the mill",
        "cost_mult": 1.0,
        "desc_suffix": ""
    },
    "superior": {
        "prefix": "Superior",
        "quality": "superior",
        "cost_mult": 4.0,
        "desc_suffix": " This is superior quality—only the first 1 counts and is rerolled; if that die comes up a 1 again, an armor die is lost."
    }
}

def calculate_cost(base_cost, quality_key):
    """Calculate cost with quality modifier, rounding up for poor quality"""
    mult = QUALITIES[quality_key]["cost_mult"]
    cost = base_cost * mult
    if quality_key == "poor":
        return int(cost + 0.5)  # Round up
    return int(cost)

def create_armor_entry(armor_type, quality_key):
    """Create a full armor suit entry"""
    quality = QUALITIES[quality_key]
    name_parts = []
    if quality["prefix"]:
        name_parts.append(quality["prefix"])
    name_parts.append(armor_type["name"])
    name = " ".join(name_parts)

    description = armor_type["description"] + quality["desc_suffix"]

    return {
        "_id": generate_id(),
        "name": name,
        "type": "armor",
        "img": armor_type["img"],
        "system": {
            "pointCost": calculate_cost(armor_type["base_cost"], quality_key),
            "quality": quality["quality"],
            "dice": armor_type["dice"],
            "hasHelm": True,
            "damageHelm": 0,
            "hasTorso": True,
            "damageTorso": 0,
            "hasLeftArm": True,
            "damageLeftArm": 0,
            "hasRightArm": True,
            "damageRightArm": 0,
            "hasLeftLeg": True,
            "damageLeftLeg": 0,
            "hasRightLeg": True,
            "damageRightLeg": 0,
            "hasShield": False,
            "damageShield": 0,
            "description": description,
            "equipped": True,
            "untrainedPenalty": armor_type["untrained"],
            **armor_type["penalties"],
            "shade": "B"
        },
        "effects": [],
        "folder": None,
        "flags": {},
        "ownership": {
            "default": 0
        }
    }

def create_helmet_entry(helmet_type, quality_key):
    """Create a helmet entry"""
    quality = QUALITIES[quality_key]
    name_parts = []
    if quality["prefix"]:
        name_parts.append(quality["prefix"])
    name_parts.append(helmet_type["name"])
    name = " ".join(name_parts)

    description = helmet_type["description"] + quality["desc_suffix"]

    return {
        "_id": generate_id(),
        "name": name,
        "type": "armor",
        "img": helmet_type["img"],
        "system": {
            "pointCost": calculate_cost(helmet_type["base_cost"], quality_key),
            "quality": quality["quality"],
            "dice": helmet_type["dice"],
            "hasHelm": True,
            "damageHelm": 0,
            "hasTorso": False,
            "damageTorso": 0,
            "hasLeftArm": False,
            "damageLeftArm": 0,
            "hasRightArm": False,
            "damageRightArm": 0,
            "hasLeftLeg": False,
            "damageLeftLeg": 0,
            "hasRightLeg": False,
            "damageRightLeg": 0,
            "hasShield": False,
            "damageShield": 0,
            "description": description,
            "equipped": True,
            "untrainedPenalty": "none",
            "agilityPenalty": 0,
            "speedObPenalty": 0,
            "speedDiePenalty": 0,
            "climbingPenalty": 0,
            "healthFortePenalty": 0,
            "throwingShootingPenalty": 0,
            "stealthyPenalty": 0,
            "swimmingPenalty": 0,
            "perceptionObservationPenalty": helmet_type["perceptionPenalty"],
            "shade": "B"
        },
        "effects": [],
        "folder": None,
        "flags": {},
        "ownership": {
            "default": 0
        }
    }

def create_shield_entry(shield_type, quality_key):
    """Create a shield entry"""
    quality = QUALITIES[quality_key]
    name_parts = []
    if quality["prefix"]:
        name_parts.append(quality["prefix"])
    name_parts.append(shield_type["name"])
    name = " ".join(name_parts)

    description = shield_type["description"] + quality["desc_suffix"]

    return {
        "_id": generate_id(),
        "name": name,
        "type": "armor",
        "img": shield_type["img"],
        "system": {
            "pointCost": calculate_cost(shield_type["base_cost"], quality_key),
            "quality": quality["quality"],
            "dice": shield_type["dice"],
            "hasHelm": False,
            "damageHelm": 0,
            "hasTorso": False,
            "damageTorso": 0,
            "hasLeftArm": False,
            "damageLeftArm": 0,
            "hasRightArm": False,
            "damageRightArm": 0,
            "hasLeftLeg": False,
            "damageLeftLeg": 0,
            "hasRightLeg": False,
            "damageRightLeg": 0,
            "hasShield": True,
            "damageShield": 0,
            "description": description,
            "equipped": True,
            "untrainedPenalty": "none",
            "agilityPenalty": 0,
            "speedObPenalty": 0,
            "speedDiePenalty": 0,
            "climbingPenalty": 0,
            "healthFortePenalty": 0,
            "throwingShootingPenalty": 0,
            "stealthyPenalty": 0,
            "swimmingPenalty": 0,
            "perceptionObservationPenalty": 0,
            "shade": "B"
        },
        "effects": [],
        "folder": None,
        "flags": {},
        "ownership": {
            "default": 0
        }
    }

def generate_all_entries():
    """Generate all armor, helmet, and shield entries"""
    entries = []

    # Generate full armor suits
    for armor_type in ARMOR_TYPES:
        for quality_key in ["poor", "run of the mill", "superior"]:
            entries.append(create_armor_entry(armor_type, quality_key))

    # Generate helmets
    for helmet_type in HELMETS:
        for quality_key in ["poor", "run of the mill", "superior"]:
            entries.append(create_helmet_entry(helmet_type, quality_key))

    # Generate shields
    for shield_type in SHIELDS:
        for quality_key in ["poor", "run of the mill", "superior"]:
            entries.append(create_shield_entry(shield_type, quality_key))

    return entries

def write_db_file(entries, filename):
    """Write entries to a NeDB file (JSON-lines format)"""
    with open(filename, 'w') as f:
        for entry in entries:
            json.dump(entry, f, separators=(',', ':'))
            f.write('\n')

if __name__ == "__main__":
    print("Generating Burning Wheel armor compendium...")

    entries = generate_all_entries()

    print(f"Generated {len(entries)} entries:")
    print(f"  - {len(ARMOR_TYPES) * 3} full armor suits")
    print(f"  - {len(HELMETS) * 3} helmets")
    print(f"  - {len(SHIELDS) * 3} shields")

    output_file = "packs/armor.db"
    write_db_file(entries, output_file)

    print(f"\nArmor compendium written to: {output_file}")
    print("Done!")
