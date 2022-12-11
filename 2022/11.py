from dataclasses import dataclass

monkeys_test = [
    {
        'items': [79, 98],
        'operation': 'old * 19',
        'test': 23,
        'throw': (3, 2),
        'inspections': 0
    },
    {
        'items': [54, 65, 75, 74],
        'operation': 'old + 6',
        'test': 19,
        'throw': (0, 2),
        'inspections': 0
    },
    {
        'items': [79, 60, 97],
        'operation': 'old * old',
        'test': 13,
        'throw': (3, 1),
        'inspections': 0
    },
    {
        'items': [74],
        'operation': 'old + 3',
        'test': 17,
        'throw': (1, 0),
        'inspections': 0
    }
    ]

monkeys_real = [
    {
        'items': [92, 73, 86, 83, 65, 51, 55, 93],
        'operation': 'old * 5',
        'test': 11,
        'throw': (4, 3),
        'inspections': 0
    },
    {
        'items': [99, 67, 62, 61, 59, 98],
        'operation': 'old * old',
        'test': 2,
        'throw': (7, 6),
        'inspections': 0
    },
    {
        'items': [81, 89, 56, 61, 99],
        'operation': 'old * 7',
        'test': 5,
        'throw': (5, 1),
        'inspections': 0
    },
    {
        'items': [97, 74, 68],
        'operation': 'old + 1',
        'test': 17,
        'throw': (5, 2),
        'inspections': 0
    },
    {
        'items': [78, 73],
        'operation': 'old + 3',
        'test': 19,
        'throw': (3, 2),
        'inspections': 0
    },
    {
        'items': [50],
        'operation': 'old + 5',
        'test': 7,
        'throw': (6, 1),
        'inspections': 0
    },
    {
        'items': [95, 88, 53, 75],
        'operation': 'old + 8',
        'test': 3,
        'throw': (7, 0),
        'inspections': 0
    },
    {
        'items': [50, 77, 98, 85, 94, 56, 89],
        'operation': 'old + 2',
        'test': 13,
        'throw': (0, 4),
        'inspections': 0
    }
]

monkeys = monkeys_real

mod = 11 * 2 * 5 * 17 * 19 * 7 * 3 * 13

for _ in range(10000): # 20 for part A
    for monkey in monkeys:
        for old in monkey['items']:
            old = eval(monkey['operation']) % mod # // 3 for part A
            test = old % monkey['test'] == 0
            throw_to = monkey['throw'][test]
            monkeys[throw_to]['items'].append(old)
            monkey['inspections'] += 1
        monkey['items'] = []

inspections = sorted([monkey['inspections'] for monkey in monkeys], reverse=True)
print("Part B: ", inspections[0] * inspections[1])
