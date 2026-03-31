from datetime import date

birth = date(1995,3,5)
death=date(2096,6,19)

life=death - birth

print(life.years())