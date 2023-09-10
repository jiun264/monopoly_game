import random
from random import randint

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
        self.amount=0

    def get_rent(self):
        return self.price*self.rent

    def sold(self, player):
        self.owner = player
        player.money -= self.price
        player.properties.append(self)


class Tax:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class GoToJail:
    def __init__(self, name):
        self.name = name
        


class Jail:
    def __init__(self, name):
        self.name = name
    
class Card:
    def __init__(self, description, action_type, argu):
        self.description = description
        self.action_type = action_type
        self.argu = argu
    def execute(self, player, space):
        if self.action_type == "teleport":
#            print("going to :", self.argu)
            for i in range(len(space)):
                if(space[i].name == self.argu):
                    player.teleport(i)
                    break
        elif self.action_type == "money":
            player.receive(self.argu)
        elif self.action_type == "FoJ":
            player.in_jail = 0
            player.jdays = 0
        elif self.action_type == "move":
            if(player.position + self.argu < 0):
                player.move(self.argu + len(space), len(space))
            else:
                player.move(self.argu, len(space))
#Chane (desription, action_type, argu)
#description : string
#action_type : "teleport", "money", "move", "FoJ(Free of Jail)"
class Chance:
    def __init__(self):
        self.name = "機會"
        self.cards = [
            Card("前往起點。", "teleport", "出發"),
            Card("前往台中公園。", "teleport", "台中公園"),
            Card("前往逢甲夜市。", "teleport", "逢甲夜市"),
            Card("銀行發放你50元股息。", "money", 50),
            Card("免費出獄一次。", "FoJ", 0),
            Card("往回走三格。", "move", -3),
            Card("向前兩格", "move", 2),
            Card("前往監獄。", "teleport", "監獄"),
            Card("繳納50元貧窮稅。", "money", -50),
            Card("前往中科火車站。", "teleport", "中科火車站"),
            Card("前往逢甲大學。", "teleport", "逢甲大學"),
            Card("你當選為董事長，獲得豐厚的報酬，$200。", "money", 200),
            Card("你的房屋貸款到期,獲得150元。", "money", 150),
            Card("你贏得了一場填字遊戲比賽,獲得100元。", "money", 100),
            Card("公司倒閉", "money", -300),
            Card("遺失金錢", "money", -150)
        ]

    def pick_card(self):
        card = random.choice(self.cards)
        return card


class Board:
    def __init__(self):
        self.spaces = [
            Property('出發', 0, 0),
            Property('彰化師範大學', 60, 0.1),
            Property('靜宜大學', 60, 0.1),
            #Tax('所得稅', 100),
            Property('臺中火車站', 200, 0.1),
            Property('東海大學', 100, 0.1),
            #Property('社區基金', 0, 0),
            Property('逢甲大學', 100, 0.1),
            Property('中興大學', 120, 0.1),
            GoToJail('監獄'),
            Property('逢甲夜市', 140, 0.1),
            Property('臺中市政府', 150, 0.1),
            Property('台中公園', 140, 0.1),
            Property('逢甲大學教學區', 160, 0.1),
            Property('中部科學園區', 200, 0.1),
            Property('一中街商圈', 180, 0.1),
            Property('社區基金', 0, 0),
            Property('豐原高中', 180, 0.1),
            Property('國立自然科學博物館', 200, 0.1),
            Chance(),
            Property('台中車站', 320, 0.1),
            Property('台中二中', 220, 0.1),
#            Property('機會', 0, 0),
            Property('大坑風景區', 220, 0.1),
            Property('麗寶樂園', 240, 0.1),
            Property('台中港鐵', 200, 0.1),
            Property('草悟道', 260, 0.1),
            Property('科博館', 260, 0.1),
            Property('台灣大道', 150, 0),
            Property('高美濕地', 280, 0.1),
            #Property('前進監獄', 0, 0),
            Property('中友百貨', 300, 0.1),
            Property('中科火車站', 300, 0.1),
            #Property('社區基金', 0, 0),
            Property('逢甲大學教學實驗區', 320, 0.1),
            Property('高鐵臺中站', 200, 0.1),
#            Property('機會', 0, 0),
            Property('勤美誠品綠園道', 350, 0.1),
            Tax('奢侈稅', 20),
            Property('逢甲大學綜合大樓', 400, 0.1),
            Chance()
        ]
#        self.space_list = [for i in self.spaces]
        # for i in range(1,38):
        #     if isinstance(self.spaces[i], Property):
        #         self.spaces[i].price = randint(300,500)
        #         self.spaces[i].rent = random.uniform(0.1, 0.3)
    def land_on_space(self, player):
        space = self.spaces[player.position]
        print(f"{player.name} landed on {space.name}")
        # 在這裡編寫玩家所需的相關邏輯


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 500
        self.properties = []
        self.position = 0
        self.in_jail=0
        self.jdays=0

    def move(self, steps, space_len):
        self.position = (self.position + steps) % space_len
        
    def teleport(self, loc):
        self.position = loc
        
    def buy_property(self, price):
        buyornot=random.randint(0, 1)
        if buyornot==1 and self.money>price:
            return buyornot
    
    def pay(self, rent):
        self.money -= rent 
    
    def receive(self,rent):
        self.money += rent

    def is_bankrupt(self):
        if(self.money<=0):
            return True
   
    def wait_in_jail(self):
        self.jdays=self.jdays-1
   
    def plusjaildays(self):
        self.jdays=2

    

