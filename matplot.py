import matplotlib.pyplot as plt

attendence = 163 
# leaves_accounted = 
# leaves unaccounted = 
total = 196
leaves = total - attendence
precent = round(attendence / total * 100,2)
xpoints = [leaves,attendence]
mylabels = ["leaves: {leaves}".format(leaves = leaves), "Moaksh Kakkar's attendence:{precent}%".format(precent = precent)]
myexplode = [0, 0.1]
colors = ["r", "g"]


plt.pie(xpoints, labels = mylabels, explode = myexplode, startangle=90, colors= colors)
# plt.legend()
plt.show()