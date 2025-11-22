import io
import contextlib

def get_function(input):
    f = io.StringIO()
    namespace = {}
    with contextlib.redirect_stdout(f):
                exec(input, namespace)  # define functions, variables, etc.
    result = None

    # Find all functions in the namespace
    functions = [obj for obj in namespace.values() if callable(obj)]

    if functions:
        # Call the last function defined
        result = functions[-1]()
    return result

def execute_function(code):
    f = io.StringIO()
    output = f.getvalue().strip()
    return output

def test_case(code, expected):
    expected = str(expected)
    return execute_function(code) == expected

problems = {
            "Two Sum": {"name":"Two Sum", 
                        "function_header": "def TwoSum(List[int], target: int) -> List[int]", 
                        "incorrect_solution":"""def (nums: List[int], target: int) -> List[int]:
                                                    for i in range(len(nums)):
                                                        for j in range(len(nums)):
                                                            if nums[i] + nums[j] == target:
                                                                return [i, j]""",
                        "description":   """Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

                                            You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

                                            Return the answer with the smaller index first.

                                            Example 1:

                                            Input: 
                                            nums = [3,4,5,6], target = 7

                                            Output: [0,1]
                                            Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

                                            Example 2:

                                            Input: nums = [4,5,6], target = 10

                                            Output: [0,2]
                                            Example 3:

                                            Input: nums = [5,5], target = 10

                                            Output: [0,1]
                                            Constraints:

                                            2 <= nums.length <= 1000
                                            -10,000,000 <= nums[i] <= 10,000,000
                                            -10,000,000 <= target <= 10,000,000
                                            """},
            "Palindrome": {"name": "Palindrome", 
                           "function_header": "def isPalindrome(s: str) -> bool", \
                           "incorrect_solution":"""def isPalindrome(s: str) -> bool:
                                                        s = s.lower()
                                                        filtered = ''.join(c for c in s if c.isalpha())
                                                        return filtered == filtered[::-1]""",
                           "description":"""Given a string s, return true if it is a palindrome, otherwise return false.

                                            A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

                                            Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

                                            Example 1:

                                            Input: s = "Was it a car or a cat I saw?"

                                            Output: true
                                            Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

                                            Example 2:

                                            Input: s = "tab a cat"

                                            Output: false
                                            Explanation: "tabacat" is not a palindrome.

                                            Constraints:

                                            1 <= s.length <= 1000
                                            s is made up of only printable ASCII characters.
                                            """},
            "Remove Node": {"name":"Remove Node",
                            "function_header": "def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:", 
                            "incorrect_solution":"""def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
                                                        length = 0
                                                        current = head
                                                        while current:
                                                            length += 1
                                                            current = current.next
                                                        current = head
                                                        for _ in range(length - n - 1):
                                                            current = current.next
                                                        current.next = current.next.next
                                                        return head""",
                            "description":   """You are given the beginning of a linked list head, and an integer n.

                                                Remove the nth node from the end of the list and return the beginning of the list.

                                                Example 1:

                                                Input: head = [1,2,3,4], n = 2

                                                Output: [1,2,4]
                                                Example 2:

                                                Input: head = [5], n = 1

                                                Output: []
                                                Example 3:

                                                Input: head = [1,2], n = 2

                                                Output: [2]
                                                Constraints:

                                                The number of nodes in the list is sz.
                                                1 <= sz <= 30
                                                0 <= Node.val <= 100
                                                1 <= n <= sz
                                                """}
            }

def get_problem(problem_name):
    try:
        return problems[problem_name]
    except:
        print("Problem not found")