def get_inverse(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return None
    finally:  # used when works with external resources like databases or text files
        print('I am always printed!')  # ‼ prints BEFORE (antes)



print(get_inverse(0))
# I am always printed! ‼
# 0.2