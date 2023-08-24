def haier(content, mode):
    """
        Возвращает спецификацию, описание и ссылки на изображения для продуктов производителя Haier

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы
                        mode (str) : режим {spec, descr, images}
                                 spec : спецификация продукта
                                 descr : описание продукта
                                 images : ссылки на изображение продукта


                Возвращаемое значение:
                        spec : dict
                        descr : list
                        images : list
    """

    if mode == 'spec':
        spec = {'Parameter': [item.text for item in content.find_all('div', 'col-md-8 font-light')],
          'Value': [item.text for item in content.find_all('div', 'col-md-4 font-regular')]}
        return spec

    if mode == 'descr':
        descr = [item.text for item in content.find_all('div', 'items-grid__item-subtitle--pdp')]
        return descr

    if mode == 'images':
        images = [item['src'] for item in content.find_all('img', 'slider-img-prod__img')]
        return images


def delonghi(content, mode):
    """
        Возвращает спецификацию, описание и ссылки на изображения для продуктов производителя Delonghi

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы
                        mode (str) : режим {spec, descr, images}
                                 spec : спецификация продукта
                                 descr : описание продукта
                                 images : ссылки на изображение продукта


                Возвращаемое значение:
                        spec : dict
                        descr : list
                        images : list
    """

    if mode == 'spec':
        spec = {'Parameter': [item.text for item in content.find_all('span', 'del-pdp__specifications__single__label')],
          'Value': [item.text.strip() for item in content.find_all('span', 'del-pdp__specifications__single__value')]}
        return spec

    if mode == 'descr':
        descr = [item.text for item in content.find_all('div', 'del-keyfeaturetile__description')]
        return descr

    if mode == 'images':
        images = [item['src'] for item in (content.find_all('section', 'swiper-wrapper')[1]).find_all('img')]
        return images


def candy(content, mode):
    """
        Возвращает спецификацию, описание и ссылки на изображения для продуктов производителя Candy

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы
                        mode (str) : режим {spec, descr, images}
                                 spec : спецификация продукта
                                 descr : описание продукта
                                 images : ссылки на изображение продукта


                Возвращаемое значение:
                        spec : dict
                        descr : list
                        images : list
    """

    if mode == 'spec':
        spec = {'Parameter': [item.text for item in content.find_all('dt', 'accordion-description-list__title')],
          'Value': [item.text for item in content.find_all('dd', 'accordion-description-list__description')]}
        return spec

    if mode == 'descr':
        descr = [item.find('p').text for item in content.find_all('div', 'triplet-content__description')]
        return descr

    if mode == 'images':
        images = [item.find('img')['src'] for item in content.find_all('div', 'pdp-main-info__img')]
        return images



def hisense(content, mode):
    """
        Возвращает спецификацию, описание и ссылки на изображения для продуктов производителя Hisense

                Параметры:
                        content (BeautifulSoup object) : содержимое веб-страницы
                        mode (str) : режим {spec, descr, images}
                                 spec : спецификация продукта
                                 descr : описание продукта
                                 images : ссылки на изображение продукта


                Возвращаемое значение:
                        spec : dict
                        descr : list
                        images : list
    """

    if mode == 'spec':
        spec = {'Parameter': [], 'Value': []}
        for item in content.find_all('div', 'group group-wrap'):
            item_list = item.find_all('li')
            for idx in range(len(item_list)):
                if idx % 2 == 0:
                    spec['Parameter'].append(item_list[idx].text.strip())
                else:
                    spec['Value'].append(item_list[idx].text)
        return spec

    if mode == 'descr':
        descr = [item.text.strip() for item in content.find_all('div', 'supporting fadeInUp')]
        return descr

    if mode == 'images':
        images = [item['src'] for item in content.find_all('img', 'attachment-half-split size-half-split')]
        return images