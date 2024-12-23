from project.tasks import power_sum

if __name__ == "__main__":
    data = list(range(1_000_000))

    square_sum = power_sum.signature((2,))
    square_sum.apply_async((data,))

    cube_sum = power_sum.s(3)  # shortcut for `.signature((3,))`
    cube_sum.delay(data)  # shortcut for `.apply_async((data,))`
