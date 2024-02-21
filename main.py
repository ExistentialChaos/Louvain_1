'''
Things to do:
Set up data file ###DONE
Be able to open and read ###DONE
Interpret path data to an app
Be able to record play times and paths taken
Have a reset button

'''

#IMPORTS
import PySimpleGUI as GUI
import matplotlib as MT

#FUNCTIONS



#FILE READ

f = open("Data.txt", "r")
lines = f.readlines()
m = []
for i in lines:
    m.append(i)
f.close()

for data in m:
    for x in range(len(data)):
        if data[x] == ":":
            a = data[x+1]
            if data[x+2] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                a += data[x+2]
            print(int(a))
            continue

GUI.theme("Dark Blue 3")

layout = [[GUI.Text('Carte de Louvain')],
          [GUI.Image("img1.png", subsample=3), GUI.Image("carte.png", subsample=4)],
          [GUI.Image("img2.png", subsample=3), GUI.Image("img3.png", subsample=3)],
          [GUI.Button('Gauche'), GUI.Button('Avancer'), GUI.Button('Droite')],
          [GUI.Button('Exit')]
          ]


window = GUI.Window('LOUVAIN Macro Micro', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == GUI.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Gauche':
        print('Aller a gauche')
window.close()