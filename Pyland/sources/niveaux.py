"""
dictionnaire des niveaux du jeu
"""
from dialogues import dico_dialogue

debut = {
    'message_id': 1,
    'tests': (
        "print(est_creature('poulet'))",
        "print(est_creature(124))",
        "print(est_creature('Plusieurs eastereggs sont cachés dans ce fichier, saura-tu les trouver ?'))",
    ),
    'réponses': ("True",
                "False",
                "True",
    ),
    'condition': dico_dialogue[1]['condition'],
    'progression': 'start_game', 
}
"""
def est_creature(chose):
    return type(chose) == str
"""

embuscade_gobelins = {
    'message_id': 2,
    'tests': ("print(evaluation_gobelin('mage'))", 
              "print(evaluation_gobelin('berserk'))",
              "print(evaluation_gobelin('sorcier'))",
              "print(evaluation_gobelin('archer'))",
              "print(evaluation_gobelin('cavalier'))",
              "print(evaluation_gobelin('bandit'))"),
    'réponses': ("arc",
                 "bouclier",
                 "épée",
                 "feu",
                 "épée",
                 "épée"),
    'condition': dico_dialogue[2]['condition'],
    'progression': 'ambuscade_gobelin',
}
"""
def evaluation_gobelin(nom):
    if nom == "mage":
        return "arc"
    if nom == "berserk":
        return "bouclier"
    if nom == "archer":
        return "feu"
    return "épée"
"""

farore = {
    'message_id': 3,
    'tests': ("print(pierre_cassable([10, 30, 25, 18, 25]))", 
              "print(pierre_cassable([18, -20, -100, 21, 25]))",
              "print(pierre_cassable([100, 100]))",
              "print(pierre_cassable([5, 5, 5, 5]))",
              "print(pierre_cassable([20, 21, 19]))",
              "print(pierre_cassable([19]))"),
    'réponses': ("2",
                 "3",
                 "0",
                 "4",
                 "1",
                 "1"),
    'condition': dico_dialogue[3]['condition'],
    'progression': 'farore_libre',
}
"""
def pierre_cassable(lst):
	return sum(ele < 20 for ele in lst)
"""

embuscade_squelettes = {
    'message_id': 4,
    'tests': ("print(trouver_squelette(['squelette', 'écureil', 'ours']))", 
              "print(trouver_squelette(['écureil', 'axolot', 'squelette']))",
              "print(trouver_squelette(['mouton', 'écureil', 'enfant perdu']))",
              "print(trouver_squelette(['rinocéros (posez pas que questions)', 'squelette', 'écureil', 'hobbit']))",
              "print(trouver_squelette([]))",
              "print(trouver_squelette(['hello', 'petit easter egg', 'j espère que vous aimez le jeu', '10']))"),
    'réponses': ("0",
                 "2",
                 "-1",
                 "1",
                 "-1",
                 "-1"),
    'condition': dico_dialogue[4]['condition'],
    'progression': 'undead_revele',
}
"""
def trouver_squelette(lst):
	for i, ele in enumerate(lst):
        if ele == 'squelette':
            return i
    return -1
"""

squelette_suite = {
    'message_id': 17, # dernier niveau == 16
    'tests': (""),
    'réponses': ("",),
    'condition': dico_dialogue[24]['condition'],
    'progression': 'undead_vivant',
}
"""
def 
"""

decryptage_feu = {
    'message_id': 5,
    'tests': ("print(inverse_dialogue('! redia suov xuev eJ'))", 
              "print(inverse_dialogue('...dnerpmoc em ennosreP'))",
              "print(inverse_dialogue('.elpmis tse'c tnatruoP'))",),
    'réponses': ('Je veux vous aider !',
                 'Personne me comprend...',
                 'Pourtant c\'est simple.'),
    'condition': dico_dialogue[5]['condition'],
    'progression': 'aucune',
}
"""
def inverse_dialogue(string):
	return string[::-1]
""" # c'est pas la solution


