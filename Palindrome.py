#Program to find if a string is a palindrome or not
def palindrome():
    word=input('Enter a string')
    if len(word)==1:
        print(word,'is a palindrome')
    elif len(word)%2==0:
        for n in range(0,int(len(word)/2)):
            if word[n]==word[len(word)-(n+1)]:
                if not n==int(len(word)/2)-1:
                    continue
                print(word,'is a palindrome')
            else:
                print(word,'is not a palindrome')
                break
    elif len(word)%2!=0:
        for n in range(0,int((len(word)/2)-0.5)):
            if word[n]==word[len(word)-(n+1)]:
                if not n==int((len(word)/2)-0.5)-1:
                    continue
                print(word,'is a palindrome')
            else:
                print(word,'is not a palindrome')
                break
