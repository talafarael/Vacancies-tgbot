from typing import List
from bson import ObjectId
from src.types.vacancies_full_obj_type import VacanciesFullType





class GetVacancies:
    def __init__(self,cluster):
        self._cluster=cluster
    async def get_vacancy(self,id: ObjectId)->VacanciesFullType:
        pipeline = [
        {'$match': {'_id': id}},  
        {'$lookup': {
            'from': 'categories',  
            'localField': 'id_category',  
            'foreignField': '_id',  
            'as': 'category'  
        }},
        {'$lookup': {
            'from': 'experiences',  
            'localField': 'id_experience', 
            'foreignField': '_id',  
            'as': 'experience'
        }},
        {'$unwind': '$category'},  
        {'$unwind': '$experience'}  
        ]
        result =await  self._cluster.test.vacancies.aggregate(pipeline).to_list(length=1)
        return result
    async def get_vacancies(self)->List[VacanciesFullType]:                      
        try:
            pipeline = [                                                                      
            {'$lookup': {                                                                     
                'from': 'categories',                                                         
                'localField': 'id_category',                                                  
                'foreignField': '_id',                                                        
                'as': 'category'                                                              
            }},                                                                               
            {'$lookup': {                                                                     
                'from': 'experiences',                                                        
                'localField': 'id_experience',                                                
                'foreignField': '_id',                                                        
                'as': 'experience'
            }},                                                                               
            {'$unwind': '$category'},                                                         
            {'$unwind': '$experience'}                                                        
            ]                                                                                 
            result =await  self._cluster.test.vacancies.aggregate(pipeline).to_list() 
            return result
        except NameError:
            print(NameError)
            return []








