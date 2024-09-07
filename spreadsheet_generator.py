import pandas as pd

df = pd.DataFrame(columns= ['name', 'gender', 'age', 'height', 'weight', 'basal_rate'])
#df.to_excel('.teste.xlsx')

#2.Tratando os dados obtidos
def basal_rate_calculation_men(age,height,weight):
    basal_rate = float(66 + (13.8 * weight) + (5 * (height * 100)) - (6.8 * age))
    return basal_rate 

def basal_rate_calculation_woman(age,height,weight):
    basal_rate = float(655 + (9.6 * weight) + (1.8 * (height * 100) - (4.7 * age)))
    return basal_rate


#1. Recebendo os dados
while True:
    people = []
    list_people = []

    name = str(input("Enter the student's name:"))
    people.append(name)
    gender = str(input("Enter the student's gender:"))
    people.append(gender)
    age = int(input("Enter the student's age:"))
    people.append(age)
    height = float(input("Enter student height:"))
    people.append(height)
    weight = float(input("Enter student weight:"))
    people.append(weight)
    response = str(input('finally?'))

    if gender == 'men':
        basal_rate = basal_rate_calculation_men(age,height,weight)
        people.append(basal_rate)

    elif gender == 'woman':
        basal_rate = basal_rate_calculation_woman(age,height,weight)
        people.append(basal_rate)

    list_people.append(people)
    print(list_people)

#3.Armazenando os dados tratados
    
    if response == 'no':
        df = df._append(pd.DataFrame(list_people, columns=df.columns), ignore_index = True)
    elif response =='yeas':
        df = df._append(pd.DataFrame(list_people, columns=df.columns), ignore_index = True)
        df.to_excel('.teste.xlsx')
