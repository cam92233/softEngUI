#coding: utf-8
# 15 books
# https://play.google.com/store/books/details/Dr_Seuss_Green_Eggs_and_Ham?id=ZK7xAwAAQBAJ
class Book:
  def __init__(self, subject="Fiction", title=None, isbn=None, author=None, detail=None, price=5.00, pic_url=None, promo=0, amount=5):
    self.attributes = [subject, title, isbn, author, detail, price, pic_url, promo, amount]
  def printBook(self):
    a = self.attributes
    string = "INSERT INTO `books` VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8])
    print string
    return string

Booklist = list()

title="The Outsiders"
isbn=9781101642610
author="S.E. Hinton"
detail="No one ever said life was easy. But Ponyboy is pretty sure that he's got things figured out. He knows that he can count on his brothers, Darry and Sodapop. And he knows that he can count on his friends-true friends who would do anything for him, like Johnny and Two-Bit. But not on much else besides trouble with the Socs, a vicious gang of rich kids whose idea of a good time is beating up on “greasers” like Ponyboy. At least he knows what to expect-until the night someone takes things too far. The Outsiders is a dramatic and enduring work of fiction that laid the groundwork for the YA genre. S. E. Hinton's classic story of a boy who finds himself on the outskirts of regular society remains as powerful today as it was the day it was first published."
pic_url="https://books.google.com/books/content/images/frontcover/ha6GIYze5lEC?fife=w400-h600"
Outsiders = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(Outsiders)

title="It"
isbn=9781501141232
author="Stephen King"
detail="Welcome to Derry, Maine. It’s a small city, a place as hauntingly familiar as your own hometown. Only in Derry the haunting is real.\
They were seven teenagers when they first stumbled upon the horror. Now they are grown-up men and women who have gone out into the big world to gain success and happiness. But the promise they made twenty-eight years ago calls them reunite in the same place where, as teenagers, they battled an evil creature that preyed on the city’s children. Now, children are being murdered again and their repressed memories of that terrifying summer return as they prepare to once again battle the monster lurking in Derry’s sewers."
pic_url="https://books.google.com/books/content/images/frontcover/-rUACwAAQBAJ?fife=w400-h600"
It = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(It)

title="Fifty Shades of Grey"
isbn=9781612130293
author="E. L. James"
detail="When literature student Anastasia Steele goes to interview young entrepreneur Christian Grey, she encounters a man who is beautiful, brilliant, and intimidating. The unworldly, innocent Ana is startled to realize she wants this man and, despite his enigmatic reserve, finds she is desperate to get close to him. Unable to resist Ana’s quiet beauty, wit, and independent spirit, Grey admits he wants her, too—but on his own terms.\
Shocked yet thrilled by Grey’s singular erotic tastes, Ana hesitates. For all the trappings of success—his multinational businesses, his vast wealth, his loving family—Grey is a man tormented by demons and consumed by the need to control. When the couple embarks on a daring, passionately physical affair, Ana discovers Christian Grey’s secrets and explores her own dark desires."
pic_url="https://books.google.com/books/content/images/frontcover/qDP6NmRAPzsC?fife=w400-h600"
FiftyShadesOfGrey = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(FiftyShadesOfGrey)

title="Fifty Shades of Grey Tentacles"
isbn=None
author="Anita Dobs"
detail="Elle James, a virginal and award winning erotica author in the college Erotic Writing Club, is one day asked to do a favor by her friend, fellow erotic writing buff, Sarah. The favor is simple, all Elle has to do is take Sarah's place and interview a world famous billionaire BDSM expert. Elle realizes the interview could really help her out with research for one of her upcoming BDSM books, and so agrees.As a strong and willful girl, Elle has no actual interest in pursuing a BDSM lifestyle, knowing that she's just not suited to it at all. But when she arrives and meets Mr. Grey at his corporation headquarters, she becomes confused, as she feels he's bending her to his will. Mr. Grey, a handsome billionaire, has a deep and dark secret though (no, not the one you're thinking of, another deep and dark secret.) Having taken on many a submissive before, he finds there is something different about Elle, something that intrigues him. Not sure whether to confide everything in Elle and trust her, the pair however embark on a sexual journey that will take Elle to her extremes, and will force Mr. Grey to make a decision that could result in his ruin..."
pic_url="https://books.google.com/books/content/images/frontcover/amdOAgAAQBAJ?fife=w400-h600"
FiftyShadesOfGreyTentacles = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(FiftyShadesOfGreyTentacles)

