'''
Logic is quite simple, use a dict(), the key is abbreviations and value is a list of all words with the same abbreviations. Check if the abbreviation of incoming word is in the dict() and the only value of such key is the word itself.

Attention: 
The dictionary given may contain duplicate words, but should append to self.dictionary only once, otherwise the output may be wrong. Given the example case "['a','a'],isUnique('a')", should return True but will return False if without duplication handling.

collections.defaultdict() is such a useful function. Default parameter is None and can be list, set, int and so on, but cannot be dict.

set doesn't support index, so should convert set into list first.
'''
import collections
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dictionary=collections.defaultdict(set)
        dic=zip([self.helper(key) for key in dictionary],dictionary)
        for key,value in dic:
            self.dictionary[key].add(value)

    def helper(self,key):
        if len(key)<3:
            return key
        return key[0]+str(len(key)-2)+key[-1]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbrev=self.helper(word)
        if len(self.dictionary[abbrev])==0:
            return True
        return len(self.dictionary[abbrev])==1 and word==list(self.dictionary[abbrev])[0]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")