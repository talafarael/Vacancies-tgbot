from get_page.get_page import GetPage



class ScrapDjinni:
    def __init__(self,get_page:GetPage) -> None:
        self._get_page=get_page 
    async def scrap_djinni(self,url:str):
        driver=await self._get_page(url)
        driver=.find_elements(By.CLASS_NAME, "job-post-page") 



