import random

class Coin:

    def __init__(self,rare=False,clean=True,heads=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare=rare
        self.is_clean=clean
        self.heads=heads

        if self.is_rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour

    def  rust(self):
        self.colour=self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour

    def flip(self):
         head_options=[True,False]
         choice=random.choice(head_options)
         self.heads=choice

    def __del__(self):                     
        print("Coin Spent!")

    def __str__(self):
        if self.original_value>=1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value*100))
    
            

class One_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.01,
            "rusty_colour":"brownish",
            "clean_colour":"bronze",
            "num_edges":1,
            "thickness":1.52, 
            "diameter":20.3,
            "mass":3.56,
            }
        super().__init__(**data)


class Two_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.02,
            "rusty_colour":"brownish",
            "clean_colour":"bronze",
            "num_edges":1,
            "thickness":1.85,
            "diameter":25.9,
            "mass":7.12,
            }
        super().__init__(**data)


class Five_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.05,
            "rusty_colour":None,
            "clean_colour":"silver",
            "num_edges":1,
            "thickness":1.77,
            "diameter":18.0,
            "mass":3.25,
            }
        super().__init__(**data)

    def rust(self):
        self.colour=self.clean_colour

    def clean(self):
        self.colour=self.clean_colour


class Ten_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.10,
            "rusty_colour":None,
            "clean_colour":"silver",
            "num_edges":1,
            "thickness":1.85,
            "diameter":24.5,
            "mass":6.50,
            }
        super().__init__(**data)

    def rust(self):
        self.colour=self.clean_colour

    def clean(self):
        self.colour=self.clean_colour


class Twenty_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.20,
            "rusty_colour":None,
            "clean_colour":"silver",
            "num_edges":7,
            "thickness":1.7,
            "diameter":21.4,
            "mass":5.00,
            }
        super().__init__(**data)

    def rust(self):
        self.colour=self.clean_colour

    def clean(self):
        self.colour=self.clean_colour


class Fifty_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.50,
            "rusty_colour":None,
            "clean_colour":"silver",
            "num_edges":7,
            "thickness":1.78,
            "diameter":27.3,
            "mass":8.00,
            }
        super().__init__(**data)

    def rust(self):
        self.colour=self.clean_colour

    def clean(self):
        self.colour=self.clean_colour

        
class One_Pound(Coin):
    def __init__(self):
        data={
            "original_value":1.00,
            "rusty_colour":"greenish",
            "clean_colour":"gold",
            "thickness":1.35,
            "diameter":2.2,
            "num_edges":1,
            "mass":9.5
            }
        super().__init__(**data)


class Two_Pound(Coin):
    def __init__(self):
        data={
            "original_value":2.00,
            "rusty_colour":"greenish",
            "clean_colour":"gold & silver",
            "thickness":2.50,
            "diameter":28.4,
            "num_edges":1,
            "mass":12.00
            }
        super().__init__(**data)

coins=[One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),Twenty_Pence(),Fifty_Pence(),One_Pound(),Two_Pound()]

for coin in coins:
    arguments=[coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.mass,coin.num_edges]

    string="{}- Colour:{},value:{},thickness(mm):{},diameter(mm):{},mass(g):{},num_edges:{}".format(*arguments)
    print(string)
    

#To check how it works

one_pound_coin=One_Pound()

print(one_pound_coin.colour)

one_pound_coin.rust()
print(one_pound_coin.colour)

one_pound_coin.clean()
print(one_pound_coin.colour)

one_pound_coin.flip()
print(one_pound_coin.heads)

one_pound_coin.flip()
print(one_pound_coin.heads)

one_pound_coin.flip()
print(one_pound_coin.heads)

 
        
