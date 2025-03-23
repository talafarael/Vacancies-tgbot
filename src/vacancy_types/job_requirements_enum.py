from enum import Enum


class ValidEnum(str,Enum):  # Наследуем str, если надо сравнивать значения строк
    @classmethod
    def is_valid(cls, value):
        return value in cls._value2member_map_
                                                             
                                                             
class Language(ValidEnum):                                   
    NoEnglish = "No English"                                 
    BeginnerElementary = "Beginner/Elementary"               
    PreIntermediate = "Pre-Intermediate"                     
    Intermediate = "Intermediate"                            
    UpperIntermediate = "Upper-Intermediate"                 
    AdvancedFluent = "Advanced/Fluent"                       
                                                             
                                                             
class Experience(ValidEnum):                                 
    Бездосвіду = "Без досвіду"                               
    рік1 = "1 рік досвіду"                                           
    роки2 = "2 роки досвіду"                                         
    роки3 = "3 роки досвіду"                                         
    роки4 = "4 роки досвіду"                                         
    років5 = "5 років досвіду"                                       
    років6 = "6 років досвіду"                                       
    років7 = "7 років досвіду"
                                       
    років8 = "8 років досвіду"                                       
    років9 = "9 років  досвіду"                                       
    років10 = "10 років досвіду"                 
                                                             
                                                             
class Employment(ValidEnum):                                 
    Тільки_офіс="Тільки офіс"
    Віддалена_робота = "Віддалена робота"                    
    Part_time = "Part-time"                                  
    В_офісі_та_віддалено="В офісі та віддалено"
    Офіс = "Офіс"                                            

                                                             
                                                             
class Region(ValidEnum):                                     
    Україна = "Україна"                                      
    Країни_ЄС = "Країни ЄС"                                  
    Інші_країни = "Інші країни"                              
    Весь_світ="Весь світ"
    Країни_Європи_крім_України="Країни Європи крім України"
    Країни_Європи_та_Україна="Країни Європи та Україна"
                                                             
                                                             
class Editorial(ValidEnum):                                  
    Вказана_зарплатна_вилка = "Вказана зарплатна вилка"      
    Ukrainian_Product = "Ukrainian Product 🇺🇦"             
    MilTech = "MilTech 🪖"                                   
    Mobilisation_Reservation = "Mobilisation reservation ⏳" 
class TypeProdcut(ValidEnum):
    Продукт="Продукт"
    

