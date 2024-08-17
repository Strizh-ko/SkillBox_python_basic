from typing import Any, Optional


class NextLink:

    def __init__(self, obj: Optional[Any], next=None) -> None:
        self.obj = obj
        self.next = next

    def __str__(self) -> str:
        return f'Следующий элемент: {str(self.obj)}'


class LinkedList:

    def __init__(self) -> None:
        self.first_obj = None
        self.length = 0

    def __str__(self) -> str:
        if self.first_obj is None:
            return 'Нет элементов в списке'

        cur_obj = self.first_obj
        list_obj = [str(cur_obj.obj)]
        while cur_obj.next is not None:
            cur_obj = cur_obj.next
            list_obj.append(str(cur_obj.obj))
        return f'{list_obj}'

    def append(self, obj) -> None:
        link = NextLink(obj)
        self.length += 1

        if self.first_obj is None:
            self.first_obj = link
            return

        last = self.first_obj
        while last.next:
            last = last.next
        last.next = link

    def remove(self, i_obj) -> None:
        cur_i = 0
        cur_obj = self.first_obj

        if i_obj == 0:
            self.first_obj = cur_obj.next
            self.length -= 1
            return

        while cur_obj is not None:
            if i_obj == cur_i:
                break
            link = cur_obj
            cur_obj = cur_obj.next
            cur_i += 1
            link.next = cur_obj.next

    def get(self, i_obj) -> Optional[Any]:
        cur_i = 0
        cur_obj = self.first_obj
        while cur_i != i_obj:
            cur_obj = cur_obj.next
            cur_i += 1
        return cur_obj.obj

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))

print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)