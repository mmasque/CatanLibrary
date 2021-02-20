"""
- Dice rolls
- Cards
- Board 
    - Tile
        attr: resource, number, hasRobber, nodes
        - Nodes
            - Road
            attr: whatIsOnMe
            
- Player
    - Cards
        [Card] {WHEAT, ROCK, BRICK}
    - points
    - SpecialCards
        [Card]
    - resources dictionary
    - buildStuff
    - validActions
    - buildStuff()
    - tradeWith()

- Trading
    - player offers trade
    - each player gets a chance to accept the trade (from tradee's side), 
    automatically rejects if tradee does not have the resources
    function that can return true/false by successive asking for input in a format like:
    Directed at Player x: Player y wants to sell you two wheat in return for 3 bricks do you accept (T/F)?

- Engine
    - validActions for each player
    - modify player points counter
    - end the game
    ?
    - roll dice
"""