title="The Subtle Art of Not Giving a F*ck: A Counterintuitive Approach to Living a Good Life"
isbn=9780062457738
author="Mark Manson"
detail='"In this generation-defining self-help guide, a superstar blogger cuts through the crap to show us how to stop trying to be "positive" all the time so that we can truly become better, happier people.\
For decades, we’ve been told that positive thinking is the key to a happy, rich life. "F**k positivity," Mark Manson says. "Let’s be honest, shit is f**ked and we have to live with it." In his wildly popular Internet blog, Manson doesn’t sugarcoat or equivocate. He tells it like it is—a dose of raw, refreshing, honest truth that is sorely lacking today. The Subtle Art of Not Giving a F**k is his antidote to the coddling, let’s-all-feel-good mindset that has infected American society and spoiled a generation, rewarding them with gold medals just for showing up.\
Manson makes the argument, backed both by academic research and well-timed poop jokes, that improving our lives hinges not on our ability to turn lemons into lemonade, but on learning to stomach lemons better. Human beings are flawed and limited—"not everybody can be extraordinary, there are winners and losers in society, and some of it is not fair or your fault." Manson advises us to get to know our limitations and accept them. Once we embrace our fears, faults, and uncertainties, once we stop running and avoiding and start confronting painful truths, we can begin to find the courage, perseverance, honesty, responsibility, curiosity, and forgiveness we seek.\
There are only so many things we can give a f**k about so we need to figure out which ones really matter, Manson makes clear. While money is nice, caring about what you do with your life is better, because true wealth is about experience. A much-needed grab-you-by-the-shoulders-and-look-you-in-the-eye moment of real-talk, filled with entertaining stories and profane, ruthless humor, The Subtle Art of Not Giving a F**k is a refreshing slap for a generation to help them lead contented, grounded lives."'
pic_url="https://books.google.com/books/content/images/frontcover/yng_CwAAQBAJ?fife=w200-h300"
TheSubtleArt = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(TheSubtleArt)

title="The Art of War"
isbn=9789380914893
author="Sun Tzu"
detail="The Art of War is a translation of Sun Tzu’s originally written book on battle strategies by author James Clavell. Sun Tzu believed war to be an essential wrongdoing that must be got rid of whenever it can be. The war should be fought fleetingly to reduce economic decline. Sun Tzu harped on the significance of placement in military tactics. The planning to position an army must be dependent on the stipulations in the physical surroundings and the subjective thoughts of various militants in those conditions. He believed that strategy cannot be considered as planning with respect to glancing through a previously decided list. It is better represented by the fact that it needs speedy and suitable reactions to altering situations. Planning gives results in restrained surroundings. But in case of an altering environment, similar plans come in each other’s ways and give rise to undesired outcomes. The book has been a profound factor in the workings of Eastern and Western military strategies, business planning, legal thought processes, and more."
pic_url="https://books.google.com/books/content/images/frontcover/yec-DAAAQBAJ?fife=w400-h600"
TheArtOfWar = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(TheArtOfWar)

title="Moby Dick"
isbn=9781504041195
author="Herman Melville"
detail="Despite strange warnings, Ishmael, a young schoolteacher from Manhattan, signs up for a voyage aboard the Pequod, a whaling ship departing from New Bedford, Massachusetts. While on shore, he strikes up a friendship with Queequeg, a tattooed South Seas cannibal. The unlikely friends are hired for the journey—only to discover their commander will be Captain Ahab, a brooding, one-legged, tyrannical old man fixated on avenging Moby Dick, the great white whale who crippled him."
pic_url="https://books.google.com/books/content/images/frontcover/lv0lDQAAQBAJ?fife=w400-h600"
MobyDick = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(MobyDick)

title="Treasure Island"
isbn=9781773130439
author="Robert Louis Stevenson"
detail='"Treasure Island is an adventure novel by Scottish author Robert Louis Stevenson, narrating a tale of "buccaneers and buried gold". It was originally serialized in the childrens magazine Young Folks between 1881 through 1882 under the title Treasure Island, or the mutiny of the Hispaniola, credited to the pseudonym "Captain George North". It was first published as a book on 14 November 1883 by Cassell & Co. Treasure Island is traditionally considered a coming-of-age story, and is noted for its atmosphere, characters, and action. It is also noted as a wry commentary on the ambiguity of morality—as seen in Long John Silver—unusual for childrens literature. It is one of the most frequently dramatized of all novels. Its influence is enormous on popular perceptions of pirates, including such elements as treasure maps marked with an "X", schooners, the Black Spot, tropical islands, and one-legged seamen bearing parrots on their shoulders."'
pic_url="https://books.google.com/books/content/images/frontcover/KMkDDQAAQBAJ?fife=w400-h600"
TreasureIsland = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(TreasureIsland)

title="Stripper Confessions 1: The Complete Series"
isbn=None
author="Solae Dehvine"
detail="Lauren is a pre-med student by day and a pole swinger by night. Lines become blurred when her roommate asks for help into the profession. Lauren soon finds out that sometimes friends and money don't mix. The strip club can make any beautiful young lady rich but at what cost."
pic_url="https://books.google.com/books/content/images/frontcover/oND_AgAAQBAJ?fife=w400-h600"
TheArtOfWar = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(TheArtOfWar)

