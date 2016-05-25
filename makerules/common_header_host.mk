#
# Common header host makefile.
#

ifndef $(COMMON_HEADER_MK)
COMMON_HEADER_MK = 1

CC1=$(MD2HTML_TOOL)
CC2=$(KINDLE_CONFIG)
LD =$(KINDLEGEN_TOOL)

OUT_BASE_DIR=$(shell pwd)

CC_OPTS=
LD_OPTS=-verbose

FILES=$(wildcard *.md)

XMLFILE=$(wildcard *.xml)
OPFFILE=*.opf

endif #	ifndef $(COMMON_HEADER_MK)
