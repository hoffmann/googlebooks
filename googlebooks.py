import requests
import json

class Api(object):
    """Google Books Api
    
    See: https://developers.google.com/books/
    """
    __BASEURL = 'https://www.googleapis.com/books/v1'
    def __init__(self ):
       pass 

    def _get(self, path, params=None):
        if params is None:
            params = {}
        resp = requests.get(self.__BASEURL+path, params=params)
        if resp.status_code == 200:
            return json.loads(resp.content)

        return resp

    def get(self, volumeId, **kwargs):
        """Retrieves a Volume resource based on ID

        volumeId -- ID of volume to retrieve.

        Optional Parameters:

        partner --  Brand results for partner ID.
        
        projection -- Restrict information returned to a set of selected fields. 

                    Acceptable values are:
                    "full" - Includes all volume data.
                    "lite" - Includes a subset of fields in volumeInfo and accessInfo.
        
        source --   String to identify the originator of this request.

        See: https://developers.google.com/books/docs/v1/reference/volumes/get
        """
        path = '/volumes/'+volumeId
        params = dict()
        for p in 'partner projection source'.split():
            if p in kwargs:
                params[p] = kwargs[p]

        return self._get(path)
    
    def list(self, q, **kwargs):
        """Performs a book search.

        q -- Full-text search query string.
            
            There are special keywords you can specify in the search terms to
            search in particular fields, such as:

            intitle: Returns results where the text following this keyword is
                    found in the title.
            inauthor: Returns results where the text following this keyword is
                    found in the author.
            inpublisher: Returns results where the text following this keyword
                    is found in the publisher.
            subject: Returns results where the text following this keyword is
                    listed in the category list of the volume.
            isbn:   Returns results where the text following this keyword is the
                    ISBN number.
            lccn:   Returns results where the text following this keyword is the
                    Library of Congress Control Number.
            oclc:   Returns results where the text following this keyword is the
                    Online Computer Library Center number.

        Optional Parameters:

        download -- Restrict to volumes by download availability. 

                    Acceptable values are:
                    "epub" - All volumes with epub.

        filter --   Filter search results. 

                    Acceptable values are:
                    "ebooks" - All Google eBooks.
                    "free-ebooks" - Google eBook with full volume text viewability.
                    "full" - Public can view entire volume text.
                    "paid-ebooks" - Google eBook with a price.
                    "partial" - Public able to see parts of text.

        langRestrict -- Restrict results to books with this language code.

        libraryRestrict	-- Restrict search to this user's library. 

                    Acceptable values are:
                    "my-library" - Restrict to the user's library, any shelf.
                    "no-restrict" - Do not restrict based on user's library.

        maxResults -- Maximum number of results to return. Acceptable values are 0 to 40, inclusive.

        orderBy	 -- Sort search results. 

                    Acceptable values are:
                    "newest" - Most recently published.
                    "relevance" - Relevance to search terms.

        partner	--  Restrict and brand results for partner ID.

        printType -- Restrict to books or magazines. 

                    Acceptable values are:
                    "all" - All volume content types.
                    "books" - Just books.
                    "magazines" - Just magazines.

        projection -- Restrict information returned to a set of selected fields. 

                    Acceptable values are:
                    "full" - Includes all volume data.
                    "lite" - Includes a subset of fields in volumeInfo and accessInfo.
        
        showPreorders -- Set to true to show books available for preorder. Defaults to false.

        source --  String to identify the originator of this request.

        startIndex -- Index of the first result to return (starts at 0)

        See: https://developers.google.com/books/docs/v1/reference/volumes/list
        """
        path = '/volumes'
        params = dict(q=q)
        for p in 'download filter langRestrict libraryRestrict maxResults orderBy partner printType projection showPreorders source startIndex'.split():
            if p in kwargs:
                params[p] = kwargs[p]

        return self._get(path, params)
