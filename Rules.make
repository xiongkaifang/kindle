#
#   Common softwares install directory.
#

ifeq ($(PROJECT_PATH), )

# Default build environment, windows or linux
ifeq ($(OS), )
  OS := linux
endif

PROJECT_RELPATH = kindle

ifeq ($(OS),Windows_NT)
  PROJECT_BASE     := $(CURDIR)/..
endif

ifeq ($(OS),linux)
  PROJECT_BASE     := $(shell pwd)/..
endif

PROJECT_PATH     := $(PROJECT_BASE)/$(PROJECT_RELPATH)

# Code gen tools
MD2HTML_NAME   := md2html.py
MD2HTML_TOOL   := $(PROJECT_PATH)/script/$(MD2HTML_NAME)
KINDLE_CONFIG  := $(PROJECT_PATH)/script/kindleconfig.py
MARKDOWN_TOOL  := $(PROJECT_PATH)/script/Markdown.pl
KINDLEGEN_NAME := kindlegen
KINDLEGEN_PATH := $(PROJECT_PATH)/bin
KINDLEGEN_TOOL := $(KINDLEGEN_PATH)/$(KINDLEGEN_NAME)
ifeq ($(OS),Windows_NT)
KINDLEGEN_NAME := kindlegen
KINDLEGEN_PATH := $(PROJECT_PATH)/bin
KINDLEGEN_TOOL := $(KINDLEGEN_PATH)/$(KINDLEGEN_NAME)
endif

# BIOS side tools

# Codecs

# Audio framework (RPE) and Codecs

# Linux side tools

ifeq ($(CORE), )
  CORE := host
endif

# Default platform
ifeq ($(PLATFORM), )
  PLATFORM := linux
endif

# Default profile
ifeq ($(PROFILE_m3video), )
  PROFILE_m3video := release
#  PROFILE_m3video := debug
endif

# Default configuration
ifeq ($(CONFIG), )
  CONFIG := debug
endif

endif

#
#   Export global environment variables.
#
export PROJECT_PATH
export MD2HTML_TOOL
export KINDLE_CONFIG
export MARKDOWN_TOOL
export KINDLEGEN_TOOL
