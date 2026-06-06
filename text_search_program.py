# Program name: salem_solomon_LA4.py Searching a Boyd of Text Author: Salem Solomon
# this statement assigns text to the paragraph below
text = """
MOSCOW — President Biden reiterated the United States’ commitment to “respond
swiftly and decisively” to a Russian attack on Ukraine, in a phone call with Ukraine’s
President Volodymyr Zelensky Sunday, as Western allies scramble to deter Russian
aggression and Moscow intensifies its pressure on NATO and Kyiv.

Biden spoke to Zelensky a day after an hour-long call between Biden and Russian
leader Vladimir Putin failed to produce a breakthrough in what U.S. officials say
is a rapidly deteriorating crisis.

“The two leaders agreed on the importance of continuing to pursue diplomacy and
deterrence in response to Russia’s military buildup on Ukraine’s borders,” the
White House said in a short statement following the 51-minute call between Biden
and Zelensky.
"""
# The while loop here will prompt the user to keep entering a search term unless they choose to hit enter in which it will "break"
while True:
    term = input('please enter a search term or hit "Enter" to quit: ')
    if not term: break
# if the term the user inputs is in the text this code will run through text to identify it
    if term in text:
        for n in range(len(text)):
         if term == text[n:n+len(term)]:
            print(term, 'is found at location',n)
# if the term the user enters is not located in text, this code will print "term not found"
    else:
        print('term not found in text')
# this will allow users to end the program by hitting "enter"
input("\n\nHit Enter to end program")






