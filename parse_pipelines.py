import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep

class ParseHA:
    """
    Класс ParseHA предназначен для парсинга веб-страниц с бытовой техникой.
    Он позволяет загрузить спецификацию и описание продукта с веб-страницы и сохранить их в формате электронной таблицы Excel.
    Также есть возможность загрузить все изображения продукта с веб-страницы.

    Атрибуты
    -------------
    url : str
        адрес веб-страницы, откуда будет загружаться информация

    headers : dict
        http заголовки

    output_path: str
        абсолютный или относительный путь, по которому будут сохранены спецификация, описание и изображения

    parser : function
        функция, для парсинга информации с конкретной веб-страницы.


    part_number : str
        номер или модель продукта, для которого будет собираться информация

    Методы
    ------------
    run()
    Запускает процесс сбора и сохранения информации с веб-страницы

    Примечание:
    Если пути, указанного в output_path не существует, то он будет создан автоматически
    Атрибут parser представляет собой функцию, которая предназначена для извлечения информации с конкретного сайта с учётом особенностей его разметки.
    Для сайта конкретного производителя эта функция создаётся отдельно.
    Атрибут part_number используется для формирования имён Excel файлов и изображений.

    """

    def __init__(self, url, headers, output_path, parser, part_number):
        self.url = url
        self.headers = headers
        self.output_path = output_path
        self.parser = parser
        self.part_number = part_number
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def _get_content(self):
        """
        Метод для загрузки веб-страницы, с которой будет извлекаться информация

            Возвращаемое значение:
                            объект Beautiful Soup
        """

        print(f'Текущий адрес веб-страницы: {self.url}')
        request = requests.get(self.url, self.headers)

        if request.ok:
            print(f'Код запроса: {request.status_code} - успешно')
            content = BeautifulSoup(request.text, 'lxml')
            print('Содержимое веб-страницы успешно получено')
            return content

        else:
            print(f'Код запроса: {request.status_code} - неудача')
            print('Содержимое веб-страницы НЕ получено')

    def _get_spec(self, content):
        """
        Возвращает спецификацию продукта в виде словаря

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы

                Возвращаемое значение:
                        spec : dict
        """
        spec = self.parser(content, 'spec')
        return spec

    def _save_spec(self, spec):
        """
        Сохраняет спецификацию продукта в виде файла в формате Excel

                Параметры:
                        spec (dict) : спецификация

                Выходной файл:
                        part_number_spec.xlsx
        """

        if [] not in spec.values():

            number = len(spec['Value'])
            print(f'\nПолучено {number} значений')
            file_name = self.part_number + '_spec'
            file_path = os.path.join(self.output_path, f'{file_name}.xlsx')

            spec_df = pd.DataFrame(spec)
            spec_df.to_excel(file_path, index=False)

            print(f'Спецификация сохранена в {os.path.join(os.getcwd(), self.output_path)}')
            print(f'Полный путь к файлу спецификации: {os.path.join(os.getcwd(), file_path)}')

        else:
            print('Сохранить нечего. Значений нет')


    def _get_descr(self, content):
        """
        Возвращает описание продукта в виде списка

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы

                Возвращаемое значение:
                        descr : list
        """
        descr = self.parser(content, 'descr')
        return descr

    def _save_descr(self, descr):
        """
        Сохраняет описание продукта в виде файла в формате Excel

                Параметры:
                        descr (list) : описание

                Выходной файл:
                        part_number_descr.xlsx
        """

        if descr != []:

            number = len(descr)
            print(f'\nПолучено {number} значений')
            file_name = self.part_number + '_descr'
            file_path = os.path.join(self.output_path, f'{file_name}.xlsx')

            descr_df = pd.DataFrame(descr)
            descr_df.to_excel(file_path, index=False)

            print(f'Описание сохранено в {os.path.join(os.getcwd(), self.output_path)}')
            print(f'Полный путь к файлу описания: {os.path.join(os.getcwd(), file_path)}')
        else:
            print('Сохранить нечего. Значений нет')

    def _get_images(self, content):
        """
        Возвращает ссылки на изображения продукта

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы

                Возвращаемое значение:
                        images : list
        """
        images = self.parser(content, 'images')
        return images

    def _save_images(self, images):
        """
        Сохраняет изображения продукта в формате JPEG

                Параметры:
                        images (list) : ссылки на изображения

                Выходные файлы:
                        part_number_num.jpg
        """

        if images != []:
            print(f'\nНайдено {len(images)} изображений')
            num = 0
            images_path = os.path.join(self.output_path, 'images')

            if not os.path.exists(images_path):
                 os.makedirs(images_path)

            for image in images:
                num += 1
                print(f'\nИзображение {num} из {len(images)}: {image}')
                req = requests.get(image)

                if req.ok:
                    print(f'Изображение {num} загружено')
                    file_name = f'{self.part_number}_{num}.jpg'
                    print(f'Имя файла изображения {file_name}')
                    file_path = os.path.join(images_path, file_name)

                    with open(file_path, 'wb') as file:
                        file.write(req.content)
                    print(f'Изображение сохранено в {file_path}')
                    sleep(10)

                else:
                    print('Невозможно загрузить изображение')
        else:
            print('Изображения отсутствуют')


    def run(self):
        """
        Запускает процесс сбора и сохранения информации с веб-страницы

        """
        content = self._get_content()
        specification = self._get_spec(content)
        self._save_spec(specification)
        description = self._get_descr(content)
        self._save_descr(description)
        image_list = self._get_images(content)
        self._save_images(image_list)
