import matplotlib.pyplot as plt

days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
active_users = [12000, 13500, 12800, 15000, 16200, 18000, 17500]

plt.figure(figsize=(10, 4))
plt.plot(days, active_users, marker='o', color='green')
plt.title('Daily Active Users on Music Streaming App')
plt.xlabel('Days')
plt.ylabel('Active Users')
plt.grid(True)
plt.show()