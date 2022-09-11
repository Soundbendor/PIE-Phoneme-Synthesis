"""
Sample texts and word lists in PIE.
"""
import random

# Schneider's fable  ʰʷ
sheep_and_horses = {'title': 'The Sheep and the Horses', 'url': 'https://en.wikipedia.org/wiki/Schleicher%27s_fable',
                    'pie': 'H₂áwej h₁josméj h₂wl̥h₁náh₂ né h₁ést, só h₁éḱwoms derḱt. Só gʷr̥hₓúm wóǵʰom wéǵʰet; só '
                           'méǵh₂m̥ bʰórom; só (dʰ)ǵʰémonm̥ h₂ṓḱu bʰéret. H₂ówis h₁ékʷojbʰ(j)os wéwkʷet: ('
                           'dʰ)ǵʰémonm̥ spéḱjoh₂ h₁éḱwoms h₁jós h₂áǵeti, ḱḗr moj agʰnutór. H₁éḱwōs tu wéwkʷont: '
                           'ḱludʰí, h₂owei! Tód spék̂jomes, n̥sméi agʰnutór ḱḗr: (dʰ)ǵʰémō pótis sē h₂áwjōm '
                           'h₂wl̥h₁nā́h₁ gʷʰérmom wéstrom (h₁)wébht, h₂áwibʰ(j)os tu h₂wl̥h₁náh₂ né h₁ésti. Tód '
                           'ḱeḱluwṓs h₂ówis h₂aǵróm bʰugét.',
                    'eng': 'A sheep that had no wool saw horses, one of them pulling a heavy wagon, one carrying a big '
                           'load, and one carrying a man quickly. The sheep said to the horses: "My heart pains me, '
                           'sheep has no wool." Having heard this, the sheep fled into the plain. '}

# King and the god
king_and_god = {'title': 'The King and the god', 'url': 'https://en.wikipedia.org/wiki/The_king_and_the_god',
                'pie': 'Tór h₃rḗǵs h₁ést. Só (h₂)népotlos h₁ést. Só h₃rḗǵs suHnúm welh₁t. Só tósyo gʷerHtérm̥ preḱt; '
                       '"SuHnús moy ǵénh₁tim!" Só gʷerHtor tóm h₃réǵm̥ wekʷt: "H₁yaǵswé deywóm H₁wérunom" Só h₃rḗǵs '
                       'deywóm H₁wérunom upó-swé-sor nu deywóm h₁yaǵtont: "ḱlewdʰi moy, ph₂tér H₁wérune!" Deywós '
                       'H₁wérunos ḱm̥teh₂ dyḗws gʷeh₂t. "Kʷíd welh₁si?" "Welh₁mi suHnúm." "Tód h₁éstu", wekʷt lewkós '
                       'deywós H₁wérunos. H₃réǵs pótnih₂ suHnúm h₁é-ǵenh₁ti. ',
                'eng': 'Once there was a king. He was childless. The king wanted a son. He asked his priest: "May a '
                       'son be born to me!" The priest said to the king: "Pray to the god Werunos." The king '
                       'approached the god Werunos to pray now to the god. "Hear me, father Werunos!" The god Werunos '
                       'came down from heaven. "What do you want?" "I want a son." "Let this be so," said the bright '
                       'god Werunos. The king\'s lady bore a son. '}

# word lists
word_lists = {}

# pronouns
pronouns = {'I': 'éǵh₂', 'I (2)': 'eǵh₂óm', 'wéy': 'we', 'you': 'túh₂', 'you (plural)': 'yū́', 'she': 'sih₂',
            'self': 'swé', 'the': 'ís', 'another': 'h₂élyos', 'other': 'h₂élteros',
            'what': 'kʷís', 'who': 'kʷos', 'which': 'yós', 'this': 'só', 'that': 'h₁énos'}
word_lists['pronouns'] = pronouns

