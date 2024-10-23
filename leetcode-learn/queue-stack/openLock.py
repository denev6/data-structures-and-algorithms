from collections import deque


class Solution:
    def openLock(self, deadends, target) -> int:
        dials = deque([("0000", 0)])  # (dial, num_trial)
        visited = set("0000")

        if "0000" in deadends:
            return -1

        while dials:
            # search dials with BFS in a Tree
            # dial: node
            # num_trial: depth
            dial, num_trial = dials.popleft()

            if dial == target:
                return num_trial

            for i in range(len(dial)):
                # turn dial up and down (search children)
                for direction in (1, -1):
                    turned = (
                        int(dial[i]) + direction
                    ) % 10  # in case 9 turns 0 or 0 turns 9
                    new_dial = "".join([dial[:i], str(turned), dial[i + 1 :]])

                    if new_dial not in deadends and new_dial not in visited:
                        visited.add(new_dial)
                        dials.append((new_dial, num_trial + 1))

        return -1