MAX_MP = 200
MAX_HP = 100


def cast_spell(heroes, hero, mp_needed, spell_name):
    if heroes[hero]['mp'] >= mp_needed:
        heroes[hero]['mp'] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")

    return heroes


def take_damage(heroes, hero, dmg, attacker):
    if heroes[hero]['hp'] - dmg > 0:
        heroes[hero]['hp'] -= dmg
        print(f"{hero} was hit for {dmg} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
    elif heroes[hero]['hp'] - dmg <= 0:
        print(f"{hero} has been killed by {attacker}!")
        del heroes[hero]

    return heroes


def recharge(heroes, hero, amount):
    amount_recovered = 0
    if heroes[hero]['mp'] + amount >= MAX_MP:
        amount_recovered = MAX_MP - heroes[hero]['mp']
        heroes[hero]['mp'] = MAX_MP

    elif heroes[hero]['mp'] + amount < MAX_MP:
        heroes[hero]['mp'] += amount
        amount_recovered = amount

    print(f"{hero} recharged for {amount_recovered} MP!")
    return heroes


def heal(heroes, hero, amount):
    amount_recovered = 0
    if heroes[hero]['hp'] + amount >= MAX_HP:
        amount_recovered = MAX_HP - heroes[hero]['hp']
        heroes[hero]['hp'] = MAX_HP


    elif heroes[hero]['hp'] + amount < MAX_HP:
        heroes[hero]['hp'] += amount
        amount_recovered = amount

    print(f"{hero} healed for {amount_recovered} HP!")
    return heroes


heroes_dict = dict()
commands = []

total_heroes = int(input())

for _ in range(total_heroes):
    name, hp, mp = input().split(' ')
    heroes_dict[name] = {'hp': int(hp), 'mp': int(mp)}

while True:
    command = input()
    if command == 'End':
        break

    commands.append(command.split(' - '))

for actions in commands:
    action, hero = actions[0], actions[1]

    if action == 'CastSpell':
        spell_name = actions[3]
        needed_mp = int(actions[2])

        heroes_dict = cast_spell(heroes_dict, hero, needed_mp, spell_name)

    elif action == 'TakeDamage':
        damage = int(actions[2])
        the_attacker = actions[3]

        heroes_dict = take_damage(heroes_dict, hero, damage, the_attacker)

    elif action == 'Recharge':
        mp_amount = int(actions[2])

        heroes_dict = recharge(heroes_dict, hero, mp_amount)


    elif action == 'Heal':
        hp_amount = int(actions[2])

        heroes_dict = heal(heroes_dict, hero, hp_amount)

for hero, items in heroes_dict.items():
    hp, mp = items['hp'], items['mp']
    print(f'{hero}\n  HP: {hp}\n  MP: {mp}')