# numbers
numerals = {'one': 'óynos', 'two': 'dwóh₁', 'three': 'tréyes', 'four': 'kʷetwóres', 'five': 'pénkʷe', 'six': 'swéḱs',
            'seven': 'septḿ̥ ', 'eight': 'oḱtṓw', 'nine': 'h₁néwn̥', 'ten': 'déḱm̥',
            'twenty': 'wídḱm̥ti', 'thirty': 'tridḱómt', 'forty': 'kʷétwr̥dḱomt', 'fifty': 'pénkʷedḱomt',
            'sixty': 'swéḱsdḱomt', 'seventy': 'septḿ̥dḱomt', 'eighty': 'oḱtódḱomt', 'ninety': 'h₁néwn̥dḱomt',
            'hundred': 'ḱm̥tóm', 'thousand': 'ǵʰéslom'}
word_lists['numerals'] = numerals

# people and society
society = {'people': 'h₁léwdʰis', 'human': 'dʰéǵʰōm', 'earthling': 'ǵʰmṓ',
           'man': 'h₂nḗr', 'woman': 'gʷḗn',
           'lineage': 'ǵénh₁os', 'tribe': 'tewtéh₂',
           'settlement': 'weyḱ-', 'city': 'tpelH-', 'home': 'dṓm',
           'chief': 'wiḱpótis', 'king': 'h₃rḗǵs', 'queen': 'h₃rḗǵnih₂', 'master': 'h₁esh₂ós', 'slave': 'h₃órbʰos',
           'warrior': 'wiHrós', 'youth': 'h₂yuHn̥téh₂', 'guest': 'gʰóstis', 'master of the house': 'déms pótis',
           'payment': 'misdʰós', 'price': 'h₂elgʷʰós',
           'punishment': 'kʷoynéh₂', 'prosperity': 'spéh₁s', 'power': 'h₂nḗr', 'fight': 'kéh₃tus',
           'thief': 'bʰṓr', 'lie': 'dʰrówgʰos', 'spy': 'spéḱs',
           'gift': 'déh₃nom', 'name': 'h₁nómn̥', 'fame': 'ḱléwos',
           'carpenter': 'tétḱō',
           'course': 'h₁éytr̥', 'path': 'póntoh₁s', 'way': 'stóygʰos', 'crossing': 'pértus', 'ford': 'pérwr̥',
           'song': 'sh₂ómn̥', 'work': 'wérǵom', 'sale': 'wósn̥', 'wages': 'misdʰós',
           'virile man': 'wérsēn', 'barren woman': 'steríh₂s',
           'voice': 'wṓkʷs', 'word': 'werdʰh₁om', 'oath': 'h₁óytos', 'strength': 'séǵʰos'}
word_lists['society'] = society

# relationships
kinship = {'mother (1)': 'méh₂tēr', 'father': 'ph₂tḗr', 'dad': 'átta', 'husband (1)': 'pótis ',
           'child': 'ǵénh₁mn̥', 'parent': 'ǵénh₁tōr', 'mother (2)': 'ǵénh₁trih₂',
           'wife': 'pótnih₂', 'husband (2)': 'wiHrós',
           'brother': 'bʰréh₂tēr', 'sister': 'swésōr', 'sibling': 'somo-pH₂tōr', 'twin': 'yemH-',
           'daughter': 'dʰugh₂tḗr', 'son': 'suHnús',
           'maternal grandfather': 'h₂éwh₂os',
           'grandson': 'népōts', 'granddaughter': 'néptih₂',
           'daughter-in-law': 'snusós', 'father-in-law': 'swéḱuros',
           'mother-in-law': 'sweḱrúh₂', 'brother-in-law': 'swēḱurós', 'sister-in-law (1)': 'dayh₂wḗr',
           'sister-in-law (2)': 'ǵh₂lōws',
           'co-sister-in-law': 'h₁yenh₂tēr', 'widow': 'h₁widʰéwh₂', 'orphan': 'h₃órbʰos'}
word_lists['kinship'] = kinship

