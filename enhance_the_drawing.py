#1.Use gradient colors to display the points. (使用漸變色來顯示點)
  points_numer = range(rw.points_num)
  ax.scatter(rw.x_values, rw.y_values, c=points_numer, cmap=plt.cm.Blues, edgecolors='none', s=15)

#2.Highlight the starting point and the ending point.(突出顯示起點和終點。)
  ax.scatter(0, 0, c="green", edgecolors='none', s=100)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#3.Hide the axes and fit to your screen.(隱藏座標軸,適應你的屏幕)
  fig, ax = plt.subplots(figsize=())
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
