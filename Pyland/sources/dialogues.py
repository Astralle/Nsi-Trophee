"""
contiens une liste de dictionnaires répértoriant chaque dialogue
"""

# imports
# =======
from constantes import dico_saved_var

# constants

# suite à un manque de temps, nous n'avons pas pu rendre ce choix fonctionnel.
# le personnage est par défaut féminin.
genre = 'feminin'
if genre == 'feminin':
    e_feminin = "e"
    a_feminin = "a"
    ma_feminin = "a"
    ere_feminin = "ère"
    euse_feminin = "se"
else :
    e_feminin = ""
    a_feminin = "e"
    ma_feminin = "on"
    ere_feminin = "er"
    euse_feminin = "x"


# liste des dialogues
# ===================

# de 1 à 12 : niveaux
# de 21 à 32 : suite niveaux (niveau +20)
# de 40 à 46 : dialogues hors niveau
# 54, 56 : suite de la suite niveau (suite niveau +30)
# -2 : maisons vides
# de -3 à -15 : pancartes


dico_dialogue = {
    1 : { # niveau 1 | dialogue d'introduction avec Master Aldirien (exercice simple pour expliquer le jeu),
        'dialogue' : (
            (
                "Narrateur\n\nVous attendez devant ce feu de camp depuis quelques instants, lorsqu'un vieil homme approche. Il s'agit de votre mentor, celui que vous appelez Master Aldirien.",
                "Master Aldirien\n\nSalut à toi, jeune apprenti{0}. Voyons si tu as en mémoire ce que nous avons appris dans la bibliothèque.".format(e_feminin),
                "Master Aldirien\n\nPour lancer des sorts, tu dois écrire du code python dans l'encadré blanc à ta droite.",
                "Master Aldirien\n\nTu en auras besoin a chaque fois qu'un niveau va démarrer. Lorsque ce sera le cas, l'énoncé expliquant ce que tu dois faire s'affichera au dessus de l'encadré blanc.",
                "Master Aldirien\n\nLe résultat de tes sorts a un impact sur notre monde, mais aussi dans le plan arcanique du terminal. C'est l'encadré noir sous la carte. Tu y verras les retours concrets de tes sorts, dont les explications si ça ne marche pas.",
                "Master Aldirien\n\nJe vais te communiquer un exercice a résoudre dans le plan de l'énoncé. Tu le vois ? Alors résous le."
            ),
        ),
        'condition' : not(dico_saved_var['start_game']),
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    2 : { # niveau 2 | ambuscade des gobelins dans la passe du sud ou sur la route de l'Est (exercice combat simple),
        'dialogue' : (
            (
            "Narrateur\n\nVous vous avancez dans le chemin tracé entre deux montagnes par une ancienne rivière assechée. La route déserte n'est animée que par le bruit du vent qui s'engouffre entre les rochers",
            "Narrateur\n\nSoudain, des cris de gobelins se mêlent au vent. Vous réalisez que vous êtes à l'endroit parfait pour une ambuscade...",
            "(les mages se servent du plan de l'énoncé pour se tirer d'affaire. Leur savoir voyage dans ce plan et leur permet de trouver des sorts rapidement pour s'en sortir.)",
            ),
        ),
        'condition' : dico_saved_var['ambuscade_gobelin'],
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    3 : { # niveau 3 | dialogue avec Farore dans l'avant-poste pillé (exercice soigner un npc),
        'dialogue' : (
            (
                "Narrateur\n\nL'extérieur de l'avant-poste porte les traces d'un combat récent. La porte semble avoir été enfoncéee. Vous pénétrez dans le bâtiment, appréhendant la suite.",
                "Narrateur\n\nParmi les meubles renversés et les corps de gobelins, d'orcs et de soldats que vous découvrez dans la pièce, le son d'une plainte se fait entendre.",
                "Farore\n\n...uhhh...",
                "Farore\n\n...Malone ?... Mal... one ?...",
                "Farore\n\nQuelqu'... un ?... A l'aide...",
                "Narrateur\n\nVous vous approchez, et découvrez un corps au sol. Un soldat, non, une soldate vous regarde.",
                "Narrator\n\nElle a beau être fortement bâtie et couverte de muscles, ses blessures l'empêche d'enlever les briques de pierres éboulées qui la bloquent au sol.",
                "Narrateur\n\nUne seule de ces briques serait d'ailleur trop lourde pour vous, mais un sort pourrait toutes les enlever. Pour cela, L'énoncé commence a former une réponse dans votre esprit.",
            ),
        ),
        'condition' : not(dico_saved_var['farore_libre']),
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    4 : { # niveau 4 | dialogue avec Kheïa dans la forêt de Darkwod (exercice recherche de créatures invisible puis exercice combat moyen),
        'dialogue' : (
            (
                "Kheïa\n\nVous ! N'approchez pas ! Des squelettes sont cachés dans les bois, prêts à vous tomber dessus.",
                "Kheïa\n\nÊtes-vous mage ? Il doit y avoir un moyen de les repérer... J'ai appris l'existence un jour d'un sort...",
                "Kheïa\n\nLe mage qui m'en avait parlé disait que vous l'apprenez tous en huitième année de magie.",
                "Narrateur\n\nAlors que la guerrière vous parle, une pensée venue du plan de l'énoncé confirme ses propos.",
            ),
        ),
        'condition' : dico_saved_var['undead_vivant'],
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    5 : { # niveau 5 | dialogue avec les élémentaires de feu dans la pyramide (exercice décodage),
        'dialogue' : (
            (
                "Narrateur\n\nLorsque vous entrez dans la pyramide, la chaleur vous surprend. Vous remarquez alors plusieurs élémentaires de feu qui tournent autour d'une fausse. De cette fausse, les cris d'une jeune femme se font entendre.",
                "Dalmä\n\nArrière, créatures infernales ! À l'aide ! Fichus monstres !",
                "Un élémentaire\n\n...redia'l ed eyasse no saiM",
                "Narrateur\n\nUn élémentaire s'est tourné vers vous, et vous avez l'impression qu'il veut vous parler. Peut-être qu'un sort pourrait traduire ses paroles ?",
                "Narrateur\n\nVous vous souvenez d'un ancien cours, et vous fixez votre savoir dans le plan de l'énoncé. Cela devrait vous aider a comprendre la créature.",
                "Un élémentaire\n\n.eunnocni nosiar enu ruop essuoper suon ellE ? elbalbmes ertov redia sap zeirduov suoV",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    6 : { # niveau 6 | entrée dans la Ziggourat du Village des Âmes perdues (exercice recherche de créatures invisible puis exercice combat moyen),
        'dialogue' : (
            (
                "Narrateur\n\nVous vous approchez d'un ancien bâtiment, probablement un lieu de culte. Il est tout aussi abandonné que le reste du village.",
                "Narrateur\n\nLorsque vous pénetrez à l'intérieur, des bruits se font entendre. C'est comme le mouvement d'une bête, mais vous ne la voyez pas.",
                "Narrateur\n\nUne longue observation de la salle circulaire ne vous informe pas plus, et le bruit se fait plus proche...",
                "Narrateur\n\nVous pensez à un sort dont Aldirien vous avait parlé il y a longtemps. Il devrait vous permettre de révéler la présence de la créature. Tout vous reviens en mémoire dans le plan de l'énoncé.",
            ),
        ),
        'condition' : dico_saved_var['araigne_vivante'],
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    7 : { # niveau 7 | combat contre le scorpion (exercice combat difficile),
        'dialogue' : (
            (
                "Narrateur\n\nLa silouhette massive d'un scorpion des plaines, qui doit bien être aussi haut que vous, avance tranquillement dans l'herbe. Alors que vous vous approchez, il vous charge.",
                "Narrateur\n\nUne partie de votre concentration part alors directement dans le plan de l'énoncé tandis que vos lèvres commencent à formuler un sort.",
            ),
        ),
        'condition' : not(dico_saved_var['scorpion_calme']),
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    8 : { # niveau 8 | entrainement dans le bastion de Sandspear (exercice combat difficile),
        'dialogue' : (
            (
                "Narrateur\n\nVous poussez les lourdes portes du bastion et pénétrez dans la place d'entraînement. Un chevalier se tourne vers vous.",
                "L'entraineur\n\nEh bien ! Voilà un guerrier bien frêle qui veut s'entrainer !\n1. Je suis mage, ne riez pas trop vite.\n2. Euh... je me suis trompé{0} de porte.".format(e_feminin),
            ),
            (
                "L'entraineur\n\nAh, un{0} mage. Un{0} petit{0} prétencieu{1}... Mais ça ne veut pas dire que vous n'avez pas besoin d'entraînement.".format(e_feminin, euse_feminin),
                "L'entraineur\n\nDe toute façon, vous les magiciens, vous avez toujours tout d'écrit dans votre *énoncé* hahahaha.",
                "L'entraineur\n\nEN GARDE !  Que la leçon commence ! Vous allez voir qu'on ne rigole pas ici.",
            ),
            (
                "L'entraineur\n\nTrompé{0} de porte ? A Sandspear ?".format(e_feminin),
                "L'entraineur\n\nAhahahaha elle est bien bonne celle-là !",
                "L'entraineur\n\nBen vous allez quand même vous entrainer.",
                "L'entraineur\n\nDe toute façon, vous les magiciens, vous avez toujours tout d'écrit dans votre *énoncé* hahaha.",
                "L'entraineur\n\nEN GARDE !  Que la leçon commence ! Vous allez voir qu'on ne rigole pas ici.",
            ),
        ),
        'condition' : True,
        'nb_options' : 2,
        'type_choix' : 'spin_box'
    },
    9 : { # niveau 9 | dialogue avec Haldarielle dans les marais de l'Est (exercice décodage),
        'dialogue' : (
            (
                "Narrateur\n\nVous entrez dans une maison sordide, perdue au milieu des marais. Une atmosphère mystique règne autour du lieu.",
                "Narrateur\n\nLa pièce que vous découvrez est plus mystique encore, plongée dans une pénombre troublée seulement par la lumière mouvante d'un feu.",
                "Narrateur\n\nAutour du feu s'assemble une cuisine d'alchimiste. Une elfe se tient devant, dos à vous. Elle ne semble pas vous avoir remarqué{0}.".format(e_feminin),
                "Haldarielle\n\nJe savais que vous alliez venir.",
                "Narrateur\n\nSa voix vous fait sursauter. Vous ne pensiez pas qu'elle vous avait vue entrer.",
                "Haladrielle\n\nOui, je savais. Je sais beaucoup de choses.",
                "Haldarielle\n\nJ'ai d'ailleurs quelque chose à vous apprendre. Approchez.",
                "Haldarielle\n\nRegardez dans cet orbe. Il s'agit d'une sphère du savoir. Elle vous apprend ce qui se passe en ce moment dans le monde.",
                "Haldarielle\n\nCertaines choses devraient vous intéresser.",
                "Narrateur\n\nVous regardez dans les nuages de magie qui évoluent dans la sphère transparente, quand un texte commence a se former...",
                "Sphère de divination\n\nKvnsbsox dbkrsc. Zkbj-Ukbv cksd. Ck wybd bofovobk.",
                "Narrateur\n\nPour interpréter la divination, vous savez qu'il vous faut une formule précise. Heureusement, vous avez déjà eu quelques cours sur le sujet qui se reforment dans l'énoncé.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    10 : { # niveau 10 | entrée dans le campement orc (exercice trouver un chemin),
        'dialogue' : (
            (
                "Narrateur\n\nAlors que vous avancez prudement sur le chemin, vous repérez un homme qui épie le campement orc au loin.",
                "Narrateur\n\nSoudain, vous sentez une branche craquer sous vos pieds.",
                "Un mage\n\nQui va là ! Ah, c'est un{0} mage. Mais... Vous n'êtes pas l'apprenti{0} d'Aldirien ?".format(e_feminin),
                "Un mage\n\nPeut importe, ce n'est pas un combat pour les jeunes. Je suis chargé de combattre ces orcs, et je ne veux pas risquer votre vie.",
                "Narrateur\n\nIroniquement, ce mage est celui qui vous avait apprit un jour à bien argumenter pour obtenir ce que vous vouliez. Il ne fallut pas longtemps pour le convaincre de vous laisser combattre.",
                "Un mage\n\nBon, Bon. C'est d'accord. Par contre, il va falloir se faufiler là-dedans sans se faire voir.",
                "Un mage\n\nC'est l'occasion de vous tester un peu tiens. Essayez de trouver un chemin hors de vue de ces monstres.",
                "Un mage\n\nPour cela, vous avez ce sort que je vais vous partager mentalement... voyons... là.",
                "Un mage\n\nTout est dans votre énoncé. Une fois que vous avez réussit, on y va.",
            ),
        ),
        'condition' : not(dico_saved_var['mage_infiltre']),
        'nb_options' : 0,
        'type_choix': 'aucun'
    },
    11 : { # niveau 11 | combat contre Parz-Karl (exercice combat difficile),
        'dialogue' : (
            (
                "Narrateur\n\nVous arrivez avec le mage à côté d'une tente apparement vide. A quelques pas, Parz-Karl contemple sa tribue en action."
                "Narrateur\n\nVous repérez une femme en armure, enchaînée près d'une tente imposante. Une épée à deux mains gise au sol proche d'elle.",
                "Un mage\n\nRegardez, une femme est emprisonnée ! On dirait l'héroïne de Pyland...",
                "Parz-Karl\n\nDes intrus ! Qui les a laissés entrer ?",
                "Parz-Karl\n\nOrcs ! Tuez-les !",
            ),
        ),
        'condition' : dico_saved_var['parz_karl_vivant'],
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    12 : { # niveau 12 | combat final contre Aldirien et son invocation-dragon
        'dialogue' : (
            (
                "Narrateur\n\nEn vous matérialisant dans la pièce, vous constatez que vos soupçons sont fondés. Celui qui a été votre mentor se tient là, devant la table centrale, arqué au dessus du Pyliarium ouvert.",
                "Master Aldirien\n\nVas-tu enfin me liver tes secrets ?! Allons, charge-toi...",
                "Narrateur\n\nSoudain, le traître s'arrête. Un silence tombe dans la pièce alors qu'il tourne son visage vers vous.",
                "Master Aldirien\n\nTiens, m{0} ch{1} apprenti{2}. J'imagine que tu n'es pas là par hasard.".format(ma_feminin, ere_feminin, e_feminin),
                "Master Aldirien\n\nAinsi tu aurais deviné...",
                "Master Aldirien\n\nMais je n'ai besoin d'aucun témoin, vois-tu...",
                "Master Aldirien\n\nMEURS !!!",
                "Un mage\n\nNous bloquons ses pouvoirs les plus puissants ! Battez-le pendant ce temps. Vite !",
                "Master Aldirien\n\nQue les forces du feu m'accompagnent ! Saal-lio ! Ils sont là !",
                "Narrateur\n\nSous votre regard terrifié, le deuxième grand mentor de la bibliothèque apparaît, tout autant corrompu que votre mentor, et lance un puissant sort de feu. Vous le voyez se transformer en dragon.",
                "Saal-lio\n\nCh{1} apprenti{0}...".format(e_feminin, ere_feminin),
                "Saal-lio\n\n... Ceci sera ta dernière leçon.",
            ),
        ),
        'condition' : dico_saved_var['aldirien_vivant'],
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    21 : { # suite 1 | après la réussite du niveau d'introduction
        'dialogue' : (
            (
                "Master Aldirien\n\nAh, tu réponds. Bon. Il est temps de tester tes connaissances hors de la bibliothèque sécurisée !",
                "Master Aldirien\n\nPour commencer, tu vas lancer une attaque sur la montagne là-b-",
                "Master Aldirien\n\nMais que ??...",
                "Narrateur\n\nSoudain, trois gobelins montés à dos de sanglier débarquent au galop depuis la passe du sud, criant à l'assaut.",
                "Un gobelin\n\nAhah, nous te tenons, vieux croû-",
                "Master Aldirien\n\nfor _ in range(3):\n    remove('gobelin') #!\n#ZBAMM !!!",
                "Narrateur\n\nLes gobelins disparaissent instantanément, ne laissant que leurs montures qui vous regardent avec inquiétude.",
                "Master Aldirien\n\n...",
                "Master Aldirien\n\nDes gobelins jusqu'ici ? Je n'aime pas ça...",
                "Master Aldirien\n\nÉcoute-moi bien. Je dois aller protéger la bibliothèque arcanique. Toi, cherche d'où ces bestioles peuvent venir.",
                "Master Aldirien\n\nJe compte sur toi, cette menace est probablement plus importante que l'on pourrait le penser.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'        
    },
    23 : { # suite 3 | Farore est soignée
        'dialogue' : (
            (
                "Farore\n\nAh, je me sens bien mieux ! Merci, sorci{0}. Sans vous, j'aurai succombé à mes blessures.".format(ere_feminin),
                "Farore\n\nQue vois-je... Malone ne fait pas partie des corps... Ils ont dû l'enlever. Écoutez-moi ! Il faut la libérer. Les orcs l'ont emmenée, ils venaient du sud. Elle est très importante, je devais l'escorter, hélas...",
                "Farore\n\nBref. Il faut la sortir d'ici. Autant pour son propre bien que celui du royaume entier !\nJe compte sur vous, je dois encore me remettre de mes coups. Encore merci à vous.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    24 : { # suite 4 | révélation des morts-vivants
        'dialogue' : (
            (
                "Narrateur\n\nVotre sort confirme les alertes de Kheïa : des morts-vivants sont cachés dans les fourés et sont prêts à vous tomber dessus. Vous réalisez que vous êtes encerclé.",
                "Narrateur\n\nPar réflexe, vous déplacez votre esprit dans le plan de l'énoncé. Le combat est imminent, les squelettes commencent à quitter leurs cachettes."
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    54 : { # suite 24 | dialogue avec Kheïa après le combat contre les squelettes
        'dialogue' : (
            (
                "Kheïa\n\nUh ! On s'en sort bien, heureusement qu'ils sont faciles à démonter. Merci. Il faut que je retrouve Gurun maintenant, il doit se faire un sang de lave refroidie.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    25 : { # suite 5 | dialogue avec Dalmä lorsqu'elle est sauvée dans la pyramide
        'dialogue' : (
            (
                "Narrateur\n\nGrâce aux indications de l'élémentaire, vous parvenez a sortir Dalmä de son piège sans y tomber à votre tour.",
                "Dalmä\n\nMerci. Sans ce piège, j'aurai récupéré des trésors à même de vous remercier, mais...",
                "Dalmä\n\nBon, mieux vaut rentrer. Balmac doit s'inquiéter. Au revoir, merci encore.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    26 : { # suite 6 | révélation de l'araignée
        'dialogue' : (
            (
                "Narrateur\n\nAlors que votre sort fait effet, vous localisez la bête. Une araignée géante se trouve juste au dessus de vous, et ses mandibules étaient à deux doigts de vous découper.",
                "Narrateur\n\nVous vous connectez instinctivement au plan de l'énoncé, et préparez un sort...",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    56 : { # suite 26 | après la mort de l'araignée géante dans la ziggourat
        'dialogue' : (
            (
                "Narrateur\n\nAlors que vous regardez le corps carbonisé de l'araignée géante, vous sentez une sorte de fierté en vous. Les esprits du village manifestent leurs remerciements sans se montrer.",
                "Narrateur\n\nVous quittez la Ziggourat avec une fierté et un bonheur tels que vous n'en n'aviez jamais ressenti avant.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    27 : {
        "Narrateur\n\nAmusé{0}, vous regardez le scorpion se trémousser à chaque pangramme que vous dites. La terrifiante créature s'arrête, vous regarde avec ses petits yeux et claque légèrement des pinces comme pour vous remercier.".format(e_feminin),
        "Narrateur\n\nElle s'en retourne finallement à ses occupations. Heureusement que vous ne l'avez pas tué, tout le monde sait que les scorpions géants des plaines sont en voie d'extinction.",
    },
    28 : { # suite 8 | dialogue après le combat contre l'entraineur
        'dialogue' : (
            (
                "Narrateur\n\nSous le regard ébahis des miliciens, vous parez l'ultime attaque de l'entraîneur. Personne ne s'attendait à ce que vous gagniez.",
                "L'entraineur\n\nRmbbl... bravo. Bravo. Allez, vous avez gagné pour ce coup-ci. À la revoyure.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    29 : { # suite 9 | décryptage de la sphère de divination
        'dialogue' : (
            (
                "Narrateur\n\nVous parvenez finalement à lire la prédicition, qui se résume en ces mots...",
                "Sphère de divination\n\nAldirien trahi. Parz-Karl sait. Sa mort révelera.",
                "Narrateur\n\nVous saviez que les messages de divination ne sont jamais précis, mais bon quand même, flou à ce point c'est pas de chance.",
                "Haldarielle\n\nJe sais que vous avez réussit. Et puisque que je peux prévoir votre question : Parz-karl est le leader des orcs installés dans la vallée au sud d'ici.",
                "Haldarielle\n\nBonne route, jeune mage.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    31 : { # suite 11 | dialogue après le combat contre Parz-Karl
        'dialogue' : (
            (
                "Parz-Karl\n\nAh, Aldirien avait menti ! Nous sommes trahis ! Arrrgg.",
                "Narrateur\n\nLe calme retombe sur la vallée tandis que les dernières paroles de Parz-Karl résonnent dans votre tête.",
                "Narrateur\n\nAldirien serait allié des orcs ? Cela ne semblait pas faire grand sens. Le mage s'appproche de vous.",
                "Un mage\n\nQuelque chose m'inquiète... J'était le seul gardien à la bibliothèque aujourd'hui, tous les autres sont en mission.",
                "Un mage\n\nAldirien m'a dit qu'il se chargeait de la défense, mais après ce que l'orc a dit...",
                "Un mage\n\nIl faut qu'on aille vérifier. Vite !",
                "Narrateur\n\nAlors que vous regardez à vos pieds les corps des orcs battus et vous apprêtez à partir, la femme guerrière se tourne vers vous.",
                "Malone\n\nÉpatant, mage ! Vous leur avez bien fait la peau. Je me présente : Malone, héroïne de Pyland en quête de la rune de Daukstringue.",
                "Malone\n\nEnfin... quand on parle d'héroïne... heureusement que vous êtes là. Je ne vous oublierais pas lorsque j'aurai accompli ma quête.",
                "Malone\n\nBon ! On se met en route ? Il paraît que vous avez un mage-sombre-traitre-mentor je ne sait quoi à tuer ?",
                "Un mage\n\nEuh... Pour gagner du temps, on va devoir se téléporter. Et vous ne pourrez pas nous suivre.",
                "Malone\n\nAh ? Dommage, je vous aurai bien prêté main forte. Dans ce cas, bonne chance ! Je m'en retourne à ma rune.",
                "Un mage\n\nBon, pour la téléportation... Pour vous c'est trop compliqué. Je m'en charge",
                "Un mage\n\nPrêt ? Alors on se retrouve là-bas."
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    32 : { # suite 12 | mort d'Aldirien et fin de jeu
        'dialogue' : (
            (
                "Narrateur\n\nL'enveloppe draconique de Saal-lio destabilisée par l'un de vos sorts se dissipe petit à petit, pendant que le dernier sort rebondis entre vous et Aldirien.",
                "Narrateur\n\nLe dragon disparaît et laisse place au corps du grand mentor qui fini de se consumer en silence. La destabilisation de son sort lui a coûté la vie.",
                "Narrateur\n\nAldirien regarde son camarade tomber. Déconcentré, il oubli de renvoyer le dernier sort. Frappé de plein fouet, le mentor traître s'écroule lui aussi.",
                "Master Aldirien\n\nNOONNN ! Mort si près du but ! Maudit-",
                "Narrateur\n\n Son corps se désintègre alors, ne laissant qu'une trainée de cendre et sa cape sur le marbre noir. Derrière lui, le pylinarium s'est refermé tout seul."
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    40 : { # hors niveau | dialogue avec le spectre du Village des Âmes perdues
        'dialogue' : (
            (
                "Narrateur\n\nAlors que vous avancez dans le silencieux village abandonné, une ombre spectrale apparaît face à vous.",
                "Narrateur\n\nVous préparez un sort d'attaque, mais le cris du mort-vivant vous arrête.",
                "Un spectre\n\nNon ! Attendez ! Je suis un spectre. Je ne vais pas vous tuer enfin. Ça ne servirait à rien, je suis déjà mort moi-même.",
                "Un spectre\n\nÉcoutez, voyageur. Nous avons besoins de vous.",
                "Un spectre\n\nUne araignée géante a installé sa toile dans la ziggourat. Elle trouble notre repos. Si vous pouviez la chasser...",
                "Un spectre\n\nNous vous serions infiniment reconnaissants.\n\n1.Je vais vous aider.\n2.Désolé, je n'ai pas le temps pour les morts.",
            ),(
                "Un spectre\n\nVos ancêtres vous remercient, jeune mage.",
            ),(
                "Un spectre\n\nLe fantôme clignote littéralement sous vos yeux, comme desarçonné par votre réponse. Avec un regard lourd de jugements, il s'estompe, ne laissant que le vide là où il se tenait.",
            ),
        ),
        'condition' : True,
        'nb_options' : 2,
        'type_choix' : 'spin_box'
    },
    41 : { # hors niveau | dialogue avec Gurun le nain marchand dans le village de Nonameburg
        'dialogue' : (
            (
                "Narrateur\n\nVous entrez dans l'échoppe du marchand de la ville, et découvrez un nain à l'air bien affairé qui vous intercepte immédiatement.",
                "Gurun\n\nDésolé jeune mage, on a rien à vendre. C'est la faillite aujourd'hui.",
                "Narrateur\n\nLe nain marque une pause, vous regarde, et vous voyez ses yeux s'attarder sur le bâton de magie que vous portez.",
                "Gurun\n\nHurmf... La route de Darkwod est pas très sûre en ce moment, je craint que la caravane que j'attend de Maintown n'ai été attaquée.",
                "Gurun\n\nVous voudriez aller vérifier ? Et sauver ceux qui peuvent encore l'être si besoin ? Vous avez l'air de maîtrier un peu de magie.",
                "Gurun\n\nMoi-même et tout le village, nous vous en serions infiniment reconnaissants.\n\n1. Je vais retrouver votre caravane.\n2. Je suis déjà très occupé.\n3. Vous avez quoi sur l'épaule ?",
            ),(
                "Gurun\n\nVraiment ?? Vous êtes quelqu'un de bien ! Ah si vous y parvenez, on va enfin pouvoir vivre tranquillement ici.",
            ),(
                "Gurun\n\nGrmbl...",
                "Gurun\n\nEnfin, c'est compréhensible. Bonne journée a vous.",
            ),(
                "Gurun\n\nHein, le bâton de feu sur mon épaule ?",
                "Gurun\n\nEhh... c'est une commande... vous inquiétez pas.",
                "Gurun\n\nEuh... hum. Bref, vous ferez gaffe en allant dans la forêt, c'est pas le coin le plus sûr. Au revoir.",
            ),
        ),
        'condition' : True,
        'nb_options' : 3,
        'type_choix' : 'spin_box'
    },
    42 : { # hors niveau | dialogue avec Balmac le forgeron dans le village de Nonameburg
        'dialogue' : (
            (
                "Narrateur\n\nBien que petit, le village possède une forge dans laquelle vous entrez. Le forgeron, un tout jeune homme, lève des yeux larmoyants vers vous.",
                "Balmac\n\nAuriez-vous croisé ma soeur ? Elle ne nomme Dalmä, elle a à peu près mon âge. Elle...",
                "Narrateur\n\nIl s'arrête, constatant le regard d'incompréhension que vous lui lancez.",
                "Balmac\n\nNon, vous ne voyez pas.",
                "Balmac\n\nQuelle infortune ! Elle est partie dans le désert, au sud d'ici, il y'a une semaine. Si vous la voyez, dites-lui que je m'inquiète.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    43 : { # hors niveau | dialogue avec Olkin l'ermite
        'dialogue' : (
            (
                "Narrateur\n\nVous arrivez dans une vallée calme, au milieu de laquelle un feu de camp brûle encore. Quelqu'un vit forcément ici.",
                "Narrateur\n\nAu moment où vous vous faites cette réflexion, un très vieil homme sort d'une grotte proche, un sourir amusé au lèvres.",
                "Olkin l'Ermite\n\nTiens, personne ne vient par ici d'habitude. Qui êtes-vous ?\n\n1. Je suis l'apprenti{0} d'Aldirien.\n2. Je suis l{1} mage l{1} plus puissant{0} de la région.\n3. Peut vous importe.".format(e_feminin, a_feminin),
            ),(
                "Olkin l'Ermite\n\nAhh, ce vieux Aldirien ! Et ça y est, il vous lâche en pleine nature ? Et si j'apportait un peu de mes connaissances à votre éducation ?",
                "Olkin l'Ermite\n\nVous seriez content de savoir celà, attendez. Donnez-moi votre codex... Voilà, je vous ai écrit quelques connaissances supplémentaires. Bon voyage !",
            ),(
                "Olkin l'Ermite\n\nHum, c'est ça. Et moi je suis une vielle chaussette qu'on a oublié là. Et qui vous dit que vous n'avez pas encore beaucoup à apprendre ?",
                "Olkin l'Ermite\n\nTenez, par exemple ! Donnez-moi votre codex... Voilà, je vous ai écrit quelques connaissances supplémentaires. Bon voyage !",
            ),(
                "Olkin l'Ermite\n\nVraiment ? Bon. Mais je vois que vous êtes mage. Voulez-vous que je vous apprenne quelques tours amusants ?",
                "Olkin l'Ermite\n\nTenez, j'ai une idée ! Donnez-moi votre codex... Voilà, je vous ai écrit quelques connaissances supplémentaires. Bon voyage !",
            ), # après ce dialogue, des formules de python supplémentaires sont ajoutées au codex
        ),
        'condition' : True,
        'nb_options' : 3,
        'type_choix' : 'spin_box'
    },
    44 : { # hors niveau | dialogue avec Felria dans le campement de Darkwod
        'dialogue' : (
            (
                "Felria\n\nBien le bonjour, qu'est-ce qui peut bien mener un mage aussi profondement dans la forêt ?\n\n1. Je cherche d'où viennent les gobelins.\n2. J'ai été ambusqué par des squelettes, il faut les dégager de cette forêt.\n3. Je cherche une certaine Malone⌈",
            ),(
                "Felria\n\nDes gobelins ? Ils viennent de la vallée des Orcs, au sud-est d'ici. Ces répugnantes créatures ont fait alliance avec les squelettes, ça me donne du fil à retordre.",
                "Felria\n\nUn peu trop même. Je suis chasseuse de morts, pas d'orcs. Si vous cherchez des gobelins, j'imagine que vous allez combattre les orcs. Tuez-les tous, ça aidera les habitants de Nonameburg.",
                "Felria\n\nça fait trop longtemps qu'ils traînent ici, et il s'est passé quelque chose récemment. Ils sont plus agressifs, ils font plus de raids.",
            ),(
                "Felria\n\nDégager les squelettes de cette forêt est toute une aventure, et surtout, c'est mon job. Par contre, je vous laisse volontier ces ordures d'orcs qui se sont alliés avec eux et mettent la perssion sur Nonameburg.",
                "Felria\n\nIls sont établis au sud-est d'ici, dans la plaine des orcs.",
                "Felria\n\nça fait trop longtemps qu'ils traînent ici, et il s'est passé quelque chose récemment. Ils sont plus agressifs, ils font plus de raids.",
            ),(
                "Fleria\n\nMalone ? C'est pas l'héroïne de Maintown ? Pas vu dans le coin non, mais il y a fort à parier qu'elle soit allée dire un bonjour aux orcs du sud-est.",
                "Felria\n\nça fait trop longtemps qu'ils traînent ici, et il s'est passé quelque chose récemment. Ils sont plus agressifs, ils font plus de raids.",
            ),
        ),
        'condition' : True,
        'nb_options' : 3,
        'type_choix' : 'spin_box'
    },
    45 : { # hors niveau | château du roi
        'dialogue' : (
            (
                "Narrateur\n\nVous pénétrez dans le grand hall du château de Maintown, la capitale de l'ouest de Pyland. L'architecture somptueuse vous impressionne.",
                "Narrateur\n\nVous êtes introduits dans la salle d'audience, où Endal II le roi lui-même écoute les plaines de son peuple. On vous fait asseoir, et vous attendez votre tour.",
                "Narrateur\n\nLorsque le roi en vient a vous, vous lui racontez l'attaque des gobelins sur la bibliothèque, l'assurant que tout est pris en main mais que vous avez besoin d'informations pour trouver le campement orc.",
                "Endal II\n\nEh bien, vous ne sortez pas assez souvent de votre tour, vous les mages. Il y a au sud d'ici une vallée que l'on nomme la Vallée des Orcs. Ces monstres y migrent en été.",
                "Endal II\n\nIls pillent nos villages de temps en temps, mais on est abitué a les repousser. C'est étrange qu'ils aient pu atteindre votre bibliothèque.",
                "Endal II\n\nTout va mal en ce moment. Malone l'héroïne en quête de la rune de Daukstring a elle aussi disparue. Mes orcales présentent d'importants évènements dans un futur proche.",
                "Narrateur\n\nLe roi s'arrête, et vous regarde pensivement.",
                "Endal II\n\nJe me demande si tout ça n'est pas lié. Puisque vous êtes missionnés pour trouver ces orcs, allez au sud dans leur vallée et revenez me dire si Malone ne s'y trouve pas.",
                "Narrateur\n\nL'entrevue prend fin, et vous quittez le palais en vous demandant comment Aldirien, lui qui sait toujours tout, pouvait ne pas connaître l'emplacement de cette vallée.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    46 : { # hors niveau | crypte
        'dialogue' : (
            (
                "Narrateur\n\nDe toute évidence, vous n'êtes pas l{0} premi{1} a découvrir cette crypte. Les coffres ont déjà été pillés.".format(a_feminin, ere_feminin),
                "Narrateur\n\nVous ressortez au grand jour, un peu dépité{0} par cette aventure.".format(e_feminin),
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -2 : { # maisons vides
        'dialogue' : (
            (
                "Narrateur\n\nLa porte semble fermée à clef.\n\n1. Toquer.\n2. Crocheter la serrure.",
            ),
            (
                "Narrateur\n\nPersonne ne daigne vous ouvrir.",
            ),
            (
                "Narrateur\n\nLa serrure résiste. Vous n'arrivez pas à la crocheter.",
            ),
        ),
        'condition' : True,
        'nb_options' : 2,
        'type_choix' : 'spin_box'
    },
    -3 : { # panneau | devant la rivière au spawn
        'dialogue' : (
            (
                "Pancarte\n\nCamp de la bibliothèque arcanique\n    Nord : Bibliothèque arcanique\n    Est : Maintown\n    Sud : Nonameburg",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -4 : { # panneau | devant la passe du sud (deux panneaux),
        'dialogue' : (
            (
                "Pancarte\n\nPasse du Sud",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -16 : { # panneau | après la rivière au spawn
        'dialogue' : (
            (
                "Pancarte\n\nChemin de la bibliothèque arcanique\n    Nord : Bibliothèque arcanique\n    Est : Vallée de l'Ermite\n    Sud : Nonameburg",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -5 : { # panneau | devant l'avant-poste
        'dialogue' : (
            (
                "Pancarte\n\nAvant-poste de la Bibliothèque Arcanique",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -6 : { # panneau | Nonameburg (deux panneaux),
        'dialogue' : (
            (
                "Pancarte\n\nBienvenue à Nonameburg",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -7 : { # panneau | devant le désert
        'dialogue' : (
            (
                "Pancarte\n\nDésert des serpents\n    Nord : Nonameburg\n    Sud : Sandspear",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -8 : { # panneau | Sandspear
        'dialogue' : (
            (
                "Pancarte\n\nBienvenue à la garnison de Sandspear\n\n|---------------------|\n|Entraînements ouverts|\n|---------------------|",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -9 : { # panneau | Forêt de Darkwod (deux),
        'dialogue' : (
            (
                "Pancarte\n\nForêt de Darkwod\n    Est : Maintown, Vallée des Orcs\n    Ouest : Nonameburg",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -10 : { # panneau | carrefour
        'dialogue' : (
            (
                "Pancarte\n\nCarrefour de la plaine\n    Nord : Maintown\n    Est : Avant-poste de Maintown\n    Sud : Vallée des Orcs\n    Ouest : Nonameburg",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -11 : { # panneau | Vallée des Orcs
        'dialogue' : (
            (
                "Pancarte\n\nVoyageur, arrêtez-vous !\nDes orcs migrent souvent dans cette vallée.\nVous avancez à vos risques et périls.",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -12 : { # panneau | Avant-poste Maintown
        'dialogue' : (
            (
                "Pancarte\n\nAvant-poste Maintown",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -13 : { # panneau | Marais
        'dialogue' : (
            (
                "Pancarte\n\nMarais de l'Est\n    Nord : Maintown",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -14 : { # panneau | Maintown (trois panneaux),
        'dialogue' : (
            (
                "Pancarte\n\nBienvenue à Maintown",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
    -15 : { # panneau | Village des Âmes perdues (deux panneaux),
        'dialogue' : (
            (
                "Pancarte\n\nVous entrez dans le\nVillage des Âmes perdues",
            ),
        ),
        'condition' : True,
        'nb_options' : 0,
        'type_choix' : 'aucun'
    },
}
