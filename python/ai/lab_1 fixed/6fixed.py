def calculateRevenue(raw_data):
    """
    calculates revenue from string 

    Parameters:
        raw_data(string): formated item,amout,price

    Returns:
        int: total revenue
    """
    total_revenue = 0
    # separates one item form another
    items = raw_data.split(";")

    for item in items:
        # separates product name, quantity and price from eachother
        parts = item.split(",")
        quantity = int(parts[1])
        price = int(parts[2])
        # calculates total revenue
        current_sum = quantity * price
        total_revenue = total_revenue + current_sum
    return total_revenue


raw_data = "Хлеб,5,40;Молоко,2,80;Сыр,1,350;Вода,10,25"
total_revenue = calculateRevenue(raw_data)
print(f"Общая выручка: {total_revenue} руб")