# worship
religion = {'sacred place': 'dʰéh₁s', 'god': 'deywós', 'goddess': 'déywih₂', 'earthling': 'ǵʰmṓ',
            'sacrifice': 'némos', 'ceremony': 'seh₂k-', 'sacred': 'ḱwen-', 'giver': 'déh₃tōr',
            'river goddess': 'déh₂nu', 'sky god': 'dyḗws', 'dawn': 'h₂éwsōs',
            'oath': 'h₁óytos', 'magic': 'soytós'}
word_lists['religion'] = religion

# home and tools
tools = {'home (1)': 'h₂wóstu', 'house': 'dʰéh₁mn̥', 'home (2)': 'dṓm', 'shelter': 'ḱléytreh₂',
         'door (1)': 'dʰwer-', 'door (2)': 'dʰwṓr', 'fence': 'kagʰyóm', 'hedge': 'kagʰyóm', 'enclosure': 'ǵʰórtos',
         'clothes': 'wéstis', 'wool': 'h₂wĺ̥h₁neh₂', 'fleece': 'moysós',
         'bathtub': 'lówh₃trom', 'peg': 'ǵómbʰos',
         'millstone': 'gʷréh₂wō', 'stone': 'h₂éḱmō',
         'vehicle': 'ḱr̥sós', 'plough': 'h₂érh₃trom', 'yoke': 'yugóm',
         'silver': 'h₂r̥ǵn̥tóm', 'copper': 'h₂éyos', 'charcoal': 'h₁óngʷl̥',
         'path': 'póntoh₁s', 'way': 'stóygʰos', 'crossing': 'pértus', 'wheel': 'kʷékʷlos', 'ford': 'pérwr̥',
         'boat': 'néh₂us', 'string': 'tónos', 'awl': 'h₁ólos', 'axle': 'h₂eḱs-', 'arrow': '(H)ísus', 'spear': 'gʷéru'}
word_lists['tools'] = tools

# body parts, mostly human
anatomy = {'head': 'káput', 'brain': 'mosgʰós', 'mind': 'ménos', 'skull': 'ḱérh₂sō', 'forehead': 'h₂entíos',
           'beard': 'bʰardʰéh₂',
           'nose': 'néh₂s', 'eye': 'h₃ókʷs', 'ear': 'h₂ṓws', 'eyebrow': 'h₃bʰrúHs', 'neck': 'gʷriHwéh₂',
           'tongue': 'dn̥ǵʰwéh₂s', 'chin': 'ǵénus', 'tooth': 'h₃dónts', 'mouth': 'h₁óh₃s',
           'hand': 'ǵʰésōr', 'arm (1)': 'bʰeh₂ǵʰús', 'arm (2)': 'dóws', 'shoulder': 'h₂ṓms', 'nail': 'h₃nṓgʰs',
           'foot': 'pṓds', 'knee': 'ĝénu', 'heel': 'tpḗrsneh₂',
           'chest': 'pérḱus', 'breast': 'pstḗn', 'heart': 'ḱérd', 'lung': 'pléwmō',
           'stomach': 'úderos', 'navel': 'h₃nóbʰōl', 'kidney': 'negʷʰrós', 'liver': 'yókʷr̥',
           'bone': 'h₃ésth₁', 'marrow': 'mosgʰós', 'blood (1)': 'h₁ésh₂r̥', 'blood (2)': 'kréwh₂s',
           'tendon': 'snéh₁wr̥', 'joint': 'koḱs-',
           'hip': 'ḱlównis', 'penis': 'pes-', 'testicle': 'h₁órǵʰis', 'vulva': 'písdeh₂',
           'poop': 'sóḱr̥', 'feces': 'ḱókʷr̥', 'urine': 'múHtrom',
           'breath (1)': 'h₂enh₁mos', 'breath (2)': 'pnéwmn̥', 'tear': 'dáḱru', 'sore': 'h₁élḱos',
           'hoof': 'ḱoph₂ós', 'udder': 'h₁ówHdʰr̥'}
word_lists['anatomy'] = anatomy

