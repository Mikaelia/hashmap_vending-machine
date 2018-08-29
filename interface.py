#!/usr/bin/env python3
"""
Interactive console
"""
import sys
import cmd
import shlex
from vending_machine import VendingHash

class VendingCommand(cmd.Cmd):
    """
    A console allowing users to interact with vending machine
    """

    prompt = ("*Beep* ")
    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True
        

    def do_EOF(self, args):
        """
        Exit progam upon EOF signal
        """
        return True


    def do_buy(self, args):
        """
        "Purchase" an item to remove it from machine
        """
        try:
            args = shlex.split(args)
            snackotron.buy(args[0].title())
        except:
            print("** Please choose an item **")


    def do_restock(self, args):
        """
        Reset machine to default item counts
        """
        snackotron.restock()


    def do_money(self, args):
        """
        Return the amount of money the machine has collected since last restock
        """
        snackotron.value()


    def do_add(self, args):
        """
        Adds/updates an item in the machine
        """
        item_dict = {
            'count': 1,
            'price': 0
        }

        try:
            args = shlex.split(args)
            item = args[0].title()
            snackotron.add(item, item_dict)
        except:
            print("** Please provide item name **")


    def do_check(self, args):
        """
        Returns information about a specific item
        """
        try:
            args = shlex.split(args)
            item = args[0].title()
            if not snackotron.find(item):
                print("There are no {}s".format(item))
        except:
            print("** Please provide item name **")


    def do_price(self, args):
        """
        Updates price of an item
        """
        item_dict = {
            'count': 0,
            'price': 0
        }
        
        try:
            args = shlex.split(args)
            item = args[0].title()
            if len(args) > 1:
                item_dict.update({'price': int(args[1])})

                snackotron.add(item, item_dict)
        
        except:
            print("** please provide item name and associated data **")


    def do_schema(self, args):
        """
        Prints vending machine hashmap schema
        """
        snackotron.schema()


    def do_inventory(self, args):
        """
        Prints all vending machine items and descriptions
        """
        snackotron.tell()


if __name__ == '__main__':
    """
    Entry point for command loop.
    """
    # Creates size of hash table
    snackotron = VendingHash(5)
    VendingCommand().cmdloop()