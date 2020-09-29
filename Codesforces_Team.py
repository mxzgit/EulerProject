def main():
    
    n = int(input())

    counter = 0

    for pb_index in range(n):
        list_int = input().split(' ')
        list_int= map(lambda x:int(x), list_int)
        if sum(list_int)>= 2 :
            counter+= 1
    print(counter) 


if __name__ == "__main__":
    main()
    