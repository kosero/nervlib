def brainfuck(code):
    memory = [0] * 30000
    pointer = 0
    output = ""
    loop_stack = []

    i = 0
    while i < len(code):
        command = code[i]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output += chr(memory[pointer])
        elif command == ',':
            memory[pointer] = ord(input("")[0])
        elif command == '[':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets > 0:
                    i += 1
                    if code[i] == '[':
                        open_brackets += 1
                    elif code[i] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(i)
        elif command == ']':
            if memory[pointer] != 0:
                i = loop_stack[-1]
            else:
                loop_stack.pop()

        i += 1

    return output

