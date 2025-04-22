#1.Use gradient colors to display the points. (使用漸變色來顯示點)
  points_numer = range(rw.points_num)
  ax.scatter(rw.x_values, rw.y_values, c=points_numer, cmap=plt.cm.Blues, edgecolors='none', s=15)

#2.Highlight the starting point and the ending point.(突出顯示起點和終點。)
