def count_vowels(text):
    vowelsounds="a","e","i","o","u"
    count=0
    for i in text:
        if i in vowelsounds:
            count+=1
            
    return count     
  