def htmlEndTagByStartTag(tag):
    return "</"+tag[1:tag.index(" " if " " in tag else ">")]+">"
    
startTag = "<button type='button' disabled>"
print(htmlEndTagByStartTag(startTag))
# = "</button>";

startTag = "<i>"
print(htmlEndTagByStartTag(startTag))
# = "</i>".
