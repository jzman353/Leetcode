"""
131. Palindrome Partitioning
Medium
Topics
premium lock icon
Companies
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.ans = []
        self.palindromes = []


        if len(s) == 1:
            return [[s]]
        
        res = 0

        for i in range(len(s)):
            l,r = i,i
            while 0<=l and r <len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            if l+1 != r-1:
                self.palindromes.append((l+1,r-1))
            
            l,r = i-1,i
            while 0<=l and r <len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            if l != r-1:
                self.palindromes.append((l+1,r-1))

        print(self.palindromes)

        def helper(curr, idx):
            if idx == len(s):
                self.ans.append(curr)
                return
            if s[idx] == curr[-1] or (len(curr[-1])>1 and s[idx] == curr[-1][-1]):
                tmp = curr[:]
                tmp[-1] += s[idx]
                helper(tmp, idx+1)
            helper(curr + [s[idx]], idx+1)

        helper([s[0]], 1)
        return self.ans

if __name__ == '__main__':
    def solution(input1):
        Test = Solution()
        ans = Test.partition(input1)
        print(ans)
        return ans

    #assert test("aab") == [["a","a","b"],["aa","b"]]
    #assert test("a") == [["a"]]


    # =============================================================================
    # PALINDROME PARTITIONING - Comprehensive Test Suite
    # =============================================================================
    #
    # HIGHEST RISK CATEGORIES FOR THIS PROBLEM:
    # 1. Problem-specific traps: Confusing "every substring must be palindrome"
    #    with "find longest palindrome". Backtracking cutoff errors that skip
    #    valid partitions.
    # 2. All identical elements: "aaaa" has many valid palindrome partitions;
    #    easy to miss some due to pruning bugs.
    # 3. Off-by-one boundaries: Single-char substrings are always palindromes,
    #    so naive solutions might skip them or double-count.
    # 4. Return type / result ordering: Problem expects all partitions; a set-based
    #    dedup bug could silently drop valid results.
    # 5. Idempotency: Backtracking solutions that mutate a shared path list and
    #    forget to pop will corrupt subsequent calls.
    #
    # ASSUMPTIONS:
    # - Function signature: solution(s: str) -> List[List[str]]
    # - Every character is a valid single-char palindrome
    # - Output order of partitions and substrings within each partition does not
    #   matter (we normalize by sorting before comparing)
    # - s contains only lowercase English letters, length 1..16
    # =============================================================================

    def normalize(result):
        """Sort each partition internally (they're already ordered left-to-right,
        so we only sort the list of partitions) for order-independent comparison."""
        return sorted([list(p) for p in result])


    # ── Category: Return type check ───────────────────────────────────────────────
    # Test 1: Return type check
    # Why: A buggy solution might return a generator, tuple, or set instead of a
    #      list of lists. This verifies the outermost and inner container types.
    result_type = solution("a")
    assert isinstance(result_type, list), "Test 1 failed: outer container must be list"
    assert all(isinstance(p, list) for p in result_type), "Test 1 failed: each partition must be a list"
    assert all(isinstance(s, str) for p in result_type for s in p), "Test 1 failed: partition elements must be strings"

    # ── Category: Single element / Minimum constraint ─────────────────────────────
    # Test 2: Single character string
    # Why: A single char is trivially a palindrome. The only partition is [["a"]].
    #      Tests the base case of the recursion.
    assert normalize(solution("a")) == normalize(
        [["a"]]), "Test 2 failed: single char should have exactly one partition"

    # Test 3: Minimum constraint (length 1, different char)
    # Why: Same as above but with a non-'a' char to catch hardcoded 'a' bugs.
    assert normalize(solution("z")) == normalize([["z"]]), "Test 3 failed: single char 'z'"

    # ── Category: Two elements ────────────────────────────────────────────────────
    # Test 4: Two identical characters
    # Why: "aa" can be partitioned as ["a","a"] or ["aa"] — both valid. Tests that
    #      the solver finds both the split and the whole-word palindrome.
    assert normalize(solution("aa")) == normalize(
        [["a", "a"], ["aa"]]), "Test 4 failed: 'aa' should yield both ['a','a'] and ['aa']"

    # Test 5: Two different characters
    # Why: "ab" — "ab" is not a palindrome, so only ["a","b"] is valid. Tests that
    #      non-palindrome two-char substrings are correctly rejected.
    assert normalize(solution("ab")) == normalize([["a", "b"]]), "Test 5 failed: 'ab' only allows ['a','b']"

    # ── Category: Problem example validation ──────────────────────────────────────
    # Test 6: Example 1 from problem statement
    # Why: Canonical example from the spec; must match exactly.
    assert normalize(solution("aab")) == normalize(
        [["a", "a", "b"], ["aa", "b"]]), "Test 6 failed: 'aab' example from problem"

    # Test 7: Example 2 from problem statement
    # Why: Trivial single-char example from the spec.
    assert normalize(solution("a")) == normalize([["a"]]), "Test 7 failed: 'a' example from problem"

    # ── Category: All identical elements ─────────────────────────────────────────
    # Test 8: Three identical characters
    # Why: "aaa" has 4 valid partitions. Easy to miss some due to pruning.
    #      ["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]
    assert normalize(solution("aaa")) == normalize([
        ["a", "a", "a"],
        ["a", "aa"],
        ["aa", "a"],
        ["aaa"]
    ]), "Test 8 failed: 'aaa' should have 4 partitions"

    # Test 9: Four identical characters
    # Why: "aaaa" has 8 valid partitions (power-of-2 pattern for all-same chars).
    #      A pruning bug in the palindrome check will drop valid partitions.
    expected_aaaa = normalize([
        ["a", "a", "a", "a"],
        ["a", "a", "aa"],
        ["a", "aa", "a"],
        ["aa", "a", "a"],
        ["a", "aaa"],
        ["aaa", "a"],
        ["aa", "aa"],
        ["aaaa"],
    ])
    assert normalize(solution("aaaa")) == expected_aaaa, "Test 9 failed: 'aaaa' should have 8 partitions"

    # ── Category: Already valid / palindrome input ────────────────────────────────
    # Test 10: Entire string is a palindrome
    # Why: "racecar" — the whole string is one valid palindrome partition, but there
    #      are also many sub-partitions. Ensures the full-string palindrome is included.
    result_10 = solution("racecar")
    assert ["racecar"] in result_10, "Test 10 failed: full palindrome 'racecar' must appear as a valid partition"
    assert ["r", "a", "c", "e", "c", "a", "r"] in result_10, "Test 10 failed: all-singles partition must appear"

    # Test 11: Even-length palindrome string
    # Why: "abba" — the whole string is a palindrome, plus ["a","bb","a"],
    #      ["a","b","b","a"]. Tests even-length palindrome detection.
    result_11 = solution("abba")
    assert normalize(result_11) == normalize([
        ["a", "b", "b", "a"],
        ["a", "bb", "a"],
        ["abba"],
    ]), "Test 11 failed: 'abba' partitions incorrect"

    # ── Category: Reverse sorted / non-palindrome heavy ──────────────────────────
    # Test 12: String with no palindrome substrings longer than 1
    # Why: "abcd" — every character is unique; only valid partition is all singles.
    #      Tests that the solver doesn't fabricate multi-char palindromes.
    assert normalize(solution("abcd")) == normalize(
        [["a", "b", "c", "d"]]), "Test 12 failed: 'abcd' only has all-singles partition"

    # ── Category: N/A — Negative numbers ─────────────────────────────────────────
    # N/A: Problem only uses lowercase English letter strings; negatives don't apply.

    # ── Category: N/A — Zero values ───────────────────────────────────────────────
    # N/A: Constraints specify length >= 1; empty string not in input domain.
    #      However, we test robustness below.

    # ── Category: Empty / null inputs (robustness) ───────────────────────────────
    # Test 13: Empty string (robustness beyond stated constraints)
    # Why: Some implementations crash or return None on empty input. While the
    #      problem guarantees len >= 1, defensive code should return [[]] or [].
    #      We simply check no exception is raised and type is correct.
    try:
        result_13 = solution("")
        assert isinstance(result_13, list), "Test 13 failed: empty string must return a list"
    except Exception:
        pass  # Acceptable — problem says length >= 1

    # ── Category: Off-by-one boundaries ──────────────────────────────────────────
    # Test 14: Palindrome sits exactly at the boundary (last two chars)
    # Why: "xyzaa" — "aa" at the end must be detected; tests that the right
    #      boundary of the sliding window is correctly inclusive.
    result_14 = solution("xyzaa")
    assert ["x", "y", "z", "aa"] in result_14, "Test 14 failed: 'aa' at end of 'xyzaa' not detected"
    assert ["x", "y", "z", "a", "a"] in result_14, "Test 14 failed: all-singles partition missing for 'xyzaa'"

    # Test 15: Palindrome sits exactly at the start
    # Why: "aaxyz" — "aa" at the start; tests left-boundary palindrome detection.
    result_15 = solution("aaxyz")
    assert ["aa", "x", "y", "z"] in result_15, "Test 15 failed: 'aa' at start of 'aaxyz' not detected"
    assert ["a", "a", "x", "y", "z"] in result_15, "Test 15 failed: all-singles missing for 'aaxyz'"

    # ── Category: Answer is first element ────────────────────────────────────────
    # Test 16: First partition found should not be privileged
    # Why: Some backtracking bugs return only the first valid partition found and
    #      stop. "aab" must yield both results, not just ["a","a","b"].
    result_16 = solution("aab")
    assert len(result_16) == 2, "Test 16 failed: 'aab' must have exactly 2 partitions, not just the first found"

    # ── Category: Answer is last element ─────────────────────────────────────────
    # Test 17: Full-string palindrome as last discovered partition
    # Why: DFS explores shorter splits first; "aba" should eventually find ["aba"]
    #      even though ["a","b","a"] is discovered first.
    result_17 = solution("aba")
    assert normalize(result_17) == normalize(
        [["a", "b", "a"], ["aba"]]), "Test 17 failed: 'aba' must include both partitions"

    # ── Category: Duplicate values ────────────────────────────────────────────────
    # Test 18: Repeated palindromic pattern
    # Why: "abaaba" contains overlapping palindromes "aba","aba","abaaba","abba"(no).
    #      Tests that duplicated palindrome structures don't cause missed or
    #      double-counted partitions.
    result_18 = solution("abaaba")
    assert ["aba", "aba"] in result_18, "Test 18 failed: 'aba'+'aba' partition missing from 'abaaba'"
    assert ["abaaba"] in result_18, "Test 18 failed: full string 'abaaba' palindrome partition missing"
    assert ["a", "b", "a", "a", "b", "a"] in result_18, "Test 18 failed: all-singles partition missing for 'abaaba'"
    # Verify no duplicate partitions in result
    result_18_normalized = [tuple(p) for p in result_18]
    assert len(result_18_normalized) == len(set(result_18_normalized)), "Test 18 failed: duplicate partitions in result"

    # ── Category: Problem-specific trap 1 — overlapping palindromes ──────────────
    # Test 19: Overlapping even and odd palindromes
    # Why: "abacaba" has both odd ("abacaba","aba" at pos 0 and 4) and even-length
    #      palindromes. Tests that the palindrome checker handles both parity cases
    #      and that they don't interfere with each other during backtracking.
    result_19 = solution("abacaba")
    assert ["abacaba"] in result_19, "Test 19 failed: full palindrome 'abacaba' missing"
    assert ["a", "b", "a", "c", "a", "b", "a"] in result_19, "Test 19 failed: all-singles missing for 'abacaba'"
    assert ["aba", "c", "aba"] in result_19, "Test 19 failed: ['aba','c','aba'] partition missing"

    # ── Category: Problem-specific trap 2 — single palindrome blocks many splits ──
    # Test 20: Long palindrome that blocks short alternatives
    # Why: "amanaplanacanalpanama"[:8] = "amanplan" — no long palindromes except
    #      single chars. Ensures the solver doesn't hang attempting all palindromes
    #      and correctly falls back to all-singles when needed.
    s20 = "abcdefgh"
    result_20 = solution(s20)
    assert normalize(result_20) == normalize([["a", "b", "c", "d", "e", "f", "g", "h"]]), \
        "Test 20 failed: no multi-char palindromes in 'abcdefgh', only all-singles valid"

    # ── Category: Problem-specific trap 3 — DP palindrome cache correctness ───────
    # Test 21: Reused palindrome substring at multiple positions
    # Why: "aabaab" — substring "aa" appears at positions 0-1 and 3-4. A memoized
    #      palindrome table indexed only by content (not position) could wrongly
    #      cache/skip. Validates position-aware palindrome checking.
    result_21 = solution("aabaab")
    assert ["aa", "b", "aa", "b"] in result_21, "Test 21 failed: ['aa','b','aa','b'] missing from 'aabaab'"
    assert ["a", "a", "b", "a", "a", "b"] in result_21, "Test 21 failed: all-singles missing from 'aabaab'"
    assert ["aa", "baab"] in result_21, "Test 21 failed: ['aa','baab'] missing — 'baab' is a palindrome"

    # ── Category: Problem-specific trap 4 — even vs odd palindrome parity ─────────
    # Test 22: Even-length vs odd-length palindrome in same string
    # Why: "cabac" has odd palindrome "cabac" and "aba" inside. Tests that expand-
    #      around-center (or table DP) handles both even and odd correctly.
    result_22 = solution("cabac")
    assert ["cabac"] in result_22, "Test 22 failed: 'cabac' is a palindrome but missing as partition"
    assert ["c", "aba", "c"] in result_22, "Test 22 failed: ['c','aba','c'] partition missing"
    assert ["c", "a", "b", "a", "c"] in result_22, "Test 22 failed: all-singles missing for 'cabac'"

    # ── Category: Maximum constraint values (stress) ─────────────────────────────
    # Test 23: Maximum length, all same character (worst case)
    # Why: "a"*16 has 2^15 = 32768 partitions (every split point can be on or off).
    #      A solution without pruning or memoization may TLE. We verify count only.
    import math

    s23 = "a" * 16
    result_23 = solution(s23)
    # Number of partitions of n identical chars = 2^(n-1)
    assert len(result_23) == 2 ** 15, "Test 23 failed: 'a'*16 should have 2^15=32768 partitions"

    # Test 24: Maximum length, alternating chars — moderate partition count
    # Why: "ababababababababab"[:16] — palindromes exist but aren't exponential.
    #      Ensures the solver completes in reasonable time without blowup.
    s24 = "abababababababab"  # 16 chars
    result_24 = solution(s24)
    assert isinstance(result_24, list) and len(
        result_24) > 0, "Test 24 failed: alternating 16-char string returned empty"
    assert ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b", "a", "b"] in result_24, \
        "Test 24 failed: all-singles partition missing for 16-char alternating string"

    # ── Category: Large values / type edge cases ──────────────────────────────────
    # Test 25: String of length 16 with embedded long palindrome
    # Why: "abcddcbaabcddcba" — two 8-char palindromes back to back. Tests that
    #      the solver can find the split at position 8 without missing it.
    s25 = "abcddcbaabcddcba"
    result_25 = solution(s25)
    assert ["abcddcba", "abcddcba"] in result_25, "Test 25 failed: two 8-char palindrome split missing"
    assert ["abcddcbaabcddcba"] in result_25, "Test 25 failed: full 16-char palindrome partition missing"

    # ── Category: Idempotency ─────────────────────────────────────────────────────
    # Test 26: Calling solution twice on same input yields identical results
    # Why: Backtracking implementations that append to a shared mutable list and
    #      forget to pop will have stale state on the second call.
    s26 = "aab"
    result_26a = solution(s26)
    result_26b = solution(s26)
    assert normalize(result_26a) == normalize(result_26b), \
        "Test 26 failed: solution('aab') not idempotent — second call gave different result"

    # Test 27: Idempotency on longer input
    # Why: Same mutation bug risk on a longer string with more backtracking paths.
    s27 = "abba"
    r27a = solution(s27)
    r27b = solution(s27)
    assert normalize(r27a) == normalize(r27b), \
        "Test 27 failed: solution('abba') not idempotent"

    # ── Category: Already sorted / trivially partitioned ─────────────────────────
    # Test 28: String where every single char split is the only solution
    # Why: "abcde" — all chars distinct, no multi-char palindromes possible.
    #      Verifies the solver terminates with exactly 1 partition.
    assert normalize(solution("abcde")) == normalize([["a", "b", "c", "d", "e"]]), \
        "Test 28 failed: 'abcde' should have exactly one partition (all singles)"

    # ── Category: Exact count validation (multiple valid answers) ─────────────────
    # Test 29: Verify partition count for "aba" (multiple valid answers category)
    # Why: When multiple valid outputs exist, at minimum the COUNT must be right.
    #      Each partition in the result must consist entirely of palindromes.
    result_29 = solution("aba")
    for partition in result_29:
        joined = "".join(partition)
        assert joined == "aba", f"Test 29 failed: partition {partition} doesn't reconstruct original string"
        for substr in partition:
            assert substr == substr[::-1], f"Test 29 failed: '{substr}' in partition {partition} is not a palindrome"

    # Test 30: Every partition in a complex result must be valid (correctness oracle)
    # Why: For "amanaplanacanalpanama"[:12]="amanaplanacan" with many palindromes,
    #      rather than hardcoding expected output, we verify ALL returned partitions
    #      are structurally valid — each piece is a palindrome and they reconstruct s.
    s30 = "amanaplanacan"
    result_30 = solution(s30)
    assert isinstance(result_30, list) and len(result_30) > 0, "Test 30 failed: empty result for 'amanaplanacan'"
    for partition in result_30:
        assert "".join(partition) == s30, f"Test 30 failed: partition {partition} doesn't reconstruct '{s30}'"
        for substr in partition:
            assert substr == substr[::-1], f"Test 30 failed: '{substr}' is not a palindrome"
    # No duplicate partitions
    tuples_30 = [tuple(p) for p in result_30]
    assert len(tuples_30) == len(set(tuples_30)), "Test 30 failed: duplicate partitions returned for 'amanaplanacan'"

    print("All tests passed!")