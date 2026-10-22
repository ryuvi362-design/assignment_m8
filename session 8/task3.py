import matplotlib.pyplot as plt

plt.style.use('ggplot')

days = list(range(1, 11))
sales = [150, 180, 170, 210, 250, 230, 280, 300, 270, 320]

plt.figure(figsize=(8, 5))
plt.plot(days, sales, color='orange', marker='o')
plt.title("Flipkart's Daily Sales (10 Days)")
plt.xlabel('Day')
plt.ylabel('Sales')
plt.show()