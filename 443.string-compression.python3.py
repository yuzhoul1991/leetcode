class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Use two pointers start and end where start is for writing and end
        # is for reading
        if not chars: return 0       
        n = len(chars)
        start = end = 0
        while end < n:
            current_char = chars[end]
            count = 0
            while end < n and chars[end] == current_char:
                count += 1
                end += 1
            chars[start] = current_char
            start += 1
            if count > 1:
                digits = list(str(count))
                chars[start:start+len(digits)] = digits
                start += len(digits)
        return start