title="The Holy Bible: King James Version"
isbn=9783736801493
author="King James Version"
detail="The Holy Bible. As interpreted in the King James Version."
pic_url="https://books.google.com/books/content/images/frontcover/WFxoAwAAQBAJ?fife=w400-h600"
Bible = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(Bible)

title="The Communist Manifesto"
isbn=9780857190079
author="Karl Marx"
detail="This book is essential for anyone seeking to understand the history of the 19th and 20th centuries. Comprehending the motives and actions of many of its leading figures is impossible unless one has read this key text. 'The Communist Manifesto' left its mark upon the souls of leaders and rebels alike and shaped the deeds of whole nations for the greater part of 100 years. It could also be said to have led indirectly to the violent death of hundreds of millions of people."
pic_url="https://books.google.com/books/content/images/frontcover/0D3y6YG0z6sC?fife=w400-h600"
SeizingTheMeansOfProduction = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(SeizingTheMeansOfProduction)

title="The Three Musketeers"
isbn=9781504033800
author="Alexandre Dumas"
detail="D’Artagnan journeys to Paris armed with nothing but his sword, his courage, and a burning desire to prove his mettle as a member of King Louis XIII’s elite guardsmen. A swashbuckling corps of gentlemen rogues, the Musketeers live to antagonize Cardinal Richelieu and sweep every woman in France off her feet. Before d’Artagnan can join their ranks, however, he must distinguish himself on the field of battle."
pic_url="https://books.google.com/books/content/images/frontcover/4VpsCwAAQBAJ?fife=w400-h600"
Musketeers = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(Musketeers)

title="The Theory of Relativity: And Other Essays"
isbn=9781453204696
author="Albert Einstein"
detail="In this collection of his seven most important essays on physics, Einstein guides his reader step-by-step through the many layers of scientific theory that formed a starting point for his discoveries. By both supporting and refuting the theories and scientific efforts of his predecessors, Einstein reveals in a clear voice the origins and meaning of such significant topics as physics and reality, the fundamentals of theoretical physics, the common language of science, the laws of science and of ethics, and an elementary derivation of the equivalence of mass and energy."
pic_url="https://books.google.com/books/content/images/frontcover/Smz0WDomeqAC?fife=w400-h600"
Einstein = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(Einstein)

title="Alice’s Adventures in Wonderland "
isbn=9780007382484
author="Lewis Carroll"
detail="‘Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, “and what is the use of a book,” thought Alice, “without pictures or conversations?”’ So begins the tale of Alice, who follows a curious White Rabbit down a hole and falls into Wonderland, a fantastical place where nothing is quite as it seems: animals talk, nonsensical characters confuse, Mad Hatters throw tea parties and the Queen plays croquet. Alice’s attempts to find her way home become increasingly bizarre, infuriating and amazing in turn."
pic_url="https://books.google.com/books/content/images/frontcover/sK4x05-Mk8wC?fife=w400-h600"
Alice = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(Alice)

title="Twilight"
isbn=9780316007443
author="Stephenie Meyer"
detail="Isabella Swan's move to Forks, a small, perpetually rainy town in Washington, could have been the most boring move she ever made. But once she meets the mysterious and alluring Edward Cullen, Isabella's life takes a thrilling and terrifying turn. Up until now, Edward has managed to keep his vampire identity a secret in the small community he lives in, but now nobody is safe, especially Isabella, the person Edward holds most dear. The lovers find themselves balanced precariously on the point of a knife-between desire and danger.Deeply romantic and extraordinarily suspenseful, Twilight captures the struggle between defying our instincts and satisfying our desires. This is a love story with bite."
pic_url="https://books.google.com/books/content/images/frontcover/ZfjzX7M8zt0C?fife=w200-h300"
Twilight = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(Twilight)

title="The Da Vinci Code"
isbn=9786022911845
author="Dan Brown"
detail="While in Paris, Harvard symbologist Robert Langdon is awakened by a phone call in the dead of the night. The elderly curator of the Louvre has been murdered inside the museum, his body covered in baffling symbols. As Langdon and gifted French cryptologist Sophie Neveu sort through the bizarre riddles, they are stunned to discover a trail of clues hidden in the works of Leonardo da Vinci—clues visible for all to see and yet ingeniously disguised by the painter."
pic_url="https://books.google.com/books/content/images/frontcover/6-pmDwAAQBAJ?fife=w400-h600"
DaVinci = Book(title=title, isbn=isbn, author=author, detail=detail, pic_url=pic_url)
Booklist.append(DaVinci)

for i in Booklist:
  i.printBook()