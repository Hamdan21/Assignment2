import plots_cli

def test_quit():
    plots_cli.quit()
    assert True

def test_student_average():
    plots_cli.student_average("stu /Users/hamdan/Downloads/GCIS.123.600-assignment2-sample.csv Gonsalves Kartik")
    assert True

def test_print_average():
    plots_cli.print_average("avg /Users/hamdan/Downloads/GCIS.123.600-assignment2-sample.csv 4")
    assert True