from Universe import Stephen_Hawking

class Life(Stephen_Hawking):
        def __init__(self):
            super().__init__()
        
            self.bestQuote = "Although my body is very limited, my mind is free to explore the universe."
            self.Attribution = "- Stephen Hawking"





if __name__ == "__main__":
    life = Life()
    print(f"{life.bestQuote}\n{life.Attribution}")
