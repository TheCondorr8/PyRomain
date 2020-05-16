def conversion(): #Function of our program

    num = int(input('Entrez un nombre sous forme arabe')) #Number entered by user

    tab = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], #Board which contains key values
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]

    number = "" #Definition of the variable number which is the result of the program
    cpt = 0 #Definition of a counter which will be useful in order to browse our board
    while num > 0: #First loop which allows to browse the board until the number is entirely converted

        while tab[cpt][0] > num: #Loop which browse our board

            cpt = cpt + 1 #Increment of the counter

        number = number + tab[cpt][1] #Conversion of our number
        num = num - tab[cpt][0] #Permit to stop our first loop

    print(number) #Display of our result

conversion()