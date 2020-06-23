import matplotlib.pyplot as plt
alphabet = "abcdefghijklmnopqrstuvwxyz"

code = """swodkdbkfovvobpbywkxkxdsaeovkxngrycksndgyfkcdkxndbexuvoccvoqcypcdyx
ocdkxnsxdronocobdxokbdrowyxdrockxnrkvpcexukcrkddobonfsckqovsocgrycop
bygxkxngbsxuvonvszkxncxoobypmyvnmywwkxndovvdrkdsdccmevzdybgovvdrycoz
kccsyxcbokngrsmriodcebfsfocdkwzonyxdrocovspovoccdrsxqcdrorkxndrkdwym
uondrowkxndrorokbddrkdponkxnyxdrozonocdkvdrocogybnckzzokbwixkwoscyji
wkxnskcusxqypusxqcvyyuyxwigybuciowsqrdikxnnoczksbxydrsxqlocsnobowksx
cbyexndronomkiypdrkdmyvycckvgbomulyexnvocckxnlkbodrovyxokxnvofovckxn
ccdbodmrpkbkgki"""

letter_counts = [code.count(l) for l in alphabet]
letter_colors = plt.cm.hsv([0.8*i/max(letter_counts) for i in letter_counts])

plt.bar(range(26), letter_counts, color = letter_colors)
plt.xticks(range(26), alphabet)
#
plt.title("Frequency of each letter (Text 1)")

plt.savefig("output.png")