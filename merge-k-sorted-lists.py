from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curNode = None
        head = None
        curRes = None
        while True:
            minVal = None
            minListIndex = None
            for listIndex in range(len(lists)):
                list = lists[listIndex]
                if list is None:
                    continue
                if minVal is None or minVal > list.val:
                    minVal = list.val
                    minListIndex = listIndex

            if minVal is None:
                break
            if head is None:
                head = ListNode(
                    minVal,
                )
                curNode = head
            else:
                newNode = ListNode(minVal)
                curNode.next = newNode
                curNode = newNode

            cur = lists[minListIndex]
            lists[minListIndex] = cur.next

            minVal = None
            minListIndex = None
        return head


def build_list(values: List[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_list(node: ListNode) -> None:
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values) + " -> None")


# In the if __name__ == "__main__" block, replace print(res) with:

if __name__ == "__main__":
    s = Solution()
    # lists = [build_list([1, 2, 4]), build_list([1, 3, 5]), build_list([3, 6])]
    lists = [build_list([1, 2, 4]), build_list([1, 3, 5]), build_list([3, 6])]
    res = s.mergeKLists(lists)
    print_list(res)
