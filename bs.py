#!usr/bin/python3

def main():
    A = [1,2,3,4,5,6,7]
    binary(A,7)
    
def binary(array,element):
        
        first = 0
        last = len(array) 
        
        while (first < last):
            mp = round((first + last)/2)
            
            if element == array[mp]:
                print("The element is at index",mp)
                break
            if element < array[mp]:
                last = mp - 1
                
            elif element > array[mp]:
                first = mp + 1
            
        if element != array[mp]: 
            print("The element does not exist in the list")
           
        
        
if __name__ == "__main__":main()