import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

#Input combat strength hero
combatStrength = int(input("Enter your combat strength(1-6): "))
if combatStrength < 1 or combatStrength > 6:
    print("Invalid input. Combat strength should be between 1 and 6.")
    combatStrength = 1 # Default value for invalid value

#Input combat strength for the monster
mCombatStrength = int(input("Enter the monster's combat strength(1-6): "))
if mCombatStrength < 1 or mCombatStrength > 6:
    print("Invalid input. Monster combat strength should be between 1 and 6.")
    mCombatStrength = 1 # Default value for invalid value

# Simulate Battle rounds 
for j in range(1, 21, 2): # Stimulation of 20 rounds, steppibg by 20
    # Dice roll for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

# Calculate the weapons
    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon= weapons[monsterRoll - 1]

# Calculate total strength
    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    # Print round results
    print(f"\nRound {j} Hero rolled {heroRoll}, and Monster rolled {monsterRoll}")
    print(f"Hero selected {heroWeapon} and Monster selected {monsterWeapon}")
    print(f"Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")

# Determine the winner
    if heroTotal > monsterTotal:
        print("Hero wins the round!")
    elif heroTotal < monsterTotal:
        print("Monster wins the round!")
    else:
        print("It's a tie round!")

    if j == 11:
        print("\n Battle Truce declread in Round 11. Game Over!")
        break
    if j != 11:
        print("\n Battle conluded after 20 rounds!")