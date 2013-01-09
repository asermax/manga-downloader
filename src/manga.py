# -*- Mode: python; coding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-
#
# Copyright (C) 2012 - Agustin Carrasco
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

class Page(object):

    def __init__(self, number, path_chunk=None, extension=None):
        self.number = number
        self.path_chunk = path_chunk if path_chunk else str(number)
        self.extension = extension if extension else 'jpg'

class Chapter(object):

    def __init__(self, number, path_chunk=None):
        self.number = number
        self.path_chunk = path_chunk if path_chunk else ('c%d' % number)
        self._pages = []

    @property
    def pages(self):
        self._pages.sort(key=lambda page: page.number)

        return self._pages

    def page_count(self):
        return len(self._pages)

    def add_page(self, number=None, page_path=None, extension=None):
        if not number:
            number = max([page.number for page in self._pages])

        page = Page(number, page_path, extension)
        self._pages.append(page)

        return page

class Volume(object):

    def __init__(self, number, path_chunk=None):
        self.path_chunk = path_chunk if path_chunk else ('v%d' % number)
        self.number = number
        self._chapters = []

    @property
    def chapters(self):
        self._chapters.sort(key=lambda chapter: chapter.number)

        return self._chapters

    def chapter_count(self):
        return len(self._chapters)

    def add_chapter(self, number=None, chapter_path=None):
        if not number:
            number = max([chapter.number for chapter in self._chapters])

        chapter = Chapter(number, chapter_path)
        self._chapters.append(chapter)

        return chapter


class Manga(object):

    def __init__(self, name, base_path):
        self.path_chunk = base_path if base_path else ('./%s' % name)
        self.name = name
        self._volumes = []

    @property
    def volumes(self):
        self._chapters.sort(key=lambda volume: volume.number)

        return self._volumes

    def volume_count(self):
        return len(self._volumes)

    def add_volume(self, number=None, volume_path=None):
        if not number:
            number = max([volume.number for volume in self._volumes])

        volume = Volume(number, volume_path)
        self._volumes.append(volume)

        return volume

