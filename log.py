#    DamienOS -- Shitty operating system (File:shared.py)
#    Copyright (C) 2023  Damien Boisvert (AlphaGameDeveloper)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import termcolor
import os
import json
import sys
#import system

global _info
global _error
global _warn
global _fatal
global _exec
global __time
global logger
_info, _error, _warn, _fatal, _exec, __time = 0, 0, 0, 0, 0, 0

class CommandLogger:
	def __init__(self, useconfig=True, broadcastInit=False):
		if useconfig == True:
			try:
				with open("/data/.config/colorconf.json", "r") as f:
					self.colorconf = json.load(f)
			except Exception as e:
				print("CANNOT USE CONFIG; I DONT WANNA DIE PLEASE DONT HURT ME WAAHHH!")
				self.colorconf = None
				self.useConfig = False
		else:
			self.colorconf = None
		self.useConfig = useconfig
		self.cstep, self.sstep = "No Step", "Undefined"
#circimport-->		self.write = system.data.get("main/debug/danger-zone")
		self.info("Logger has finished initalizing!")

	def info(self, text, noct=False):
		print("[{0}]  {1}".format(termcolor.colored("INFO", (
		"green" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["info"])), text))
		if not noct:
			global _info
			_info += 1

	def exec(self, text):
		print("[{0}]  {1}".format(termcolor.colored("EXEC", (
		"magenta" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["exec"])), text))
		global _exec
		_exec += 1

	def time(self, text):
		print("[{0}]  {1}".format(termcolor.colored("TIME", (
		"cyan" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["time"])), text))
		global __time
		__time += 1

	def error(self, text):
		print("[{0}]  {1}".format(termcolor.colored("ERR!", (
		"red" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["error"])), text))
		global _error
		_error += 1

	def warn(self, text):
		print("[{0}]  {1}".format(termcolor.colored("WARN", (
		"yellow" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["warn"])), text))
		global _warn
		_warn += 1

	def fatal(self, text):
		print("[{0}]  {1}".format(termcolor.colored("FATL", (
		"yellow" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["fatal"]), "on_red"), text))
		global _fatal
		_fatal += 1

	def step(self, step):
		self.cstep = step
		print("[{0}]  Reached target <{1}>".format(termcolor.colored("STEP", (
		"cyan" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["step"])), self.cstep))
  
	def substep(self, step):
		global sstep
		self.sstep = step
		print("[{0}]  Reached subtarget <{1}/{2}>".format(termcolor.colored("STEP", (
		"cyan" if self.useConfig == False or self.colorconf == None else self.colorconf["logs"]["step"])), self.cstep, self.sstep))

# create default (shared) CommandLogger instance.
# commands may create a new instance by doing
# type(shared.logger) or type(shared.log.logger)
# Logger (should) be accessed via shared lib
# not direct, to prevent ImportError.
logger = CommandLogger()
