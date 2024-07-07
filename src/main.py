from pyfun_my.option import Option
from pyfun_my.pyfunList import PyfunList

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    option_five: Option = Option(5)

    program = (
        option_five
        .map(lambda x: x + 1)
        .flat_map(lambda x: Option(x + 1))
        # .filter(lambda x: x == 1)
        .get_or_else(0)
    )

    # Some more function examples using, filter, foldleft,  map etc.

    #  all functions can take a named method like def is_even or a lambda function

    mixed_list = [1, "a", 2, "b", 3, "c", 4, "d", 5, "e", 6, "f", 7, "g", 8, "h", 9, "i", 10]

    # filter only ints
    only_int_list = (
        PyfunList(mixed_list)
        .filter(lambda x: isinstance(x, int))
    )

    print(only_int_list.to_list())

    # filter only strings
    only_strings_list = (
        PyfunList(mixed_list)
        .filter(lambda x: not isinstance(x, int))
    )

    print(only_strings_list.to_list())
    print(only_strings_list.fold_left("")(lambda x, y: x + y))

    # foldleft is like a iterator operation where it applies the function x + y to all elements in the list.
    sum_all_ints_in_list = only_int_list.fold_left(0)(lambda x, y: x + y)  # in this case it sums all numbers total = 55

    print(sum_all_ints_in_list)


    def is_even(x) -> bool:
        return x % 2 == 0


    #  .filter(bool)   filters the list based on the boolean condition
    only_even_numbers_please = only_int_list.filter(is_even)
    print(only_even_numbers_please.to_list())

    #  .map()   applies a tranformation of some kind
    multiply_even_numbers_by_two = only_even_numbers_please.map(lambda x: x * 2)

    print(multiply_even_numbers_by_two.to_list())

    # ------------------------------------------------------------

    # # Example usage:
    # nums = [2, 7, 11, 15]
    # target = 9
    # print(two_sum(nums, target))  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
    #
    # # Example usage with a larger list:
    # nums_large = [1, 9, 3, 7, 5, 11, 2, 8, 6, 4]
    # target_large = 15
    # print(f"nums_large: {nums_large}")
    # print(f"target_large: {target_large}")
    # print(f"Indices of the two numbers that sum up to {target_large}: {two_sum(nums_large, target_large)}")
