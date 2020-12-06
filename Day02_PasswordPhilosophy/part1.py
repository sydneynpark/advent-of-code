import helpers







if __name__ == '__main__':
    pw_n_pol = helpers.parse_file('./resources/passwords.txt', helpers.PositionPolicy)
    num_valid = sum(1 for (pw, policy) in pw_n_pol if policy.validate(pw))
    print(len(pw_n_pol))
    print(num_valid)