# weather, time, space, nature
nature = {'earth': 'dʰéǵʰōm', 'sun': 'sóh₂wl̥', 'moon (1)': 'mḗh₁n̥s', 'moon (2)': 'lówksneh₂',
          'star': 'h₂stḗr', 'sky': 'dyḗws', 'well': 'bʰréh₁wr̥', 'estuary': 'gʷriHwéh₂',
          'field': 'h₂éǵros', 'hill': 'bʰerǵʰ-', 'mountain': 'pérwr̥',
          'tree': 'dóru', 'branch': 'h₃ósdos', 'bloom': 'h₂éndʰos', 'leaf': 'pornóm', 'seed': 'séh₁mn̥',
          'ash tree': 'Heh₃s-', 'mountain elm': 'h₁élem', 'beech': 'bʰeh₂ǵos', 'hazel': 'kóslos', 'oak': 'pérkus',
          'grass': 'h₂et-', 'alder': 'wern-', 'twig': 'wéh₁itis', 'birch': 'bʰerHǵós', 'fern': 'pornóm',
          'ice': 'h₁eyg-', 'snow (1)': 'snéygʷʰs', 'snow (2)': 'ǵʰéyōm',
          'cloud (1)': 'snéygʷʰs', 'cloud (2)': 'nébʰos', 'rain cloud': 'n̥bʰrós', 'mist': 'h₃mígʰleh₂',
          'water': 'h₂ékʷeh₂', 'lake': 'léymō', 'pond': 'lókus', 'sea': 'móri', 'marsh': 'sélos',
          'summer': 'semh₂-', 'spring': 'wósr̥', 'winter': 'ǵʰéyōm', 'warm weather': 'gʷʰéros', 'thunder': 'gʰromós',
          'fire': 'péh₂wr̥', 'smoke': 'dʰuh₂mós', 'pebble': 'ḱorkeh₂', 'stone': 'h₂éḱmō',
          'darkness': 'h₁régʷos', 'shadow': '(s)ḱeh₃ih₂', 'dawn': 'h₂éwsōs'}
word_lists['nature'] = nature

colors = {'bright': 'lewk-', 'shine': 'bʰel-', 'shining (1)': 'h₂erǵ-', 'shining (2)': 'gʰleh₂dʰ-',
          'silver': 'h₂r̥ǵn̥tóm', 'white': 'ḱweyt-',
          'black': 'kr̥snós', 'gray': 'ḱey-', 'brown (1)': 'bʰer-', 'brown (2)': 'bʰerH-', 'brownish': 'h₁el-',
          'yellow': 'gʰel-', 'green': 'ǵʰelh₃-', 'red (1)': 'h₁rudʰrós', 'red (2)': 'h₁rewdʰ-'}
word_lists['colors'] = colors

# animal words: domestic and wild
animals = {'cow': 'woḱéh₂', 'cow (2)': 'h₂eǵʰ-', 'bull': 'táwros', 'cattle': 'gʷṓws', 'heifer': 'steríh₂s',
           'auroch': 'táwros', 'ox': 'uksḗn', 'livestock': 'péḱu',
           'horse': 'h₁éḱwos (1)', 'wild horse': 'márkos', 'horse (2)': 'ǵʰéyos',
           'male goat': 'kápros', 'goat': 'h₂eyǵ-', 'buck': 'bʰuǵ-', 'male animal': 'wérsēn', 'yoked': 'yéwgos',
           'lamb': 'h₂egʷnós', 'sheep': 'h₂ówis', 'ram': 'wr̥h₁ḗn', 'piglet': 'pórḱos', 'pig': 'suH-', 'deer': 'h₁el-',
           'goose': 'ǵʰh₂éns', 'duck': 'h₂énh₂ts', 'worm': 'wr̥mis', 'wolf': 'wĺ̥kʷos', 'she-wolf': 'wl̥kʷíh₂s',
           'flea': 'plúsis', 'louse': 'lewH-', 'leech': 'ǵelu-', 'wasp': 'wóps', 'bee': 'bʰey-', 'ant': 'morwi-',
           'snake': 'h₂éngʷʰis', 'adder': '(s)néHtr̥',
           'bear': 'h₂ŕ̥tḱos', 'otter': 'udrós', 'weasel': 'gl̥h₁éys', 'dog': 'ḱwṓ', 'hedgehog': 'h₁eǵʰis',
           'beaver': 'bʰébʰrus', 'mouse': 'múh₂s', 'dormouse': 'mouse',
           'catfish': '(s)kʷálos', 'fish': 'peysḱ-',
           'bird': 'h₂éwis', 'eagle': 'h₃érō', 'crane': 'gerh₂ōws', 'heron': 'gerh₂ḗn', 'sparrow': 'spḗr',
           'nest': 'nisdós', 'dung (1)': 'ḱókʷr̥', 'dung (2)': 'sóḱr̥', 'wing': 'péth₂r̥'}
