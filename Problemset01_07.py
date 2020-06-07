def getRatios(vect1, vect2):
  print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
  ratios = []
  for index in range(len(vect1)):
    try:
      print(ratios.append(vect1[index] / float(vect2[index])))
    except ZeroDivisionError as E:
      print(E)
      print(ratios.append(float('nan')) ) # nan = Not a Number
    except:
      raise ValueError('getRatios called with bad arguments')
  return ratios

