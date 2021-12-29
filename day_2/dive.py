def forward(position, move):
    print(f"Moving forward by {move}")
    return position + move


def up(depth, y):
    print(f"Moving up by {y}")
    return depth - y


def down(depth, y):
    print(f"Moving down by {y}")
    return depth + y


with open('input.txt') as f:
    commands = f.readlines()

position = 0
depth = 0

print(f"Beginning command processing with position={position} and depth={depth}")

for cmd in commands:
    movement, unit = cmd.split()
    func = locals()[movement]
    if movement == 'forward':
        position = func(position, int(unit))
    else:
        depth = func(depth, int(unit))

print(f"Ending command processing with position={position} and depth={depth}")
print(f"Multiplied Result = {position * depth}")