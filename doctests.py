def bounded_avg(nums):
    """Return avg of nums (making sure nums are 1-100)
    
    >>> bounded_avg([2,4,6])
    4.0

    """

    for n in nums:
        if n < 1 or n >100:
            raise ValueError("Outside of bounds 1-100")

    return sum(nums) / len(nums)
