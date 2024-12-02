# Advent Of Code 2024: Day 2
def load(file: str):
    with open(file, "r") as f:
        return f.read().strip().split("\n")


def parse_numbers(problems):
    list_of_numbers = []
    for problem in problems:
        list_of_numbers.append([int(num) for num in problem.split()])
    return list_of_numbers


def is_safe(numbers):
    prev_number = numbers[0]
    increasing = numbers[0] < numbers[1]

    for index, number in enumerate(numbers):
        if index == 0:
            continue

        diff = abs(prev_number - number)
        if not (0 < diff < 4) or (prev_number < number) != increasing:
            return False
        prev_number = number

    return True


def part1(list_of_numbers):
    unsafe_reports = 0
    for numbers in list_of_numbers:
        if not is_safe(numbers):
            unsafe_reports += 1
    return len(list_of_numbers) - unsafe_reports


def part2(list_of_numbers):
    unsafe_reports = 0

    for numbers in list_of_numbers:
        if is_safe(numbers):
            continue

        safe_after_removal = False
        
        for i in range(len(numbers)):
            modified_numbers = numbers[:i] + numbers[i + 1:]
            
            if is_safe(modified_numbers):
                safe_after_removal = True
                break

        if not safe_after_removal:
            unsafe_reports += 1

    return len(list_of_numbers) - unsafe_reports

if __name__ == "__main__":
    problems = load("day2/input.txt")
    list_of_numbers = parse_numbers(problems)
    
    total1 = part1(list_of_numbers)
    total2 = part2(list_of_numbers)
    
    print(f"Total number of safe reports in part 1: {total1}")
    print(f"Total number of safe reports in part 2: {total2}")
