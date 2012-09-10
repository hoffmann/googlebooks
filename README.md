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
{
  "totalItems": 1, 
  "items": [
    {
      "kind": "books#volume", 
      "volumeInfo": {
        "publisher": "O'Reilly Media", 
        "description": "Demonstrates the programming language's strength as a Web development tool, covering syntax, data types, built-ins, the Python standard module library, and real-world examples.", 
        "language": "en", 
        "publishedDate": "2005-03-18", 
        "imageLinks": {
          "smallThumbnail": "http://bks9.books.google.de/books?id=1Shx_VXS6ioC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api", 
          "thumbnail": "http://bks9.books.google.de/books?id=1Shx_VXS6ioC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        }, 
        "previewLink": "http://books.google.de/books?id=1Shx_VXS6ioC&printsec=frontcover&dq=isbn:0596007973&hl=&cd=1&source=gbs_api", 
        "title": "Python Cookbook", 
        "printType": "BOOK", 
        "pageCount": 807, 
        "canonicalVolumeLink": "http://books.google.de/books/about/Python_Cookbook.html?hl=&id=1Shx_VXS6ioC", 
        "contentVersion": "0.1.0.0.preview.3", 
        "industryIdentifiers": [
          {
            "identifier": "0596007973", 
            "type": "ISBN_10"
          }, 
          {
            "identifier": "9780596007973", 
            "type": "ISBN_13"
          }
        ], 
        "authors": [
          "Alex Martelli", 
          "Anna Martelli Ravenscroft", 
          "David Ascher"
        ], 
        "ratingsCount": 21, 
        "infoLink": "http://books.google.de/books?id=1Shx_VXS6ioC&dq=isbn:0596007973&hl=&source=gbs_api", 
        "categories": [
          "Computers"
        ], 
        "averageRating": 3.5
      }, 
      "searchInfo": {
        "textSnippet": "Demonstrates the programming language&#39;s strength as a Web development tool, covering syntax, data types, built-ins, the Python standard module library, and real-world examples."
      }, 
      "saleInfo": {
        "country": "DE", 
        "saleability": "NOT_FOR_SALE", 
        "isEbook": false
      }, 
      "etag": "jd9A6ca9s2s", 
      "accessInfo": {
        "webReaderLink": "http://books.google.de/books/reader?id=1Shx_VXS6ioC&hl=&printsec=frontcover&output=reader&source=gbs_api", 
        "publicDomain": false, 
        "embeddable": true, 
        "country": "DE", 
        "textToSpeechPermission": "ALLOWED_FOR_ACCESSIBILITY", 
        "pdf": {
          "isAvailable": true
        }, 
        "viewability": "PARTIAL", 
        "epub": {
          "isAvailable": true
        }, 
        "accessViewStatus": "SAMPLE"
      }, 
      "id": "1Shx_VXS6ioC", 
      "selfLink": "https://www.googleapis.com/books/v1/volumes/1Shx_VXS6ioC"
    }
  ], 
  "kind": "books#volumes"
}
```
