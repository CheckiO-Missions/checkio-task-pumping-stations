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
            "answer": [4, 4],
            "explanation": [
                [1, 1, 1, 2],
                [2, 1, 2, 2],
                [1, 3, 1, 4],
                [2, 3, 2, 4],
            ]
        },
        #Second
        {
            "input":
                [
                    [1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1]
                ],
            "answer": [0, 0],
            "explanation": [
            ]
        },
        #Third
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 1]
                ],
            "answer": [3, 5],
            "explanation": [
                [1, 1, 1, 4],
                [1, 4, 2, 4],
                [2, 3, 2, 4],
            ]
        },
        #Fourth
        {
            "input":
                [
                    [1, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1]
                ],
            "answer": [1, 1],
            "explanation": [
                [1, 1, 1, 2],
            ]
        },
        #Fifth
        {
            "input":
                [
                    [1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0]
                ],
            "answer": [1, 3],
            "explanation": [
                [1, 1, 1, 4],
            ]
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
            "answer": [3, 9],
            "explanation": [
                [1, 1, 1, 4],
                [1, 1, 4, 1],
                [1, 4, 4, 4],
            ]
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
            "answer": [4, 4],
            "explanation": [
                [1, 1, 2, 1],
                [1, 4, 2, 4],
                [3, 1, 4, 1],
                [3, 4, 4, 4],
            ]
        },
        {
            "input":
                [[1, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1, 0, 1]],
            "answer": [2, 2],
            "explanation": [
                [1, 1, 1, 2],
                [4, 4, 4, 6],
            ]
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
            "answer": [0, 0],
            "explanation": []
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
            "answer": [0, 0],
            "explanation": [
            ]
        },
        #H3
        {
            "input":
                [
                    [1, 1, 1],
                    [0, 0, 0],
                    [1, 1, 1]
                ],
            "answer": [1, 1],
            "explanation": [
                [1, 1, 2, 1],
            ]
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
            "answer": [4, 6],
            "explanation": [
                [1, 1, 1, 2],
                [1, 3, 1, 4],
                [1, 1, 4, 1],
                [4, 2, 4, 3],
            ]
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
            "answer": [3, 3],
            "explanation": [
                [3, 2, 4, 2],
                [2, 3, 2, 4],
                [4, 3, 4, 4],
            ]
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
            "answer": [0, 0],
            "explanation": [
            ]
        },

    ]
}
