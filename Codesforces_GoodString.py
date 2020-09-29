def isGoodString(input):
    if len(input) == 2 :
        return True
    elif (input[1:]+input[0]) == (input[-1]+input[0:-1]):
        return True
    else:
        return False 


def main():
    
    n = int(input())

    

    for _ in range(n):
        dict_visited = {}
        input_char = input()
        dict_visited[input_char] = False

        if isGoodString(input_char):
            print(0)
        else:
            dict_visited[input_char] = True
            for i in range(len(input_char)):
                new_char = input_char[0:i]+input_char[i+1:]
                if isGoodString(new_char):
                    print(len(input_char) - len(new_char))
                    break
                else:
                    dict_visited[new_char] = True
                    min
            pass



if __name__ == "__main__":
    main()
    