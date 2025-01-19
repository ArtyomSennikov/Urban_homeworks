def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
# inner_function() # Вызов этой функции в глобальной области видимости приведёт к ошибке программы.