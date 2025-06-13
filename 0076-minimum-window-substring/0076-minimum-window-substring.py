class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # Step 1: Count frequency of each character in t
        t_count = Counter(t)
        required = len(t_count)

        # Step 2: Initialize sliding window pointers and variables
        l = 0
        formed = 0
        window_counts = {}
        min_len = float('inf')
        min_window = (0, 0)

        # Step 3: Right pointer expands the window
        for r, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if this character contributes to a valid window
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # Step 4: Try to shrink from the left while valid
            while l <= r and formed == required:
                # Update result if this window is smaller
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)

                # Try shrinking from the left
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                l += 1

        # Step 5: Return result
        if min_len == float('inf'):
            return ""
        return s[min_window[0]:min_window[1]+1]
            