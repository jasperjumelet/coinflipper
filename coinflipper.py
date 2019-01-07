# The modules that needs to be imported for the coinflipper
import time
import random 

# The global variables which count the heads and tails
heads = 0
tails = 0

# The function that counts how many time the coin flipped on heads or tails
def flipping():
    global heads
    global tails
    flips = 1
    while flips <= 100:
        if random.randint(1, 2) == 1:
            heads += 1
            flips += 1
	
        else:
            tails += 1
            flips += 1
		
# The function that checks which one wins, head or tails
def win_check():
    global heads
    global tails
    if heads > tails:
        print("Heads wins with {}!".format(heads - tails))
    elif heads < tails:
        print("Tails wins with {}!".format(tails - heads))
    else:
        print("Its a draw play another time.")

# The main function that executes the entire code
def main():
    flipping()
    print("pls wait 10 seconds while we are flipping the coins. ^_^ ")
    time.sleep(10)
    win_check()

# Here we call the main function
main()