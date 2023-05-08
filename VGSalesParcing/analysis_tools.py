
import math


class MyMath:

    def cleanup(data):
        """ Takes out blank spaces in data and turns values into floats"""
        # Takes the '' spaces out of a list
        clean_data = [i for i in data if i != '']
        # Turns each value of list into a float
        clean_data = [float(i) for i in clean_data]
        return clean_data

    def mean(data):
        """ Gets the mean value from a list of values """
        # Sets a variable to hold total
        total = 0
        # Goes through list of data and adds it to total
        for item in data:
            total += item
        # Returns total divided by length to give mean
        return (total / len(data))

    def median(data):
        """ Gets the median values from a list of values """
        # Sorts the passed in list from low-high
        new_data = sorted(data)
        # Runs if list length is odd
        if int(len(new_data) % 2) != 0:
            # Gets the index of the middle value in the list
            middle = int((len(new_data) - 1) / 2)
            return new_data[middle]

        # Runs if the length of the list is even
        else:
            # Gets the indexes of the two middle elements
            mid1 = int(len(new_data) / 2)
            mid2 = mid1 - 1
            return (new_data[mid1] + new_data[mid2]) / 2

    def stddev(data):
        """ Gets the standard deviation of a list """
        total = 0
        new_list = []
        # Gets the mean of the passed in list
        mean_num = MyMath.mean(data)
        # Gets each item in the list minus the mean, squared
        for item in data:
            new_list.append((item - mean_num) ** 2)
        # Takes each val in the new list and adds them all together
        for val in new_list:
            total += val
        # Returns the sqrt of the (total divided by the length of the list)
        return math.sqrt((total / len(data)))

    def min(data):
        """ Returns min value of passed in list """
        return min(data)

    def max(data):
        """ Returns max value of passed in list """
        return max(data)




