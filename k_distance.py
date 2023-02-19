star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
  total_difference = 0
  for i in range(len(movie1)):
    total_difference += (movie1[i] - movie2[i]) ** 2
  return total_difference ** 0.5

print(distance(star_wars,raiders))
print(distance(star_wars,mean_girls))
