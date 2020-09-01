# ETTUParser
This project parses ETTU(Ekaterinburg Tram and Trolley Administration) site for mass transit schedule. 

Этот проект парсит сайт ЕТТУ(Екатеринбургское трамвайно-троллейбусное управление) на предмет времени до прибытия автобуса/трамвая на остановку.

*The documentation for this repository is written in Russian, cause a problem that this project solves is applicable only to Yekaterinburg.*

## Использование
Данный модуль зависит от `lxml` и `pandas`.

Единственной функцией данного модуля(на данный момент) является `ettuparser.parseStation(stationID)`. Параметр `stationID` можно взять из URL остановки, информацию о которой требуется получить. К примеру: ht<span>tps://</span>mobile.ettu.ru/station/***3431*** (насколько я понимаю для трамваев они четырехзначные, для троллейбусов-пятизначные). Возвращает данная функция `pandas.DataFrame`.
