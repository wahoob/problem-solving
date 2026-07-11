class Solution:
    def encode(self, strs: list[str]) -> str:
        result = ""
        for s in strs:
            result += f"#{len(s)}!{s}"
        return result

    def decode(self, s: str) -> list[str]:
        i = 0
        result = []
        while i < len(s):
            j = i + 1
            while s[j] != "!":
                j += 1
            length = int(s[i + 1: j])
            word = s[j + 1: j + length + 1]
            result.append(word)
            i = j + 1 + length
        return result