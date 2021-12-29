def forward(p, d, a, move):
    print(f"Moving forward by {move}")
    new_position = p + move
    new_depth = d + (a * move)
    return new_position, new_depth


def up(a, y):
    print(f"Decreasing aim by {y}")
    return a - y


def down(a, y):
    print(f"Increasing aim by {y}")
    return a + y


with open('input.txt') as f:
    commands = f.readlines()

position = 0
depth = 0
aim = 0

print(f"Beginning command processing with position={position}, depth={depth} and aim={aim}")

for cmd in commands:
    movement, unit = cmd.split()
    func = locals()[movement]
    if movement == 'forward':
        position, depth = func(position, depth, aim, int(unit))
    else:
        aim = func(aim, int(unit))

print(f"Ending command processing with position={position}, depth={depth} and aim={aim}")
print(f"Multiplied Result = {position * depth}")