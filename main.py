import plotly.express as px

mark_breakdown = {
    "Homework": "10%",
    "Midterm 1": "23%",
    "Midterm 2": "22%",
    "Final Exam": "45%",
}

percents = list(map(lambda weight : int(weight.replace("%", "")), mark_breakdown.values()))
tasks = list(mark_breakdown.keys())

for task, weight in mark_breakdown.items():
    print(f"{task}\t{weight}")

px.pie(values=percents, names=tasks).show()