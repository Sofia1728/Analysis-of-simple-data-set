import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

print("Первые строки данных:")
print(data.head())

print("\nОсновные статистики:")
print(data.describe())

total_sales_by_product = data.groupby("Product")["Sales"].sum()
print("\nСуммарные продажи по продуктам:")
print(total_sales_by_product)

data.groupby("Date").sum()["Sales"].plot(kind="bar", title="Общая сумма продаж по дням")
plt.ylabel("Сумма продаж")
plt.xlabel("Дата")
plt.tight_layout()
plt.savefig("sales_chart.png")  
plt.show()
