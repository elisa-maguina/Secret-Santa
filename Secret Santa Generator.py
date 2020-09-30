import random
import emoji    
  

santa_recip_list = ['NAME1', 'NAME2', 'NAME3', 'NAME4', 'NAME5', 'NAME6', 'NAME7']
random_santa_recip = random.choice(santa_recip_list)
max_amount = '$30 (+/- $5)'
rule_intro = ('The rules for this year are as follows:')
rule_1 = ('\n1. Stay within the dollar limit of ' + max_amount + '.')
rule_2 = ('\n2. Gift wrap, cards, and accessesories do NOT count towards the dollar limit.')
Wishlist = "https://tinyurl.com/xmaslist19"
Deadline = ("EOD 12/14/2019")
Welcome_Message = "Ho ho ho! Welcome to Secret Santa 2019."
print((emoji.emojize(':sparkles: ')), Welcome_Message, (emoji.emojize(':sparkles:')))
print("You have been randomly selected to be", random_santa_recip + "'s", "Secret Santa!")
print(rule_intro, rule_1, rule_2,)
print("Please fill out the wishlist at " + Wishlist + " by " + Deadline + ".")
print("Merry Christmas!")



