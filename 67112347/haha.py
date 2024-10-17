sleep_values = [7.5, 8, 6.5, 7, 8, 7.5]
def weekly_sleep_average(sleep_values): 
    if sleep_values == []:
        return "No sleep data"
    else:
        x = sum(sleep_values) / len(sleep_values)
        print(round(x, 1))  
weekly_sleep_average(sleep_values)


        

