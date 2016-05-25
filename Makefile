#
#
#

# include global Rules.mak

#
# include local rules.make
#
include Rules.make

#################################################
#                                               #
# Kindle Ebooks System Top Level Build Targets  #
#                                               #
#################################################

.PHONY : clean

all: clean ebooks

EBOOKS=$(shell ls ebooks)

clean:
	@$(foreach book,$(EBOOKS),$(MAKE) -fMAKEFILE.MK -C$(PROJECT_PATH)/ebooks/$(book) EBOOK=$(book) clean;)

ebooks: dumy
	@$(foreach book,$(EBOOKS),$(MAKE) -fMAKEFILE.MK -C$(PROJECT_PATH)/ebooks/$(book) EBOOK=$(book);)
	@echo Finished to generate ebooks.

dumy:
	@echo Begin to generate ebooks ...
