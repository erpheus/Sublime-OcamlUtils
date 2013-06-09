import sublime, sublime_plugin
import re

class OcamlTypesParser():
	def search(self,filename,offset):
		try:
			f = open(filename.rsplit( ".", 1 )[ 0 ]+".annot")
		except IOError:
			return "Couldn't open .annot file. Remember compiling with -annot"
		lineM = re.compile('^\\\"[^\\\"]*\\\"\s\d+\s\d+\s(\d+)\s\\\"[^\\\"]*\\\"\s\d+\s\d+\s(\d+)$');
		endM = re.compile('^\\)$')
		typeDescr = "Not found"
		line = f.readline()
		while line:
			result = re.match(lineM,line)
			if result == None:
				line = f.readline()
				continue
			elif int(result.group(1)) > offset:
				break
			elif int(result.group(2)) < offset:
				line = f.readline()
				continue
			line = f.readline() # type line
			typeDescr = "";

			line = f.readline()
			while (line):
				if re.match(endM,line):
					break
				typeDescr += line
				line = f.readline()
			break

		f.close()
		print typeDescr
		return typeDescr

class OcamlTypesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		pos = self.view.sel()[0].begin()		

		parser = OcamlTypesParser()
		result = parser.search(self.view.file_name(),pos)

		self.view.set_status("ocaml-types","Type: " + result)


