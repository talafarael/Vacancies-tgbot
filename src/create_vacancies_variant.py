

{
  "categories": ["Business Analyst", "Data Science", "ML AI", "Web Analyst", "Data Analyst", "Data Engineer", "SQL", "Technical Writing", "Marketing", "Digital Marketing", "Digital Marketing Manager", "Social Media", "Content Marketing", "Content Writing", "Content Manager", "Advertising", "Affiliate Manager", "Media Buying", "PPC", "Marketing Analyst", "PR Manager", "Sales", "Lead Generation", "SEO", "HR", "Recruiter", "Support"],
  "executives": ["Head Chief", "CEO", "CFO", "CIO", "COO", "CPO", "CSO", "CMO", "CBDO", "CCO"],
  "finances": ["Finances", "Other"],
  "experience": ["no_exp", "1y", "2y", "3y", "4y", "5y", "6y", "7y", "8y", "9y", "10y"],
  "work_format": ["remote", "parttime", "office"],
  "company_type": ["agency", "outsource", "outstaff", "product", "startup"],
  "english_level": ["no_english", "basic", "pre", "intermediate", "upper", "fluent"],
  "ukraine_cities": ["kyiv", "vinnytsia", "dnipro", "ivano-frankivsk", "zhytomyr", "zaporizhzhia", "lviv", "mykolaiv", "odesa", "ternopil", "kharkiv", "khmelnytskyi", "cherkasy", "chernihiv", "chernivtsi", "uzhhorod"],
  "other_countries": ["BGR", "FRA", "EST", "GBR", "SWE", "ROU", "MLT", "POL", "SVK", "CZE", "AUT", "ITA", "PRT", "LTU", "HRV", "NLD", "HUN", "ESP", "BEL", "DEU", "LVA", "UKR", "CYP", "USA", "MDA", "KAZ", "GEO", "ARM", "UZB", "MNE", "CAN", "KGZ", "TJK", "AZE", "ARE", "OMN", "QAT", "TUR", "MEX", "ARG", "BRA", "SRB", "VNM", "CHE", "UMI", "ALB", "ISR", "IND", "SAU", "SGP", "ZAF", "BOL", "PRY", "GTM", "SLV", "ABW", "PER", "AUS", "MKD", "NPL", "IDN", "CHL", "CHN", "VIR", "PRI", "COL", "CRI"],
  "vacancy_filters": ["has_public_salary", "ukrainian_product", "miltech", "reservation"]
}

async def create_vacancies(dou_name:str,djinnni_name:str):
    vacancies={
        dou_name:dou_name,
        djinnni_name:djinnni_name
    }

