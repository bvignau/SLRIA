if 'entry' in ref:
	self.entry = str(ref['entry']).split("'")[1].lower()
else:
	self.entry ="unknow entry"
if 'title ' in ref:
	self.title  = str(ref['title ']).split("'")[1].lower()
else:
	self.title  ="unknow title "
if 'url ' in ref:
	self.url  = str(ref['url ']).split("'")[1].lower()
else:
	self.url  ="unknow url "
if 'author ' in ref:
	self.author  = str(ref['author ']).split("'")[1].lower()
else:
	self.author  ="unknow author "
if 'year ' in ref:
	self.year  = str(ref['year ']).split("'")[1].lower()
else:
	self.year  ="unknow year "
if 'booktitle' in ref:
	self.booktitle = str(ref['booktitle']).split("'")[1].lower()
else:
	self.booktitle ="unknow booktitle"
if 'journal' in ref:
	self.journal = str(ref['journal']).split("'")[1].lower()
else:
	self.journal ="unknow journal"
if 'chapter' in ref:
	self.chapter = str(ref['chapter']).split("'")[1].lower()
else:
	self.chapter ="unknow chapter"
if 'editor' in ref:
	self.editor = str(ref['editor']).split("'")[1].lower()
else:
	self.editor ="unknow editor"
if 'howpublished' in ref:
	self.howpublished = str(ref['howpublished']).split("'")[1].lower()
else:
	self.howpublished ="unknow howpublished"
if 'institution' in ref:
	self.institution = str(ref['institution']).split("'")[1].lower()
else:
	self.institution ="unknow institution"
if 'month' in ref:
	self.month = str(ref['month']).split("'")[1].lower()
else:
	self.month ="unknow month"
if 'number' in ref:
	self.number = str(ref['number']).split("'")[1].lower()
else:
	self.number ="unknow number"
if 'organization' in ref:
	self.organization = str(ref['organization']).split("'")[1].lower()
else:
	self.organization ="unknow organization"
if 'pages' in ref:
	self.pages = str(ref['pages']).split("'")[1].lower()
else:
	self.pages ="unknow pages"
if 'publisher' in ref:
	self.publisher = str(ref['publisher']).split("'")[1].lower()
else:
	self.publisher ="unknow publisher"
if 'volume' in ref:
	self.volume = str(ref['volume']).split("'")[1].lower()
else:
	self.volume ="unknow volume"
