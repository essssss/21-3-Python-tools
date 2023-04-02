# <center>PYTHON TOOLS AND TECHNIQUES</center>

## Packing and Unpacking:

-  **_Unpacking_** is a way of creating variables or extracting values from some sort of _iterable_

   ```python
   names = ["charlie", "lucy"]

   name1, name2 = names

   # name1 = 'charlie'
   # name2 = 'lucy'
   ```

-  we can gather rest using `*` before variable:

   ```py
   letters = ['a', 'b', 'c']

   first, *rest = letters
   ```

   ```py
   sorted_scores = [2400, 2350, 2100, 1960]

   top_score, *scores = sorted_scores

   # top_score = 2400
   # scores = [2350, 2100, 1960]
   ```

-  Unpacking with nested data:

   -  must use the tuple `()` parentheses in order to mimic the data.

   ```py
   color_pairs = [['red', 'green'], ['purple', 'orange']]

   pair1, pair2 = color_pairs

   # pair1 = ['red', 'green']
   # pair2 = ['purple', 'orange']

   ((primary1, secondary1), (primary2, secondary2)) = color_pairs

   # primary1 = 'red'
   # secondary1 = 'green'
   # primary2 = 'purple'
   # secondary2 = 'orange'
   ```

---

# Spread:

-  can `spread` iterables:

```py
nums = [2, 4, 6, 8]

[-2, 0, *nums]
# [-2, 0, 2, 4, 6, 8]

odds = [1, 3, 5, 7, 9]
[*odds, *nums]
# [1, 3, 5, 7, 9, 2, 4, 6, 8]
```

-  to spread into a dictionary use `**`

```py
rainfall = {'Jan': 2.5, 'Feb': 4.9}

# {*rainfall} will just make a set out of keys, not a dictionary

{'Dec': 0.5, **rainfall}

# this will 'spread' our rainfall dict into the new dictionary
```

---

# Error handling:

In general, Python raises errors in places where JS simply returns `undefined`

-  provide too few/too many arguments to a function
-  index a list beyond length of list
-  retrieve item from a dictionary that doesn't exist
-  use missing attribute on an instance
-  conversion failures (eg: converting "hello" to an int)
-  division by 0
-  many more!

Python is simply more explicit which means it requires more error handling!

---

## Catching Errors:

```py
# try to convert this to a number

try:
    age = int(data_we_received)
    print("You are ", age)

except:
    print("Hey, you, that's not an age!")

# The next line will be run either way...
```

-  We can try to anticipate every situation with conditionals: "if this is right and that is right, yadda yadda"
   -  Instead we do a `try` block and see if it works and if it doesn't we `except` it
   -  make sure we check for the right types of errors:

---

## Common Error Types

| ERROR CODE       | DESCRIPTION                                            |
| ---------------- | ------------------------------------------------------ |
| `AttributeError` | Couldn't find attr: `o.missing`                        |
| `KeyError`       | Couldn't find key: `d["missing"]`                      |
| `IndexError`     | Couldn't find index: `lst[9999]`                       |
| `NameError`      | Couldn't find variable: `not_speeled_right`            |
| `OSError`        | Operating system error: can't read/write file, etc     |
| `ValueError`     | Incorrect value (tried to convert "hello" to int, etc) |

So let's clarify our error handler:

```py
def get_days_alive(person):
    try:
        days = person['age'] * 365
        print(f"{person['name']} has been alive for {days} days")

    except KeyError as exc:
        print(f"Missing key: {exc}")

    except TypeError:
        print("Expected person to be a dict")
```

-  here we have defined our `KeyError` exception. The `exc` further clarifies which particular KeyError.

---

# Raising Errors

In python it is common to raise a specific error to signal problems:

```py
raise ValueError("Fix that value!")
```

---

EXAMPLE:

```py
def bounded_avg(nums):
    "Return avg of nums (making sure nums are 1-100)"

    for n in nums:
        if n < 1 or n >100:
            raise ValueError("Outside of bounds 1-100")

    return sum(nums) / len(nums)

def handle_data():
    "Process data from database"

    ages = get_ages(from_my_db)

    try:
        avg = bounded_avg(ages)
        print("Average was", avg)

    except ValueError as exc:
        # exc is exception object -- you can examine it!
        print("Invalid age in list of ages")
```

-  We can RAISE the error where it happens, and then we can HANDLE that error where it's useful to.

---

-  Docstrings & Doctests:
   -  docstrings support built-in tests!!

```py
def bounded_avg(nums):
    """Return avg of nums (makes sure nums are 1-100)

        >>> bounded_avg ([1, 2, 3])
        2

        >>> bounded_avg([1, 2, 101])
        Traceback (most recent call last):
            ...
        ValueEror: Outside bounds of 1-100
    """

    for n in nums:
        if N < 1 or n > 100:
            raise ValueError Outside bounds of 1-100"
        return sum(nums) / len(nums)
```

---

# WE RUN THE FOLLOWING IN THE COMMAND LINE (not ipython)

```
$ python3 -m doctest -v your-file.py
```

(use the **_doctest_** module, verbosely showing tests found and run)

To doctest an error, we copy the `Traceback` and then ... and then the error msg.

The doctests show up in a function's "help" menu

---

# Importing

Python includes a "standard library" of dozens of useful modules.  
These are not in the namespace of your script automatically.  
You have to _import_ them.

-  simply add `import math` or w/e your desired library is.
   -  call the function by typing the library name
-  OR just import only one or two particular functions from a module
   -  we don't have to call the library out in this case
   ```py
   from random import choice
   ```
   -  change the function name with `as` keyword
