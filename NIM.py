print('Type play_nim() to play.')
def play_nim():
    def valid(selection):
        try:
            if int(selection) in range(1,4):
                return True
        except:
            return False
        return False
    p=12
    print('There are 12 pins. You and the computer take turns removing 1, 2, or 3 pins. The one that takes the last pin wins.')
    print('You go first.')
    for i in range(1,4):
        n=input('How many pins would you like to remove? ')
        while not valid(n):
            n=input('That input was invalid. Please type a whole number from 1 to 3. ')
        p-=4
        print('You removed '+n+' pin(s) leaving '+str(p-n+4)+' pin(s).')
        print('The computer removed '+str(4-int(n))+' pin(s) leaving '+str(p)+' pin(s).')
    print('The computer has removed the last pin and won. Type play_nim() to play again.')
