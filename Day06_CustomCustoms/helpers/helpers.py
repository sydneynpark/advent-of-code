

def count_questions_anyone_answered(group_answers):

    questions_any_answered_yes_to = set()

    for person_answers in group_answers:
        questions_any_answered_yes_to = questions_any_answered_yes_to.union(person_answers)

    return len(questions_any_answered_yes_to)

def count_questions_everyone_answered(group_answers):

    # Grab the first person's answers to start with
    questions_all_answered_yes_to = set(group_answers[0])

    for person_answers in group_answers:
        questions_all_answered_yes_to = questions_all_answered_yes_to.intersection(person_answers)

    return len(questions_all_answered_yes_to)


def read_answers_file(filepath):
    with open(filepath, 'r') as f:
        contents = f.read()

        answers_by_group = contents.split('\n\n')
        print(answers_by_group)


        group_answers_by_person = [
            group_answer_string.split('\n')
            for group_answer_string
            in answers_by_group
        ]
        print(group_answers_by_person)


        group_answers_by_person_by_question = [
            [
                [
                    # break out each person's survey
                    # into the individual questions they answered YES to
                    question_letter
                    for question_letter
                    in person_answers
                ]

                # one group is represented by a list
                # containing each individual's answer lists
                for person_answers
                in group_answers
            ]

            # the full survey results are respresented by a list
            # containing each group's results as an item in that list
            for group_answers
            in group_answers_by_person
        ]
        print(group_answers_by_person_by_question)

        return group_answers_by_person_by_question
