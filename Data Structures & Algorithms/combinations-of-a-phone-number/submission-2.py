class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = [
            [],
            [],
            list("abc"),
            list("def"),
            list("ghi"),
            list("jkl"),
            list("mno"),
            list("pqrs"),
            list("tuv"),
            list("wxyz"),
        ]

        queue = deque()
        queue.append("")
        total = set()
        while queue:
            c_seq = queue.popleft()
            if len(c_seq) < len(digits):
                #for d, letters in digit_map.items():
                for c in digit_map[int(digits[len(c_seq)])]:
                    n_seq = c_seq + c
                    if len(n_seq) == len(digits):
                        total.add(n_seq)
                    queue.append(n_seq)
        return list(total)