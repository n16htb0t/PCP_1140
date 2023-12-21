#Write a function that takes a tuple where there are 15 words, the program should copy to another tuple only the words that contain the letters a and b and their length is more than 4
def copy():
    tuple1=("daksh","khurana","Maksim","Maksimka","Maks","football","tennis","khuranab")
    tuple2=()
    for words in tuple1:
       if len(words)>4 and "a" in words and "b" in words:
           tuple2+=(words,) 
    print(tuple2)
copy()