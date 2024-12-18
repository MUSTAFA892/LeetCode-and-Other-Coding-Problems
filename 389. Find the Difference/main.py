class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      s_ = Counter(s)
      t_ = Counter(t)
      diff = t_ - s_
      return list(diff.keys())[0]