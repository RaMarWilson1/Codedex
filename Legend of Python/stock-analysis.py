stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
    return stock_prices[i-1]

def max_price(start, end):
    max_p = price_at(start)
    for i in range(start, end + 1):
        p = price_at(i)
        if p > max_p:
            max_p = p
    return max_p
   
def min_price(start,end):
    min_p = price_at(start)
    for i in range (start, end +1):
        p = price_at(i)
        if p > min_p:
            min_p = p
    return min_p
            
