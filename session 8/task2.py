import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
zomato = [20, 25, 22, 30, 35, 45, 40]
swiggy = [18, 22, 25, 28, 32, 42, 38]

plt.figure(figsize=(8, 5))
plt.plot(days, zomato, linestyle='--', marker='o', color='red', label='Zomato')
plt.plot(days, swiggy, linestyle=':', marker='s', color='orange', label='Swiggy')
plt.title('Food Orders: Zomato vs Swiggy')
plt.xlabel('Days')
plt.ylabel('Number of Orders')
plt.legend()
plt.show()