#
# Common footer host makefile.
#

ifndef $(COMMON_FOOTER_MK)
COMMON_FOOTER_MK = 1

OBJS=$(subst .md,.html, $(FILES))

OUT=$(EBOOK).mobi

$(EBOOK): html mobi

%.html:%.md
	@echo \# $(EBOOK): Compiling $<
	$(CC1) $(MARKDOWN_TOOL) $<

html: $(OBJS)

opf:
	@echo \# $(EBOOK): Configuring $(XMLFILE) ...
	$(CC2) $(CC_OPTS) $(XMLFILE)

mobi: opf
	@echo \# $(EBOOK): Compiling $(OUT) ...
	$(LD) $(LD_OPTS) $(OPFFILE) -o $(EBOOK).mobi
	@echo \# $(EBOOK): Generated ebook: $(OUT) !!!
	@echo \#

clean:
	@echo \# $(EBOOK): Deleting temporary files ...
	-rm -f  $(OUT_BASE_DIR)/$(OUT)
	-rm -f  $(OUT_BASE_DIR)/*.opf
	-rm -f  $(OUT_BASE_DIR)/*.ncx
	-rm -f  $(OUT_BASE_DIR)/*.html

endif #	ifndef $(COMMON_FOOTER_MK)
