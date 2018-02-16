# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'SteveRB'


class SimpleSkill(MycroftSkill):
    def __init__(self):
        super(SimpleSkill, self).__init__(name="SimpleSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        assistant_intent = IntentBuilder("AssistantIntent").require("AssistantKeyword").build()
        self.register_intent(assistant_intent, self.assistant_intent)

    def assistant_intent(self, message):
        self.speak_dialog("assistant")

    def stop(self):
        pass

def create_skill():
    return SimpleSkill()