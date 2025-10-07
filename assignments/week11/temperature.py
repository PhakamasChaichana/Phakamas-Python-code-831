"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

#ทำเอง  
def get_temperatures() :
    temps = []
    print("Enter temperatures for 7 day: ")
    for i in range(7) :
        temp = float(input(f"Day {i+1}: "))
        temps.append(temp)
    return temps

def analyze_temps(temp_list):
    avg_temp = sum(temp_list) / len(temp_list)
    high_temp = max(temp_list)
    low_temp = min(temp_list)
    return avg_temp, high_temp, low_temp

def display_analysis(avg, high, low):
    print("\nTemperature Analysis for Week: ")
    print(f"Average: {avg:.1f} ํC")
    print(f"Highest: {high} ํC")
    print(f"Lowest: {low} ํC")

temperatures = get_temperatures()
average, highest, lowest = analyze_temps(temperatures)
display_analysis(average, highest, lowest)


#ตามอาจารย์
def get_temperatures():
    temperatures = [31, 32, 30, 29, 28, 31, 32]
    return temperatures

def analyze_temps(temp_list):
    avg_temp = 0
    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)

    sum = 0 
    for temp in temp_list:
        sum = sum + temp
    avg_temp = sum / len(temp_list)
    return (avg_temp, highest_temp, lowest_temp)

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week: ")
    print("Average: %.2f C" % (avg))
    print(f"Highest: {high} C")
    print("Lowest: ", low, "C")

my_temps = get_temperatures()
analyzed_temps = analyze_temps(my_temps)
display_analysis(analyzed_temps[0], analyzed_temps[1], analyzed_temps[2])