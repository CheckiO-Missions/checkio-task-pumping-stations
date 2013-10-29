"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        #First
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 1]
                ],
            "answer": [4, 4]
        },
        #Second
        {
            "input":
                [
                    [1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1]
                ],
            "answer": [0, 0]
        },
        #Third
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 1]
                ],
            "answer": [3, 5]
        },
        #Fourth
        {
            "input":
                [
                    [1, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1]
                ],
            "answer": [1, 1]
        },
        #Fifth
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0]
                ],
            "answer": [1, 3]
        },
        #Sixth
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 1]
                ],
            "answer": [3, 9]
        },
        #Seventh
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 1]
                ],
            "answer": [4, 4]
        },
    ],
    "Extra": [
        #H1 - square
        {
            "input":
                [
                    [1, 1],
                    [1, 1]
                ],
            "answer": [0, 0]
        },
        #H2 - diagonal cross
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [1, 0, 0, 0, 1]
                ],
            "answer": [0, 0]
        },
        #H3
        {
            "input":
                [
                    [1, 1, 1],
                    [0, 0, 0],
                    [1, 1, 1]
                ],
            "answer": [1, 1]
        },
        #H4 - tricky length
        {
            "input":
                [
                    [1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                ],
            "answer": [4, 6]
        },
        #H5
        {
            "input":
                [
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 1],
                ],
            "answer": [3, 3]
        },
        #H6
        {
            "input":
                [
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1],
                    [0, 0, 1, 1, 1],
                    [0, 0, 1, 1, 1],
                ],
            "answer": [0, 0]
        },

    ]
}
