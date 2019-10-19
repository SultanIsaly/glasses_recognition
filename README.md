## Быстрый запуск (из архива)

sudo . eyeglasses.sh  
cd (назад к папке с glasses recognition)  
python run.py --input='result_test'

## Полная установка (создание датасета, обучение, инференс)

### Установка зависимостей
sudo . eyeglasses.sh

### Датасет 
Можно скачать по [ссылке](https://drive.google.com/file/d/1V0c8p6MOlSFY5R-Hu9LxYZYLXd8B8j9q/view)

Разархивирование
unzip MeGlass_120x120.zip

### Присланные файлы поместить в папку 

Загрузить присланные фотографии в папку result_test(сразу сами файлы, без внутреннего разделения на glasses, not glasses)

### Запуск

prepare_data.py - подготовка датасета  
train_model.py - обучение модели  
run.py - инференс

'''
python prepare_data.py  
python train_model.py  
python run.py --input='result_test'
'''

### Замечания

1. Так как в выборках нет изображений очков не на лицу, то не обязательно детектить само лицо,
   достаточно только определить есть ли очки или нет. Ограничения на модель
   (вес, время инференса, точность - подробнее в ноутбуке) удается выполнить трансфером 
   (squeezenet1_1,обученная весит 2.9 МБ) на обрезанную выборку лиц с очками и без. 
   
   PS: В принципе при необходимости классифицировать сложные случаи, можно поподбирать сетки с
   [InsightFace Model Zoo](https://github.com/deepinsight/insightface/wiki/Model-Zoo) и что-нибудь 
   подобное [RetinaFace](https://github.com/deepinsight/insightface/tree/master/RetinaFace) для 
   обнаружения области лица.
   
2. Добавление динамического квантования из torch не уменьшило размер модели(смотрите ноутбук).
3. Инференс дополнительно можно ускорять добавлением параллельности(multiprocessing).
4. Итоговые значения метрик тестил в ноутбуке для присланной выборки Recall(unglasses) = 1, 
   Recall(glasses) = 0.9. 

### Основные зависимости
torch - 1.3.0  
numpy - 1.16.1
  torchvision - 0.4.1  
sklearn - 0.20.2  
argparse - 1.1  
pandas - 0.25.1



  
