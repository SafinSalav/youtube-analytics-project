class NonexistentID(Exception):
    """
    Класс исключения при передаче несуществующего id.
    """
    def __init__(self, *args, **kwargs):
        """
        Вызывается при создании объекта ошибки NonexistentID.
        Принимает любые позиционные аргументы *args и
        любые именованные аргументы **kwargs.
        """
        self.message = args[0] if args else 'Такой id не существует.'

    def __str__(self):
        """
        Возвращает сообщение ошибки при ее срабатывании.
        """
        return self.message
