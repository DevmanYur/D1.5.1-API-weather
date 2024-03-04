# Скрипт по выводу прогноза погоды

## Описание работы скрипта
Данный скрипт позволяет выводить в терминал прогноз погоды
в зависимости от заданных параметров


## Как установить
1. Python3 должен быть уже установлен. 
2. Используйте `pip` для установки зависимостей:

```
pip install -r requirements.txt
```

3. Запустите сайт из терминала командой:

```
python main.py
```

4. Чтобы изменить город, вызовите функцию с параметрами:

``` python
get_city_characteristics (city,ci,wind,version,language)
```

где:
- city - [поддерживаемые типы местоположений](https://github.com/DevmanYur/D1.5.1-API-weather?tab=readme-ov-file#%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D1%82%D0%B8%D0%BF%D1%8B-%D0%BC%D0%B5%D1%81%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9)
- ci - [единицы измерений](https://github.com/DevmanYur/D1.5.1-API-weather?tab=readme-ov-file#%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D1%8B-%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D0%B9)
- wind - [скорость ветра](https://github.com/DevmanYur/D1.5.1-API-weather?tab=readme-ov-file#%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C-%D0%B2%D0%B5%D1%82%D1%80%D0%B0)
- version - [опции отображения](https://github.com/DevmanYur/D1.5.1-API-weather?tab=readme-ov-file#%D0%BE%D0%BF%D1%86%D0%B8%D0%B8-%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
- language - [поддерживаемые языки](https://github.com/DevmanYur/D1.5.1-API-weather?tab=readme-ov-file#%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D1%8F%D0%B7%D1%8B%D0%BA%D0%B8)


5. Пример функции после подстановки:
``` python
get_city_characteristics("Череповец", "m", "M", "Tnq", "ru")
```
Где:

      city = "Череповец"
      ci = "m" - метрические (СИ) (используются везде кроме США)
      wind = "M" - показывать скорость ветра в м/с
      version = "Tnq"
         T - отключить терминальные последовательности (без цветов)
         n - узкая версия (только день и ночь)
         q - тихая версия (без текста "Прогноз погоды")
      language = "ru"  - русский язык



## Полное описание запросов
### Использование:

    $ curl wttr.in          # текущее местоположение
    $ curl wttr.in/svo      # погода в аэропорту Шереметьево (код ICAO: SVO)

### Поддерживаемые типы местоположений:

    /paris                  # город
    /~Eiffel+tower          # любое местоположение
    /Москва                 # юникодное имя любого местоположения на любом языке
    /muc                    # код аэропорта ICAO (3 буквы)
    /@stackoverflow.com     # доменное имя
    /94107                  # почтовый индекс (только для США)
    /-78.46,106.79          # GPS-координаты

### Специальные условные местоположения:

    /moon                   # Фаза Луны (добавьте ,+US или ,+France для города Moon в США/Франции)
    /moon@2016-10-25        # Фаза Луны для указанной даты (@2016-10-25)

### Единицы измерений:

    ?m                      # метрические (СИ) (используются везде кроме США)
    ?u                      # USCS (используются в США)

### Скорость ветра
    ?M                      # показывать скорость ветра в м/с

### Опции отображения:

    ?0                      # только текущая погода
    ?1                      # погода сегодня + 1 день
    ?2                      # погода сегодня + 2 дня
    ?n                      # узкая версия (только день и ночь)
    ?q                      # тихая версия (без текста "Прогноз погоды")
    ?Q                      # сверхтихая версия (без "Прогноз погоды", нет названия города)
    ?T                      # отключить терминальные последовательности (без цветов)

### PNG-опции:

    /paris.png              # сгенерировать PNG-файл
    ?p                      # добавить рамочку вокруг
    ?t                      # transparency=150 (прозрачность 150)
    transparency=...        # прозрачность от 0 до 255 (255 = не прозрачный)

### Опции можно комбинировать:

    /Paris?0pq
    /Paris?0pq&lang=fr
    /Paris_0pq.png          # в PNG-запросах опции указываются после _
    /Rome_0pq_lang=it.png   # длинные опции разделяются знаком подчёркивания _

### Локализация:

    $ curl fr.wttr.in/Paris
    $ curl wttr.in/paris?lang=fr
    $ curl -H "Accept-Language: fr" wttr.in/paris

### Поддерживаемые языки:

    am ar af be bn ca da de el et fr fa gl hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw (поддерживаются)
    az bg bs cy cs eo es eu fi ga hi hr hy is ja jv ka kk ko ky lv mk ml mr nl fy nn pt pt-br sk sl sr sr-lat sv sw te uz zh zu he (в процессе)

### Специальные страницы:

    /:help                  # показать эту страницу
    /:bash.function         # показать рекомендованную функцию wttr()
    /:translation           # показать список переводчиков wttr.in

