class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        if not source: return []
        ret = []
        in_blk_comment = False
        missing_newline = False
        updated_line = []
        for line in source:
            in_comment = False
            idx = 0
            while idx < len(line):
                char = line[idx]
                # Notice the last condition
                if char == '/' and idx + 1 < len(line) and line[idx+1] == '/' and not in_blk_comment:
                    if not in_blk_comment: 
                        in_comment = True
                        idx += 1
                elif char == '/' and idx + 1 < len(line) and line[idx+1] == '*' and not in_blk_comment:
                    if not in_comment:
                        in_blk_comment = True
                        if idx != 0: missing_newline = True
                        idx += 1
                elif char == '*' and idx + 1 < len(line) and line[idx+1] == '/' and in_blk_comment:
                    if not in_comment:
                        in_blk_comment = False
                        idx += 1
                else:
                    if not in_comment and not in_blk_comment:
                        updated_line.append(char)
                idx += 1
            # Only clear updated_line if blk_comment has ended, this will account for
            # the implicit newlines getting removed by blk_comment
            if updated_line and not in_blk_comment:
                ret.append("".join(updated_line))
                updated_line = []

        return ret

                
