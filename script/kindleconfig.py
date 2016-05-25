#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
################################################################################
#
#
#  @File name  : kindleconfig.py
#
#  @Author     : xiong-kaifang   Version: v1.0   Date: 2016-05-23
#
#  @Description: The script to configuring kindle's ebook using xml file.
#
#
#  @History    : Review history
#
#	<author>	    <time>	     <version>	    <desc>
#  xiong-kaifang   2016-05-23     v1.0          Rewrite this script.
#
################################################################################

import os
import sys
import time
import traceback

import xml.dom.minidom
from   xml.dom.minidom import parse

xmlfile   = os.sys.argv[1]
dom       = xml.dom.minidom.parse(xmlfile)
node_name = dom.documentElement.nodeName;

def getText(nodelist):
    rc = [];
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data);
    return ''.join(rc);

################################################################################
#
# Generating opf file.
#
################################################################################
opfxml = xml.dom.minidom.Document();

package = opfxml.createElement("package");
package.setAttribute("xmlns", "http://www.idpf.org/2007/opf");
package.setAttribute("version", "2.0");
package.setAttribute("unique-identifier", "BookId");
opfxml.appendChild(package);

################################################################################
#
# Generating opf-metadata element.
#
################################################################################
in_metadata = dom.documentElement.getElementsByTagName("ebook_metadata")[0];

metadata = opfxml.createElement("metadata");
metadata.setAttribute("xmlns:dc", "http://purl.org/dc/elements/1.1/");
metadata.setAttribute("xmlns:opf=", "http://www.idpf.org/2007/opf");
package.appendChild(metadata);

# Title.
in_title    = in_metadata.getElementsByTagName("title")[0];

title = opfxml.createElement("dc:title");
title_text = opfxml.createTextNode(getText(in_title.childNodes));
title.appendChild(title_text);
metadata.appendChild(title);

# Language.
in_lan = in_metadata.getElementsByTagName("language")[0];

lan = opfxml.createElement("dc:language");
lan_text = opfxml.createTextNode(getText(in_lan.childNodes));
lan.appendChild(lan_text);
metadata.appendChild(lan);

# meta.
meta = opfxml.createElement("meta");
meta.setAttribute("name", "cover");
meta.setAttribute("content", "ebook_cover");
metadata.appendChild(meta);

# Identifier.
in_isbn = in_metadata.getElementsByTagName("identifier")[0];

iden = opfxml.createElement("dc:identifier");
iden.setAttribute("id", "BookId");
iden.setAttribute("opf:scheme", "ISBN");
iden_text = opfxml.createTextNode(getText(in_isbn.childNodes));
iden.appendChild(iden_text);
metadata.appendChild(iden);

# Author.
in_author = in_metadata.getElementsByTagName("author")[0];

author = opfxml.createElement("dc:creator");
author_text = opfxml.createTextNode(getText(in_author.childNodes));
author.appendChild(author_text);
metadata.appendChild(author);

# Publisher.
in_pub = in_metadata.getElementsByTagName("publisher")[0];

publisher = opfxml.createElement("dc:publisher");
publisher_text = opfxml.createTextNode(getText(in_pub.childNodes));
publisher.appendChild(publisher_text);
metadata.appendChild(publisher);

# Subject.
in_refer = in_metadata.getElementsByTagName("subject")[0];

refer = opfxml.createElement("dc:subject");
refer_text = opfxml.createTextNode(getText(in_refer.childNodes));
refer.appendChild(refer_text);
metadata.appendChild(refer);

# Date.
in_date = in_metadata.getElementsByTagName("date")[0];

date = opfxml.createElement("dc:date");
date_text = opfxml.createTextNode(getText(in_date.childNodes));
date.appendChild(date_text);
metadata.appendChild(date);

# Description.
in_desp = in_metadata.getElementsByTagName("description")[0];

desp = opfxml.createElement("dc:description");
desp_text = opfxml.createTextNode(getText(in_desp.childNodes));
desp.appendChild(desp_text);
metadata.appendChild(desp);

################################################################################
#
# Generating opf-manifest element.
#
################################################################################
in_manifest = dom.documentElement.getElementsByTagName("ebook_manifest")[0];

manifest = opfxml.createElement("manifest");

# Add all items.
elemlists = in_manifest.getElementsByTagName("item");
for elem in elemlists:
    id   = elem.getAttribute("id");
    type = elem.getAttribute("media-type");
    href = elem.getAttribute("href");

    item = opfxml.createElement("item");
    item.setAttribute("id", "{0}".format(id));
    item.setAttribute("media-type", "{0}".format(type));
    item.setAttribute("href", "{0}".format(href));
    manifest.appendChild(item);

package.appendChild(manifest);

################################################################################
#
# Generating opf-spine element.
#
################################################################################
in_spine = dom.documentElement.getElementsByTagName("ebook_spine")[0];

spine = opfxml.createElement("spine");
spine.setAttribute("toc", "{0}".format(in_spine.getAttribute("toc")));

# Add all itemrefs.
itemlists = in_spine.getElementsByTagName("itemref");
for item in itemlists:
    idref   = item.getAttribute("idref");
    itemref = opfxml.createElement("itemref");
    itemref.setAttribute("idref", "{0}".format(idref));
    spine.appendChild(itemref);