word_lists['animals'] = animals

# food words
food = {'water': 'wódr̥', 'meat': 'mḗms', 'egg': 'h₂ōwyóm', 'honey (1)': 'mélit', 'honey (2)': 'kn̥h₂ónks',
        'apple': 'h₂ébōl', 'seed': 'séh₁mn̥',
        'beer': 'h₂elut-', 'wine': 'wéyh₁ō', 'mead': 'médʰu',
        'butter': 'h₃éngʷn̥', 'grease': 'smérus', 'salt': 'séh₂ls', 'broth': 'yúHs',
        'cereal': 'yéwos', 'rye': 'Hrugʰís', 'barley': 'h₂élbʰit', 'plant juice': 'sokʷós',
        'grain (1)': 'ǵr̥h₂nóm', 'grain (2)': 'dʰoHnéh₂', 'wheat': 'puHrós', 'hazel': 'kóslos',
        'turnip': '(s)rā́ps', 'dregs': 'dʰrā́ks', 'taste': 'ǵéwstus'}
word_lists['food'] = food

# time
time = {'now': 'nu', 'yesterday': 'dʰǵʰyésteros',
        'night (1)': 'nókʷts', 'night (2)': 'kʷséps', 'evening': 'wek(ʷ)speros', 'dawn': 'h₂éwsōs',
        'summer': 'semh₂-', 'spring': 'wósr̥', 'winter': 'ǵʰéyōm',
        'year': 'yóh₁r̥', 'month': 'mḗh₁n̥s',
        'lifetime': 'h₂óyu', 'lifespan': 'sh₂éytlom', 'short': 'mréǵʰus', 'interval': 'déh₂itis',
        'sleep': 'supnós', 'slumber': 'swépnos', 'darkness (1)': 'h₁régʷos', 'darkness (2)': 'témHos'}
word_lists['time'] = time

