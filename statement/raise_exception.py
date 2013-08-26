#coding:utf-8

import exceptions, sys

class ConfigError(exceptions.Exception):
    def __init__(self, arg=None):
        self.args = arg

raise ConfigError, "Invalid header."
