'''Write a program that checks if a character entered by the user is a vowel or a consonant. If the 
input is neither a vowel nor a consonant (e.g., a number or special character), print "Invalid input."'''
CH=input("ENTER THE CHARACTER YOU WISH TO CHECK:")
if CH.upper() in ("A","E","I","O","U"):
    print("THE ENTERED CHARACTER ",CH,"IS A VOWEL.")
elif CH.lower() in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
        print("THE ENTERED CHARACTER ",CH,"IS A CONSONANT.")
else:
      print("INVALID INPUT.")

