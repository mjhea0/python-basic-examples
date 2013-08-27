#coding:utf-8

albums = ('A', 'B', 'C', 'D')
years = (1976, 1987, 1990, 2003)

for album in sorted(albums):
     print album,

for album in reversed(albums):
     print album,

for i, album in enumerate(albums):
     print i, album

for album, yr in zip(albums, years):
     print yr, album
