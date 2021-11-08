income = 12 * 8900
text  = "your yearly income is %s " % income
print(text)

text1 = "your yearly income is {}".format(income)
print(text1)

text2 = f"your yearly income is {income}"
print(text2)

asia_population = 4_647_000_000
world_population = 7_807_000_000
percent = asia_population / world_population
print(f'Proportion of global population living in Asia: {percent:.0%}')
