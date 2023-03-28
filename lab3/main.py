import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.animation as animation

years = np.array([2000, 2002, 2005, 2007, 2010]).reshape((-1, 1))
percentages = np.array([6.5, 7.0, 7.4, 8.2, 9.0]).reshape((-1, 1))

model = LinearRegression().fit(years, percentages)
year = int(input('Wpisz rok: '))
predicted_percentage = model.predict([[year]])

predicted_12percentage = 0
year_12percent = 2010
while predicted_12percentage < 12:
    year_12percent += 1
    predicted_12percentage = model.predict([[year_12percent]])[0][0]

print(f"Przewidywany procent bezrobotnych w roku {year}: {predicted_percentage[0][0]:.3f}")
print(f"W roku {year_12percent} przewidywany procent bezrobotnych przekroczy 12 procent i bedzie wynosil: "
      f"{predicted_12percentage:.3f} ")

year = [2000, 2002, 2005, 2007, 2010]
percentage = [6.5, 7.0, 7.4, 8.2, 9.0]

fig, ax = plt.subplots()
ax.set_xlim([1998, 2012])
ax.set_ylim([0, 12])
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')

points, = ax.plot(year, percentage, 'bo')
x_line = np.arange(1998, 2012, 0.1)
y_line = np.zeros_like(x_line)
line, = ax.plot(x_line, y_line, 'r-')


# def update(frame):
    # slope, intercept = np.polyfit(year, percentage, 1)
    # y_line = slope * x_line + intercept
    # line.set_ydata(y_line)
    # return [points, line]


# ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

# plt.show()
