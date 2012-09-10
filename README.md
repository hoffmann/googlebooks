googlebooks
===========

[Google Books API][api] search access with Python.

[api]: https://developers.google.com/books/

```python
import googlebooks
api = googlebooks.Api()
api.list('isbn:0596007973')
```

Returns the following json response
```json
{u'items': [{u'accessInfo': {u'accessViewStatus': u'SAMPLE',
    u'country': u'DE',
    u'embeddable': True,
    u'epub': {u'isAvailable': True},
    u'pdf': {u'isAvailable': True},
    u'publicDomain': False,
    u'textToSpeechPermission': u'ALLOWED_FOR_ACCESSIBILITY',
    u'viewability': u'PARTIAL',
    u'webReaderLink': u'http://books.google.de/books/reader?id=1Shx_VXS6ioC&hl=&printsec=frontcover&output=reader&source=gbs_api'},
   u'etag': u'jd9A6ca9s2s',
   u'id': u'1Shx_VXS6ioC',
   u'kind': u'books#volume',
   u'saleInfo': {u'country': u'DE',
    u'isEbook': False,
    u'saleability': u'NOT_FOR_SALE'},
   u'searchInfo': {u'textSnippet': u'Demonstrates the programming language&#39;s strength as a Web development tool, covering syntax, data types, built-ins, the Python standard module library, and real-world examples.'},
   u'selfLink': u'https://www.googleapis.com/books/v1/volumes/1Shx_VXS6ioC',
   u'volumeInfo': {u'authors': [u'Alex Martelli',
     u'Anna Martelli Ravenscroft',
     u'David Ascher'],
    u'averageRating': 3.5,
    u'canonicalVolumeLink': u'http://books.google.de/books/about/Python_Cookbook.html?hl=&id=1Shx_VXS6ioC',
    u'categories': [u'Computers'],
    u'contentVersion': u'0.1.0.0.preview.3',
    u'description': u"Demonstrates the programming language's strength as a Web development tool, covering syntax, data types, built-ins, the Python standard module library, and real-world examples.",
    u'imageLinks': {u'smallThumbnail': u'http://bks9.books.google.de/books?id=1Shx_VXS6ioC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api',
     u'thumbnail': u'http://bks9.books.google.de/books?id=1Shx_VXS6ioC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api'},
    u'industryIdentifiers': [{u'identifier': u'0596007973',
      u'type': u'ISBN_10'},
     {u'identifier': u'9780596007973', u'type': u'ISBN_13'}],
    u'infoLink': u'http://books.google.de/books?id=1Shx_VXS6ioC&dq=isbn:0596007973&hl=&source=gbs_api',
    u'language': u'en',
    u'pageCount': 807,
    u'previewLink': u'http://books.google.de/books?id=1Shx_VXS6ioC&printsec=frontcover&dq=isbn:0596007973&hl=&cd=1&source=gbs_api',
    u'printType': u'BOOK',
    u'publishedDate': u'2005-03-18',
    u'publisher': u"O'Reilly Media",
    u'ratingsCount': 21,
    u'title': u'Python Cookbook'}}],
 u'kind': u'books#volumes',
 u'totalItems': 1}
```
