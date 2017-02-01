#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests

KEY = 'trnsl.1.1.20170201T143054Z.986822ff91b4828f.2498d2a36251f10fb4eeb56f0318dfaed31756f3'

#функция определяет   направление перевода
def detect_lang(text):
    URl = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    # https://translate.yandex.net/api/v1.5/tr.json/detect ?
    # key=<API-ключ>
    #  & text=<текст>
    #  & [hint=<список вероятных языков текста>]
    #  & [callback=<имя callback-функции>]


    params = {
        'key': KEY,
        'text': text

    }
    response = requests.get(URl, params=params).json()
    return response['lang']


text1 = 'hi '

#функция переводит текст с определенного языка, который определился в вышеописаной функции

def translete_some_text(text,lingve):
    URl = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'

        #
        # https://translate.yandex.net/api/v1.5/tr.json/translate?
        # key=<API-ключ>
        #  & text=<переводимый текст>
        #  & lang=<направление перевода>
        #  & [format=<формат текста>]
        #  & [options=<опции перевода>]
        #  & [callback=<имя callback-функц

    params= {
        'key':KEY,
        'text':text,
        'lang': lingve,

    }
    response=requests.get(URl,params=params)
    data = (response.json())
    transled = data['text']
    transled = "".join(transled)
    return transled



# Функция для чтения заданного файла и сохранение его в заданную директорию

def file_manipulate(file_open,file_close):
    temp = []
    f=open(file_open,'r',encoding='utf-8')
    for line in f:
        temp.append(line)
    f.close()
    lingve = detect_lang(temp) + "-" + 'ru'
    text_for_save = translete_some_text(temp,lingve)



    f = open(file_close, 'w')
    for index in text_for_save:
        f.write(index )

    f.close()
    return text_for_save

# определяем названия и путь до файлов
# может быть сделать так. что бы переводил все файлы лежащие в заданной директории независимо от их количества и языка?

file_open_de=r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-2\Homework\DE.txt'
file_close_de = r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-2\Homework\DE_ru.txt'
file_open_es=r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-2\Homework\ES.txt'
file_close_es = r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-2\Homework\ES_ru.txt'
file_open_fr=r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-2\Homework\FR.txt'
file_close_fr = r'c:\Users\roman\Documents\GitHub\артем черняков\Lesson_3-2\Homework\FR_ru.txt'

file_manipulate(file_open_de,file_close_de)
file_manipulate(file_open_es,file_close_es)
file_manipulate(file_open_fr,file_close_fr)
