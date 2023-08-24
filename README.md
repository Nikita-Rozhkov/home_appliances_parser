# Парсер для сохранения с сайта производителя бытовой техники информации о продукте
## Описание
Довольно часто возникают задачи, когда нужно собрать много информации с веб-страниц в Интернете и сохранить её на компьютере в определённом формате.
Делать это вручную очень долго и не удобно. Поэтому для решения этой задачи используются специальные **скрипты-парсеры**, которые собирают необходимую информацию с веб-страницы
и сохраняют её на жёстком диске или облачном хранилище в удобном для чтения и обработки формате. 

В данном репозитории содержится парсер *(см. рисунки ниже)*, который собирает информацию о **бытовой технике с сайта производителя**. Он позволяет сохранить изображения продукта в формате **JPEG**, спецификацию и описание продукта в виде **электронной таблицы Excel**. Данное решение может быть полезно для людей и компаний, занимающихся подготовкой контента для описания товаров в Интернет-магазинах.

*По данной ссылке можно ознакомиться с примерами использования парсера:* https://colab.research.google.com/drive/1BO_yd30WXEH2Nk_L3J6_BlrCMxcfYxuw?usp=sharing
![Парсинг изображений продукта](https://github.com/Nikita-Rozhkov/white_goods_parser/blob/main/images/parse_image_1.jpg?raw=true)
![Парсинг текстовой информации](https://github.com/Nikita-Rozhkov/white_goods_parser/blob/main/images/parse_image_2.jpg?raw=true)
## Состав репозитория
- `parse_pipelines.py` - содержит класс `ParseWG`, который используется для запуска и работы парсера
- `parsers.py` - содержит функции-парсеры для извлечения информации с сайтов определённых производителей. В данном случае поддерживаются следующие производители: *Haier, Delonghi, Candy, Hisense*
- `wg_parsing_examples.ipynb` - блокнот с примерами работы парсера
- `requirements.txt` - содержит сведения о версиях библиотек, которые используются для запуска парсера
- `images` - папка с изображениями, которые используются в данном `README.md`
- `results` - папка с результатами работы парсера, содержит примеры изображений и Excel-таблиц для нескольких продуктов
## Используемые технологии
- язык программирования: `Python 3.11`
- python-библиотеки: `requests`; `BeautifulSoup` и `lxml`; `pandas` и `openpyxl`
## Запуск и использование парсера
**Внимание!** Для запуска парсера должны быть установлены все библиотеки, указанные в файле `requirments.txt`.


Для начала работы необходимо импортировать: `parsers.py` и `parse_pipelines.py`
```
import parse_pipelines
import parsers
```
Для запуска парсера необходимо задать следующие параметры:
- **адрес веб-страницы**[`url : str`]
- **http заголовки** [`headers : dict`]
- **путь для сохранения полученной с веб-страницы информации** [`output_path : str`]
- **функция-парсер** [`parser : function`]
- **номер/модель продукта** [`part_number : str`]<br>


**Примечания:**
- *http заголовки необходимы для корректной загрузки веб-страницы с сервера. Берём стандартные заголовки, которые используются в браузере: `{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}`*
- *`output_path` можно задавать в абсолютном или относительном формате. Если указанного пути не сущетсвует, то он будет создан автоматически. По этому пути будут сохранены описание и спецификация продукта в формате Excel, также будут сохранены фотографии продукта в формате JPEG*
- *функция-парсер извлекает с веб-страницы информацию о продукте с учётом её разметки. Для сайта каждого производителя существует отдельная функция-парсер. В данном случае имеются функции-парсеры для следующих производителей бытовой техники: `Haier, Delonghi, Hisense, Candy`. Эта функция содержится в `parsers.py`*
- *`part_number` используется для формирования имён файлов с полученной информацией о продукте (Excel-таблицы, изображения)*

Для примера будет получена информация для кофемашины **Delonghi EPAM960.75.GLM**. 

Параметры для запуска скрипта: <br>
```
url = 'https://www.delonghi.com/en-gb/epam960-75-glm-maestosa-automatic-coffee-maker/p/EPAM960.75.GLM'        # адрес веб-страницы
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}    # заголовки
output_path = 'results/EPAM96075GLM'                                                                          # путь, по которому будут сохранены данные
parser = parsers.delonghi                                                                                             # функция-парсер для извлечения информации
part_number = 'EPAM96075GLM'                                                                                  # номер или модель продукта
```
Запуск скрипта осуществляется с помощью класса `ParseWG`, в который передаются указанные выше параметры.
```
delonghi_coffee = parse_pipelines.ParseWG(url, headers, output_path, parser, part_number)
delonghi_coffee.run()
```
Парсер работает в консоли. На рисунке можно видеть вид экрана при работе парсера.
![Процесс парсинга веб-страницы](https://github.com/Nikita-Rozhkov/white_goods_parser/blob/main/images/parse_image_2.jpg?raw=true)