# adjectives
adjectives = {'a name from Tanais': 'érh₂onts', 'alive': 'gʷih₃wós', 'new (2)': 'néwyos', 'aware': 'bʰudʰtós',
              'bare': 'bʰosós', 'bearded': 'bʰardʰéh₂tos', 'begotten': 'n̥h₁tós', 'big': 'méǵh₂s', 'bigger': 'méǵh₂yōs',
              'bitter': 'h₂eh₃mós', 'black': 'kr̥snós', 'bloody': 'kruh₂rós', 'blowing': 'h₂wéh₁n̥ts',
              'brief': 'mréǵʰus', 'broad': 'h₁wérus', 'campestral': 'h₂éǵr̥yos', 'carved': 'gr̥bʰtós',
              'covered': 'ḱlitós', 'dark (1)': 'reh₁mós', 'dark (2)': 'kr̥snós', 'dead (1)': 'mr̥tós',
              'dead (2)': 'néḱus', 'dear': 'priHós', 'deep (1)': 'dʰubʰnós', 'deep (2)': 'dʰubʰrós',
              'dense, thick': 'bʰénǵʰus', 'dirty': 'reh₁mós', 'far away': 'dweh₂rós', 'flat': 'pléth₂us',
              'floated': 'plutós', 'full': 'pl̥h₁nós', 'given': 'dh₃tós', 'good': 'h₁wésus', 'happy': 'priHós',
              'heard': 'ḱlutós', 'heavenly': 'diwyós', 'heavy': 'gʷréh₂us', 'high': 'bʰérǵʰonts', 'higher': 'údteros',
              'homely': 'ḱóymos', 'ill-disposed': 'dusmenḗs', 'immortal': 'n̥mr̥tós', 'in a bad mood': 'tréystis',
              'inside': 'h₁énteros', 'invoked': 'ʰutós', 'known (1)': 'n̥h₃tós', 'known (2)': 'widtós',
              'famous': 'ḱlutós', 'lean': 'mh₂ḱrós', 'leaning': 'ḱlitós', 'left': 'sewyós', 'libated': 'ʰutós',
              'lifted': 'tl̥h₂tós', 'lightweight (1)': 'h₁léngʰus', 'lightweight (2)': 'h₁ln̥gʷʰrós',
              'loaded': 'h₃enh₂ostos', 'long (1)': 'dl̥h₁gʰós', 'long (2)': 'dlongʰos', 'long (3)': 'dweh₂rós',
              'middle': 'médʰyos', 'mortal (1)': 'mr̥tós', 'mortal (2)': 'néḱus', 'narrow': 'h₂énǵʰus',
              'new (1)': 'néwos', 'aquatic': 'udrós', 'old (1)': 'érh₂onts', 'old (2)': 'sénos', 'blind': 'kéh₂ikos',
              'otter': 'udrós', 'passable (1)': 'gʷm̥tós', 'passable (2)': 'h₁itós', 'standing': 'sth₂tós',
              'uncooked': 'h₂eh₃mós', 'recognisable': 'n̥h₃tós', 'red': 'h₁rudʰrós', 'same': 'somh₁ós',
              'seated': 'sedtós', 'seen': 'widtós', 'seized': 'kaptós', 'sharp': 'h₂ḱrós', 'stiff': 'tr̥nós',
              'short': 'mréǵʰus', 'sloped': 'ḱleywós', 'soft': 'ml̥dus', 'sour': 'súHros', 'cloven': 'bʰidnós',
              'split': 'bʰidtós', 'straightened': 'h₃reǵtós', 'extended': 'tn̥tós', 'stretched': 'str̥h₃tós',
              'stubborn': 'tréystis', 'sweet (1)': 'dléwkus', 'sweet (2)': 'swéh₂dus',
              'that which blowsr': 'h₂wéh₁n̥ts', 'thick': 'tégus', 'thin': 'ténh₂us', 'this one': 'ḱíteros',
              'trusted': 'bʰidʰtós', 'very sweet': 'swéh₂dyōs', 'washed': 'plutós', 'which of two': 'kʷóteros',
              'white': 'albʰós', 'wide': 'pl̥th₂enós', 'worked': 'wr̥ǵtós', 'yesterday': 'dʰǵʰyésteros',
              'yoked': 'yugtós', 'young (1)': 'h₂yéwHō', 'young (2)': 'h₂yuHn̥ḱós', 'true': 'weh₁ros'}
word_lists['adjectives'] = adjectives

# adverbs
adverbs = {'about': 'h₂m̥bʰi', 'above (1)': 'upér', 'above (2)': 'upéri', 'afterwards': 'pós', 'again': 'h₂ew',
           'against': 'wi', 'and': 'nu', 'apart': 'wi', 'around': 'per', 'away': 'h₂pó', 'away from': 'h₂ew',
           'before': 'h₂énti', 'beside': 'ḱóm', 'between': 'h₁entér', 'beyond': 'éti', 'by': 'pós', 'early': 'h₂éyeri',
           'facing': 'h₂m̥bʰi', 'half': 'sēmi', 'in': 'h₁én', 'in exchange for': 'h₂m̥bʰi', 'in front': 'h₂énti',
           'in the middle of': 'me', 'in two': 'dwís', 'into': 'h₁n̥dó', 'last year': 'péruti', 'near': 'h₂énti',
           'now': 'nu', 'off': 'h₂epó', 'on': 'h₁epi', 'onto': 'h₂en-', 'opposite': 'h₂énti', 'out': 'h₁eǵʰs',
           'over (1)': 'éti', 'over (2)': 'upér', 'partially': 'sēmi', 'sparsely': 'h₁réh₁', 'then': 'h₁é',
           'through (1)': 'per', 'through (2)': 'tr̥h₂és', 'to': 'h₂éd', 'toward': 'pró', 'twice': 'dwís',
           'under (1)': 'h₁n̥dʰér', 'under (2)': 'h₁n̥dʰí', 'under (3)': 'upó', 'upwards': 'úd', 'well': 'nu',
           'yesterday': 'dʰǵʰyés'}
