import random
import time
import os

targets = [
    "Ali",
    "Sanya",
    "Amir Abass",
    "Mehrab",
    "Yashar",
    "Arad",
    "Yashar(KhanAli)",
    "Amir Reza",
    "Mehrdad",
    "Sam",
    "All"
]

def clear():
    os.system("clear")

def fake_codes(name):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    print(f"\n[+] {name} Is Fund")
    print("[+] Generating fake data...\n")

    for _ in range(25):
        code = ''.join(random.choice(chars) for _ in range(random.randint(10, 25)))
        print(f"{name.upper()}{code}")
        time.sleep(0.04)

    print("\n[!] DEMO COMPLETE - NO REAL DATA ACCESSED")

while True:
    clear()

    print("╔════════════════════════════════╗")
    print("║       FAKE HACKING DEMO        ║")
    print("╚════════════════════════════════╝\n")

    print("What your target?\n")

    for i, target in enumerate(targets, 1):
        print(f"{i}. {target}")

    print("12. exit")

    try:
        choice = int(input("\nSelect: "))
    except ValueError:
        continue

    if choice == 12:
        print("\nExiting...")
        break

    if 1 <= choice <= 11:
        if choice == 11:
            for target in targets:
                fake_codes(target)
        else:
            fake_codes(targets[choice - 1])

        input("\nPress Enter to continue...")
