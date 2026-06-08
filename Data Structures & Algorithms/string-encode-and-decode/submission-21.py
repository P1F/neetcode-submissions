salt_comma = "9SokuFR0$lzQXT!T0"
separator = ","
salt_empty = "089ZVV7!N3AcftjR$"

class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            if separator in strs[i]:
                strs[i] = strs[i].replace(separator, salt_comma)
            if strs[i] == "":
                strs[i] = salt_empty

        encoded_str = separator.join(strs)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
            
        decoded_strs = s.split(separator)
        for i in range(len(decoded_strs)):
            if salt_comma in decoded_strs[i]:
                decoded_strs[i] = decoded_strs[i].replace(salt_comma, separator)
            if salt_empty in decoded_strs[i]:
                decoded_strs[i] = decoded_strs[i].replace(salt_empty, "")

        return decoded_strs
