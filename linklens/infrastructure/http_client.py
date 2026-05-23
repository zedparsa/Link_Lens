import logging
import requests

logger = logging.getLogger(__name__)

class HTTPClient:
    
    def __init__(self):
        
        self.session = requests.Session()
        self.session.headers.update({
                    "User-Agent" : "Link_Lens" ,
                    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" ,
                    "Accept-Language" : "en-US,en;q=0.9"
                })
    
    # these are for Session()
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.session.close()
    
    # the main function
    def fetch_html(self , url:str , timeout: int = 10 ) -> str:
                            
        try:      
            response = self.session.get(url , timeout=timeout)
            response.raise_for_status()
            html_content = response.text
               
            logger.info(f"Succesfully fetched: {url}")   
            return html_content 
            
        except requests.HTTPError as error:  
            logger.exception(f"Failed to fetch {url} : {error}")
            raise
            
        except requests.RequestException as error:
            logger.exception(f"Failed to fetch {url} : {error}")            
            raise
        
# for test         
if __name__ == "__main__" :
    
    logging.basicConfig(level=logging.INFO , format="%(levelname)s:%(message)s")

    with HTTPClient() as client :             
        try :
            html = client.fetch_html("https://dls4.iran-onemovies-dcenter.com/DonyayeSerial/series2/tt0944947/SoftSub/S01/1080p.x265.10bit.BluRay/")
            print(f"Successfully fetched , lenth: {len(html)}")
            
        except Exception :
            print(f"Failed , check logs")
