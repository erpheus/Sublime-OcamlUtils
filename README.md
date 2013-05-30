Sublime-OcamlUtils
==================

Utilities to work with Ocaml in Sublime Text 2. Includes build and run system and type annotations viewer.

### Instalation ###

This plug-in can be installed through Sublime Package Control.

### Usage ###

**Build System:** On any .ml file, just press your usual shortcut for building (cmd+b or ctrl+b) to compile 
the file and see any compilation errors on the console. If you append shift to the build shotcut the file will
be built and run on console afterwards.

As with the C build system, this works for simple OCaml programs whith only one file.

**Type annotations:** On any OCaml proyect, if you have compiled your files with the -dtypes flag, whenever you press
alt + a, the type of the expresion beneath the caret will appear in the status bar.

If there was a compilation error types until the error will be displayed, which is useful for debugging.


