from matplotlib import pyplot as plt
import json
from datetime import date, timedelta
import numpy as np

today = str(date.today())
tday = date.today()
tdelta = timedelta()

with open('C:/Corona Mining/data/%s/DE_vaccine_history.json' % today) as f:
    data_history = json.load(f)

with open('C:/Corona Mining/data/%s/DE_vaccine.json' % today) as f:
    data = json.load(f)

vaccinatedList = []
totalVaccinated = 0
sundayDates = []
xyz = [""]
firstVaccinated = 0
secondVaccinated = 0
firstVaccinatedList = []
secondVaccinatedList = []

firstDate = date(2020, 12, 27)
currentDate = firstDate

while currentDate <= tday - timedelta(days=1):
    if currentDate.day == 1:
        sundayDates.append(currentDate.strftime("%B"))
    currentDate += timedelta(days=1)

for day in data_history["data"]["history"]:
    totalVaccinated += day["vaccinated"]
    vaccinatedList.append(totalVaccinated)
    firstVaccinated += day["firstVaccination"]
    firstVaccinatedList.append(firstVaccinated)
    secondVaccinated += day["secondVaccination"]
    secondVaccinatedList.append(secondVaccinated)

vaccine_x = np.arange(len(vaccinatedList))

print(vaccinatedList)
print(firstVaccinatedList)
print(secondVaccinatedList)

fig1, ax1 = plt.subplots()

ax1.plot(vaccine_x, vaccinatedList)
ax1.plot(vaccine_x, firstVaccinatedList)
ax1.plot(vaccine_x, secondVaccinatedList)
ax1.set_xticks(np.arange(len(vaccinatedList),step=7))
ax1.set_xticklabels([])
ax1.set_xlim(0,len(vaccinatedList)-1)
ax1.set_ylim(0,max(vaccinatedList))
ax1.set_title("Insgesamte Impfungen")
fig1.show()
fig1.savefig("C:/Corona Mining/data/%s/All_Vaccine.png" % today, transparent=True)

Slices = []
Labels = ['Erste Impfung', 'Zweite Impfung']
Colors = ['#50c732', '#2e8416']
firstVaccineted = data["data"]["vaccinated"]
secondVaccineted = data["data"]["secondVaccination"]["vaccinated"]

Slices.append(firstVaccineted)
Slices.append(secondVaccineted)

plt.pie(Slices, labels= Labels, colors= Colors, wedgeprops={'edgecolor': 'black'}, shadow=True, startangle=90)
plt.show()
plt.savefig("C:/Corona Mining/data/%s/ImpfungenPieChart.png" % today, transparent=True)

Slices1 = []
Labels1 = ['Biontech', 'Moderna', 'Astra Zeneca']
Colors1 = ['#0095FF', '#E71837', '#950F5D']
biontech = data["data"]["vaccination"]["biontech"]
moderna = data["data"]["vaccination"]["moderna"]
astraZeneca = data["data"]["vaccination"]["astraZeneca"]
Slices1.append(biontech)
Slices1.append(astraZeneca)
Slices1.append(astraZeneca)

plt.pie(Slices1, labels= Labels1, colors= Colors1, wedgeprops={'edgecolor': 'black'}, shadow=True)
plt.show()
plt.savefig("C:/Corona Mining/data/%s/ImpfStoffAnteile.png" % today, transparent=True)