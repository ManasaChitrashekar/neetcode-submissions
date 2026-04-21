class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        handsmap = Counter(hand)
        groupcount = len(hand) // groupSize

        for h in sorted(hand):
            count = handsmap[h]
            if count > 0 :
                for i in range(groupSize):
                    if handsmap[h+i]<count:
                        return False
                    handsmap[h+i] -= count
        return True   