
import requests 

def ConvertVariants(ListOfVariants,source='variantid',target='rsid'):
    
    OT_url='https://api.genetics.opentargets.org/graphql'
    MappingDict={}
    if (source=='variantid') & (target=='rsid'):
        query="""{
               variantInfo(variantId:"%s"){
                   rsId
                   }
              }"""
        for variant in ListOfVariants:
            r = requests.post(OT_url, json={'query': query % (variant)})
            JsonResponse=r.json()
            MappingDict[variant]=JsonResponse['data']['variantInfo']['rsId']
        return list(map(MappingDict.get,ListOfVariants))

    elif (source=='rsid') & (target=='variantid'):
        query="""{
              search(queryString:"%s"){
                  variants{
                      id
                      }
                   }
              }
              """
        for variant in ListOfVariants:
            r = requests.post(OT_url, json={'query': query % (variant)})
            JsonResponse=r.json()
            MappingDict[variant]=JsonResponse['data']['search']['variants'][0]['id']
        return list(map(MappingDict.get,ListOfVariants))