class Dice:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
        # print("dice:", self.value)
        return self.value


class Monopoly:
    def __init__(self, jail_fee):
        self.anomal = False
        self.jail_fee = jail_fee
        self.losers_place = []
        self.board = Board()
        self.players = [Player('Player 1'), Player(
            'Player 2'), Player('Player 3')]
        self.current_player_index = random.randint(0, len(self.players)-1)
        self.game_over = False
        self.winner = None
        self.dice = Dice()
        self.jdays=[0,0,0]
        self.debug = 0
        self.end_round = 0
   
    def play_game(self):
        if self.debug:
            round =10
        while not self.game_over:
            self.end_round += 1
            # Get current player
            current_player = self.players[self.current_player_index]
            if self.debug:
                round -= 1
                if round<=0:
                    break
            print(f"It's {current_player.name}'s turn.")       
            # If the player is in jail, wait and skip the turn 善齊改的
            if current_player.in_jail:
                print("cur money: ", current_player.money)
                current_player.money -= self.jail_fee
                print("inJail: ",current_player.money)
                current_player.wait_in_jail()  # Player waits in jail, reduces remaining jail turns
                if current_player.jdays == 0:
                    current_player.in_jail = False
                    print(f"{current_player.name} has left the jail.")
                else:
                    print(f"{current_player.name} remains in jail.")
                if current_player.is_bankrupt():
                    print(f"{current_player.name} is bankrupt and out of the game.")
                    self.losers_place.append(self.board.spaces[self.players[self.current_player_index].position])
                    self.players.remove(current_player)
                # Check if game is over
                if len(self.players) == 1:
                    self.game_over = True
                    self.winner = self.players[0]
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
                continue
            #改到這

            # Roll dice and move player
            roll = self.dice.roll()
            current_player.move(roll, len(self.board.spaces))
            self.board.land_on_space(current_player)
            space = self.board.spaces[current_player.position]
            print(f"{current_player.name} rolled {roll} and landed on {space.name}")
            print(current_player.position)
            #execute chances first, maybe players will move to some properties and execute extra movements.
            if isinstance(space, Chance):
                 # Chance space
                card = space.pick_card()
                card.execute(current_player, self.board.spaces)
                #update space based on player's location after Chance executed
                space = self.board.spaces[current_player.position]
                print(
                     f"{current_player.name} drew a chance card: {card.description}")
            
            # Execute action based on space type
            if isinstance(space, Property):
#                print("landing on property: ", space.name)
                # Property space
                if space.name != '出發':
                    if space.owner == None:
                        # Property is unowned, ask player if they want to buy it
                        if current_player.buy_property(space.price):
                            space.sold(current_player)
                            print(
                                f"{current_player.name} bought {space.name} for {space.price} dollars.")
#                        else:
#                            print("current player has no enough money for this place, haha!")
                    # Property is current_player ,Build a house on space 
                    elif space.owner == current_player.name:
                        space.rent+=0.1
                        current_player.pay(space.price*0.1)
                        print(
                            f"{current_player.name} paid {space.price*0.1} dollars to build a house.")
                    else:
                        # Property is owned by someone else, pay rent
                        rent = space.get_rent()
                        current_player.pay(rent)
                        space.owner.receive(rent)
                        print(
                            f"{current_player.name} paid {rent} dollars in rent to {space.owner.name}.")

#            elif isinstance(space, Chance):
#                 # Chance space
#                card = Chance.pick_card()
#                card.execute(current_player, self.board.spaces)
#                print(
#                     f"{current_player.name} drew a chance card: {card.description}")

            elif isinstance(space, Tax):
                # Tax space
                tax = space.amount
                current_player.pay(tax)
                print(f"{current_player.name} paid {tax} dollars in taxes.")


            elif isinstance(space, GoToJail): #善齊修改了一點
                # Go to jail space
                current_player.in_jail = True
                current_player.plusjaildays()  # 玩家被送到監獄，增加監獄回合數 
                print(f"{current_player.name} is now in jail.")
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
                continue

            # elif isinstance(space, Jail):
            #     # Jail space
            #     if current_player.in_jail:
            #         current_player.wait_in_jail()
            #         print(f"{current_player.name} is still in jail.")
            #     else:
            #         print(f"{current_player.name} is just visiting jail.")

            # Check if player is bankrupt
            if current_player.is_bankrupt():
                print(f"{current_player.name} is bankrupt and out of the game.")
                self.losers_place.append(self.board.spaces[self.players[self.current_player_index].position])
                self.players.remove(current_player)

            # Check if game is over
            if len(self.players) == 1:
                self.game_over = True
                self.winner = self.players[0]

            print(current_player.name, ": ", current_player.money)
            if current_player.money > 5000:
                self.anomal = True
                print("Unknown Error----------------")
                break
            # Switch to next player
            self.current_player_index = (
                self.current_player_index + 1) % len(self.players)
            
            # current_player.money = round(current_player.money, 2)
        # Print game over message
        if(self.winner.in_jail==False):
            print(f"{self.winner.name} has won the game with a total wealth of {self.winner.money} dollars.")
        else:
            print(f"{self.winner.name} has won the game with a total wealth of {self.winner.money} dollars.太神啦坐牢也能贏")

    def get_winner(self):
        return self.players[0], self.losers_place, self.end_round, self.players[0].money, self.anomal, self.board.spaces[self.players[self.current_player_index].position]