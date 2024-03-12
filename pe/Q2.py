import random
class Main:
    def computer_guess(self, min_val, max_val):
        guess = random.randint(min_val, max_val)
        return guess
    #====================GuessNumber function====================
    def GuessNumber(self, number):

        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        max_val = int(number)
        min_val = 0
        guess = self.computer_guess(min_val, max_val)

        while True:
            answer = input("Is {} too high (h), too low (l), or correct (c)? ".format(guess))
            if answer == 'l':
                min_val = guess + 1
                guess = self.computer_guess(min_val, max_val)
            elif answer == 'h':
                max_val = guess - 1
                guess = self.computer_guess(min_val, max_val)
            elif answer == 'c':
                print("Welldone! The computer guessed your number {} correctly!".format(guess))
                break
            else:
                print("Invalid answer. Please enter h, l, or c.")
                guess = self.computer_guess(min_val, max_val)
        pass
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
