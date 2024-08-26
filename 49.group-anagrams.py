class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    h = defaultdict(list)
    for s in strs:
      sorted_word = "".join(sorted(s))
      h[sorted_word].append(s)
    return h.values()
