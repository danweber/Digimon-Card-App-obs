wikiLink = 'https://digimoncardgame.fandom.com'
promo = '/wiki/P-'
gallery = '/Gallery'
ruling = '/Rulings'
cardCount = 0
normalCards = []
cards = []
rulings = {}
cardLinks = []
wikiPageLinks = [
    {'name': '▹RELEASE SPECIAL BOOSTER 1.0 [BT01-BT03]',
     'url': 'https://digimoncardgame.fandom.com/wiki/BT01-03:_Release_Special_Booster_Ver.1.0'},
    {'name': '▹RELEASE SPECIAL BOOSTER 1.5 [BT01-BT03]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT01-03:_Release_Special_Booster_Ver.1.5'},
    {'name': '▹BOOSTER GREAT LEGEND [BT04]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-04:_Booster_Great_Legend'},
    {'name': '▹BOOSTER BATTLE OF OMNI [BT05]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-05:_Booster_Battle_Of_Omni'},
    {'name': '▹BOOSTER DOUBLE DIAMOND [BT06]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-06:_Booster_Double_Diamond'},
    {'name': '▹BOOSTER NEXT ADVENTURE [BT07]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-07:_Booster_Next_Adventure'},
    {'name': '▹BOOSTER NEW AWAKENING [BT08]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-08:_Booster_New_Awakening'},
    {'name': '▹BOOSTER X RECORD [BT09]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-09:_Booster_X_Record'},
    {'name': '▹BOOSTER XROS ENCOUNTER [BT10]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-10:_Booster_Xros_Encounter'},
    {'name': '▹BOOSTER DIMENSIONAL PHASE [BT11]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-11:_Booster_Dimensional_Phase'},
    {'name': '▹BOOSTER ACROSS TIME [BT12]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-12:_Booster_Across_Time'},
    {'name': '▹BOOSTER VERSUS ROYAL KNIGHT [BT13]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-13:_Booster_Versus_Royal_Knights'},
    {'name': '▹BOOSTER BLAST ACE [BT14]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-14:_Booster_Blast_Ace'},
    {'name': '▹BOOSTER EXCEED APOCALYPSE [BT15]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-15:_Booster_Exceed_Apocalypse'},
    {'name': '▹BOOSTER BEGINNING OBSERVER [BT16]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-16:_Booster_Beginning_Observer'},
    {'name': '▹BOOSTER SECRET CRISIS [BT17]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-17:_Booster_Secret_Crisis'},
    {'name': '▹BOOSTER ELEMENTAL SUCCESSOR [BT18]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-18:_Booster_Elemental_Successor'},
      {'name': '▹BOOSTER XROS EVOLUTION [BT19]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-19:_Booster_Xros_Evolution'},
    {'name': '▹SPECIAL BOOSTER VER.2.0 [BT18-BT19]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT18-19:_Special_Booster_Ver.2.0'},
    {'name': '▹SPECIAL BOOSTER VER.2.5 [BT19-BT20]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT19-20:_Special_Booster_Ver.2.5'},
    {'name': '▹BOOSTER WORLD COMVERGENCE [BT21]',
        'url': 'https://digimoncardgame.fandom.com/wiki/BT-21:_Booster_World_Convergence'},
  
    {'name': '▹THEME BOOSTER CLASSIC COLLECTION [EX01]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-01:_Theme_Booster_Classic_Collection'},
    {'name': '▹THEME BOOSTER DIGITAL HAZARD [EX02]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-02:_Theme_Booster_Digital_Hazard'},
    {'name': '▹THEME BOOSTER DRAGONIC ROAR [EX03]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-03:_Theme_Booster_Draconic_Roar'},
    {'name': '▹THEME BOOSTER ALTERNATIVE BEING [EX04]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-04:_Theme_Booster_Alternative_Being'},
    {'name': '▹THEME BOOSTER ANIMAL COLOSSEUM [EX05]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-05:_Theme_Booster_Animal_Colosseum'},
    {'name': '▹THEME BOOSTER INFERNAL ASCENSION [EX06]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-06:_Theme_Booster_Infernal_Ascension'},
    {'name': '▹EXTRA BOOSTER DIGIMON LIBERATOR [EX07]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-07:_Extra_Booster_Digimon_Liberator'},
      {'name': '▹EXTRA BOOSTER CHAIN OF LIBERATION [EX08]',
        'url': 'https://digimoncardgame.fandom.com/wiki/EX-08:_Extra_Booster_Chain_of_Liberation'},

    {'name': 'BOOSTER RESURGENCE BOOSTER [RB1]',
        'url': 'https://digimoncardgame.fandom.com/wiki/RB-01:_Resurgence_Booster'},

    {'name': 'STARTER DECK GAIA RED [ST1]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-1:_Starter_Deck_Gaia_Red'},
    {'name': 'STARTER DECK COCYTUS BLUE [ST2]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-2:_Starter_Deck_Cocytus_Blue'},
    {'name': 'STARTER DECK HEAVEN\'S Yellow[ST3]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-3:_Starter_Deck_Heaven%27s_Yellow'},
    {'name': 'STARTER DECK GIGA GREEN [ST4]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-4:_Starter_Deck_Giga_Green'},
    {'name': 'STARTER DECK MACHINE BLACK [ST5]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-5:_Starter_Deck_Machine_Black'},
    {'name': 'STARTER DECK VENOMOUS VIOLET [ST6]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-6:_Starter_Deck_Venomous_Violet'},
    {'name': 'STARTER DECK GALLANTMON [ST7]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-7:_Starter_Deck_Gallantmon'},
    {'name': 'STARTER DECK ULLFORCEVEEDRAMON [ST8]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-8:_Starter_Deck_UlforceVeedramon'},
    {'name': 'STARTER DECK ULTIMATE ANCIENT DRAGON [ST9]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-9:_Starter_Deck_Ultimate_Ancient_Dragon'},
    {'name': 'STARTER DECK PARALLEL WORLD TACTICIAN [ST10]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-10:_Starter_Deck_Parallel_World_Tactician'},
    {'name': 'STARTER DECK JESMON [ST12]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-12:_Starter_Deck_Jesmon'},
    {'name': 'STARTER DECK RAGNALOARDMON[ST13]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-13:_Starter_Deck_RagnaLoardmon'},
    {'name': 'ADVANCE DECK BEELZEMON [ST14]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-14:_Advanced_Deck_Set_Beelzemon'},
    {'name': 'STARTER DECK DRAGON OF COURAGE [ST15]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-15:_Starter_Deck_Dragon_of_Courage'},
    {'name': 'STARTER DECK WOLF OF FRIENDSHIP [ST16]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-16:_Starter_Deck_Wolf_of_Friendship'},
    {'name': 'STARTER DECK DOUBLE TYPHOON [ST17]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-17:_Advanced_Deck_Set_Double_Typhoon'},
    {'name': 'STARTER DECK GUARDIAN VORTEX [ST18]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-18:_Starter_Deck_Guardian_Vortex'},
    {'name': 'STARTER DECK FABLE WALTZ [ST19]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-19:_Starter_Deck_Fable_Waltz'},
    {'name': 'STARTER DECK PROTECTOR OF LIGHT [ST20]',
        'url': 'https://digimoncardgame.fandom.com/wiki/ST-20:_Starter_Deck_Protector_of_Light'},
    {'name': 'STARTER DECK HERO OF HOPE [ST21]',
       'url': 'https://digimoncardgame.fandom.com/wiki/ST-21:_Starter_Deck_Hero_of_Hope'},
  
    {'name': 'LIMITED PACK DIGIMON GHOST GAME',
        'url': 'https://digimoncardgame.fandom.com/wiki/LM-01:_Limited_Pack_Digimon_Ghost_Game'},
    {'name': 'LIMITED PACK DIGIMON DEATHXMON',
        'url': 'https://digimoncardgame.fandom.com/wiki/LM-02:_Limited_Pack_DeathXmon'},
    {'name': 'LM-03: Limited Card Set 2024',
        'url': 'https://digimoncardgame.fandom.com/wiki/LM-03:_Limited_Card_Set_2024'},
    {'name': 'SPEICIAL LIMITED SET [LM03-04]',
        'url': 'https://digimoncardgame.fandom.com/wiki/Digimon_Card_Game_Special_Limited_Set'},
]
NoteDictionary = {
    'BT01-03: Release Special Booster Ver.1.0': '▹RELEASE SPECIAL BOOSTER 1.0 [BT01-B0T3]',
    'BT01-03: Release Special Booster Ver.1.5': '▹RELEASE SPECIAL BOOSTER 1.5 [BT01-B0T3]',
    'BT-04: Booster Great Legend': '▹BOOSTER GREAT LEGEND [BT04]',
    'BT-05: Booster Battle Of Omni': '▹BOOSTER BATTLE OF OMNI [BT05]',
    'BT-06: Booster Double Diamond': '▹BOOSTER DOUBLE DIAMOND [BT06]',
    'BT-07: Booster Next Adventure': '▹BOOSTER NEXT ADVENTURE [BT07]',
    'BT-08: Booster New Awakening': '▹BOOSTER NEW AWAKENING [BT08]',
    'BT-09: Booster X Record': '▹BOOSTER X RECORD [BT09]',
    'BT-10: Booster Xros Encounter': '▹BOOSTER XROS ENCOUNTER [BT10]',
    'BT-11: Booster Dimensional Phase': '▹BOOSTER DIMENSIONAL PHASE [BT11]',
    'BT-12: Booster Across Time': '▹BOOSTER ACROSS TIME [BT12]',
    'BT-13: Booster Versus Royal Knights': '▹BOOSTER VERSUS ROYAL KNIGHT [BT13]',
    'BT-14: Booster Blast Ace': '▹BOOSTER BLAST ACE [BT14]',
    'BT-15: Booster Exceed Apocalypse': '▹BOOSTER EXCEED APOCALYPSE [BT15]',
    'BT-16: Booster Beginning Observer': '▹BOOSTER BEGINNING OBSERVER [BT16]',
    'BT-17: Booster Secret Crisis': '▹BOOSTER SECRET CRISIS [BT17]',
    'BT-18: Booster Elemental Successor': '▹BOOSTER ELEMENTAL SUCCESSOR [BT18]',
    'BT-19: Booster Xros Evolution': '▹BOOSTER XRO EVOLUTION [BT19]',
    'BT18-19: Special Booster Ver.2.0': '▹SPECIAL BOOSTER VER.2.0 [BT18-19]',
    'BT19-20: Special Booster Ver.2.5': '▹SPECIAL BOOSTER VER.2.5 [BT19-20]',
    'BT-21: Booster World Convergence': '▹BOOSTER WORLD CONVERGENCE [BT21]',

    'EX-01: Theme Booster Classic Collection': '▹THEME BOOSTER CLASSIC COLLECTION [EX01]',
    'EX-02: Theme Booster Digital Hazard': '▹THEME BOOSTER DIGITAL HAZARD [EX02]',
    'EX-03: Theme Booster Draconic Roar': '▹THEME BOOSTER DRAGONIC ROAR [EX03]',
    'EX-04: Theme Booster Alternative Being': '▹THEME BOOSTER ALTERNATIVE BEING [EX04]',
    'EX-05: Theme Booster Animal Colosseum': '▹THEME BOOSTER ANIMAL COLOSSEUM [EX05]',
    'EX-06: Theme Booster Infernal Ascension': '▹THEME BOOSTER INFERNAL ASCENSION [EX06]',
    'EX-07: Extra Booster Digimon Liberator': '▹EXTRA BOOSTER DIGIMON LIBERATOR [EX07]',
    'EX-08: Extra Booster Chain of Liberation': '▹EXTRA BOOSTER CHAIN OF LIBERATION [EX08]',

    'RB-01: Resurgence Booster': 'BOOSTER RESURGENCE BOOSTER [RB01]',

    'ST-1: Starter Deck Gaia Red': 'STARTER DECK GAIA RED [ST01]',
    'ST-2: Starter Deck Cocytus Blue': 'STARTER DECK COCYTUS BLUE [ST02]',
    'ST-3: Starter Deck Heaven\'s Yellow': 'STARTER DECK HEAVEN\'S Yellow[ST03]',
    'ST-4: Starter Deck Giga Green': 'STARTER DECK GIGA GREEN [ST04]',
    'ST-5: Starter Deck Machine Black': 'STARTER DECK MACHINE BLACK [ST05]',
    'ST-6: Starter Deck Venomous Violet': 'STARTER DECK VENOMOUS VIOLET [ST06]',
    'ST-7: Starter Deck Gallantmon': 'STARTER DECK GALLANTMON [ST07]',
    'ST-8: Starter Deck UlforceVeedramon': 'STARTER DECK ULLFORCEVEEDRAMON [ST08]',
    'ST-9: Starter Deck Ultimate Ancient Dragon': 'STARTER DECK ULTIMATE ANCIENT DRAGON [ST09]',
    'ST-10: Starter Deck Parallel World Tactician': 'STARTER DECK PARALLEL WORLD TACTICIAN [ST10]',
    'ST-12: Starter Deck Jesmon': 'STARTER DECK JESMON [ST12]',
    'ST-13: Starter Deck RagnaLoardmon': 'STARTER DECK RAGNALOARDMON[ST13]',
    'ST-14: Advanced Deck Set Beelzemon': 'ADVANCE DECK BEELZEMON [ST14]',
    'ST-15: Starter Deck Dragon of Courage': 'STARTER DECK DRAGON OF COURAGE [ST15]',
    'ST-16: Starter Deck Wolf of Friendship': 'STARTER DECK WOLF OF FRIENDSHIP [ST16]',
    'ST-17: Advanced Deck Set Double Typhoon': 'ADVANCED DECK DOUBLE TYPHOON [ST17]',
    'ST-18: Starter Deck Guardian Vortex': 'STARTER DECK GUARDIAN VORTEX [ST18]',
    'ST-19: Starter Deck Fable Waltz': 'STARTER DECK FABLE WALTZ [ST19]',
    'ST-20: Starter Deck Protector of Light': 'STARTER DECK PROTECTOR OF LIGHT [ST20]',
    'ST-21: Starter Deck Hero Hope': 'STARTER DECK HERO OF HOPE [ST21]',
  
    'LM-01: Limited Pack Digimon Ghost Game': 'LIMITED PACK DIGIMON GHOST GAME [LM01]',
    'LM-02: Limited Pack Digimon DeathXmon': 'LIMITED PACK DIGIMON DEATHXMON [LM02]',
    'LM-03: Limited Pack': 'LIMITED PACK [LM03]',
    'Digimon Card Game Special Limited Set': 'SPEICIAL LIMITED SET [LM03-04]',
}
replacements = [
    '(After this card is placed, by trashing it the next turn or later, activate the effect below.)',
    '(When your other red or black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion).',
    '(When your other black or white Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion).',
    '(When your other black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion).',
    '(This Digimon can attack the turn it comes into play)',
    '(At blocker timing, by suspending this Digimon, it becomes the attack target)',
    '(Trash this card in your battle area to activate the effect below. You can\'t activate this effect the turn this card enters play.)',
    '(When this Digimon attacks and deletes an opponent\'s Digimon and survives the battle, it performs any security checks it normally would)',
    '(Place the top card of your deck on top of your security stack)',
    '(This Digimon can\'t be deleted in battles against Security Digimon)',
    '(Trash all of the digivolution cards on that Digimon.)',
    '(This Digimon checks 1 additional security card.)',
    '(This Digimon checks 1 fewer security cards)',
    '(This Digimon checks 1 additional security card)',
    '(This Digimon checks 2 fewer security cards)',
    '(This Digimon checks 3 fewer security cards)',
    '(This Digimon checks 2 additional security cards)',
    '(Trash up to 2 cards from the top of one of your opponent\'s Digimon. If it has no digivolution cards, or becomes a level 3 Digimon, you can\'t trash any more cards)',
    '(Unsuspend this Digimon during your opponent\'s unsuspend phase)',
    '(Trash up to 4 cards from the top of one of your opponent\'s Digimon. If it has no digivolution cards, or becomes a level 3 Digimon, you can\'t trash any more cards)',
    '(Draw 1 card from your deck.)',
    '(Draw 1 card from your deck)',
    '(Draw 2 cards from your deck)',
    '(Draw 3 cards from your deck)',
    '(When one of your Digimon digivolves into this card from your hand, you may suspend 1 of your Digimon to reduce the memory cost of the digivolution by 2)',
    '(When one of your Digimon digivolves into this card from your hand, you may suspend 1 of your Digimon to reduce the memory cost of the digivolution by 3)',
    '(Trash up to 1 card from the top of one of your opponent\'s Digimon. If it has no digivolution cards, or becomes a level 3 Digimon, you can\'t trash any more cards)',
    '(When this Digimon is deleted after losing a battle, delete the Digimon it was battling)',
    '(This Digimon checks 1 fewer security card)',
    '(Trash all of its digivolution cards.)',
    '(This Digimon can attack the turn it comes into play)',
    '(When this Digimon would be deleted, you may trash the top card of this Digimon to prevent that deletion)',
    '(You may place this card under one of your Tamers)',
    '(If your opponent has 1 or more memory, this Digimon may attack)',
    '(When this Digimon would be deleted, you may place 1 card in this Digimon\'s DigiXros requirements from this Digimon\'s digivolution cards under 1 of your Tamers)',
    '(When this Digimon would be deleted, you may place 2 cards in this Digimon\'s DigiXros requirements from this Digimon\'s digivolution cards under 1 of your Tamers)',
    '(When this Digimon would be deleted, you may place 3 cards in this Digimon\'s DigiXros requirements from this Digimon\'s digivolution cards under 1 of your Tamers)',
    '(When this Digimon would be deleted, you may place 4 cards in this Digimon\'s DigiXros requirements from this Digimon\'s digivolution cards under 1 of your Tamers)',
    '(When one of your other Digimon with [Bagra Army]\u00a0trait would be deleted by an opponent\'s effect, you may delete this Digimon to prevent that deletion)',
    '(When this Digimon attacks, you may switch the target of attack to 1 of your opponent\'s unsuspended Digimon with the highest DP)',
    '(When this Digimon would be deleted, you may suspend it to prevent that deletion)',
    '(When this Digimon would be deleted in battle, by trashing the top card of your security stack, prevent that deletion)',
    '(Your Digimon may digivolve into this card without paying the cost)',
    '(When this card is sent from battle area or under your card to another area, lose 3 memory)',
    '(Place this Tamer under 1 of your Digimon without a Tamer in its digivolution cards)',
    '(Place the top 2 cards of your deck on top of your security stack)',
    '(You may trash 1 of this Digimon\'s digivolution cards to activate the effect below)',
    '(You may trash 2 of this Digimon\'s digivolution cards to activate the effect below)',
    '(You may trash 4 of this Digimon\'s digivolution cards to activate the effect below)',
    '(When this Digimon is deleted after losing a battle, delete the Digimon it was battling.)',
    '(When this Digimon attacks, by suspending 1 of your other Digimon, add the suspended Digimon\'s DP to this Digimon and it gains \uff1cSecurity Attack +1\uff1e for the attack)',
    '(When this Digimon attacks, by suspending 1 of your other Digimon, add the suspended Digimon\'s DP to this Digimon and it gains \uff1cSecurity A. +1\uff1e for the attack)',
    '(Trash up to 3 cards from the top of one of your opponent\'s Digimon. If it has no digivolution cards, or becomes a level 3 Digimon, you can\'t trash any more cards)',
    '(When one of your Digimon digivolves into this card from your hand, you may suspend 1 of your Digimon to reduce the memory cost of the digivolution by 3)',
    '(You may trash 3 of this Digimon\'s digivolution cards to activate the effect below)',
    '(When your other black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(You may trash up to 4 of this Digimon\'s digivolution cards to activate the effect below)',
    '(When this card is sent from battle area or under your card to another area, lose 4 memory)',
    '(When this Digimon is deleted while it has digivolution cards, play it without paying its cost)',
    'When you would play this card, you may place specified cards from your hand/battle area under it. Each placed card reduces the play cost.',
    '(When one of your other black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent that deletion)',
    '(When your other Black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When your other Black/White Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When one of your other red or black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent that deletion)',
    '(When your other black or white Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When your other bagra army Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When your other [D-Brigade] trait Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When your other [Puppet] trait Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When your other Red/Black Digimon would be deleted by an opponent\'s effect, you may delete this Digimon to prevent 1 of those Digimon\'s deletion)',
    '(When this Digimon that has 1 of each specified cards in its digivolution cards would leave the battle area other than by your own effects or by battle, you may play 1 of each card without paying their costs)',
    '(When this Digimon that has 1 of each specified cards in its digivolution cards would leave the battle area other than by your own effects or by battle, you may play 1 of each card without paying their costs)',
    '(1 of your specified Digimon and 1 specified card in hand may DNA digivolve into this card.)',
    '(During this Digimon\'s attack, all of your opponent\'s Digimon gain ＜Blocker＞, and must block if possible)',
    '(Other than against Security Digimon, compare the number of digivolution cards instead of DP in this Digimon's battles)',
    '(At the end of your turn, this Digimon may attack an opponent\'s Digimon. With this effect, it can attack the turn it was played)',
    '(At the end of your turn, by deleting 1 of your Tokens or other [Puppet] trait Digimon, this Digimon attacks a player without suspending)',
    '(At the end of your turn, by deleting 1 of your Tokens or other [Composite] trait Digimon, this Digimon attacks a player without suspending)',
    '(Trash the top card. You can\'t trash past level 3 cards)',
    '(Trash up to 2 cards from the top. You can\'t trash past level 3 cards)',
    '(Trash up to 3 cards from the top. You can\'t trash past level 3 cards)',
    '(Trash up to 4 cards from the top. You can\'t trash past level 3 cards)',
    '(When this Digimon would be deleted, by trashing any 3 of its digivolution cards, it isn\'t deleted)',
    'When this would be played, you may place specified cards from your hand/battle area under it. Each one reduces the play cost.',
    '(As this card moves from the field or under a card to an area other than those, lose 3 memory.)',
    '(As this card moves from the field or under a card to an area other than those, lose 4 memory.)',
    '(As this card moves from the field or under a card to an area other than those, lose 5 memory.)',
    '(Place this Tamer as that Digimon\'s bottom digivolution card if there are no Tamer cards in its digivolution cards)',
    'At the end of the burst digivolution turn, trash this Digimon\'s top card.',
    'Digivolve unsuspended with the 2 specified Digimon stacked on top of each other.',
    'Stack the 2 specified Digimon and digivolve unsuspended.',
    '(When this Digimon with each of the specified digivolution cards would leave the battle area other than by your own effects or by battle, you may play 1 each of the specified cards without paying the costs)',
    '(1 of your specified Digimon and 1 specified card in hand may DNA digivolve into this card)',
    '(When this Digimon would be deleted other than by your effects, by deleting 1 of your other Digimon, prevent that deletion)',
    '(When this Digimon with digivolution cards is deleted, play this card without paying the cost)',
    '(At the end of your turn, by deleting 1 of your Tokens or other [Puppet] trait Digimon, this Digimon attacks a player without suspending)',
    '(At the end of your turn, by deleting 1 of your Tokens or other [Composite] trait Digimon, this Digimon attacks a player without suspending)',
    '(At the end of your turn, by deleting 1 of your Tokens or other [Unidentified] trait Digimon, this Digimon attacks a player without suspending)',
]
