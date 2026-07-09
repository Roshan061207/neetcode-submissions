class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]
        for i in range(len(words)):
            current_word=words[i]
            for j in range(len(words)):
                if i==j:
                    continue
                if current_word in words[j]:
                    result.append(current_word)
                    break
        return result

        