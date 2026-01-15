class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            def distance(num):
                return abs(num - x)

            closest = arr[0]
            min_dist = abs(arr[0] - x)

            for num in arr:
                dist = abs(num - x)
                if dist < min_dist:
                    min_dist = dist
                    closest = num
            idx = arr.index(closest)

            l = idx - 1
            r = idx + 1

            ans = [closest]

            while len(ans) < k:
                if l >= 0 and r < len(arr):
                    if distance(arr[l]) <= distance(arr[r]):
                        ans.append(arr[l])
                        l -= 1
                    else:
                        ans.append(arr[r])
                        r += 1
                elif l >= 0:
                    ans.append(arr[l])
                    l -= 1
                elif r < len(arr):
                    ans.append(arr[r])
                    r += 1
                else:
                    break

            return sorted(ans)
