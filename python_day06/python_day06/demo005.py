def foo():
    print("in foo")

    def bar():
        print("in bar")
    bar()

foo()
