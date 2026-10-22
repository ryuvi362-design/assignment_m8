import matplotlib.pyplot as plt

# Reset style in case a previous cell changed it
plt.style.use('default')

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
posts = [3, 5, 2, 4, 6, 7, 3]

# Instagram gradient colors (yellow, orange, pink, magenta, purple, blue, indigo)
instagram_colors = ['#FEDA75', '#FA7E1E', '#D62976', '#962FBF', '#4F5BD5', '#405DE6', '#833AB4']

plt.figure(figsize=(8, 5))
plt.bar(days, posts, color=instagram_colors)
plt.title('Instagram Posts Uploaded Per Day')
plt.xlabel('Days')
plt.ylabel('Number of Posts')
plt.show()