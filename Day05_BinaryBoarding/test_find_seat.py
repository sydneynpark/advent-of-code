import unittest
import part1

class MyTestCase(unittest.TestCase):

    def test_find_seat(self):
        '''
        BFFFBBFRRR: row 70, column 7, seat ID 567.
        FFFBBBFRRR: row 14, column 7, seat ID 119.
        BBFFBBFRLL: row 102, column 4, seat ID 820.
        '''
        test_cases = {
            "FBFBBFFRLR": 357,
            "BFFFBBFRRR": 567,
            "FFFBBBFRRR": 119,
            "BBFFBBFRLL": 820
        }

        for boarding_pass, seat_id in test_cases.items():
            found_seat = part1.find_seat(boarding_pass)
            self.assertEqual(seat_id, found_seat)

if __name__ == '__main__':
    unittest.main()
