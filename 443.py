"""443 - Medium

This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of
1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001).

"""

from math import log2
import sys
from typing import Iterator


NBIT_MAX = 64


def main(integer: int) -> int:
    """Compute the next biggest integer with the same number of 1-bits on.

    Parameters
    ----------
    integer : int
        Integer used as reference.

    Returns
    -------
    int
        Next biggest integer with same number of 1-bits. 0 if no solution
        found.

    """
    if not 0 < integer < 2 ** NBIT_MAX:
        return 0

    ref = count_one_bits(integer)
    print(f"{integer} = 0b{integer:0b} :: {ref} one-bits")

    guess = integer
    for i in range(1, 2 ** NBIT_MAX):
        guess += 1
        onebits = count_one_bits(guess)
        if onebits == ref:
            break

    if guess == 2 ** NBIT_MAX:
        print(f"No solution found in {NBIT_MAX} bit integer.")
        return 0

    # Fetch all bits
    bits = "".join(str(b) for b in iter_bits(guess))
    # Compute the required padding for a fancier display
    padding = int(log2(guess)) + 1
    # Compute the bits in little-endian with padding
    bits = bits[:padding][::-1]
    print(f"-> {guess} = 0b{bits} :: {onebits} one-bits\n")

    return guess


def count_one_bits(integer: int) -> int:
    """Count the number of 1-bits in in integer.

    Parameters
    ----------
    integer : int
        Integer used as reference.

    """
    return sum(iter_bits(integer))


def iter_bits(integer: int) -> Iterator[int]:
    """Yield bit of an integer starting at LSB.

    Parameters
    ----------
    integer : int
        Integer used as reference.

    Yields
    ------
    int
        Value of the bit number `x`.

    """
    for x in range(NBIT_MAX):
        yield integer >> x & 0x1


def test_challenge() -> None:
    """Test expected values."""
    assert main(0) == 0
    assert main(1) == 2
    assert main(6) == 9
    assert main(2 ** 4) == 2 ** 5
    assert main(2 ** 8) == 2 ** 9
    assert main(10922) == 10924
    assert main(2 ** NBIT_MAX) == 0


if __name__ == "__main__":

    # Terrible args management but hey... This is scripting
    if len(sys.argv) == 2:

        if sys.argv[1] == "test":
            test_challenge()
            exit(0)

        number = int(sys.argv[1])
    else:
        number = 6

    main(number)
