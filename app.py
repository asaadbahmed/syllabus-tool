import plotly.express as px

print("################################################\n\t\tSyllabus Tool\n################################################")
number_of_evaluations = 0
while True:
    try:
        number_of_evaluations = int(input("How many evaluations are there? Enter a number (1 to 100): "))
    except:
        continue
    else:
        if 0 < number_of_evaluations <= 100: break
        continue

evaluations = dict()
total_worth = 0
counter = 1

# TODO: Write input validation
for i in range(number_of_evaluations):
    name = input("Enter the evaluation name (optional): ") or f"Evaluation_{counter}"
    worth = int(input("Enter the percent that this evaluation is worth: "))
    counter += 1
    evaluations[name] = worth
    total_worth += worth

print(total_worth)
if total_worth != 100:
    raise Exception("Check your percents, it does not add up to 100%")

print(evaluations)
names = evaluations.keys()
percents = list(evaluations.values())
px.pie(values=percents, names=names).show()