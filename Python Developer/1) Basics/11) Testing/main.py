import pdb

if __name__ == '__main__':
    print('inside main')

def do_stuff(a):
    try:
        if a ==None:
            return TypeError
        return int(a) + 5
    except ValueError as err:
        return err