package.appendChild(spine);

################################################################################
#
# Generating opf-guide element.
#
################################################################################
in_guide = dom.documentElement.getElementsByTagName("ebook_guide")[0];

guide = opfxml.createElement("guide");

# Add all refereces.
itemlists = in_guide.getElementsByTagName("reference");
for item in itemlists:
    type  = item.getAttribute("type");
    title = item.getAttribute("title");
    href  = item.getAttribute("href");
    refer = opfxml.createElement("reference");
    refer.setAttribute("type" , "{0}".format(type));
    refer.setAttribute("title", "{0}".format(title));
    refer.setAttribute("href" , "{0}".format(href));
    guide.appendChild(item);

package.appendChild(guide);

opf_file = open(node_name + ".opf", "w");
opf_file.write(opfxml.toprettyxml(indent = "    ", newl="\n", encoding="utf-8"));
opf_file.close();

################################################################################
#
# Generating ncx file.
#
################################################################################
ncxxml = xml.dom.minidom.Document();

ncx = ncxxml.createElement("ncx");
ncx.setAttribute("xmlns", "http://www.daisy.org/z3986/2005/ncx/");
ncx.setAttribute("version", "2005-1");
ncx.setAttribute("xml:lang", "en-US");
ncxxml.appendChild(ncx);

# Add head.
head = ncxxml.createElement("head");
head.setAttribute("http-equiv", "Content-Type");
head.setAttribute("content", "text/xhtml+xml");
head.setAttribute("charset", "utf-8");

dtb_uid    = ncxxml.createElement("meta");
dtb_uid.setAttribute("name"   , "dtb:uid");
dtb_uid.setAttribute("content", "BookId");
head.appendChild(dtb_uid);

dtb_depth = ncxxml.createElement("meta");
dtb_depth.setAttribute("name"   , "dtb:depth");
dtb_depth.setAttribute("content", "2");
head.appendChild(dtb_depth);

dtb_page = ncxxml.createElement("meta");
dtb_page.setAttribute("name"   , "dtb:totalPageCount");
dtb_page.setAttribute("content", "0");
head.appendChild(dtb_page);

dtb_number = ncxxml.createElement("meta");
dtb_number.setAttribute("name"   , "dtb:maxPageNumber");
dtb_number.setAttribute("content", "0");
head.appendChild(dtb_number);

ncx.appendChild(head);

# Add title.
docTitle = ncxxml.createElement("docTitle");
text = ncxxml.createElement("text");
title_text = ncxxml.createTextNode(getText(in_title.childNodes));
text.appendChild(title_text);
docTitle.appendChild(text);
ncx.appendChild(docTitle);

# Add author.
docAuthor = ncxxml.createElement("docAuthor");
text = ncxxml.createElement("text");
title_text = ncxxml.createTextNode(getText(in_author.childNodes));
text.appendChild(title_text);
docAuthor.appendChild(text);
ncx.appendChild(docAuthor);

# Add all navmaps.
in_ncx = dom.documentElement.getElementsByTagName("ebook_ncx")[0];

navmap = ncxxml.createElement("navMap");

itemlists = in_ncx.getElementsByTagName("navPoint");

def navpHandle(id, cls, src, order, txt):

    # Create an new navPoint.
    navp = ncxxml.createElement("navPoint");
    navp.setAttribute("id", "{0}".format(id));
    navp.setAttribute("class", "{0}".format(cls));
    navp.setAttribute("playOrder", "{0}".format(order));

    # navLabel and text.
    navl = ncxxml.createElement("navLabel");
    navl_text_elem = ncxxml.createElement("text");
    navl_text_node = ncxxml.createTextNode(getText(text.childNodes));
    navl_text_elem.appendChild(navl_text_node);
    navl.appendChild(navl_text_elem);
    navp.appendChild(navl);

    # content.
    content = ncxxml.createElement("content");
    content.setAttribute("src", "{0}#{1}".format(src, id));
    navp.appendChild(content);

    return navp;

for item in itemlists:
    id    = item.getAttribute("id");
    cls   = item.getAttribute("class");
    src   = item.getAttribute("src");
    order = item.getAttribute("playOrder");

    text = item.getElementsByTagName("text")[0];

    # navPoint.
    navp1 = navpHandle(id, cls, src, order, text);

    # Add the navPoint to the navMap.
    navmap.appendChild(navp1);

    #
    # Process second navp if neccessary(up to two levels).
    #
    itemlists2 = item.getElementsByTagName("navPoint2");
    if (itemlists2.length > 0):
        for item2 in itemlists2:
            id    = item2.getAttribute("id");
            cls   = item2.getAttribute("class");
            src   = item2.getAttribute("src");
            order = item2.getAttribute("playOrder");

            text = item2.getElementsByTagName("text")[0];

            # navPoint.
            navp2 = navpHandle(id, cls, src, order, text);
            
            # Add the navPoint to the navMap.
            navp1.appendChild(navp2);
    
ncx.appendChild(navmap);

ncx_file = open(node_name + ".ncx", "w");
ncx_file.write(ncxxml.toprettyxml(indent = "    ", newl="\n", encoding="utf-8"));
ncx_file.close();

################################################################################
#
# Generating ebbook using KindleGen tools.
#
################################################################################
