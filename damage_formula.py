import random as rand

# FUNZIONE CHE SERVE PER CALCOLARE IL DANNO

# [ attacco * (potenza attacco * 0.3) ] - [ difesa del nemico + (valore tra 1 a 7) ]

def damage_formula(atk,skill_atk,defn):
    return [atk * (skill_atk * 0.3)] - [defn + rand.randrange(1,8)]