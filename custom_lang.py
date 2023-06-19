  #  =====================================================================================================
  # 	 ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #   ／|、         ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  # （ﾟ､ ｡ つ               ﾞ☆ﾞ             ﾞ☆ﾞ               ﾞ☆ﾞ            ﾞ☆ﾞ              ﾞ☆ﾞ              ﾞ☆ﾞ
  #  |、ﾞ  ヽ        ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #  じーし__ )つ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ            ﾞ☆ﾞ
  #  =====================================================================================================
  #  МЕТОДЫ ПРОГРАММИРОВАНИЯ | LAB 1 10.06.2023 | ВАРИАНТ 12
  #  by crytech7
  #  =====================================================================================================
  #  > ВАРИАНТ 12:
  # 	Используя паттерн Command (команда) разработать тестовый язык (например, типа shell), 
  #	поддерживающий несколько видов команд с возможностью их отмены (undo) и повторения (redo). 
  #  =====================================================================================================

from sys import stdout

HISTO = list()
TRASH = list()

class Terminator(Exception):
	def __init__(self, value):
		self.value = value


class Command:
	def execute(self):
		raise NotImplementedError()

	def cancel(self):
		raise NotImplementedError()		

	def name():
		raise NotImplementedError()


class CMD_history(Command):
	def execute(self):
		i = 0
		for cmd in HISTO:
			stdout.write("{0}: {1}\n".format(i, cmd.name()))
			i = i + 1
	def name(self):
		print("history")


class CMD_exit(Command):
	def execute(self):
		raise Terminator("[INFO]: SEE YOU\n")

	def name(self):
		return "exit"


class CMD_uptime(Command):
	def execute(self):
		stdout.write("[ INFO ]: \"purr\" command\n")

	def cancel(self):
		stdout.write("[ INFO ]: canceled \"purr\" command\n")
	
	def name(self):
		return "uptime"


class CMD_undo(Command):
	def execute(self):
		try:
			cmd = HISTO.pop()
			TRASH.append(cmd)
			stdout.write("[ INFO ]: Undo command \"{0}\"\n".format(cmd.name()))
			cmd.cancel()
			
		except IndexError:
			stdout.write("[ ERROR ]: < history is empty >\n")
	
	def name(self):
		return "undo"

# Команда redo
class CMD_redo(Command):
	def execute(self):
		try:
			cmd = TRASH.pop()
			HISTO.append(cmd)
			stdout.write("[ INFO ]: Redo command \"{0}\"\n".format(cmd.name()))
			cmd.execute()

		except IndexError:
			stdout.write("[ ERROR ]: < trash is empty >\n")
	def name(self):
		return "redo"



COMDS = {'mew': CMD_history(), 'hiss': CMD_exit(), 'purr': CMD_uptime(), 'redo': CMD_redo(), 'undo': CMD_undo()}   


def main():

	try:
		while True:
			stdout.flush()
			stdout.write("custom_lang <3 ")
			
			cmd = input()
			
			try:

				command = COMDS[cmd]
				command.execute() 

				if not isinstance(command, CMD_undo) and not isinstance(command, CMD_redo) and not isinstance(command, CMD_history):
					TRASH = list()
					HISTO.append(command)
				
			except KeyError:
				stdout.write("[ ERROR ]: < Command \"%s\" not found >\n" % cmd)

	except Terminator as e:
		stdout.write(e.value)		
	

if __name__ == "__main__": main()
