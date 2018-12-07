Description of Problem
- The project is an implementation of the game of Monopoly.

Details Regarding UI
- Select number of players from keyboard.

Python Libraries Used
- pygame
- random
- sys


      - Dice (Felippe) - RollDice() function returns the total for both rolled die. There is a double checker as well for jail.
      
      - Player (Sam) - Player class handles the majority of the logic. It handles painting the players on the board, testing for logical rules that affect the player, and more. 
      
      - Board - The board is painted using the PyGame GUI elements. The player's pawns are placed on each square using absolute positioning. Many elements of the board (buttons, players, etc.) are created and placed in external functions. 
      
      - Chance Deck - The chance deck randomly picks out of a card array of chance objects. It provides monopoly.py with a type of card and the effect the card has on either the users position or wallet. Chance cards are known to be involved more with movement of the player. 
      
      - Community Chest - The community chest deck randomly picks out of a card array of community chest card objects. It provides monopoly.py with a type of card and the effect the card has on either the users position or wallet. Community chest cards are known more for involving the players current money and impacting that.
      
      - Real Estate (Mark) -When a player is taking a turn, they have the option to purchase houses for their properties as long as they have sufficient funds and they do not already have 4 houses on the property. In order to do this, the player must press the "buy houses" button on the bottom of the screen, and then click their mouse on the name of the property that they want to add a house to. This will update their money shown on screen upon completion of the purchase. The number of properties affects the rent that players will pay you when they land on the space. 
      
      - Utility (Chelsea) - Created with the same method as real estate, using a dictionary. Dictionary has many key/value pairs to access different information about utilities, railroads, and properties.
      
      - Railroad (Chelsea) - Same as above.
      
      - Jail (Nick) - Simple function that pushes player's position from the "Go to Jail" square into the jail square, and keeps them there for three rounds.

Other Resources
- button implementation
    https://inventwithpython.com/blog/2012/10/30/designing-a-button-ui-module-for-pygame/

Extra features beyond proposal
- No extra features beyond proposal.

Description of separation of work
- Chelsea implemented
    Jail logic
    Pay rent logic and whether the house is available
    Helper functions in player (buyHouse, payRent, mortgageProperty, buyProperty, isPropertyOwner, checkForMonopoly)
    Half of Estate Dictionary
    Double checking
    writing README
- Mark:
    implemented half of Estate Dictionary
    Assisted with GUI
    assisted with Chance and Community Chest cards
    assisted with takeTurn function in player
- Felippe
    wrote Community Chest and Chance classes
    assisted with takeTurn function
    implemented Dice class
    in Player class implemented the Community Chest and Chance logic
- Nick and Sam
    Board GUI
    Implemented double checking
    Making the game loop
    Making players change position on the board
    Buying houses and checking whether to pay rent or buy the house
    Building player sidebar
    Button class
    Assisted with Chance and Community Chest
