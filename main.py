def calculate_love_score(name1, name2):
    first_step = 0
    second_step = 0
    correct_letter1 = ["t", "r", "u", "e"]
    correct_letter2 = ["l", "o", "v", "e"]
    names = [name1, name2]

    for name in names:
        for letter in correct_letter1:
            first_step += name.lower().count(letter)

        for letter in correct_letter2:
            second_step += name.lower().count(letter)

    print(f"First Step (TRUE letters): {first_step}")
    print(f"Second Step (LOVE letters): {second_step}")

    love_score = int(str(first_step) + str(second_step))
    print(f"Love Score: {love_score}")


name1 = input("Name and Surname for first person:   ")
name2 = input("Name and Surname for second person:   ")
calculate_love_score(name1, name2)
