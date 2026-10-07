# boss_mini.py

# Security Audit: The hardcoded secret and cheat code need to be removed for security.
# BONUS FIX: The SECRET_CODE variable and its cheat logic block were entirely removed.

p_hp = 50
b_hp = 50

# Attack Logic: The boss needs to lose 10 HP every time the player attacks.
# BONUS FIX: Added `b_hp -= 10` so the boss actually takes damage.
def attack():
    global b_hp
    b_hp -= 10
    print("You deal 10 damage!")

# Healing Guardrails: Add checks so HP cannot go above 50 or heal when the player is at 0 HP.
# BONUS FIX: Added conditional checks to prevent zombie healing and over-healing.
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > 50:
        p_hp = 50
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    
    # Security Audit: Removed the '[c]heat' option from the prompt
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

# Win Condition: When the boss reaches 0 HP, print "Victory!" and stop the game loop.
    # BONUS FIX: Added check to see if b_hp reaches 0 to print "Victory!" and terminate the loop.
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