word_lists['adverbs'] = adverbs

# verbs
verbs = {'(he) is carrying': 'bʰéreti', 'to arrive (1)': 'gʷémt', 'to arrive (2)': 'h₁ludʰét',
         'to awaken': 'bʰowdʰéyeti', 'to be': 'h₁ésti', 'to be afraid': 'dedwóye', 'to be alert': 'bʰebʰówdʰe',
         'to be awake': 'bʰéwdʰeti', 'to be becoming': 'bʰuHyéti', 'to be breaking': 'Hrunépti',
         'to be carrying around': 'bʰoréyeti', 'to be climbing': 'stéygʰeti', 'to be cooking': 'pékʷeti',
         'to be covering': 'ḱéleti', 'to be cutting off': 'skinédti', 'to be doing': 'dʰédʰeh₁ti',
         'to be driving': 'h₂éǵeti', 'to be farting': 'pérdetor', 'to be following': 'sékʷetor',
         'to be getting dark': 'h₁regʷesyéti', 'to be getting up': 'stísteh₂ti', 'to be giving': 'dédeh₃ti',
         'to be hear well': 'h₂ḱh₂owsyéti', 'to be heard': 'ḱeḱlówe', 'to be holding up': 'tetólh₂e',
         'to be joining': 'yunégti', 'to be leaning': 'ḱlinéh₂ti', 'to be leaving': 'linékʷti',
         'to be licking': 'léyǵʰti', 'to be lifting': 'tl̥néh₂ti', 'to be listening': 'ḱl̥néwti',
         'to be looking at': 'spéḱyeti', 'to be lying down': 'légʰyeti', 'to be lying flat': 'ḱéytor',
         'to be mindful': 'memóne', 'to be missing': 'lelóykʷe', 'to be nourishing': 'h₂életi',
         'to be ploughing': 'h₂éryeti', 'to be pointing out': 'déyḱti', 'to be productive (1)': 'dʰedʰówgʰe',
         'to be productive (2)': 'dʰéwgʰti', 'to be protecting': 'h₂lékseti', 'to be putting': 'dʰédʰeh₁ti',
         'to be red': 'h₁rudʰéh₁ti', 'to be satisfied': 'tetórpe', 'to be saying': 'wéryeti', 'to be seized': 'kapyéti',
         'to be sipping': 'srobʰéyeti', 'to be sitting': 'sédyeti', 'to be sitting down': 'sísdeti',
         'to be smearing': 'h₂linéHti', 'to be splitting': 'bʰinédti', 'to be standing (1)': 'stéh₂yeti',
         'to be standing (2)': 'stestóh₂e', 'to be straightening': 'h₃réǵeti', 'to be stretched': 'tetóne',
         'to be stretching': 'tn̥néwti', 'to be striking down': 'gʷʰénti', 'to be transporting': 'wéǵʰeti',
         'to be trusting': 'bʰebʰóydʰe', 'to be turned towards': 'wewórte', 'to be turning around': 'wértti',
         'to be upset': 'h₂eh₂ógʰe', 'to be urinating': 'h₃méyǵʰeti', 'to be walking (1)': 'gʷm̥sḱéti',
         'to be walking (2)': 'stéygʰeti', 'to be wearing': 'wéstor', 'to be working': 'wr̥ǵyéti', 'to become': 'bʰúHt',
         'to become cut': '(s)kérdʰh₁eti', 'to become full': 'pléh₁dʰh₁eti', 'to believe': 'ḱréddʰh₁eti',
         'to blow': 'h₂wḗh₁ti', 'to break': 'Hréwpt', 'to breathe': 'h₂énh₁ti', 'to burn': 'dʰégʷʰeti',
         'to buy': 'kʷrinéh₂ti', 'to cause to carry': 'bʰoréyeti', 'to cause to lean': 'ḱléyeti',
         'to cause to sip': 'srobʰéyeti', 'to cause to stand': 'stoh₂éyeti', 'to clothe': 'woséyeti',
         'to come': 'gʷm̥sḱéti', 'to copulate': 'h₃yébʰeti', 'to cultivate': 'tḱéyti', 'to cut off': 'skéydt',
         'to dare': 'dʰedʰórse', 'to die': 'mért', 'to do': 'dʰéh₁t', 'to drink': 'píph₃eti', 'to dwell': 'tḱéyti',
         'to eat': 'h₁édti', 'to extend': 'tonéyeti', 'to fly': 'péth₂eti', 'to get through': 'térh₂t',
         'to get to know': 'ǵnéh₃t', 'to give': 'déh₃t', 'to give a sign': 'séh₂gyeti', 'to go': 'h₁éyti',
         'to guard': 'péh₂sti', 'to have power': '(me)mógʰe', 'to have reached': 'h₂eh₂nóḱe', 'to have seen': 'wóyde',
         'to have the feet planted': 'gʷegʷóme', 'to hear': 'ḱléwt', 'to heat': 'gʷʰoréyeti',
         'to increase': 'pléh₁dʰh₁eti', 'to keep asking': 'pr̥sḱéti', 'to keep requesting': 'gʷʰédʰyeti',
         'to know (1)': 'ǵnéh₃t', 'to know (2)': 'ǵn̥néh₃ti', 'to lead': 'déwkti', 'to lean on': 'ḱléyeti',
         'to leave': 'léykʷt', 'to lift': 'télh₂t', 'to live': 'gʷíh₃weti', 'to make aware': 'bʰowdʰéyeti',
         'to make dry': 'torséyeti', 'to overcome': 'térh₂uti', 'to place': 'stnéh₂ti', 'to point out': 'dḗyḱst',
         'to possess': 'h₂eh₂óyḱe', 'to pull': 'déwkti', 'to put': 'dʰéh₁t', 'to recognise': 'ǵn̥h₃sḱéti',
         'to remain': 'h₂wéseti', 'to remember': 'memóne', 'to renew': 'néweh₂ti', 'to ripen': 'pékʷeti',
         'to say (1)': 'mléwHti', 'to say (2)': 'wéwket', 'to scrape': 'ksnéwti', 'to set': 'sodéyeti',
         'to settle': 'tḱéyti', 'to shepherd': 'péh₂sti', 'to sit down': 'sédt', 'to spawn': 'strowéyeti',
         'to speak': 'bʰéh₂ti', 'to split': 'bʰéydt', 'to stand up': 'stéh₂t', 'to step': 'gʷémt',
         'to straighten': 'h₃roǵéyeti', 'to strew': 'strowéyeti', 'to swallow': 'gʷérh₃ti', 'to swim': '(s)néh₂ti',
         'to taste': 'ǵéwseti', 'to transport': 'wḗǵʰst', 'to trust': 'bʰéydʰeti', 'to turn': 'wortéyeti',
         'to want to see': 'wéydseti'}
word_lists['verbs'] = verbs


def sample(d: dict) -> str:
    """
    Sample one value from a PIE vocab list dictionary

    Parameters
    ----------
    d : dict
        PIE vocab dictionary.

    Returns
    -------
    str
        A single word sampled randomly from the dictionary.
    """

    return random.choice(list(d.values()))


def vocab_word(category: str) -> str:
    """
    Sample a word from PIE, given a category.

    Parameters
    ----------
    category : str
        Category of word list to sample.

    Returns
    -------
    str
         A single word sampled randomly from the category.
    """
    if category in word_lists:
        return sample(word_lists[category])
    else:
        return sample(numerals)
