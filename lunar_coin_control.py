import xml.etree.ElementTree as ET
from misc.menu import Command, ArgumentError
from misc.const import *
from misc.generic import SAVEPATH

MAX_COINS = 2**31 - 1 - 1000

def set_coins(xml_path: str, coins: int):
    """
    Set the number of coins in the XML file.
    """

    if not isinstance(coins, int):
        raise TypeError(f"Coins value must be of type int, not {type(coins).__name__}")
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    coins_element = root.find('coins')
    if coins_element is not None:
        coins_element.text = str(coins)
        tree.write(xml_path)
    else:
        raise ValueError("No 'coins' element found in the XML file.")

def get_coins(xml_path: str):
    """
    Get the number of coins from the XML file.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    coins_element = root.find('coins')
    if coins_element is not None and coins_element.text is not None:
        return int(coins_element.text)
    else:
        raise ValueError("No 'coins' element found in the XML file.")



class SetCoinsCommand(Command):
    
    name = "lunar"
    description = "Set the number of Lunar Coins. Leave empty for max coins."
    
    def run(self, *args):
        if SAVEPATH:
            if len(args) == 0:
                coins = MAX_COINS
            else:
                try:
                    coins = int(args[0])
                except ValueError:
                    raise ArgumentError("Lunar Coins value must be an integer.")
            
            try:
                set_coins(str(SAVEPATH), coins)
                console.print(f"Set Lunar Coins to {coins}⊙.")
            except Exception as e:
                console.print(f"Error setting Lunar Coins: {e}")
        else:
            raise ValueError("Save path not given. Use 'savepath' command")