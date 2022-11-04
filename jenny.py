import random
import sys

leetify = False

if sys.argv[1] == "-s":
    silent = True
else:
    silent = False

if len(sys.argv) > 2:
    if sys.argv[2] == "-l":
        leetify = True
    else:
        leetify = False
elif sys.argv[1] == "-l":
    leetify = True

if "-h" in sys.argv:
    print("-h       display this message")
    print("-s       silent mode  | hide title message")
    print("-l       leetify mode | leetify your name with 1337 chars")
else:

    if(not silent):

        title = "_______ _____ "
        a="####### |      l\    |  l\    |  i    i"
        b="   %|   |  *   l \   |  l \   |   i  i"
        c="   ||   |____  l  \  |  l  \  |    ii"
        d="   |^   |      l   \ *  l   \ *    ||"
        e=" \/1    |____  l    \|  l    \|    |l"

        print(title)
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print("JENNY: The 1337 T34M N@Me GENERATOR!")
        print("")

    alphabet = {
    " ":" ",
    "a":"A",
    "b":"b",
    "c":"c",
    "d":"d",
    "e":"3",
    "f":"f",
    "g":"g",
    "h":"h",
    "i":"1",
    "j":"j",
    "k":"k",
    "l":"L",
    "m":"m",
    "n":"n",
    "o":"0",
    "p":"p",
    "q":"Q",
    "r":"R",
    "s":"5",
    "t":"7",
    "u":"u",
    "v":"v",
    "w":"w",
    "x":"X",
    "y":"y",
    "z":"Z",
    "(":"(",
    ")":")",
    "-":"-",
    "/":"/",
    "&":"&",
    "é":"é"
    }

    #todo: use api or wiki to pull word candidates
    #todo: add arguments for user customisation

    f = [
    'the',
    "adorable",
    "agreeable",
    "amused",
    "annoying",
    "ashamed",
    "awful",
    "better",
    "bloody",
    "blushing",
    "brave",
    "busy",
    "cautious",
    "clean",
    "cloudy",
    "combative",
    "condemned",
    "courageous",
    "crowded",
    "cute",
    "dead",
    "delightful",
    "different",
    "distinct",
    "doubtful",
    "adventurous",
    "alert",
    "angry",
    "anxious",
    "attractive",
    "bad",
    "bewildered",
    "blue",
    "bored",
    "breakable",
    "calm",
    "charming",
    "clear",
    "clumsy",
    "comfortable",
    "confused",
    "crazy",
    "cruel",
    "dangerous",
    "defeated",
    "depressed",
    "difficult",
    "disturbed",
    "drab",
    "aggressive",
    "alive",
    "annoyed",
    "arrogant",
    "average",
    "beautiful",
    "black",
    "blue-eyed",
    "brainy",
    "bright",
    "careful",
    "cheerful",
    "clever",
    "colorful",
    "concerned",
    "cooperative",
    "creepy",
    "curious",
    "dark",
    "defiant",
    "determined",
    "disgusted",
    "dizzy",
    "dull",
    "eager",
    "elegant",
    "encouraging",
    "envious",
    "expensive",
    "faithful",
    "fantastic",
    "fine",
    "frail",
    "frightened",
    "gifted",
    "glorious",
    "graceful",
    "grumpy",
    "healthy",
    "hilarious",
    "horrible",
    "ill",
    "inexpensive",
    "itchy",
    "jolly",
    "easy",
    "embarrassed",
    "energetic",
    "evil",
    "exuberant",
    "famous",
    "fierce",
    "foolish",
    "frantic",
    "funny",
    "glamorous",
    "good",
    "grieving",
    "handsome",
    "helpful",
    "homeless",
    "hungry",
    "important",
    "innocent",
    "jealous",
    "joyous",
    "elated",
    "enchanting",
    "enthusiastic",
    "excited",
    "fair",
    "fancy",
    "filthy",
    "fragile",
    "friendly",
    "gentle",
    "gleaming",
    "gorgeous",
    "grotesque",
    "happy",
    "helpless",
    "homely",
    "hurt",
    "impossible",
    "inquisitive",
    "jittery",
    "kind",
    "lazy",
    "lonely",
    "lucky",
    "modern",
    "mushy",
    "naughty",
    "nutty",
    "odd",
    "outrageous",
    "perfect",
    "poised",
    "precious",
    "putrid",
    "real",
    "rich",
    "shiny",
    "sleepy",
    "sore",
    "spotless",
    "stupid",
    "light",
    "long",
    "magnificent",
    "motionless",
    "mysterious",
    "nervous",
    "obedient",
    "old",
    "outstanding",
    "plain",
    "poor",
    "prickly",
    "puzzled",
    "relieved",
    "scary",
    "shy",
    "smiling",
    "sparkling",
    "stormy",
    "successful",
    "lively",
    "lovely",
    "misty",
    "muddy",
    "nasty",
    "nice",
    "obnoxious",
    "open",
    "panicky",
    "pleasant",
    "powerful",
    "proud",
    "quaint",
    "repulsive",
    "selfish",
    "silly",
    "smoggy",
    "splendid",
    "strange",
    "super",
            ]
    m = [
    "absolute zero",
    "Acid green",
    "Aero",
    "African violet",
    "Air superiority blue",
    "Alice blue",
    "Alizarin",
    "Alloy orange",
    "Almond",
    "Amaranth deep purple",
    "Amaranth pink",
    "Amaranth purple",
    "Amazon",
    "Amber",
    "Amethyst",
    "Android green",
    "Antique brass",
    "Antique bronze",
    "Antique fuchsia",
    "Antique ruby",
    "Antique white",
    "Apricot",
    "Aqua",
    "Aquamarine",
    "Arctic lime",
    "Artichoke green",
    "Arylide yellow",
    "Ash gray",
    "Atomic tangerine",
    "Aureolin",
    "Azure",
    "Azure (X11/web color)",
    "Baby blue",
    "Baby blue eye",
    "Baby pink",
    "Baby powder",
    "Baker-Miller pink",
    "Banana Mania",
    "Barn red",
    "Battleship grey",
    "Beau blue",
    "Beaver",
    "Beige",
    "Bdazzled blue",
    "Big dip oruby",
    "Bisque",
    "Bistre",
    "Bistre brown",
    "Bitter lemon",
    "Black",
    "Black bean",
    "Black coral",
    "Black olive",
    "Black Shadows",
    "Blanched almond",
    "Blast-off bronze",
    "Bleu de France",
    "Blizzard blue",
    "Blood red",
    "Blue",
    "Blue (Crayola)",
    "Blue (Munsell)",
    "Blue (NCS)",
    "Blue (Pantone)",
    "Blue (pigment)",
    "Blue bell",
    "Blue-gray (Crayola)",
    "Blue jean",
    "Blue sapphire",
    "Blue-violet",
    "Blue yonder",
    "Bluetiful",
    "Blush",
    "Bole",
    "Bone",
    "Brick red",
    "Bright lilac",
    "Bright yellow (Crayola)",
    "Bronze",
    "Brown sugar",
    "Bud green",
    "Buff",
    "Burgundy",
    "Burlywood",
    "Burnished brown",
    "Burnt orange",
    "Burnt sienna",
    "Burnt umber",
    "Byzantine",
    "Byzantium",
    "Cadet blue",
    "Cadet grey",
    "Cadmium green",
    "Cadmium orange",
    "Café au lait",
    "Café noir",
    "Cambridge blue",
    "Camel",
    "Cameo pink",
    "Canary",
    "Canary yellow",
    "Candy pink",
    "Cardinal",
    "Caribbean green",
    "Carmine",
    "Carmine (M&P)",
    "Carnation pink",
    "Carnelian",
    "Carolina blue",
    "Carrot orange",
    "Catawba",
    "Cedar Chest",
    "Celadon",
    "Celeste",
    "Cerise",
    "Cerulean",
    "Cerulean blue",
    "Cerulean frost",
    "Cerulean (Crayola)",
    "Champagne",
    "Champagne pink",
    "Charcoal",
    "Charm pink",
    "Chartreuse (web)",
    "Cherry blossom pink",
    "Chestnut",
    "Chili red",
    "China pink",
    "Chinese red",
    "Chinese violet",
    "Chinese yellow",
    "Chocolate",
    "Chocolate",
    "Cinnabar",
    "Cinnamon Satin",
    "Citrine",
    "Citron",
    "Claret",
    "Coffee",
    "Columbia Blue",
    "Congo pink",
    "Cool grey",
    "Copper",
    "Copper (Crayola)",
    "Copper penny",
    "Copper red",
    "Copper rose",
    "Coquelicot",
    "Coral",
    "Coral pink",
    "Cordovan",
    "Corn",
    "Cornflower blue",
    "Cornsilk",
    "Cosmic cobalt",
    "Cosmic latte",
    "Coyote brown",
    "Cotton candy",
    "Cream",
    "Crimson",
    "Crimson (UA)",
    "Cultured",
    "Cyan",
    "Cyan (process)",
    "Cyber grape",
    "Cyber yellow",
    "Cyclamen",
    "Dark brown",
    "Dark byzantium",
    "Dark cyan",
    "Dark electric blue",
    "Dark goldenrod",
    "Dark green (X11)",
    "Dark jungle green",
    "Dark khaki",
    "Dark lava",
    "Dark liver",
    "Dark magenta",
    "Dark olive green",
    "Dark orange",
    "Dark orchid",
    "Dark purple",
    "Dark red",
    "Dark salmon",
    "Dark sea green",
    "Dark sienna",
    "Dark sky blue",
    "Dark slate blue",
    "Dark slate gray",
    "Dark spring green",
    "Dark turquoise",
    "Dark violet",
    "Davys grey",
    "Deep cerise",
    "Deep champagne",
    "Deep chestnut",
    "Deep jungle green",
    "Deep pink",
    "Deep saffron",
    "Deep sky blue",
    "Deep Space Sparkle",
    "Deep taupe",
    "Denim",
    "Denim blue",
    "Desert",
    "Desert sand",
    "Dim gray",
    "Dodger blue",
    "Drab dark brown",
    "Duke blue",
    "Dutch white",
    "Ebony",
    "Ecru",
    "Eerie black",
    "Eggplant",
    "Eggshell",
    "Electric lime",
    "Electric purple",
    "Electric violet",
    "Emerald",
    "Eminence",
    "English lavender",
    "English red",
    "English vermillion",
    "English violet",
    "Erin",
    "Eton blue",
    "Fallow",
    "Falu red",
    "Fandango",
    "Fandango pink",
    "Fawn",
    "Fern green",
    "Field drab",
    "Fiery rose",
    "Finn",
    "Firebrick",
    "Fire engine red",
    "Flame",
    "Flax",
    "Flirty",
    "Floral white",
    "Forest green (web)",
    "French beige",
    "French bistre",
    "French blue",
    "French fuchsia",
    "French lilac",
    "French lime",
    "French mauve",
    "French pink",
    "French raspberry",
    "French sky blue",
    "French violet",
    "Frostbite",
    "Fuchsia",
    "Fuchsia (Crayola)",
    "Fulvous",
    "Fuzzy Wuzzy"
            ]
    l = [
    "Actor",
    "Advertisement",
    "Afternoon",
    "Airport",
    "Ambulance",
    "Animal",
    "Answer",
    "Apple",
    "Army",
    "Australia",
    "Balloon",
    "Banana",
    "Battery",
    "Beach",
    "Beard",
    "Bed",
    "Belgium",
    "Boy",
    "Branch",
    "Breakfast",
    "Brother",
    "Camera",
    "Candle",
    "Car",
    "Caravan",
    "Carpet",
    "Cartoon",
    "Church",
    "Crayon",
    "Crowd",
    "Daughter",
    "Death",
    "Denmark",
    "Diamond",
    "Dinner",
    "Disease",
    "Doctor",
    "Dog",
    "Dream",
    "Dress",
    "Easter",
    "Egg",
    "Eggplant",
    "Egypt",
    "Elephant",
    "Energy",
    "Engine",
    "England",
    "Evening",
    "Eye",
    "Family",
    "Finland",
    "Fish",
    "Flag",
    "Flower",
    "Football",
    "Forest",
    "Fountain",
    "France",
    "Furniture",
    "Garage",
    "Gold",
    "Grass",
    "Greece",
    "Guitar",
    "Hair",
    "Hamburger",
    "Helicopter",
    "Helmet",
    "Holiday",
    "Honey",
    "Horse",
    "Hospital",
    "House",
    "Hydrogen",
    "Ice",
    "Insect",
    "Insurance",
    "Iron",
    "Island",
    "Jackal",
    "Jelly",
    "Jewellery",
    "Jordan",
    "Juice",
    "Kangaroo",
    "King",
    "Kitchen",
    "Kite",
    "Knife",
    "Lamp",
    "Lawyer",
    "Leather",
    "Library",
    "Lighter",
    "Lion",
    "Lizard",
    "Lock",
    "London",
    "Lunch",
    "Machine",
    "Magazine",
    "Magician",
    "Manchester",
    "Market",
    "Match",
    "Microphone",
    "Monkey",
    "Morning",
    "Motorcycle",
    "Nail",
    "Napkin",
    "Needle",
    "Nest",
    "Nigeria",
    "Night",
    "Notebook",
    "Ocean",
    "Oil",
    "Orange",
    "Oxygen",
    "Oyster",
    "Ghost",
    "Painting",
    "Parrot",
    "Pencil",
    "Piano",
    "Pillow",
    "Pizza",
    "Planet",
    "Plastic",
    "Portugal",
    "Potato",
    "Queen",
    "Quill",
    "Rain",
    "Rainbow",
    "Raincoat",
    "Refrigerator",
    "Restaurant",
    "River",
    "Rocket",
    "Room",
    "Rose",
    "Russia",
    "Sandwich",
    "School",
    "Scooter",
    "Shampoo",
    "Shoe",
    "Soccer",
    "Spoon",
    "Stone",
    "Sugar",
    "Sweden",
    "Teacher",
    "Telephone",
    "Television",
    "Tent",
    "Thailand",
    "Tomato",
    "Toothbrush",
    "Traffic",
    "Train",
    "Truck",
    "Uganda",
    "Umbrella",
    "Van",
    "Vase",
    "Vegetable",
    "Vulture",
    "Wall",
    "Whale",
    "Window",
    "Wire",
    "Xylophone",
    "Yacht",
    "Yak",
    "Zebra",
    "Zoo",
    "Garden",
    "Gas",
    "Girl",
    "Glass",
            ]

    x = random.randint(0, len(f)-1)
    a = f[x].lower()
    y = random.randint(0, len(m)-1)
    b = m[y].lower()
    z = random.randint(0, len(l)-1)
    c = l[z].lower()


    name = a+" "+b+"-"+c+"s"
    newname = ""

    def leetify_func(name):
        newname = ""
        count = 0
        for i in name:
            if count % 2 == 0:
                newname = newname + ''.join(alphabet.get(i))
            else: newname = newname + i
            count += 1
        return newname

    if(leetify == True):
        newname = leetify_func(name)

    if(not silent):
        print("Your team name: ", newname) 
        print("Your non-leet name: ", name) 
    elif(silent == True and leetify == True):
        print(newname)
    else:
        print(name)


