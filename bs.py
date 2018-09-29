#!usr/bin/python3

def main():
    Array1 = [9,22,39.3,47,59,65,73]
    binary(Array1,47)
    
def binary(array,element):    
        first = 0
        last = len(array) 
        while (first < last):
            midpoint = round((first + last)/2) #round function to round the division off to nearest integer
            if element == array[midpoint]:
                print("The element is at index",midpoint)
                break
            if element < array[midpoint]:
                last = midpoint - 1
            elif element > array[midpoint]:
                first = midpoint + 1
        if element != array[midpoint]: 
            print("The element does not exist in the array")
if __name__ == "__main__":main()
