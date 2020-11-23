import ttt as program_file
import os
import csv
import multiprocessing

# Help functie voor het uitprinten van het resultaat van een test met gegeven nummer en boolean die het succes van de test weergeeft
def print_result(test_nb, succes_boolean):
    test_string = 'Test ' + str(test_nb) + ':'
    if succes_boolean:
        print(test_string, 'correct')
    else:
        print(test_string, 'foutief')


# Testen voor de functie eentonige_lijst(l)
def test_eentonige_lijst(program_file, scores):
    score = 0.0
    # Test 1
    expected = True
    try:
        succes = program_file.eentonige_lijst([]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    if succes:
        score += 1.0
    # Test 2
    expected = True
    try:
        succes = program_file.eentonige_lijst([5]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    if succes:
        score += 1.0
    # Test 3
    expected = True
    try:
        succes = program_file.eentonige_lijst([6, 6]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    if succes:
        score += 1.0
    # Test 4
    expected = False
    try:
        succes = program_file.eentonige_lijst([1, 7]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)
    if succes:
        score += 1.0
    # Test 5
    expected = False
    try:
        succes = program_file.eentonige_lijst([1, '1']) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(5, succes)
    if succes:
        score += 1.0
    # Test 6
    expected = True
    try:
        succes = program_file.eentonige_lijst(['1', '1']) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(6, succes)
    if succes:
        score += 1.0
    # Test 7
    expected = True
    try:
        succes = program_file.eentonige_lijst([False, False]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(7, succes)
    if succes:
        score += 1.0
    # Test 8
    expected = False
    try:
        succes = program_file.eentonige_lijst([True, False]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(8, succes)
    if succes:
        score += 1.0
    scores[0] = score/8.0
    return score/8.0


# Testen voor de functie is_lege_matrix(m)
def test_is_lege_matrix(program_file, scores):
    score = 0.0
    # Test 1
    expected = True
    try:
        succes = program_file.is_lege_matrix([]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    if succes:
        score += 1.0
    # Test 2
    expected = True
    try:
        succes = program_file.is_lege_matrix([[]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    if succes:
        score += 1.0
    # Test 3
    expected = False
    try:
        succes = program_file.is_lege_matrix([6, 4]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    if succes:
        score += 1.0
    # Test 4
    expected = False
    try:
        succes = program_file.is_lege_matrix([22]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)
    if succes:
        score += 1.0
    # Test 5
    expected = False
    try:
        succes = program_file.is_lege_matrix([False]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(5, succes)
    if succes:
        score += 1.0
    scores[1] = score/5.0
    return score/5.0


# Testen voor de functie is_matrix(m)
def test_is_matrix(program_file, scores):
    score = 0.0
    # Test 1
    expected = True
    try:
        succes = program_file.is_matrix([]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    if succes:
        score += 1.0
    # Test 2
    expected = True
    try:
        succes = program_file.is_matrix([[]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    if succes:
        score += 1.0
    # Test 3
    expected = True
    try:
        succes = program_file.is_matrix([[1]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    if succes:
        score += 1.0
    # Test 4
    expected = True
    try:
        succes = program_file.is_matrix([[4, 'c']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)
    if succes:
        score += 1.0
    # Test 5
    expected = True
    try:
        succes = program_file.is_matrix([[1, 'z'], [False, 1.9]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(5, succes)
    if succes:
        score += 1.0
    # Test 6
    expected = False
    try:
        succes = program_file.is_matrix([[1, 'a'], [True, 1.2], ["hello"]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(6, succes)
    if succes:
        score += 1.0
    # Test 7
    expected = False
    try:
        succes = program_file.is_matrix([[1, 'a'], [True, 1.2, 'd']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(7, succes)
    if succes:
        score += 1.0
    # Test 8
    expected = False
    try:
        succes = program_file.is_matrix([[1, 'a', False], [True, 1.2], ["hello", 25, '8']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(8, succes)
    if succes:
        score += 1.0
    scores[2] = score/8.0
    return score/8.0


# Testen voor de functie gelijke_rand_matrix(m)
def test_gelijke_rand_matrix(program_file, scores):
    score = 0.0
    # Test 1
    expected = False
    try:
        succes = program_file.gelijke_rand_matrix([[1, 'a'], [False, 1.2]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    if succes:
        score += 1.0
    # Test 2
    expected = False
    try:
        succes = program_file.gelijke_rand_matrix([[1, 1, 1, 1],
                                                   [1, 1.2, True, 1],
                                                   [1, 1, 2, 1]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    if succes:
        score += 1.0
    # Test 3
    expected = True
    try:
        succes = program_file.gelijke_rand_matrix([[1, 1, 1, 1],
                                                   [1, 1.2, True, 1],
                                                   [1, 1, 1, 1]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    if succes:
        score += 1.0
    # Test 4
    expected = True
    try:
        succes = program_file.gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                                                   ['a', 1.2, True, 'a'],
                                                   ['a', 1, 2, 'a'],
                                                   ['a', 'a', 'a', 'a']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)
    if succes:
        score += 1.0
    # Test 5
    expected = False
    try:
        succes = program_file.gelijke_rand_matrix([['a', 'a', 'a', 'a'],
                                                   ['a', 1.2, True, 'a'],
                                                   ['a', 25, 1, 'a'],
                                                   ['a', 'b', 'a', 'a']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(5, succes)
    if succes:
        score += 1.0
    # Test 6
    expected = False
    try:
        succes = program_file.gelijke_rand_matrix([[False, False, False, False, False],
                                                   [False, False, False, False, False],
                                                   [False, False, False, False, False],
                                                   [False, False, False, False, False],
                                                   [False, False, False, False, True]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(6, succes)
    if succes:
        score += 1.0
    # Test 7
    expected = True
    try:
        succes = program_file.gelijke_rand_matrix([[False, False, False, False, False],
                                                   [False, 1, 1, False, False],
                                                   [False, False, 1, False, False],
                                                   [False, 1, False, 1, False],
                                                   [False, False, False, False, False]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(7, succes)
    if succes:
        score += 1.0
    scores[3] = score/7.0
    return score/7.0


# Testen voor de functie strip_matrix(m)
def test_strip_matrix(program_file, scores):
    score = 0.0
    # Test 1
    expected = [ [1.2, True], [1, 1] ]
    try:
        succes = program_file.strip_matrix([['a', 'a', 'a', 'a'],
                                            ['a', 1.2, True, 'a'],
                                            ['a', 1, 1, 'a'],
                                            ['a', 'b', 'a', 'a']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(1, succes)
    if succes:
        score += 1.0
    # Test 2
    expected = [ [1.2, True] ]
    try:
        succes = program_file.strip_matrix([['a', 'a', 'a', 'a'],
                                            ['a', 1.2, True, 'a'],
                                            ['a', 'b', 'a', 'a']]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(2, succes)
    if succes:
        score += 1.0
    # Test 3
    expected = False
    try:
        succes = program_file.strip_matrix([[1, 1, 1, 1]]) == [] or program_file.strip_matrix([[1, 1, 1, 1]]) == [[]]
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(3, succes)
    if succes:
        score += 1.0
    # Test 4
    expected = [ [1, 1, False],[False, 1, False],[1, False, 1]]
    try:
        succes = program_file.strip_matrix([[False, False, False, False, False],
                                                   [False, 1, 1, False, False],
                                                   [False, False, 1, False, False],
                                                   [False, 1, False, 1, False],
                                                   [False, False, False, False, False]]) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(4, succes)
    if succes:
        score += 1.0
    # Test 5
    expected = [[True]]
    try:
        succes = program_file.strip_matrix(program_file.strip_matrix([[False, False, False, False, False],
                                                   [False, False, False, False, False],
                                                   [False, False, True, False, False],
                                                   [False, False, False, False, False],
                                                   [False, False, False, False, True]])) == expected
    except Exception as e:
        succes = False
        print('Je programma gooide volgende error:', e)
    print_result(5, succes)
    if succes:
        score += 1.0
    scores[4] = score/5.0
    return score/5.0

from multiprocessing import Process
from time import sleep

def f(time):
    sleep(time)

def run_all_tests_for_user(program_file):
    manager = multiprocessing.Manager()
    scores = manager.dict()
    scores[0] = 0.0
    scores[1] = 0.0
    scores[2] = 0.0
    scores[3] = 0.0
    scores[4] = 0.0
    print('###')
    print('Testen voor de functie:', 'eentonige_lijst(l)')
    test_eentonige_lijst(program_file, scores)
    print('###')
    print('Testen voor de functie:', 'is_lege_matrix(m)')
    test_is_lege_matrix(program_file, scores)
    print('###')
    print('Testen voor de functie:', 'is_matrix(m)')
    test_is_matrix(program_file, scores)
    print('###')
    print('Testen voor de functie:', 'gelijke_rand_matrix(m)')
    test_gelijke_rand_matrix(program_file, scores)
    print('###')
    print('Testen voor de functie:', 'strip_matrix(m)')
    test_strip_matrix(program_file, scores)
    print('###')
    line = [scores[0]] + [scores[1]] + [scores[2]] + [scores[3]] + [scores[4]]
    print(line)


def main():
    examens = []
    # r=root, d=directories, f = files
    for root, dirs, files in os.walk("."):
        for file_name in files:
            if file_name.endswith(".py") and "quoteer" not in file_name:
                examens.append(file_name[:-3])
                print(file_name[:-3])
    result_file = open('Resultaten.csv', 'w', newline='')
    result_writer = csv.writer(result_file, delimiter=';')
    result_writer.writerow(["file_name", "eentonig", "lege matrix", "is matrix", "gelijke rand", "strip matrix"])
    for examen in examens:
        print(examen)
        scores = run_all_tests_for_user(examen)
        print(scores)
        examen_name = examen.split('_')[1]
        line = [examen_name] + [scores[0]] + [scores[1]] + [scores[2]] + [scores[3]] + [scores[4]]
        result_writer.writerow(line)

if __name__ == "__main__":
    run_all_tests_for_user(program_file)