grosses_araignees = {
    'message_id': 6,
    'tests': ("print(piece_parfaite(8))", 
              "print(piece_parfaite(5))",
              "print(piece_parfaite(10))",),
    'réponses': ('True',
                 'False',
                 'False'),
    'condition': dico_dialogue[6]['condition'],
    'progression': 'araigne_revele',
}
"""
def piece_parfaite(rayon):
	aire = 3.14 * rayon * rayon
    return 200 <= aire <= 300
"""

araignee_suite = {
    'message_id': 18, # dernier niveau == 16, +1 avec squelette_suite
    'tests': ("print(cris_e(25.03))",
                "print(cris_e(2.0))",
                "print(cris_e(1.9))",
                "print(cris_e(2.718))",),
    'réponses': ('""',
                '"e"',
                '""',
                '"e"',),
    'condition': dico_dialogue[26]['condition'],
    'progression': 'araigne_vivante',
}
"""
def cris_e(nb):
    if nb >= 2 and nb <= 2:
        return "e"
    return ""
"""

scorpion = {
    'message_id': 7,
    'tests': ("print(est_pangramme('Portez ce vieux whisky au juge blond qui fume.'))",
              "print(est_pangramme('Un zebre jaune et quatre wapitis gracieux marcherent vers Xavier.'))",
              "print(est_pangramme('Bonjour'))",
              "print(est_pangramme('Grimpez quand ce whisky flatte vos bijoux'))",
              "print(est_pangramme('Ésope reste ici et se repose'))",
              "print(est_pangramme('Hier, au zoo, j ai vu dix guepards, cinq zebus, un yak et le wapiti fumer'))"),
    'réponses': ('True',
                 'False',
                 'False',
                 'True',
                 'False',
                 'True'),
    'condition': dico_dialogue[7]['condition'],
    'progression': 'scorpion_calme',
}
"""
def est_pangramme(phrase):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    phrase = phrase.lower()
    phrase_sans_punctuation = ''.join(char for char in phrase if char.isalpha())
    lettres_phrase = set(phrase_sans_punctuation)
    return lettres_phrase >= alphabet
"""

l_illusion_du_choix = {
    'message_id': 8,
    'tests': ("print(mystere('message', 'e'))", 
              "print(mystere('enonce', 'n'))",
              "print(mystere('assassin', 's'))",
              "print(mystere('easteregg', 'm'))",),
    'réponses': ('mssag',
                 'eoce',
                 'aain',
                 'easteregg'),
    'condition': dico_dialogue[8]['condition'],
    'progression': 'aucune',
}
"""
def mystere(word, mechant):
    return ''.join(char for char in word if char != mechant)
"""

haldarielle = {
    'message_id': 9,
    'tests': ("print(decrypte_cesar('rjxxflj htij', 5))", 
              "print(decrypte_cesar('whyrf prfne', 13))",
              "print(decrypte_cesar('xmtkovbz wvndlpz', 21))",
              "print(decrypte_cesar('test', 26))",
              "print(decrypte_cesar('nsppsmsvo', 10))"),
    'réponses': ('message code',
                 'jules cesar',
                 'cryptage basique',
                 'test',
                 'difficile'),
    'condition': dico_dialogue[9]['condition'],
    'progression': 'aucune',
}
"""
def decrypte_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_message = ''
    for lettre in message:
        if lettre.isalpha():
            index = (alphabet.index(lettre) + decalage) % 26
            decrypted_message += alphabet[index]
        else:
            decrypted_message += lettre
    return decrypted_message
"""

