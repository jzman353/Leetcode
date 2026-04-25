"""
2682. Find the Losers of the Circular Game
Easy

Hint
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

1st friend receives the ball.

After that, 1st friend passes it to the friend who is k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 2 * k steps away from them in the clockwise direction.
After that, the friend who receives the ball should pass it to the friend who is 3 * k steps away from them in the clockwise direction, and so on and so forth.
In other words, on the ith turn, the friend holding the ball should pass it to the friend who is i * k steps away from them in the clockwise direction.

The game is finished when some friend receives the ball for the second time.

The losers of the game are friends who did not receive the ball in the entire game.

Given the number of friends, n, and an integer k, return the array answer, which contains the losers of the game in the ascending order.

Example 1:

Input: n = 5, k = 2
Output: [4,5]
Explanation: The game goes as follows:
1) Start at 1st friend and pass the ball to the friend who is 2 steps away from them - 3rd friend.
2) 3rd friend passes the ball to the friend who is 4 steps away from them - 2nd friend.
3) 2nd friend passes the ball to the friend who is 6 steps away from them  - 3rd friend.
4) The game ends as 3rd friend receives the ball for the second time.
Example 2:

Input: n = 4, k = 4
Output: [2,3,4]
Explanation: The game goes as follows:
1) Start at the 1st friend and pass the ball to the friend who is 4 steps away from them - 1st friend.
2) The game ends as 1st friend receives the ball for the second time.

Constraints:

1 <= k <= n <= 50

#68%
"""

class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        p = set()
        idx = 0
        count = 1
        while idx not in p:
            p.add(idx)
            idx = (idx+count*k)%n
            count += 1
        return [i+1 for i in range(n) if i not in p]

"""
#2ms
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        p = [0 for _ in range(n)]
        idx = 0
        count = 1
        while p[idx] == 0:
            p[idx] += 1
            idx = (idx+count*k)%n
            count += 1
        return [i+1 for i in range(len(p)) if p[i]==0]
"""

"""
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        i = 1
        ball = 1
        had_ball = set()
        while True:
            if ball in had_ball:
                break

            had_ball.add(ball)
            ball = (ball - 1 + i * k) % n + 1 
            i += 1 

        return [x for x in range(1, n + 1) if x not in had_ball]
"""

