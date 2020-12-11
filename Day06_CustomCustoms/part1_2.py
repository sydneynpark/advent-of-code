from helpers import helpers



if __name__ == '__main__':
    survey_results = helpers.read_answers_file('resources/customs_answers.txt')

    total_yeses = sum([
        helpers.count_questions_anyone_answered(group_answers)
        for group_answers
        in survey_results
    ])

    unanimous_yeses = sum([
        helpers.count_questions_everyone_answered(group_answers)
        for group_answers
        in survey_results
    ])

    print(total_yeses)
    print(unanimous_yeses)