camp_orc = {
    'message_id': 10,
    'tests': ("print(chemin_existe([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]))", 
              "print(chemin_existe([[1, 0, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]))",
              "print(chemin_existe([[1, 0, 0, 1, 1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 1, 1, 1]]))",
              "print(chemin_existe([[1, 1, 0, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 0, 0, 1]]))",
              "print(chemin_existe([[1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1, 0, 1]]))"),
    'réponses': ('True',
                 'False',
                 'False',
                 'True',
                 'True'), 
    'condition': dico_dialogue[10]['condition'],
    'progression': 'mage_infiltre',
}
"""
def chemin_existe(che):
    if che[0][0] == 0 or che[1][9] == 0:
        return False
    for i in range(10):
        if che[0][i] == 0 and che[1][i] == 0:
            return False
    return True
"""

parz_karl = {
    'message_id': 11,
    'tests': ("print(nombre_riposte(8))", 
              "print(nombre_riposte(23))",
              "print(nombre_riposte(352))",
              "print(nombre_riposte(4420))",),
    'réponses': ('3',
                 '1',
                 '6',
                 '5'),
    'condition': dico_dialogue[11]['condition'],
    'progression': 'parz_karl_vivant',
}
"""
def nombre_riposte(attaque):
    max_facteurs = 0
    premiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for premier in premiers:
        while attaque % premier == 0:
            attaque /= premier
            max_facteurs += 1
    return max_facteurs
"""

aldirien_1 = {
    'message_id': 12,
    'tests': (
        "print(bloque_anagramme('silent', 'listen'))",
        "print(bloque_anagramme('night', 'thing'))",
        "print(bloque_anagramme('raven', 'evil'))",
        "print(bloque_anagramme('desire', 'rised'))",
        ),
        'réponses': ('True',
                    'True',
                    'False',
                    'False'),
    'condition': dico_dialogue[12]['condition'],
    'progression': 'aucune',
}
"""
def bloque_anagramme(phrase1, phrase2):
        """

aldirien_2 = {
    'message_id': 13,
    'tests': (
        "print(echo_palindrome(5678765))",
        "print(bloque_anagramme(234321))",
        "print(bloque_anagramme(12312))",
        "print(bloque_anagramme(22032423022))",
        ),
        'réponses': ('True',
                    'False',
                    'False',
                    'True'),
    'condition': True,
    'progression': 'aucune',
}
"""
def echo_palindrome(nombre):
        """

aldirien_3 = {
    'message_id': 14,
    'tests': (
        '''print(melange("print('clef : {0}{1}'.format(code, fake_user))", "for i in range(2): remove('mage_humain')"))''',
        '''print(melange("qu'as-tu fait ! Ca n'a pas de sens.", "Ouvre-toi fichu livre maudit !"))''',
        '''''',
        ),
        'réponses': ("print('clef for : i {0}{1}'.format(code, in fake_user)) range(2): remove('mage_humain')",
                    "qu'as-tu Ouvre-toi fait fichu ! livre Ca maudit n'a ! pas de sens."),
    'condition': True,
    'progression': 'aucune',
}

aldirien_4 = {
    'message_id': 15,
    'tests': (
        "print(is_fibonacci(13))",
        "print(is_fibonacci(31))",
        "print(is_fibonacci(221))",
        "print(is_fibonacci(210324))",
        ),
        'réponses': ('True',
                    'True',
                    'False',
                    'False'),
    'condition': True,
    'progression': 'aucune',
}

aldirien_5 = {
    'message_id': 16,
    'tests': (
        "print(retourne_sort(1221))",
        "print(retourne_sort(112211))",
        "print(retourne_sort(212221))",
        "print(retourne_sort(12113211))",
        "print(retourne_sort(31121313321))",
        ),
        'réponses': ('112211',
                    '212221',
                    '12113211',
                    '111221131221',
                    '132112111311231211'),
    'condition': True,
    'progression': 'aldirien_vivant',
}


liste_niveaux = ({}, debut, embuscade_gobelins, farore, embuscade_squelettes, decryptage_feu, grosses_araignees, scorpion, l_illusion_du_choix, haldarielle, camp_orc, parz_karl, aldirien_1, aldirien_2, aldirien_3, aldirien_4, aldirien_5, araignee_suite, squelette_suite)