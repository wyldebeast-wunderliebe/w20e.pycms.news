# -*- coding: utf-8 -*-
from w20e.pycms.models.base import BaseContent


class News(BaseContent):

    add_form = edit_form = "../forms/news.xml"

    @property    
    def base_id(self):

        return self.__data__['title']


    @property
    def title(self):

        return self.__data__['title']


    @property
    def text(self):

        return self.__data__['text']
