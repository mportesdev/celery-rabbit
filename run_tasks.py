from project.tasks import power_sum, write_to_text_file

if __name__ == "__main__":
    data = list(range(1_000_000))

    square_sum = power_sum.signature((2,))
    cube_sum = power_sum.s(3)  # shortcut for `.signature((3,))`

    write_to_results = write_to_text_file.s('results.txt')

    (square_sum | write_to_results)(data)
    (cube_sum | write_to_results)(data)
