'''
Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
Подготовка:
Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.
Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, предварительно закомментировав другой.

Пример результата выполнения программы:
Выполняемый код:
def read_info(name):
...
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

# Многопроцессный

Вывод на консоль, 2 запуска (результаты могут отличаться):
0:00:03.046163 (линейный)
0:00:01.092300 (многопроцессный)

Примечания:
Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
Выводить или возвращать список all_data в функции не нужно. Можете сделать это, но кол-во информации в файлах достигает - 10^9 строк.
Дополнительно о классе Pool можете прочитать здесь.
Файл module_10_5.py загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
Успехов!
'''
import time
import multiprocessing
from multiprocessing import Lock,Queue


lock = multiprocessing.Lock()

count=0
def read_info_q(name,q):
    global count
    with open(f'{name}','r',encoding='utf-8') as file:
        start_time1=time.time()
        while True:
            content = file.readline()
            if not content:
                break
        end_time1 = time.time()
        count += 1
        print(f'read_info_q запущен {count} раз')
        q.put(end_time1-start_time1)
        
lock.acquire()
def read_info(name):
    global count
    with open(f'{name}','r',encoding='utf-8') as file:
        start_time1=time.time()
        while True:
            content = file.readline()
            if not content:
                break
        end_time1 = time.time()
        count += 1
        print(f'read_info запущен {count} раз')
        return (end_time1-start_time1)

print(read_info('file 1.txt')+read_info('file 2.txt')+read_info('file 3.txt')+read_info('file 4.txt'), "секунд в линейном режиме")
lock.release()
if __name__ == '__main__':
    q = Queue()
    process1=multiprocessing.Process(target=read_info_q,args=('file 1.txt',q))
    process2=multiprocessing.Process(target=read_info_q,args=('file 2.txt',q))
    process3=multiprocessing.Process(target=read_info_q,args=('file 3.txt',q))
    process4=multiprocessing.Process(target=read_info_q,args=('file 4.txt',q))

    process1.start()
    process2.start()
    process3.start()
    process4.start()


    print(f"{q.get()+q.get()+q.get()+q.get()}, Секунд в многопроцессерном режиме")
    print(count)


