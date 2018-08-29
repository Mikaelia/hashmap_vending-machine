# Hash Map Vending Machine
> Practicing Hash Maps by creating a simple vending machine app and interactive console.

## Environment
Project  was developed and tested with `Ubuntu 14.04 LTS`

## Installing/ Getting Started
1. Clone repository and run  console with `./interface.py`
2. Enter supported commands (listed below)


## Features

|   **Command**  |   **Description**   |
| -------------- | --------------------- |
| `add <item>` | Adds an item to the machine |
| `buy <item>` | Purchase item from machine. Item count will reflect change |
| `check <item>` | Checks price and quantity of an item |
| `price <item>` | Changes the price of an item |
| `schema` | Prints the hash table schems |
| `inventory` | Prints the vending machine inventory |
| `money` | Prints total value of vending machine items |
| `restock` | Restocks the vending machine |
| `quit` | Exits the program |


#### Example
```
$ ./interface.py
*Beep* schema
None
None
None
None
None
*Beep* restock
*Beep* inventory
There are 10 Yogurts left. Yogurts cost $2.20
There are 10 Cookies left. Cookies cost $3.00
There are 10 Gatorades left. Gatorades cost $2.75
There are 10 Apples left. Apples cost $1.00
There are 10 Cheeses left. Cheeses cost $1.50
There are 10 Chocolates left. Chocolates cost $2.00
There are 10 Crackers left. Crackers cost $1.69
There are 10 Carrots left. Carrots cost $2.00
*Beep* buy yogurt
Yogurt
You bought a Yogurt for $2.20
*Beep* check yogurt
Yogurts cost $2.20. There are 9 left
*Beep* money
This machine has $159.20 worth of food
*Beep* add grape
*Beep* check grape
Grapes cost $0.00.
*Beep* price grape 2
*Beep* check grape
Grapes cost $2.00.

```