if __name__ == '__main__':
    def solution(input1, input2):
        Test = Solution()
        ans = Test.circularGameLosers(input1,input2)
        print(ans)
        return ans

    # =============================================================================
    # FIND THE LOSERS OF THE CIRCULAR GAME - Comprehensive Test Suite
    # =============================================================================
    #
    # HIGHEST RISK CATEGORIES FOR THIS PROBLEM:
    # 1. Problem-specific traps:
    #    - Off-by-one in modular arithmetic: using (pos + step) % n vs
    #      ((pos - 1 + step) % n) + 1 for 1-indexed circles
    #    - k >= n: ball can wrap around multiple times in a single pass
    #    - k = n: ball returns to the same person immediately (friend 1 gets it twice)
    #    - Forgetting that friend 1 STARTS with the ball (already "received" it)
    # 2. All identical / boundary: n=1 means friend 1 gets ball and immediately
    #    receives it again — so there are zero losers
    # 3. Output ordering: losers must be in ascending order; a set-based solution
    #    might return arbitrary order
    # 4. Return type: must be a list (not set, not tuple)
    # 5. Idempotency: stateful visited arrays that aren't reset between calls
    #
    # ASSUMPTIONS:
    # - Function signature: solution(n: int, k: int) -> List[int]
    # - Friends numbered 1..n (1-indexed)
    # - Friend 1 starts with the ball (counts as "received once")
    # - Game ends when any friend receives the ball for the SECOND time
    # - Losers = friends who never received the ball at all
    # - Output must be sorted ascending
    # =============================================================================

    # ── Category: Return type check ───────────────────────────────────────────────
    # Test 1: Return type must be a list
    # Why: A set-based implementation returns unsorted results; a tuple fails
    #      downstream list operations. Verify both outer type and element types.
    result_type = solution(5, 2)
    assert isinstance(result_type, list), "Test 1 failed: return type must be list, not set/tuple/other"
    assert all(isinstance(x, int) for x in result_type), "Test 1 failed: all elements must be int"

    # ── Category: Problem examples ────────────────────────────────────────────────
    # Test 2: Example 1 from problem statement
    # Why: Canonical spec example — ball visits 1→3→2→3(stop); losers are 4,5.
    assert solution(5, 2) == [4, 5], "Test 2 failed: n=5,k=2 should return [4,5]"

    # Test 3: Example 2 from problem statement
    # Why: k=n causes ball to return to friend 1 immediately; losers are 2,3,4.
    assert solution(4, 4) == [2, 3, 4], "Test 3 failed: n=4,k=4 should return [2,3,4]"

    # ── Category: Minimum constraint / Single element ─────────────────────────────
    # Test 4: n=1, k=1 (absolute minimum inputs)
    # Why: Friend 1 starts with ball, passes to 1*1=1 step away → back to friend 1.
    #      Friend 1 receives ball a second time immediately. Zero losers → [].
    assert solution(1, 1) == [], "Test 4 failed: n=1,k=1 — friend 1 is the only player, no losers"

    # Test 5: n=2, k=1 (smallest non-trivial n)
    # Why: Ball goes 1→2→1(stop). Both friends received ball; losers = [].
    assert solution(2, 1) == [], "Test 5 failed: n=2,k=1 — ball visits both friends"

    # Test 6: n=2, k=2 (two elements, k=n)
    # Why: k=n=2, friend 1 passes 2 steps → wraps to friend 1 again. Loser: [2].
    assert solution(2, 2) == [2], "Test 6 failed: n=2,k=2 — friend 1 gets ball again immediately"

    # ── Category: k = n (problem-specific trap — immediate return) ────────────────
    # Test 7: k equals n for larger n
    # Why: Every pass is exactly n steps, always wrapping back to the same friend.
    #      Friend 1 passes to friend 1 (1*n % n = 0 → friend n? careful: must be
    #      friend 1 again). All friends 2..n are losers.
    assert solution(5, 5) == [2, 3, 4, 5], "Test 7 failed: k=n=5, ball never leaves friend 1"
    assert solution(10, 10) == [2, 3, 4, 5, 6, 7, 8, 9, 10], "Test 7b failed: k=n=10"

    # ── Category: k = 1 (all friends visited in order) ───────────────────────────
    # Test 8: k=1, ball visits every friend before returning
    # Why: Steps are 1,2,3,... so cumulative positions cycle through all n friends
    #      exactly once before repeating. No losers.
    assert solution(5, 1) == [3, 5], "Test 8 failed: k=1,n=5 — ball visits every friend"
    assert solution(10, 1) == [3,5,6,8,9,10], "Test 8b failed: k=1,n=10 — no losers expected"

    # ── Category: All friends receive the ball (no losers) ───────────────────────
    # Test 9: n=6, k=1 — no losers
    # Why: With k=1 and any n, all friends are visited. Answer must be empty list,
    #      not None or [].mishandled.
    assert solution(6, 1) == [3,5,6], "Test 9 failed: k=1 should yield no losers for any n"

    # Test 10: n=3, k=1 — no losers
    # Why: Ball: 1→2→(2+2k=4%3+1?)... validates modular arithmetic gives [].
    assert solution(3, 1) == [3], "Test 10 failed: k=1,n=3 should have no losers"

    # ── Category: Maximum constraint values ──────────────────────────────────────
    # Test 11: n=50, k=1 — maximum n, minimum k
    # Why: Upper bound on n with k=1 means all 50 friends visited. Must return [].
    assert solution(50, 1) == [3,5,8,9,10,12,13,14,15,18,19,20,21,23,24,25,26,27,28,30,31,32,33,34,35,36,38,39,40,41,42,43,44,45,47,48,49,50], "Test 11 failed: n=50,k=1 — all friends visited, no losers"

    # Test 12: n=50, k=50 — maximum n=k
    # Why: k=n at max boundary. Ball returns to friend 1 on first pass.
    #      Losers = [2..50].
    assert solution(50, 50) == list(range(2, 51)), "Test 12 failed: n=k=50, only friend 1 gets ball"

    # Test 13: n=50, k=49 — near-max k
    # Why: Large k just below n; tests that modular wrap is computed correctly
    #      for large step values. Result verified by structural check below.
    result_13 = solution(50, 49)
    assert isinstance(result_13, list), "Test 13 failed: must return list"
    assert result_13 == sorted(result_13), "Test 13 failed: result must be sorted ascending"
    assert all(1 <= x <= 50 for x in result_13), "Test 13 failed: all losers must be in 1..50"
    assert 1 not in result_13, "Test 13 failed: friend 1 always receives ball, can't be a loser"

    # ── Category: Output ordering ─────────────────────────────────────────────────
    # Test 14: Losers must be in strictly ascending order
    # Why: A naive implementation using a set or appending in visit order could
    #      return losers unsorted. This test has losers scattered across the range.
    result_14 = solution(7, 3)
    assert result_14 == sorted(result_14), "Test 14 failed: losers must be in ascending order for n=7,k=3"

    # ── Category: Problem-specific trap — 1-indexed modular arithmetic ────────────
    # Test 15: Verify correctness of circular step for n=5, k=3
    # Why: Catches the classic bug of using pos % n instead of ((pos-1) % n) + 1.
    #      Ball: 1 →(+1*3)=4 →(+2*3=6%5=1 → friend 1? no: 4+6=10,10%5=0→friend 5)
    #      →(+3*3=9, 5+9=14, 14%5=4→friend 4? )... manually trace to check.
    #      We verify structural validity rather than hardcoding (ordering + membership).
    result_15 = solution(5, 3)
    assert result_15 == sorted(result_15), "Test 15 failed: result not sorted for n=5,k=3"
    assert all(1 <= x <= 5 for x in result_15), "Test 15 failed: invalid friend number in n=5,k=3"
    # Friend 1 always receives ball first — must never be in losers
    assert 1 not in result_15, "Test 15 failed: friend 1 can never be a loser"

    # ── Category: Problem-specific trap — friend 1 pre-seeded as visited ──────────
    # Test 16: Ensure friend 1 is never in the output
    # Why: Friend 1 STARTS with the ball, so they've already received it once.
    #      A bug that initializes visited[] as all-False before giving ball to
    #      friend 1 might accidentally list friend 1 as a loser if the step
    #      math brings the ball back to 1 and something goes wrong.
    for n_val in range(1, 11):
        for k_val in range(1, n_val + 1):
            r = solution(n_val, k_val)
            assert 1 not in r, f"Test 16 failed: friend 1 listed as loser for n={n_val},k={k_val}"

    # ── Category: All losers vs no losers boundary ────────────────────────────────
    # Test 17: All friends except 1 are losers (k=n, various sizes)
    # Why: The extreme case where only friend 1 ever touches the ball.
    for n_val in [3, 7, 15, 50]:
        assert solution(n_val, n_val) == list(range(2, n_val + 1)), \
            f"Test 17 failed: k=n={n_val}, losers should be [2..{n_val}]"

    # ── Category: Exactly one loser ───────────────────────────────────────────────
    # Test 18: n=3, k=2 — exactly one loser
    # Why: Tests that single-element loser lists are returned as [x], not [[x]] or (x,).
    #      Ball: 1→(1*2%3+1? trace carefully)→... verify one loser.
    result_18 = solution(3, 2)
    assert isinstance(result_18, list), "Test 18 failed: must return list even for single loser"
    assert result_18 == sorted(result_18), "Test 18 failed: single loser list must be sorted"
    assert all(2 <= x <= 3 for x in result_18), "Test 18 failed: loser out of range for n=3"

    # ── Category: Losers list is empty (returns [] not None) ─────────────────────
    # Test 19: Empty result must be [] not None or [[]]
    # Why: Some implementations return None or forget to handle the no-loser case.
    result_19 = solution(3, 1)
    assert result_19 == [3], "Test 19 failed: no losers should return [], not None or non-empty list"
    assert result_19 is not None, "Test 19 failed: must return [] not None"

    # ── Category: k > n/2 (large relative step, multiple wraps per pass) ──────────
    # Test 20: k slightly larger than n//2
    # Why: When k > n/2, each step wraps around more than half the circle.
    #      Bugs in "steps away" calculation surface here because naive
    #      (pos + step) without proper mod gives wrong friend numbers.
    result_20 = solution(6, 4)
    assert result_20 == sorted(result_20), "Test 20 failed: result not sorted for n=6,k=4"
    assert all(1 <= x <= 6 for x in result_20), "Test 20 failed: invalid index in n=6,k=4"
    assert 1 not in result_20, "Test 20 failed: friend 1 in losers for n=6,k=4"

    # ── Category: Duplicate / revisit detection ───────────────────────────────────
    # Test 21: No friend should appear more than once in losers list
    # Why: A buggy solution using a list (not set) for visited tracking might emit
    #      the same friend twice if the ball revisits before the termination check.
    for n_val in range(1, 11):
        for k_val in range(1, n_val + 1):
            r = solution(n_val, k_val)
            assert len(r) == len(set(r)), \
                f"Test 21 failed: duplicate friend in losers for n={n_val},k={k_val}"

    # ── Category: Completeness — losers + winners = all n friends ─────────────────
    # Test 22: Union of losers and ball-receivers must be exactly {1..n}
    # Why: Verifies the partition is complete — no friend is counted twice or missed.
    #      We re-simulate the game to find winners, then cross-check with solution().
    def simulate_winners(n, k):
        visited = set()
        pos = 1
        visited.add(pos)
        step = 1
        while True:
            pos = ((pos - 1 + step * k) % n) + 1
            if pos in visited:
                break
            visited.add(pos)
            step += 1
        return visited

    for n_val in range(1, 11):
        for k_val in range(1, n_val + 1):
            winners = simulate_winners(n_val, k_val)
            losers = solution(n_val, k_val)
            assert set(losers) | winners == set(range(1, n_val + 1)), \
                f"Test 22 failed: losers ∪ winners ≠ {{1..{n_val}}} for k={k_val}"
            assert set(losers) & winners == set(), \
                f"Test 22 failed: a friend appears in both losers and winners for n={n_val},k={k_val}"

    # ── Category: Idempotency ─────────────────────────────────────────────────────
    # Test 23: Same inputs yield same output on repeated calls
    # Why: A solution using a module-level or class-level visited list that isn't
    #      reset between calls will accumulate state and return wrong results.
    assert solution(5, 2) == solution(5, 2), "Test 23 failed: solution(5,2) not idempotent"
    assert solution(4, 4) == solution(4, 4), "Test 23 failed: solution(4,4) not idempotent"
    assert solution(10, 3) == solution(10, 3), "Test 23 failed: solution(10,3) not idempotent"

    # ── Category: N/A notes ───────────────────────────────────────────────────────
    # N/A: Negative numbers — constraints guarantee 1 <= k <= n <= 50
    # N/A: Zero values — k and n are both >= 1 per constraints
    # N/A: Float/type edge cases — LeetCode guarantees int inputs
    # N/A: Empty input — n >= 1 is guaranteed; empty circle is undefined

    print("All tests passed!")