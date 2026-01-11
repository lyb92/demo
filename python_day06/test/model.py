def outer(func):
    def inner(a1,a2):
        print ("==== start =====")
        r = func(a1,a2)
        print ("==== end ====")
        return r
    return inner

@outer
def faa(a1,a2):
    print ("普通函数中的功能")

