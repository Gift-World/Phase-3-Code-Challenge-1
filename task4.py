def count_vowels(text):
    vowel_sounds="a","e","i","o","u"
    count=0
    for i in text:
        if i in vowel_sounds:
            count+=1
            
    return count     
  