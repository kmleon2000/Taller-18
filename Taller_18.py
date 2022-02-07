import matplotlib.pyplot as plt
import numpy as np

def GetCharts():
  # Creates a two pltos division on the frame
  # fig = plt.figure()
  fig, (line_plt, ellipse_plt) = plt.subplots(2,1)

  # Data to line plot
  l_coords = {
    'x': np.linspace(0, 10, 100),
    'y': np.full(100, 5, np.int0)
  }
  # Adding data to Line plot
  line_plt.plot(l_coords['x'], l_coords['y'])
  
  # Data to Ellipse plot
  rad = np.linspace(0, 2*np.pi, 100)
  center = { 'x': 2, 'y': 1 } # Coords of the ellipse's center #
  dim = { 'height': 2, 'width': 3 }
  # Returns 
  e_coords = {
    'x': center['x'] + dim['width'] * np.cos(rad),
    'y': center['y'] + dim['height'] * np.sin(rad)
  }
  # Adding data to Ellipse's plot
  ellipse_plt.plot(e_coords['x'], e_coords['y'])
  plt.show()

GetCharts()