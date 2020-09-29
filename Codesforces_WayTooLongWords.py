def main():
    
    n = int(input())
    list_words = []
    
    for _ in range(n):
        word = input()
        list_words.append(word)
        
    for word in list_words:
        if(len(word) > 10):
            print(""+word[0]+str(len(word[1:-1]))+word[-1]+"")
        else:
            print(word)




if __name__ == "__main__":
    main()
    