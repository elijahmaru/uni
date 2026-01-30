"""
Описание:
Программа получает на ввод список предметов и список их количества в том же порядке. Сначало находит индекс предмета в списке предметов, а потом в списке количества 
"""
products = ["apple", "banana", "orange", "milk"]
stocks = [10, 5, 20, 8]


def get_stock(product_name):
    """
    Findes how many of given item is in stock

    Parameters:
        product_name(string): name of item

    Returns:
        int: amount of items in stock
    """
    found_index = -1
    for i in range(len(products)):
        # if findes index of product in list of items
        if products[i] == product_name:
            found_index = i
            break
    #if index is found returns amount in stock 
    if found_index != -1:
        return stocks[found_index]
    else:
        return 0


item = "banana"
quantity = get_stock(item)
print(f"На складе {item}: {quantity} шт.")
